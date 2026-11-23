# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 91, 42, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    validate_localization(

        objects=[
            
            waitForObject(names.frmHeader_lbHeader_QLabel),
            waitForObject(names.systemInformationPage_label_2_QLabel),
            waitForObject(names.systemInformationPage_label_3_QLabel),
            waitForObject(names.systemInformationPage_label_QLabel)
        ],

        screen_name="SYSTEM INFORMATION",

        expected_strings=[
            "SYSTEM INFORMATION",
            "SOFTWARE VERSION:",
            "MODEL NUMBER:",
            "SERIAL NUMBER:"
        ],
    )
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "PODACI O SUSTAVU")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "PODACI O SUSTAVU": 
        test.passes("SYSTEM INFORMATION screen verified")
    else: test.fail("SYSTEM INFORMATION screen verification failed")
