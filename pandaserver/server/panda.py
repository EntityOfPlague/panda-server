"""
entry point

"""

# config file
from config import panda_config

# initialzie TaskBuffer
from taskbuffer.TaskBuffer import taskBuffer
taskBuffer.init(panda_config.dbhost,panda_config.dbpasswd,panda_config.nDBConnection)

# initialize JobDispatcher
from jobdispatcher.JobDispatcher import jobDispatcher
jobDispatcher.init(taskBuffer)

# initialize DataService
from dataservice.DataService import dataService
dataService.init(taskBuffer)

# initialize UserIF
from userinterface.UserIF import userIF
userIF.init(taskBuffer)

# import web I/F
from taskbuffer.Utils            import isAlive,putFile,deleteFile,getServer
from dataservice.DataService     import datasetCompleted
from jobdispatcher.JobDispatcher import getJob,updateJob,isThereAnalysisJob,getStatus
from userinterface.UserIF        import submitJobs,getJobStatus,queryPandaIDs,killJobs,reassignJobs,\
     getJobStatistics,getJobStatisticsPerSite,resubmitJobs,queryLastFilesInDataset,getPandaIDsSite,\
     getJobsToBeUpdated,updateProdDBUpdateTimes,runTaskAssignment,getAssigningTask,getSiteSpecs,\
     getCloudSpecs,runBrokerage,seeCloudTask,queryJobInfoPerCloud,registerProxyKey,getProxyKey
