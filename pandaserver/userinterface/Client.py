'''
client methods

'''

import os
import re
import sys
import urllib
import commands
import cPickle as pickle


# configuration
try:
    baseURL = os.environ['PANDA_URL']
except:
    baseURL = 'http://pandasrv.usatlas.bnl.gov:25080/server/panda'
try:
    baseURLSSL = os.environ['PANDA_URL_SSL']
except:
    baseURLSSL = 'https://pandasrv.usatlas.bnl.gov:25443/server/panda'
try:
    baseURLDQ2 = os.environ['PANDA_URL_DQ2']
except:
    baseURLDQ2 = 'http://dms02.usatlas.bnl.gov:80/dq2'
try:
    baseURLDQ2LRC = os.environ['PANDA_URL_DQ2LRC']
except:
    baseURLDQ2LRC = 'http://dms02.usatlas.bnl.gov:8000/dq2/lrc'
try:
    baseURLSUB = os.environ['PANDA_URL_SUB']
except:
    baseURLSUB = 'https://gridui01.usatlas.bnl.gov:24443/dav/test'


# exit code
EC_Failed = 255


# URLs
serverURLs = {'default' : {'URL'    : baseURL,
                           'URLSSL' : baseURLSSL},
              'CERN'    : {'URL'    : 'http://pandasrv.cern.ch:25080/server/panda',
                           'URLSSL' : 'https://pandasrv.cern.ch:25443/server/panda'},
              'BNL'     : {'URL'    : 'http://pandasrv.usatlas.bnl.gov:25080/server/panda',
                           'URLSSL' : 'https://pandasrv.usatlas.bnl.gov:25443/server/panda'},
              }

# bamboo
baseURLBAMBOO = 'http://lxmrrb5310.cern.ch:25080/bamboo/bamboo'


# get URL
def _getURL(type,srvID=None):
    if serverURLs.has_key(srvID):
        urls = serverURLs[srvID]
    else:
        urls = serverURLs['default']
    return urls[type]
    

# get Panda srvIDs
def getPandas():
    srvs = serverURLs.keys()
    # remove 'default'
    try:
        srvs.remove('default')
    except:
        pass
    return srvs


# look for a grid proxy certificate
def _x509():
    # see X509_USER_PROXY
    try:
        return os.environ['X509_USER_PROXY']
    except:
        pass
    # see the default place
    x509 = '/tmp/x509up_u%s' % os.getuid()
    if os.access(x509,os.R_OK):
        return x509
    # no valid proxy certificate
    # FIXME
    print "No valid grid proxy certificate found"
    return ''


