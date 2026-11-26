# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 260, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 89, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btUtilities_QPushButton))
    clickButton(waitForObject(names.frmHeader_rbFiberInfo_QRadioButton))
    validate_localization(

        objects=[
            waitForObject(names.frmHeader_lbHeader_QLabel),
            waitForObject(names.stackedWidget_lbTitle_QLabel),
            waitForObject(names.stackedWidget_lbDiameterTitle_QLabel),
            waitForObject(names.stackedWidget_lbMaximumPowerTitle_QLabel),
            waitForObject(names.stackedWidget_lbUsesReminingTitle_QLabel),
            waitForObject(names.stackedWidget_lbSerialNumberTitle_QLabel),
            waitForObject(names.stackedWidget_lbExpirationDateTitle_QLabel)
            
        ],

        screen_name="FIBER INFORMATION",

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
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "PODACI O VLAKNU")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "PODACI O VLAKNU":
        test.passes("FIBER INFORMATION screen verified")
    else: test.fail("FIBER INFORMATION screen verification failed")
    
