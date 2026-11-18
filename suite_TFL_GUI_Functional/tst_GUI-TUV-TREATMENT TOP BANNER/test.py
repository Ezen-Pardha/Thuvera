# -*- coding: utf-8 -*-

import names
from common import *


def main():
    test.log("SVV TAG - TU-165: Treatments Logs Screen Top Banner Displayed")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_p_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_r_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_o_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_f_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_i_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_l_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton))  
    clickButton(waitForObject(names.apollo_btTreatmentLogs_QPushButton)) 
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "TREATMENT LOGS")
    # test.vp("treatmentLogsScreen")
    test.imagePresent("treatmentLogsPage")
    test.log("SVV TAG - TU-166: Treatments Logs Screen Side Bar Displayed")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton)) 
    clickButton(waitForObject(names.apollo_btTreatmentLogs_QPushButton))
    if test.imagePresent("treatmentLogsButton"):
       test.passes("Treatment Button is available on the side bar")
    else:
        test.fail("Treatment Button is not available on the side bar")
        
        
    test.log("SVV TAG - TU-166: Treatments Logs Screen Side Bar Displayed")
    
    
    # test.breakpoint()
    