# curl class
class _Curl:
    # constructor
    def __init__(self):
        # path to curl
        self.path = 'curl'
        # verification of the host certificate
        self.verifyHost = False
        # request a compressed response
        self.compress = True
        # SSL cert/key
        self.sslCert = ''
        self.sslKey  = ''
        # verbose
        self.verbose = False


    # GET method
    def get(self,url,data):
        # make command
        com = '%s --silent --get' % self.path
        if not self.verifyHost:
            com += ' --insecure'
        if self.compress:
            com += ' --compressed'
        if self.sslCert != '':
            com += ' --cert %s' % self.sslCert
        if self.sslKey != '':
            com += ' --key %s' % self.sslKey
        # data
        strData = ''
        for key in data.keys():
            strData += 'data="%s"\n' % urllib.urlencode({key:data[key]})
        # write data to temporary config file
        try:
            tmpName = os.environ['PANDA_TMP']
        except:
            tmpName = '/tmp'
        tmpName += '/%s_%s' % (commands.getoutput('whoami'),commands.getoutput('uuidgen'))
        tmpFile = open(tmpName,'w')
        tmpFile.write(strData)
        tmpFile.close()
        com += ' --config %s' % tmpName
        com += ' %s' % url
        # execute
        if self.verbose:
            print com
            print commands.getoutput('cat %s' % tmpName)
        ret = commands.getstatusoutput(com)
        # remove temporary file
        os.remove(tmpName)
        if ret[0] != 0:
            ret = (ret[0]%255,ret[1])
        if self.verbose:
            print ret
        return ret


    # POST method
    def post(self,url,data):
        # make command
        com = '%s --silent' % self.path
        if not self.verifyHost:
            com += ' --insecure'
        if self.compress:
            com += ' --compressed'
        if self.sslCert != '':
            com += ' --cert %s' % self.sslCert
        if self.sslKey != '':
            com += ' --key %s' % self.sslKey
        # data
        strData = ''
        for key in data.keys():
            strData += 'data="%s"\n' % urllib.urlencode({key:data[key]})
        # write data to temporary config file
        try:
            tmpName = os.environ['PANDA_TMP']
        except:
            tmpName = '/tmp'
        tmpName += '/%s_%s' % (commands.getoutput('whoami'),commands.getoutput('uuidgen'))
        tmpFile = open(tmpName,'w')
        tmpFile.write(strData)
        tmpFile.close()
        com += ' --config %s' % tmpName
        com += ' %s' % url
        # execute
        if self.verbose:
            print com
            print commands.getoutput('cat %s' % tmpName)
        ret = commands.getstatusoutput(com)
        # remove temporary file
        os.remove(tmpName)
        if ret[0] != 0:
            ret = (ret[0]%255,ret[1])
        if self.verbose:
            print ret
        return ret


    # PUT method
    def put(self,url,data):
        # make command
        com = '%s --silent' % self.path
        if not self.verifyHost:
            com += ' --insecure'
        if self.compress:
            com += ' --compressed'
        if self.sslCert != '':
            com += ' --cert %s' % self.sslCert
        if self.sslKey != '':
            com += ' --key %s' % self.sslKey
        # emulate PUT 
        for key in data.keys():
            com += ' -F "%s=@%s"' % (key,data[key])
        com += ' %s' % url
        # execute
        if self.verbose:
            print com
        ret = commands.getstatusoutput(com)
        if ret[0] != 0:
            ret = (ret[0]%255,ret[1])
        if self.verbose:
            print ret
        return ret
            

'''
public methods

'''

# submit jobs
def submitJobs(jobs,srvID=None):
    # set hostname
    hostname = commands.getoutput('hostname')
    for job in jobs:
        job.creationHost = hostname
    # serialize
    strJobs = pickle.dumps(jobs)
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    # execute
    url = _getURL('URLSSL',srvID) + '/submitJobs'
    data = {'jobs':strJobs}
    status,output = curl.post(url,data)
    if status!=0:
        print output
        return status,output
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr =  "ERROR submitJobs : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# run task assignment
def runTaskAssignment(jobs):
    # set hostname
    hostname = commands.getoutput('hostname')
    for job in jobs:
        job.creationHost = hostname
    # serialize
    strJobs = pickle.dumps(jobs)
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    # execute
    url = baseURLSSL + '/runTaskAssignment'
    data = {'jobs':strJobs}
    status,output = curl.post(url,data)
    if status!=0:
        print output
        return status,output
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr =  "ERROR runTaskAssignment : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# get job status
def getJobStatus(ids,srvID=None):
    # serialize
    strIDs = pickle.dumps(ids)
    # instantiate curl
    curl = _Curl()
    # execute
    url = _getURL('URL',srvID) + '/getJobStatus'
    data = {'ids':strIDs}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR getJobStatus : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# get assigning task
def getAssigningTask():
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/getAssigningTask'
    status,output = curl.get(url,{})
    try:
        return status,pickle.loads(output)
    except:
        print output
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR getAssigningTask : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# get assigned cloud for tasks
def seeCloudTask(ids):
    # serialize
    strIDs = pickle.dumps(ids)
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/seeCloudTask'
    data = {'ids':strIDs}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR seeCloudTask : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# kill jobs
