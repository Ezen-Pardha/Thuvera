# -*- coding: utf-8 -*-

import names
from common import *

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    clickButton(waitForObject(names.keyboardFrame_a_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_T_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_A_KeyButtonShift))
    clickButton(waitForObject(names.keyboardFrame_e_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_s_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_t_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_123_KeyButtonNumSwitch))
    clickButton(waitForObject(names.keyboardFrame_1_KeyButtonLetter))
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    test.compare(str(waitForObjectExists(names.apollo_lbProfileName_QLabel).text), "TEST1")
    """Verify TEST1 Profile is loaded"""

    profile_name = str(waitForObjectExists(names.apollo_lbProfileName_QLabel).text)
    
    if profile_name == "TEST1":
        test.passes("User Profile settings are loaded and verified")
    else:
        test.fail("User Profile settings are not loaded. Actual profile: {}".format(profile_name))
    
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
   
