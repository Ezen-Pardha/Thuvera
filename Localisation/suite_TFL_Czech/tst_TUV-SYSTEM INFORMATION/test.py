# -*- coding: utf-8 -*-
import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 480, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "čeština (Czech Republic)"), 181, 43, Qt.NoModifier, Qt.LeftButton)
 
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))

    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "INFORMACE O SYSTÉMU")
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_lbHeader_QLabel).visible, True)
    test.log("System Information Screen verification")

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
