# -*- coding: utf-8 -*-

import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 465, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "hrvatski (Croatia)"), 80, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btHome_QPushButton))
    
    validate_localization(

        objects=[

            waitForObject(names.apollo_lbProfileTitle_QLabel),
            waitForObject(names.apollo_lbProfileName_QLabel),
            waitForObject(names.apollo_lbLasingTimeTitle_QLabel),
            waitForObject(names.apollo_lbTotalEnergyTitle_QLabel),
            waitForObject(names.apollo_lbFiberDiameterTitle_QLabel),
            waitForObject(names.apollo_lbUsesLeftTitle_QLabel),
            waitForObject(names.apollo_lbExpirationTitle_QLabel),
            
        ],

        screen_name="Top Navigation bar",

        expected_strings=[
            "DEFAULT",
            "PROFILE",
            "LASING TIME",
            "TOTAL Kj",
            "FIBER (μm)",
            "USES LEFT",
            "EXPIRATION"
        ],
    )

    if test.imagePresent: 
        test.passes("TOP NAVIGATION BAR verified")
    else: test.fail("TOP NAVIGATION BAR verification failed")