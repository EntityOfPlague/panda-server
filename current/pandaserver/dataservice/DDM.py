"""
provide primitive methods for DDM

"""

import types
import commands
from config import panda_config


# environment variables
_env = 'PATH=%s:%s:$PATH '    % (panda_config.native_python,panda_config.globus_dir+'/bin')
_env+= 'LD_LIBRARY_PATH=%s '  % (panda_config.globus_dir+'/lib')
_env+= 'DQ2_HOME=%s/opt/dq2 ' % panda_config.dq2_dir
_env+= 'http_proxy=%s '       % panda_config.httpProxy
_env+= 'https_proxy=%s '      % panda_config.httpProxy

_env+= 'PYTHONPATH=%s/usr/lib/python2.3/site-packages:$PYTHONPATH' \
       % panda_config.dq2_dir

# method object wrapping DQ2 method
class _DQMethod:
    # constructor
    def __init__(self,moduleName,methodName):
        self.moduleName = moduleName
        self.methodName = methodName

    # method emulation
    def __call__(self,*args):
        # main method has disappeared since 0.3
        args = list(args)
        if self.methodName == 'main':
            self.methodName = args[0]
            args.pop(0)
        # build command
        com  = 'import dq2.clientapi.cli.cliutil; '
        #com += 'import sys; sys.tracebacklimit=0; '
        com += 'dq2api = dq2.clientapi.cli.cliutil.getDQ2(None); '
        if self.moduleName == 'DQ2':
            # DQ2 is top-level module
            com += 'print dq2api.%s(' % self.methodName
        else:
            com += 'print dq2api.%s.%s(' % (self.moduleName,self.methodName)
        # expand args
        for i in range(len(args)):
            arg = args[i]
            if i != 0:
                com += ','
            if isinstance(arg,types.StringType):
                com = "%s'%s'" % (com,arg)
            else:
                com = '%s%s' % (com,str(arg))
        com += ")"
        # execute
        return commands.getstatusoutput('env %s python -c "%s"' % (_env,com))
        

# DQ module class
class _DQModule:
    # constructor
    def __init__(self,moduleName):
        self.moduleName = moduleName

    # factory method
    def __getattr__(self,methodName):
        return _DQMethod(self.moduleName,methodName)


# factory class
class DDM:
    def __getattr__(self,moduleName):
        return _DQModule(moduleName)


# instantiate
ddm = DDM()
del DDM
