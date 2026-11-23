# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 184, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Български (Bulgaria)"), 130, 25, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.apollo_btHome_QPushButton))

    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    mouseClick(waitForObject(names.stackedWidget_systemInformationPage_QFrame), 754, 48, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 71, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbHeader_QLabel), 203, 27, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.systemInformationPage_label_2_QLabel), 479, 18, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.systemInformationPage_label_3_QLabel), 481, 24, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.systemInformationPage_label_QLabel), 497, 27, Qt.NoModifier, Qt.LeftButton)

    test.vp("systemInformation")

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
