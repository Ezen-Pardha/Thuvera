## -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 184, 44, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Български (Bulgaria)"), 130, 25, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbFiberInfo_QRadioButton))

    test.vp("fiberInformation")

    validate_localization(
        objects=[
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.apollo_lbTitle_QLabel),
            waitForObject(names.stackedWidget_lbDiameterTitle_QLabel),
            waitForObject(names.stackedWidget_lbMaximumPowerTitle_QLabel),
            waitForObject(names.stackedWidget_lbUsesReminingTitle_QLabel),
            waitForObject(names.stackedWidget_lbSerialNumberTitle_QLabel),
            waitForObject(names.stackedWidget_lbExpirationDateTitle_QLabel)
        ],
        screen_name="Fiber Information Screen",
        expected_strings=[
            "FIBER INFORMATION",
            "Currently inserted fiber information:",
            "FIBER CORE DIAMETER:",
            "MAXIMUM POWER / ENERGY:",
            "FIBER USES REMAINING:",
            "FIBER SERIAL NUMBER:",
            "EXPIRATION DATE:"
        ],
    )
