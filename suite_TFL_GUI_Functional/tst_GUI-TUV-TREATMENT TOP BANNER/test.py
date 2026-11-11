# -*- coding: utf-8 -*-

import names
from common import *


def main():
    test.log("SVV TAG - TU-165: Treatments Logs Screen Top Banner Displayed")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    setWindowState(waitForObject(names.apollo_MainWindow), WindowState.Minimize)
    setWindowState(waitForObject(names.apollo_MainWindow), WindowState.Normal)
    clickButton(waitForObject(names.sclProfiles_thuvera_ProfileButton))
    clickButton(waitForObject(names.apollo_btTreatmentLogs_QPushButton))
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "TREATMENT LOGS")
    test.vp("treatmentLogsScreen")

    test.log("SVV TAG - TU-166: Treatments Logs Screen Side Bar Displayed")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.sclProfiles_thuvera_ProfileButton))
    clickButton(waitForObject(names.apollo_btTreatmentLogs_QPushButton))
    if test.imagePresent("treatmentLogsButton"):
       test.passes("Treatment Button is available on the side bar")
    else:
        test.fail("Treatment Button is not available on the side bar")
        
        
    test.log("SVV TAG - TU-166: Treatments Logs Screen Side Bar Displayed")
    
    
    # test.breakpoint()
    
