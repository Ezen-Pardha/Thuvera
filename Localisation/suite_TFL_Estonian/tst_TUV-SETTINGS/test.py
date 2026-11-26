# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 451, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Eesti (Estonia)"), 120, 36, Qt.NoModifier, Qt.LeftButton)
    validate_localization(

        objects=[
            
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbLang_QLabel),
            waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Eesti (Estonia)"),
            waitForObject(names.centralWidget_lbVolume_QLabel),
            waitForObject(names.centralWidget_lbBrightness_QLabel),
            
        ],

        screen_name="SETTINGS",

        expected_strings=[
            
            "SETTINGS",
            "LANGUAGE",
            "Estonian",
            "SPEAKER VOLUME",
            "DISPLAY BRIGHTNESS"

        ],
    ) 

    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "SÄTTED")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "SÄTTED": 
        test.passes("SETTINGS Screen verified")
    else: test.fail("SETTINGS Screen verification failed")     