def killJobs(ids,code=None,verbose=False,srvID=None):
    # serialize
    strIDs = pickle.dumps(ids)
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    curl.verbose = verbose
    # execute
    url = _getURL('URLSSL',srvID) + '/killJobs'
    data = {'ids':strIDs,'code':code}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR killJobs : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# reassign jobs
def reassignJobs(ids):
    # serialize
    strIDs = pickle.dumps(ids)
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    # execute
    url = baseURLSSL + '/reassignJobs'
    data = {'ids':strIDs}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR reassignJobs : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# query PandaIDs
def queryPandaIDs(ids):
    # serialize
    strIDs = pickle.dumps(ids)
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/queryPandaIDs'
    data = {'ids':strIDs}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR queryPandaIDs : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# query job info per cloud
def queryJobInfoPerCloud(cloud,schedulerID=None):
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/queryJobInfoPerCloud'
    data = {'cloud':cloud}
    if schedulerID != None:
        data['schedulerID'] = schedulerID
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR queryJobInfoPerCloud : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr

    
# get job statistics
def getJobStatistics(sourcetype=None):
    # instantiate curl
    curl = _Curl()
    # execute
    ret = {}
    for srvID in getPandas():
        url = _getURL('URL',srvID) + '/getJobStatistics'
        data = {}
        if sourcetype != None:
            data['sourcetype'] = sourcetype            
        status,output = curl.get(url,data)
        try:
            tmpRet = status,pickle.loads(output)
            if status != 0:
                return tmpRet
        except:
            print output
            type, value, traceBack = sys.exc_info()
            errStr = "ERROR getJobStatistics : %s %s" % (type,value)
            print errStr
            return EC_Failed,output+'\n'+errStr
        # gather
        for tmpCloud,tmpVal in tmpRet[1].iteritems():
            if not ret.has_key(tmpCloud):
                # append cloud values
                ret[tmpCloud] = tmpVal
            else:
                # sum statistics
                for tmpStatus,tmpCount in tmpVal.iteritems():
                    if ret[tmpCloud].has_key(tmpStatus):
                        ret[tmpCloud][tmpStatus] += tmpCount 
                    else:
                        ret[tmpCloud][tmpStatus] = tmpCount    
    return 0,ret
 

# get jobs updated recently
def getJobsToBeUpdated(limit=5000,lockedby='',srvID=None):
    # instantiate curl
    curl = _Curl()
    # execute
    url = _getURL('URL',srvID) + '/getJobsToBeUpdated'
    status,output = curl.get(url,{'limit':limit,'lockedby':lockedby})
    try:
        return status,pickle.loads(output)
    except:
        print output
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR getJobsToBeUpdated : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# update prodDBUpdateTimes
def updateProdDBUpdateTimes(params,verbose=False,srvID=None):
    # serialize
    strPar = pickle.dumps(params)
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    curl.verbose = verbose
    # execute
    url = _getURL('URLSSL',srvID) + '/updateProdDBUpdateTimes'
    data = {'params':strPar}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR updateProdDBUpdateTimes : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# get PandaID at site
def getPandaIDsSite(site,status,limit=500):
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/getPandaIDsSite'
    status,output = curl.get(url,{'site':site,'status':status,'limit':limit})
    try:
        return status,pickle.loads(output)
    except:
        print output
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR getPandaIDsSite : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr

    
# get job statistics per site
def getJobStatisticsPerSite(predefined=False):
    # instantiate curl
    curl = _Curl()
    # execute
    ret = {}
    for srvID in getPandas():
        url = _getURL('URL',srvID) + '/getJobStatisticsPerSite'
        status,output = curl.get(url,{'predefined':predefined})
        try:
            tmpRet = status,pickle.loads(output)
            if status != 0:
                return tmpRet
        except:
            print output
            type, value, traceBack = sys.exc_info()
            errStr = "ERROR getJobStatisticsPerSite : %s %s" % (type,value)
            print errStr
            return EC_Failed,output+'\n'+errStr
        # gather
        for tmpSite,tmpVal in tmpRet[1].iteritems():
            if not ret.has_key(tmpSite):
                # append site values
                ret[tmpSite] = tmpVal
            else:
                # sum statistics
                for tmpStatus,tmpCount in tmpVal.iteritems():
                    if ret[tmpSite].has_key(tmpStatus):
                        ret[tmpSite][tmpStatus] += tmpCount 
                    else:
                        ret[tmpSite][tmpStatus] = tmpCount    
    return 0,ret


