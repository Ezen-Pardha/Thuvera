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

    test.compare(str(waitForObjectExists(names.apollo_lbApolloLogo_QLabel).text), "")

    test.imagePresent("topNavigationBarBulgaria")

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
