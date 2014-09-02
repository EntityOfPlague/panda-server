import re
import sys
import commands
from liveconfigparser.LiveConfigParser import LiveConfigParser

# get ConfigParser
tmpConf = LiveConfigParser()

# read
tmpConf.read('panda_server.cfg')

# get server section
tmpDict = tmpConf.server

# expand all values
tmpSelf = sys.modules[ __name__ ]
for tmpKey,tmpVal in tmpDict.iteritems():
    # convert string to bool/int
    if tmpVal == 'True':
        tmpVal = True
    elif tmpVal == 'False':
        tmpVal = False
    elif re.match('^\d+$',tmpVal):
        tmpVal = int(tmpVal)
    # update dict
    tmpSelf.__dict__[tmpKey] = tmpVal

# set hostname
if not tmpSelf.__dict__.has_key('pserverhost'):
    tmpSelf.__dict__['pserverhost'] = commands.getoutput('hostname -f')
if not tmpSelf.__dict__.has_key('pserverhostssl'):
    tmpSelf.__dict__['pserverhostssl'] = commands.getoutput('hostname -f')

# set port for http
if not tmpSelf.__dict__.has_key('pserverporthttp'):
    tmpSelf.__dict__['pserverporthttp'] = 25080

# set host for http
if not tmpSelf.__dict__.has_key('pserverhosthttp'):
    tmpSelf.__dict__['pserverhosthttp'] = tmpSelf.__dict__['pserverhost']

# set port for cache
if not tmpSelf.__dict__.has_key('pserverportcache'):
    tmpSelf.__dict__['pserverportcache'] = 25085

# change the number of database connections for FastCGI/WSGI
if tmpSelf.__dict__['useFastCGI'] or tmpSelf.__dict__['useWSGI']:
    tmpSelf.__dict__['nDBConnection'] = tmpSelf.__dict__['nDBConForFastCGIWSGI']

# DB backend
if not tmpSelf.__dict__.has_key('backend'):
    tmpSelf.__dict__['backend'] = 'oracle'
if not tmpSelf.__dict__.has_key('dbport'):
    tmpSelf.__dict__['dbport'] = 0


# schemas
if not tmpSelf.__dict__.has_key('schemaPANDA'):
    tmpSelf.__dict__['schemaPANDA'] = 'ATLAS_PANDA'
if not tmpSelf.__dict__.has_key('schemaPANDAARCH'):
    tmpSelf.__dict__['schemaPANDAARCH'] = 'ATLAS_PANDAARCH'
if not tmpSelf.__dict__.has_key('schemaMETA'):
    tmpSelf.__dict__['schemaMETA'] = 'ATLAS_PANDAMETA'
if not tmpSelf.__dict__.has_key('schemaJEDI'):
    tmpSelf.__dict__['schemaJEDI'] = 'ATLAS_PANDA'
if not tmpSelf.__dict__.has_key('schemaDEFT'):
    tmpSelf.__dict__['schemaDEFT'] = 'ATLAS_DEFT'
if not tmpSelf.__dict__.has_key('schemaGRISLI'):
    tmpSelf.__dict__['schemaGRISLI'] = 'ATLAS_GRISLI'



# dict for plugins
g_pluginMap = {}    

# parser for plugin setup
def parsePluginConf(modConfigName):
    global tmpSelf
    global g_pluginMap
    if not g_pluginMap.has_key(modConfigName):
        g_pluginMap[modConfigName] = {}
    # parse plugin setup
    try:
        for configStr in getattr(tmpSelf,modConfigName).split(','):
            configStr = configStr.strip()
            items = configStr.split(':')
            vos          = items[0].split('|')
            moduleName   = items[1]
            className    = items[2]
            for vo in vos:
                # import
                mod = __import__(moduleName)
                for subModuleName in moduleName.split('.')[1:]:
                    mod = getattr(mod,subModuleName)
                # get class
                cls = getattr(mod,className)
                g_pluginMap[modConfigName][vo] = cls
    except:
        pass


# accessor for plugin
def getPlugin(modConfigName,vo):
    if not g_pluginMap.has_key(modConfigName):
        return None
    elif g_pluginMap[modConfigName].has_key(vo):
        # VO specified
        return g_pluginMap[modConfigName][vo]
    elif g_pluginMap[modConfigName].has_key('any'):
        # catch all
        return g_pluginMap[modConfigName]['any']
    # undefined
    return None



# plug-ins
parsePluginConf('adder_plugins')
parsePluginConf('setupper_plugins')
