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
    test.compare(str(waitForObjectExists(names.apollo_lbHeader_QLabel).text), "EINSTELLUNGEN")
    test.compare(str(waitForObjectExists(names.apollo_centralWidget_QFrame).windowIconText), "")
    test.compare(waitForObjectExists(names.apollo_centralWidget_QFrame).visible, True)
    test.log("Settings Screen Verification")
    
    validate_localization(
        objects=[
            waitForObject(names.apollo_lbHeader_QLabel),
            waitForObject(names.centralWidget_lbLang_QLabel),
            waitForObject(names.centralWidget_lbVolume_QLabel),
            waitForObject(names.centralWidget_lbBrightness_QLabel),
            waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Deutsch (Germany)"),
        
        ],
        screen_name="Settings Screen",
        expected_strings=[
            "German",
            "SETTINGS",
            "LANGUAGE",
            "SPEAKER VOLUME",
            "DISPLAY BRIGHTNESS",
        ],
    )
