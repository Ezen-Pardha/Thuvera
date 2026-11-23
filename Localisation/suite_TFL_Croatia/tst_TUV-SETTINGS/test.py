# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 478, 27, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 85, 27, Qt.NoModifier, Qt.LeftButton)

    validate_localization(

        objects=[
            
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbLang_QLabel),
            waitForObjectItem(names.frmComboBox_cbLang_QComboBox,  "hrvatski (Croatia)"),
            waitForObject(names.centralWidget_lbVolume_QLabel),
            waitForObject(names.centralWidget_lbBrightness_QLabel)
            
        ],

        screen_name="SETTINGS",

        expected_strings=[
            
            "SETTINGS",
            "LANGUAGE",
            "Croatian",
            "SPEAKER VOLUME",
            "DISPLAY BRIGHTNESS"

        ],
    )
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "POSTAVKE")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "POSTAVKE":
        test.passes("SETTINGS screen verified")
    else: test.fail("SETTINGS screen verification failed")
