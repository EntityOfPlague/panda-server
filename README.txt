Release Note

* 0.0.5 (5/15/2009)
  * subtract N*250M from available space in brokerage
  * use tasktype2 for RW recalculation
  * allow transferring in updateJob
  * use job stat per process group in brokerage
  * added prodUserName
  * added validation to test
  * fixed TA
  * use prodUserName for users
  * added nEvents to JD
  * added pilotowners
  * added rc_test
  * added a hint for Datasets.name
  * enabled validatedReleases for all clouds
  * set high priority for production role
  * added realDatasetsIn
  * get empty list of LFNs for empty dataset
  * set modificationTime to ARCH tables
  * fixed getUserParameter
  * added nInputFiles for HC
  * added countryGroup for country share
  * use a hint for filesTable4.dataset
  * fixed lookup for mail addr
  * use PandaMover for US
  * give higher priorities to /atlas/xyz/Role=production
  * set workingGroup when jobs are submitted with prod role
  * fixed peekJobLog
  * replica location lookup for containers
  * fixed broker_util to use proper python
  * use jobParamsTable
  * fixed python path to use 64bit glite
  * fixed for ArchivedDB
  * fixed FQAN extraction for GRST_CONN
  * dispatchDBlockToken
  * converted datetime to str for stateChangeTime
  * use 12hr limit in getJobStatisticsForBamboo
  * use CERN-PROD_DAQ for prestaging when _DATATAPE is not a location
  * ignore token=ATLASDATATAPE when no tape copy
  * pandasrv -> pandaserver
  * set old=False for listDatasetReplicas
  * fixed copyArchived for ArchiveDB
  * added _zStr/_nullAttrs in JobSpec
  * fixed getJobStatisticsForExtIF()
  * fixed for schedID/pilotID
  * removed redundant debug message
  * fixed for Notification
  * input token for mover
  * set NULL for creationHost,AtlasRelease,transformation,homepackage
  * use sequences directly for PandaID and row_ID
  * use SUBCOUNTER_SUBID_SEQ directly
  * added a hint to countFilesWithMap
  * fixed getNUserJobs
  * removed log/cache dirs making
  * put alias to filesTable4 in countFilesWithMap
  * introduced PANDA_URL_MAP
  * suppressed meta in JobSpec
  * error handling in Adder
  * fixed enddate in Notifier
  * use CURRENT_DATE in copyArch
  * added nprestage
  * added startTime/endTime in updateJob
  * validatedreleases and accesscontrol
  * 3 -> 1hour for movers (discarded)
  * added 'IS NULL' to copyArch 
  * added bulk reading for PandaID to copyArch to avoid redundant lookup
  * added a hint to updateOutFilesReturnPandaIDs
  * use Null instead of 'NULL'
  * don't reset jobParameters when reassigned
  * added a hint to all fileTable4+destinationDBlock
  * use JOBSARCHIVED4_MODTIME_IDX
  * addSiteAccess and listSiteAccess
  * hours=1 -> 3 for movers
  * retry in peekJob
  * reconnection in rollback 
  * added hint to queryDatasetWithMap
  * use bind-variables for all queries
  * fixed freezeDS 
  * fixed a duplicated variable in Closer 
  * truncate ddmErrorDiag
  * hint to freezeDS
  * removed deleteFiles in copyArchived
  * not update modTime in copyArchived when peekJob failed
  * container-aware
  * validatedreleases and space check in brokerage
  * added deleteJobSimple
  * use validatedreleases for FR too
  * fixed reassignXYZ
  * use archivedFlag for copy/delete
  * fine lock for reassignRepro 
  * threading for reassignRepro 
  * improved expiration messages
  * failed when input dataset is not found in DQ2
  * debug messages in Setupper
  * added other error codes in rollback

* 0.0.4 (2/23/2009)
  * GSI authentication for pilots
  * tag-based security mechanism for scheduler-pilot-server chain
  * fixed test/add.py to use Oracle instead of MySQL
  * fixed querySQLS for DELETE
  * added panda_server-grid-env.sh
  * merged DB proxies to reduce the number of connections
  * added lock for worker MPM
  * use common write account

* 0.0.3 (2/16/2009)
  * sync to production version

* 0.0.2 (12/18/2008)
  * adjustments for CERN

* 0.0.1 (12/4/2008)
  * first import
