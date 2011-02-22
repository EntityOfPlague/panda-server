# !!!!!!! This file is OBSOLETE. Its content has been absorbed into pilotController.py in the autopilot repository.
# !!!!!!! Questions to Torre Wenaus.
PandaSiteIDs = {
    'AGLT2'                  : {'nickname':'AGLT2-condor','status':'OK'},
    'ALBERTA-LCG2'           : {'nickname':'ALBERTA-LCG2-lcgce01-atlas-lcgpbs','status':'OK'},
    'ANALY_AGLT2'            : {'nickname':'ANALY_AGLT2-condor','status':'OK'},
    'ANALY_ALBERTA'          : {'nickname':'ALBERTA-LCG2-lcgce01-atlas-lcgpbs','status':'OK'},    
    'ANALY_BEIJING'          : {'nickname':'BEIJING-LCG2-lcg002-atlas-lcgpbs','status':'OK'},    
    'ANALY_BNL'              : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},
    'ANALY_BNL_ATLAS_1'      : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},
    'ANALY_BNL_ATLAS_2'      : {'nickname':'BNL_ATLAS_2-condor','status':'OK'},
    #'ANALY_BNL_LOCAL'        : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},
    'ANALY_BNL_test'         : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},
    'ANALY_BNL_test2'        : {'nickname':'ANALY_BNL_ATLAS_1-condor','status':'OK'},
    'ANALY_BNL_test3'        : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},    
    'ANALY_BRUNEL'           : {'nickname':'UKI-LT2-Brunel-dgc-grid-44-atlas-lcgpbs','status':'notOK'},
    'ANALY_CERN'             : {'nickname':'CERN-PROD-ce123-grid_atlas-lcglsf','status':'notOK'},
    'ANALY_CNAF'             : {'nickname':'INFN-CNAF-gridit-ce-001-lcg-lcgpbs','status':'notOK'},
    'ANALY_CPPM'             : {'nickname':'IN2P3-CPPM-marce01-atlas-pbs','status':'OK'},
    'ANALY_FZK'              : {'nickname':'FZK-LCG2-ce-5-fzk-atlasXS-pbspro','status':'OK'},
    'ANALY_GLASGOW'          : {'nickname':'UKI-SCOTGRID-GLASGOW-svr021-q3d-lcgpbs','status':'OK'},
    'ANALY_GLOW-ATLAS'       : {'nickname':'GLOW-ATLAS-condor','status':'OK'},
    'ANALY_GRIF-IRFU'        : {'nickname':'GRIF-IRFU-node07-atlas-lcgpbs','status':'OK'},
    'ANALY_GRIF-LAL'         : {'nickname':'GRIF-LAL-grid10-atlasana-pbs','status':'notOK'},
    'ANALY_GRIF-LPNHE'       : {'nickname':'GRIF-LPNHE-lpnce-atlas-pbs','status':'notOK'},
    'ANALY_HU_ATLAS_Tier2'   : {'nickname':'ANALY_HU_ATLAS_Tier2-lsf','status':'OK'},
    'ANALY_LANCS'            : {'nickname':'UKI-NORTHGRID-LANCS-HEP-fal-pygrid-18-atlas-lcgpbs','status':'notOK'},
    'ANALY_LAPP'             : {'nickname':'IN2P3-LAPP-lapp-ce01-atlas-pbs','status':'notOK'},
    'ANALY_LIV'              : {'nickname':'UKI-NORTHGRID-LIV-HEP-hepgrid2-atlas-lcgpbs','status':'notOK'},
    'ANALY_LONG_BNL'         : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},
    'ANALY_LONG_BNL_ATLAS'   : {'nickname':'BNL_ATLAS_2-condor','status':'OK'},
    'ANALY_LONG_BNL_LOCAL'   : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},
    'ANALY_LONG_LYON'        : {'nickname':'IN2P3-CC-T2-cclcgceli05-long-bqs','status':'OK'},
    'ANALY_LPC'              : {'nickname':'IN2P3-LPC-clrlcgce03-atlas-lcgpbs','status':'notOK'},
    'ANALY_LPSC'             : {'nickname':'IN2P3-LPSC-lpsc-ce-atlas-pbs','status':'OK'},
    'ANALY_LYON'             : {'nickname':'IN2P3-CC-T2-cclcgceli05-medium-bqs','status':'OK'},
    'ANALY_MANC'             : {'nickname':'UKI-NORTHGRID-MAN-HEP-ce01-atlas-lcgpbs','status':'OK'},
    'ANALY_MCGILL'           : {'nickname':'MCGILL-LCG2-atlas-ce-atlas-lcgpbs','status':'OK'},
    'ANALY_MWT2'             : {'nickname':'ANALY_MWT2-condor','status':'notOK'},
    'ANALY_MWT2_SHORT'       : {'nickname':'ANALY_MWT2_SHORT-pbs','status':'notOK'},        
    'ANALY_NET2'             : {'nickname':'ANALY_NET2-pbs','status':'OK'},    
    'ANALY_OU_OCHEP_SWT2'    : {'nickname':'ANALY_OU_OCHEP_SWT2-condor','status':'notOK'},
    'ANALY_PIC'              : {'nickname':'pic-ce07-gshort-lcgpbs','status':'OK'},
    'ANALY_RAL'              : {'nickname':'RAL-LCG2-lcgce01-atlasL-lcgpbs','status':'OK'},
    'ANALY_ROMANIA02'        : {'nickname':'RO-02-NIPNE-tbat01-atlas-lcgpbs','status':'notOK'},
    'ANALY_ROMANIA07'        : {'nickname':'RO-07-NIPNE-tbit01-atlas-lcgpbs','status':'notOK'},
    'ANALY_SARA'             : {'nickname':'SARA-MATRIX-mu6-short-pbs','status':'notOK'},
    'ANALY_SFU'              : {'nickname':'SFU-LCG2-snowpatch-hep-atlas-lcgpbs','status':'notOK'},
    'ANALY_SHEF'             : {'nickname':'UKI-NORTHGRID-SHEF-HEP-lcgce0-atlas-lcgpbs','status':'OK'},
    'ANALY_SLAC'             : {'nickname':'ANALY_SLAC-lsf','status':'OK'},
    'ANALY_SWT2_CPB'         : {'nickname':'ANALY_SWT2_CPB-pbs','status':'OK'},    
    'ANALY_TAIWAN'           : {'nickname':'Taiwan-LCG2-w-ce01-atlas-lcgpbs','status':'OK'},
    'ANALY_TEST'             : {'nickname':'ANALY_TEST','status':'OK'},
    'ANALY_TORONTO'          : {'nickname':'TORONTO-LCG2-bigmac-lcg-ce2-atlas-pbs','status':'OK'},
    'ANALY_TOKYO'            : {'nickname':'TOKYO-LCG2-lcg-ce01-atlas-lcgpbs','status':'OK'},
    'ANALY_TRIUMF'           : {'nickname':'TRIUMF-LCG2-ce1-atlas-lcgpbs','status':'OK'},    
    'ANALY_UBC'              : {'nickname':'UBC-pbs','status':'OK'},
    'ANALY_UIUC-HEP'         : {'nickname':'ANALY_UIUC-HEP-condor','status':'OK'},
    'ANALY_UTA'              : {'nickname':'UTA-DPCC-pbs','status':'OK'},
    'ANALY_UTA-DPCC'         : {'nickname':'UTA-DPCC-test-pbs','status':'notOK'},
    'ANALY_VICTORIA'         : {'nickname':'VICTORIA-LCG2-lcg-ce-general-lcgpbs','status':'OK'},
    'AUVERGRID'              : {'nickname':'AUVERGRID-iut15auvergridce01-atlas-lcgpbs','status':'notOK'},
    'ASGC'                   : {'nickname':'Taiwan-LCG2-w-ce01-atlas-lcgpbs','status':'OK'},
    'ASGC_REPRO'             : {'nickname':'ASGC_REPRO','status':'notOK'},    
    'Australia-ATLAS'        : {'nickname':'Australia-ATLAS-agh2-atlas-lcgpbs','status':'OK'},
    'BARNETT_TEST'           : {'nickname':'BARNETT_TEST','status':'notOK'},
    'BEIJING'                : {'nickname':'BEIJING-LCG2-lcg002-atlas-lcgpbs','status':'OK'},
    'BNLPROD'                : {'nickname':'BNL_ATLAS_1-condor','status':'notOK'},
    'BNL_ATLAS_1'            : {'nickname':'BNL_ATLAS_1-condor','status':'OK'},
    'BNL_ATLAS_2'            : {'nickname':'BNL_ATLAS_2-condor','status':'OK'},
    'BNL_ATLAS_DDM'          : {'nickname':'BNL_DDM-condor','status':'notOK'},
    'BNL_ATLAS_test'         : {'nickname':'BNL_ATLAS_2-condor','status':'notOK'},
    'BU_ATLAS_Tier2'         : {'nickname':'BU_ATLAS_Tier2-pbs','status':'OK'},
    'BU_ATLAS_Tier2o'        : {'nickname':'BU_ATLAS_Tier2o-pbs','status':'OK'},
    'BU_ATLAS_test'          : {'nickname':'BU_ATLAS_Tier2-pbs','status':'NOTOK'},
    'HU_ATLAS_Tier2'         : {'nickname':'HU_ATLAS_Tier2-lsf','status':'OK'},
    'CERN-BUILDS'            : {'nickname':'CERN-BUILDS','status':'notOK'},    
    'CERN-RELEASE'           : {'nickname':'CERN-RELEASE','status':'notOK'},    
    'CERN-UNVALID'           : {'nickname':'CERN-UNVALID','status':'notOK'},    
    'CGG'                    : {'nickname':'CGG-LCG2-ce1-atlas-lcgpbs','status':'notOK'},        
    'CHARMM'                 : {'nickname':'CHARMM','status':'notOK'},
    'CNR-ILC-PISA'           : {'nickname':'CNR-ILC-PISA-gridce-atlas-lcgpbs','status':'notOK'},
    'CPPM'                   : {'nickname':'IN2P3-CPPM-marce01-atlas-pbs','status':'OK'},
    'CSCS-LCG2'              : {'nickname':'CSCS-LCG2-ce01-egee48h-lcgpbs','status':'OK'},
    'csTCDie'                : {'nickname':'csTCDie-gridgate-himem-pbs','status':'OK'},
    'CYF'                    : {'nickname':'CYFRONET-LCG2-ce-atlas-pbs','status':'OK'},    
    'DESY-HH'                : {'nickname':'DESY-HH-grid-ce3-default-lcgpbs','status':'OK'},
    'DESY-ZN'                : {'nickname':'DESY-ZN-lcg-ce0-atlas-lcgpbs','status':'OK'},
    'EFDA-JET'               : {'nickname':'EFDA-JET-grid002-atlas-lcgpbs','status':'notok'},
    'FZK-LCG2'               : {'nickname':'FZK-LCG2-ce-1-fzk-atlasXL-pbspro','status':'OK'},
    'FZK_REPRO'              : {'nickname':'FZK_REPRO','status':'notOK'},    
    'FZU'                    : {'nickname':'praguelcg2-golias25-lcgatlas-lcgpbs','status':'OK'},    
    'GLOW'                   : {'nickname':'GLOW-CMS-cmsgrid02-atlas-condor','status':'notOK'},
    'GLOW-ATLAS'             : {'nickname':'GLOW-ATLAS-condor','status':'OK'},
    'GoeGrid'                : {'nickname':'GoeGrid-ce-goegrid-atlas-lcgpbs','status':'OK'},    
    'GRIF-IRFU'              : {'nickname':'GRIF-IRFU-node07-atlas-lcgpbs','status':'OK'},
    'GRIF-LAL'               : {'nickname':'GRIF-LAL-grid10-atlas-pbs','status':'OK'},
    'GRIF-LPNHE'             : {'nickname':'GRIF-LPNHE-lpnce-atlas-pbs','status':'OK'},
    'HEPHY-UIBK'             : {'nickname':'HEPHY-UIBK-hepx4-atlas-lcgpbs','status':'OK'},    
    'IFAE'                   : {'nickname':'ifae-ifaece01-ifae-lcgpbs','status':'OK'},
    'IFIC'                   : {'nickname':'IFIC-LCG2-ce01-atlas-pbs','status':'OK'},	
    'IHEP'                   : {'nickname':'BEIJING-LCG2-lcg002-atlas-lcgpbs','status':'OK'},
    'ITEP'                   : {'nickname':'ITEP-ceglite-atlas-lcgpbs','status':'OK'},
    'IN2P3-LPSC'             : {'nickname':'IN2P3-LPSC-lpsc-ce-atlas-pbs','status':'OK'},
    'INFN-BARI'              : {'nickname':'INFN-BARI-gridba2-long-lcgpbs','status':'notOK'},
    'INFN-BOLOGNA'           : {'nickname':'INFN-BOLOGNA-boalice3-atlas-lcgpbs','status':'notOK'},
    'INFN-CAGLIARI'          : {'nickname':'INFN-CAGLIARI-grid002-atlas-lcglsf','status':'notOK'},
    'INFN-CNAF'              : {'nickname':'INFN-CNAF-gridit-ce-001-lcg-lcgpbs','status':'notOK'},
    'INFN-FERRARA'           : {'nickname':'INFN-FERRARA-grid0-lcg-lcgpbs','status':'notOK'},
    'INFN-FIRENZE'           : {'nickname':'INFN-FIRENZE-grid001-atlas-lcgpbs','status':'notOK'},
    'INFN-FRASCATI'          : {'nickname':'INFN-FRASCATI-atlasce-atlas-lcgpbs','status':'OK'},
    'INFN-GENOVA'            : {'nickname':'INFN-GENOVA-grid01-atlas-lcgpbs','status':'notOK'},
    'INFN-LECCE'             : {'nickname':'INFN-LECCE-gridce-atlas-lcgpbs','status':'notOK'},
    'INFN-LNL-2'             : {'nickname':'INFN-LNL-2-t2-ce-02-atlas-lcglsf','status':'notOK'},
    'INFN-LNS'               : {'nickname':'INFN-LNS-grid-ce-infinite-lcgpbs','status':'notOK'},
    'INFN-MILANO'            : {'nickname':'INFN-MILANO-t2-ce-01-atlas-lcgpbs','status':'OK'},
    'INFN-NAPOLI-ATLAS'      : {'nickname':'INFN-NAPOLI-ATLAS-atlasce01-atlas_short-lcgpbs','status':'OK'},
    'INFN-NAPOLI'            : {'nickname':'INFN-NAPOLI-griditce01-atlas-lcgpbs','status':'notOK'},
    'INFN-NAPOLI-PAMELA'     : {'nickname':'INFN-NAPOLI-PAMELA-pamelace01-atlas-lcgpbs','status':'notOK'},
    'INFN-PADOVA'            : {'nickname':'INFN-PADOVA-prod-ce-01-atlas-lcglsf','status':'notOK'},
    'INFN-PISA'              : {'nickname':'INFN-PISA-gridce2-atlas4-lcglsf','status':'notOK'},
    'INFN-ROMA1'             : {'nickname':'INFN-ROMA1-atlas-ce-01-atlasglong-lcglsf','status':'OK'},
    'INFN-T1'                : {'nickname':'INFN-T1-ce05-lcg-atlas-lcglsf','status':'OK'},
    'INFN-T1_REPRO'          : {'nickname':'INFN-T1_REPRO','status':'notOK'},    
    'INFN-TORINO'            : {'nickname':'INFN-TORINO-t2-ce-01-atlas-lcgpbs','status':'notOK'},
    'INFN-TRIESTE'           : {'nickname':'INFN-TRIESTE-grid001-atlas-lcglsf','status':'notOK'},
    'IU_OSG'                 : {'nickname':'IU_OSG-pbs','status':'OK'},
    'IPNO'                   : {'nickname':'GRIF-IPNO-ipnls2001-atlas-pbs','status':'notOK'},
    'JINR-LCG2'              : {'nickname':'JINR-LCG2-lcgce01-atlas-lcgpbs', 'status':'OK'},
    'LAPP'                   : {'nickname':'IN2P3-LAPP-lapp-ce01-atlas-pbs','status':'OK'},
    'LIP-COIMBRA'            : {'nickname':'LIP-Coimbra-grid006-atlas-lcgpbs','status':'OK'},
    'LIP-LISBON'             : {'nickname':'LIP-Lisbon-ce02-atlasgrid-lcgsge','status':'OK'},    
    'LLR'                    : {'nickname':'GRIF-LLR-polgrid1-atlas-pbs','status':'notOK'},    
    'LPC'                    : {'nickname':'IN2P3-LPC-clrlcgce03-atlas-lcgpbs','status':'OK'},
    'LRZ'                    : {'nickname':'LRZ-LMU-lcg-lrz-ce-atlas-sge','status':'OK'},    
    'LYON'                   : {'nickname':'IN2P3-CC-cclcgceli02-long-bqs','status':'OK'},
    'LYON_REPRO'             : {'nickname':'LYON_REPRO','status':'notOK'},        
    'Lyon-T2'                : {'nickname':'IN2P3-CC-T2-cclcgceli05-long-bqs','status':'OK'},    
    'LTU_CCT'                : {'nickname':'LTU_CCT-pbs','status':'OK'},
    'MANC'                   : {'nickname':'UKI-NORTHGRID-MAN-HEP-ce02-atlas-lcgpbs','status':'OK'},    
    'MCGILL-LCG2'            : {'nickname':'MCGILL-LCG2-atlas-ce-atlas-pbs','status':'OK'},
    'MONTREAL'               : {'nickname':'Umontreal-LCG2-lcg-ce-atlas-lcgpbs','status':'notOK'},
    'MPP'                    : {'nickname':'MPPMU-grid-ce-long-sge','status':'OK'},
    'MWT2_IU'                : {'nickname':'MWT2_IU-pbs','status':'OK'},
    'MWT2_UC'                : {'nickname':'MWT2_UC-pbs','status':'OK'},
    'NDGF'                   : {'nickname':'NDGF-condor','status':'OK'},
    'NIKHEF-ELPROD'          : {'nickname':'NIKHEF-ELPROD-gazon-atlas-pbs','status':'OK'},
    'NIKHEF_REPRO'           : {'nickname':'NIKHEF_REPRO','status':'notOK'},
    'OUHEP_ITB'              : {'nickname':'OUHEP_ITB-condor','status':'notOK'},
    'OU_PAUL_TEST'           : {'nickname':'OU_OCHEP_SWT2-condor','status':'notOK'},    
    'OU_OCHEP_SWT2'          : {'nickname':'OU_OCHEP_SWT2-condor','status':'OK'},
    'OU_OSCER_ATLAS'         : {'nickname':'OU_OSCER_ATLAS-lsf','status':'OK'},
    'OU_OSCER_ATLASdeb'      : {'nickname':'OU_OSCER_ATLASdeb-lsf','status':'notOK'},
    'PSNC'                   : {'nickname':'PSNC-ce-atlas-pbs','status':'OK'},    
    'PIC'                    : {'nickname':'pic-ce05-glong-lcgpbs','status':'OK'},
    'PIC_REPRO'              : {'nickname':'PIC_REPRO','status':'notOK'},
    'prague_cesnet_lcg2'     : {'nickname':'prague_cesnet_lcg2-skurut17-egee_atlas-lcgpbs','status':'notOK'},
    'RAL'                    : {'nickname':'RAL-LCG2-lcgce02-grid1000M-lcgpbs','status':'OK'},
    'RAL_REPRO'              : {'nickname':'RAL_REPRO','status':'notOK'},    
    'ru-Moscow-SINP-LCG2'    : {'nickname':'ru-Moscow-SINP-LCG2-lcg02-atlas-lcgpbs','status':'OK'},
    'ru-PNPI'                : {'nickname':'ru-PNPI-cluster-atlas-pbs','status':'OK'},
    'RDIGTEST'               : {'nickname':'RDIGTEST','status':'notOK'},
    'ROMANIA02'              : {'nickname':'RO-02-NIPNE-tbat01-atlas-lcgpbs','status':'OK'},
    'ROMANIA07'              : {'nickname':'RO-07-NIPNE-tbit01-atlas-lcgpbs','status':'OK'},
    'RRC-KI'                 : {'nickname':'RRC-KI-gate-atlas-lcgpbs','status':'OK'},
    'RU-Protvino-IHEP'       : {'nickname':'RU-Protvino-IHEP-ce0003-atlas-lcgpbs','status':'OK'},
    'SARA_REPRO'             : {'nickname':'SARA_REPRO','status':'notOK'},
    'SFU-LCG2'               : {'nickname':'SFU-LCG2-snowpatch-atlas-lcgpbs','status':'OK'},    
    'SLACXRD'                : {'nickname':'SLACXRD-lsf','status':'OK'},
    'SLAC_PAUL_TEST'         : {'nickname':'SLACXRD-lsf','status':'notOK'},
    'SNS-PISA'               : {'nickname':'SNS-PISA-gridce-atlas-lcgpbs','status':'notOK'},
    'SPACI-CS-IA64'          : {'nickname':'SPACI-CS-IA64-square-atlas-lsf','status':'notOK'},
    'SWT2_CPB'               : {'nickname':'SWT2_CPB-pbs','status':'OK'},    
    'Taiwan-IPAS-LCG2'       : {'nickname':'Taiwan-IPAS-LCG2-atlasce-atlas-lcgcondor','status':'notOK'},
    'TEST1'                  : {'nickname':'TEST1','status':'notOK'},
    'TEST2'                  : {'nickname':'TEST2','status':'notOK'},
    'TEST3'                  : {'nickname':'TEST3','status':'notOK'},
    'TEST4'                  : {'nickname':'TEST4','status':'notOK'},
    'TESTCHARMM'             : {'nickname':'TESTCHARMM','status':'notOK'},
    'TESTGLIDE'              : {'nickname':'TESTGLIDE','status':'notOK'},
    'TOKYO'                  : {'nickname':'TOKYO-LCG2-lcg-ce01-atlas-lcgpbs','status':'OK'},    
    'TORONTO-LCG2'           : {'nickname':'TORONTO-LCG2-bigmac-lcg-ce2-atlas-pbs','status':'OK'},
    'TPATHENA'               : {'nickname':'TPATHENA','status':'notOK'},
    'TPPROD'                 : {'nickname':'TPPROD','status':'notOK'},
    'TRIUMF'                 : {'nickname':'TRIUMF-LCG2-ce1-atlas-lcgpbs','status':'OK'},
    'TRIUMF_DDM'             : {'nickname':'TRIUMF_DDM','status':'notOK'},    
    'TRIUMF_REPRO'           : {'nickname':'TRIUMF_REPRO','status':'notOK'},
    'TW-FTT'                 : {'nickname':'TW-FTT-f-ce01-atlas-lcgpbs','status':'OK'},
    'TWTEST'                 : {'nickname':'TWTEST','status':'notOK'},
    'TestPilot'              : {'nickname':'TestPilot','status':'notOK'},
    'UAM-LCG2'		     : {'nickname':'UAM-LCG2-grid003-atlas-lcgpbs','status':'OK'},		
    'UBC'                    : {'nickname':'UBC-pbs','status':'OK'},
    'UBC_PAUL_TEST'          : {'nickname':'UBC-pbs','status':'notOK'},    
    'UIUC-HEP'               : {'nickname':'UIUC-HEP-condor','status':'OK'},
    'UCITB_EDGE7'            : {'nickname':'UCITB_EDGE7-pbs','status':'OK'},        
    'UC_ATLAS_MWT2'          : {'nickname':'UC_ATLAS_MWT2-condor','status':'OK'},
    'UC_ATLAS_test'          : {'nickname':'UC_ATLAS_MWT2-condor','status':'OK'},
    'UC_Teraport'            : {'nickname':'UC_Teraport-pbs','status':'notOK'},
    'UMESHTEST'              : {'nickname':'UMESHTEST','status':'notOK'},
    'UNI-FREIBURG'           : {'nickname':'UNI-FREIBURG-ce-atlas-pbs','status':'OK'},
    'UTA-DPCC'               : {'nickname':'UTA-DPCC-pbs','status':'OK'},
    'UTA-DPCC-test'          : {'nickname':'UTA-DPCC-test-pbs','status':'OK'},
    'UTA_PAUL_TEST'          : {'nickname':'UTA-SWT2-pbs','status':'notOK'},
    'UTA_SWT2'               : {'nickname':'UTA-SWT2-pbs','status':'OK'},
    'UTD-HEP'                : {'nickname':'UTD-HEP-pbs','status':'OK'},
    'VICTORIA-LCG2'          : {'nickname':'VICTORIA-LCG2-lcg-ce-general-lcgpbs','status':'OK'},
    'Wuppertal'              : {'nickname':'wuppertalprod-grid-ce-dg_long-lcgpbs','status':'OK'},
}


# cloud-MoverID mapping
PandaMoverIDs = {
    'US' : 'BNL_ATLAS_DDM',
    'CA' : 'TRIUMF_DDM',
    'FR' : 'TRIUMF_DDM',
    'IT' : 'TRIUMF_DDM',
    'NL' : 'TRIUMF_DDM',
    'DE' : 'TRIUMF_DDM',
    'TW' : 'TRIUMF_DDM',
    'UK' : 'TRIUMF_DDM',
    'ES' : 'TRIUMF_DDM',                    
    }
