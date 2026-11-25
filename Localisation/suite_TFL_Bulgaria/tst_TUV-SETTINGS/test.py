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
    
    test.vp("settingsScreen")

    validate_localization(
        objects=[
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbLang_QLabel),
            waitForObject(names.centralWidget_lbVolume_QLabel),
            waitForObject(names.centralWidget_lbBrightness_QLabel),
            waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Български (Bulgaria)"),
        
        ],
        screen_name="Settings Screen",
        expected_strings=[
            "Bulgarian",
            "SETTINGS",
            "LANGUAGE",
            "SPEAKER VOLUME",
            "DISPLAY BRIGHTNESS",
        ],
    )
