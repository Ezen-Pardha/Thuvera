
# -*- coding: utf-8 -*-

import names
from common import *


def main():

    
    enterpin()

    clickButton(
        waitForObject(names.frmPopup_pbAccept_QPushButton)
    )

    clickButton(
        waitForObject(names.sclProfiles_Default_ProfileButton)
    )

    snooze(2)

  
    try:

       
        # test.vp("Verified Preset Screen")

        waitForObject(
            names.apollo_centralWidget_QStackedWidget
        )

        test.verify(
            True,
            "Treatment screen displayed successfully"
        )

    except Exception as e:

        test.fail(
            "Treatment screen verification failed: " + str(e)
        )

        return


    try:

        clickButton(
            waitForObject(names.apollo_btPresets_QPushButton)
        )
        test.vp("Verified Preset Screen")

        snooze(2)

        test.log("Clicked Presets button on sidebar")

    except Exception as e:

        test.fail(
            "Unable to click Presets button: " + str(e)
        )

        return

   

    try:

        waitForObject(
            names.apollo_tvPresets_PresetsTable
        )

        test.verify(
            True,
            "Program successfully navigated to Presets screen"
        )

    except Exception as e:

        test.fail(
            "Presets screen was not displayed: " + str(e)
        )

  
