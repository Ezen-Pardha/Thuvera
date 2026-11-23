# -*- coding: utf-8 -*-
import names
from squish import *
from common import *
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))

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
    test.imagePresent("Verifying Top Navigation Bar")

    
