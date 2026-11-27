# -*- coding: utf-8 -*-

import names
from squish import *
from common import *

def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_settings()
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 480, 30, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "suomi (Finland)"), 136, 27, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.apollo_btHome_QPushButton))

    test.compare(waitForObjectExists(names.apollo_wdProfile_QWidget).visible, True)
    test.log("Top Navigation Bar Verification")
    
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

        screen_name="Home Screen",
        expected_strings=[
            "DEFAULT",
            "PROFILE",
            "LASING TIME",
            "TOTAL Kj",
            "FIBER (μm)",
            "USES LEFT",
            "EXPIRATION",
            # "NOT CONNECTED"
        ],
    )
