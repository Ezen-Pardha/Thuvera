# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 461, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Dansk (Denmark)"), 91, 42, Qt.NoModifier, Qt.LeftButton)

    validate_localization(

        objects=[
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbLang_QLabel),
            waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Dansk (Denmark)"),
            waitForObject(names.centralWidget_lbVolume_QLabel),
            waitForObject(names.centralWidget_lbBrightness_QLabel),
            
        ],

        screen_name="SETTINGS",

        expected_strings=[
            
            "SETTINGS",
            "LANGUAGE",
            "Danish",
            "SPEAKER VOLUME",
            "DISPLAY BRIGHTNESS"

        ],
    ) 
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "INDSTILLINGER")
    if str(waitForObjectExists(names.apollo_lbHeader_QLabel).text) == "INDSTILLINGER": 
        test.passes("SETTINGS Screen verified")
    else: test.fail("SETTINGS Screen verification failed")     
