# -*- coding: utf-8 -*-

import names
from common import *


def main():

    # Login
    enterpin()

    
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))

    
    default_button = waitForObjectExists(
        names.sclProfiles_Default_ProfileButton
    )

    test.compare(
        str(default_button.text),
        "Default",
        "Default profile button is present on Profile Selection screen"
    )

   
    clickButton(default_button)

    snooze(2)

    
    left_pedal = waitForObjectExists(
        names.centralWidget_wdLeftPedal_PedalSettingsWidget
    )

    right_pedal = waitForObjectExists(
        names.centralWidget_wdRightPedal_PedalSettingsWidget
    )

    test.compare(
        bool(left_pedal.visible and right_pedal.visible),
        True,
        "Program exits to treatment screen in Default profile"
    )

    
    mouseClick(
        waitForObject(names.centralWidget_wdLeftPedal_PedalSettingsWidget),
        575, 138,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.centralWidget_wdRightPedal_PedalSettingsWidget),
        25, 115,
        Qt.NoModifier,
        Qt.LeftButton
    )