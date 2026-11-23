# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_5_QPushButton))
    doubleClick(waitForObject(names.wdKeypad_pushButton_5_QPushButton), 67, 78, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.wdKeypad_pushButton_5_QPushButton))
    mouseClick(waitForObject(names.passwordScreen_mInvalidPassNotif_QLabel), 234, 61, Qt.NoModifier, Qt.LeftButton)
    
    validate_localization(

        objects=[

            waitForObjectExists(names.passwordScreen_mInvalidPassNotif_QLabel)
        ],

        screen_name="Login",

        expected_strings=[
            
            "Invalid Passcode"
            
        ],
    ) 

    test.compare(str(waitForObjectExists(names.passwordScreen_mInvalidPassNotif_QLabel).text), "Invalid Passcode")
    if str(waitForObjectExists(names.passwordScreen_mInvalidPassNotif_QLabel).text) == "Invalid Passcode": 
        test.passes("Login Screen verified")
    else: test.fail("Login Screen verification failed")
