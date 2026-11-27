# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 479, 33, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Deutsch (Germany)"), 169, 35, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.apollo_btHome_QPushButton))
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "SYSTEMINFORMATIONEN")
    test.log("System Information Screen Verification")

    validate_localization(
        objects=[
            waitForObject(names.apollo_lbHeader_QLabel),
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
