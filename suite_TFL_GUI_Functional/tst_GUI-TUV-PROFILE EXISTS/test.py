# -*- coding: utf-8 -*-

import names
from common import *

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    test.log("Profile selection screen is verified ")
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    setWindowState(waitForObject(names.apollo_MainWindow), WindowState.Minimize)
    setWindowState(waitForObject(names.apollo_MainWindow), WindowState.Normal)
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
    snooze(2)
    if test.imagePresent("profileEditButton"):
        test.passes("Profile Edit Button is available")
    else:
        test.fail("Profile Edit Button is not available")

    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "profile1")
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    mouseClick(waitForObject(names.apollo_Warning_MessageBox), 490, 205, Qt.NoModifier, Qt.LeftButton)
    if test.compare(str(waitForObjectExists(names.warning_TextLabel_QLabel).text),
                    'The profile name "profile1"<br>already exists.'):
        test.passes("Duplicate profile name warning message is verified successfully")
    else:
        test.fail("Duplicate profile name warning message verification failed")
    clickButton(waitForObject(names.warning_OK_QPushButton))
    clickButton(waitForObject(names.keyboardFrame_Cancel_KeyButtonCancel))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_profile1_ProfileButton))
    clickButton(waitForObject(names.question_OK_QPushButton))
    # test.breakpoint()
    