# query last files in datasets
def queryLastFilesInDataset(datasets):
    # serialize
    strDSs = pickle.dumps(datasets)
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/queryLastFilesInDataset'
    data = {'datasets':strDSs}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        print "ERROR queryLastFilesInDataset : %s %s" % (type,value)
        return EC_Failed,None
                                                                

# put file
def putFile(file):
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    # execute
    url = baseURLSSL + '/putFile'
    data = {'file':file}
    return curl.put(url,data)


# delete file
def deleteFile(file):
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    # execute
    url = baseURLSSL + '/deleteFile'
    data = {'file':file}
    return curl.post(url,data)


# query files in dataset
def queryFilesInDataset(name):
    # instantiate curl
    curl = _Curl()
    # get VUID
    url = baseURLDQ2 + '/repository/dataset'
    data = {'name':name,'version':0}
    status,out = curl.get(url,data)
    if status != 0:
        print "ERROR : could not get VUID"
        print status,out
        return {}
    # parse
    match = re.findall('(\w+-\w+-\w+-\w+-\w+$)',out)
    if len(match) != 1:
        print "ERROR : could not find VUID"        
        print status,out
        return {}
    vuid = match[0]
    # get files
    url = baseURLDQ2 + '/content/files'
    data = {'vuid':vuid}
    status,out =  curl.get(url,data)
    if status != 0:
        print "ERROR : could not get files: VUID=%s" % vuid
        print status,out
        return {}
    # parse
    ret = {}
    for line in out.split('\n'):
        item = line.split()
        if len(item) != 2:
            print "ERROR : could not parse files"
            print status,out
            return {}
        ret[item[1]] = item[0]
    return ret            


# resubmit jobs
def resubmitJobs(ids):
    # serialize
    strIDs = pickle.dumps(ids)
    # instantiate curl
    curl = _Curl()
    curl.sslCert = _x509()
    curl.sslKey  = _x509()
    # execute
    url = baseURLSSL + '/resubmitJobs'
    data = {'ids':strIDs}
    status,output = curl.post(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        print "ERROR resubmitJobs : %s %s" % (type,value)
        return EC_Failed,None


# get site specs
def getSiteSpecs():
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/getSiteSpecs'
    status,output = curl.get(url,{})
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR getSiteSpecs : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# get cloud specs
def getCloudSpecs():
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/getCloudSpecs'
    status,output = curl.get(url,{})
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR getCloudSpecs : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr


# run brokerage
def runBrokerage(sites,atlasRelease,cmtConfig=None):
    # serialize
    strSites = pickle.dumps(sites)
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURL + '/runBrokerage'
    data = {'sites':strSites,
            'atlasRelease':atlasRelease}
    if cmtConfig != None:
        data['cmtConfig'] = cmtConfig
    return curl.get(url,data)


# get RW
def getRW(priority=0):
    # instantiate curl
    curl = _Curl()
    # execute
    url = baseURLBAMBOO + '/getRW'
    # get RWs for high priority tasks
    data = {'priority':priority}        
    status,output = curl.get(url,data)
    try:
        return status,pickle.loads(output)
    except:
        type, value, traceBack = sys.exc_info()
        errStr = "ERROR getRW : %s %s" % (type,value)
        print errStr
        return EC_Failed,output+'\n'+errStr
