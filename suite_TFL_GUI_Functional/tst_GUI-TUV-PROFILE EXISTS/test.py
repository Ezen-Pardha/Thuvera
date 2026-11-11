# -*- coding: utf-8 -*-

import names
from common import *

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
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
    
    
