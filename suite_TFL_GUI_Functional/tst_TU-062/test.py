
# -*- coding: utf-8 -*-

import names
from common import *

TARGET_ENERGY = 0.025
MAX_ATTEMPTS = 20

def get_energy(obj_name, description):

    try:
        obj = waitForObject(obj_name)
        raw_value = str(obj.text).strip()

        energy = float(raw_value)

        test.log(
            "{} pulse energy: {} J".format(
                description, energy
            )
        )

        return energy

    except Exception as e:

        test.fail(
            "FAIL: Unable to read {} pulse energy: {}".format(
                description, str(e)
            )
        )

        return None

def set_energy_to_minimum(
        slider_name, value_name, description,
        start_x, start_y, drag_x, drag_y):

    try:

        slider = waitForObject(slider_name)


        mouseDrag(
            slider,
            start_x, start_y,
            drag_x, drag_y,
            1,
            Qt.LeftButton
        )

        snooze(1)

        energy = get_energy(value_name, description)

        if energy is None:
            return False

        attempts = 0

 
        while energy > TARGET_ENERGY and attempts < MAX_ATTEMPTS:

            slider = waitForObject(slider_name)

            mouseDrag(
                slider,
                100, 45,
                -10, 0,
                1,
                Qt.LeftButton
            )

            snooze(0.5)

            energy = get_energy(value_name, description)

            if energy is None:
                return False

            attempts += 1

        result = abs(energy - TARGET_ENERGY) < 0.000001

        test.verify(
            result,
            "{} pulse energy set to 0.025 J | Actual: {} J".format(
                description, energy
            )
        )

        return result

    except Exception as e:

        test.fail(
            "FAIL: Unable to set {} pulse energy: {}".format(
                description, str(e)
            )
        )

        return False

def verify_decrease_disabled(button_name, description):

    try:

        button = waitForObjectExists(button_name)

        snooze(0.5)

        enabled_status = button.enabled

        test.verify(
            enabled_status == False,
            "{} pulse energy decrease button disabled | Enabled: {}".format(
                description, enabled_status
            )
        )

    except Exception as e:

        test.fail(
            "FAIL: Unable to verify {} decrease button: {}".format(
                description, str(e)
            )
        )

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

        waitForObject(names.apollo_centralWidget_QStackedWidget)

        test.verify(
            True,
            "Treatment screen displayed successfully"
        )

    except Exception as e:

        test.fail("Treatment screen not displayed: " + str(e))
        return

    left_set = set_energy_to_minimum(
        names.centralWidget_wdSlider_Slider,
        names.centralWidget_lbValue_FlashableLabel_3,
        "Left pedal",
        280, 46, -252, 9
    )

    right_set = set_energy_to_minimum(
        names.centralWidget_wdSlider_Slider_2,
        names.centralWidget_lbValue_FlashableLabel,
        "Right pedal",
        278, 43, -263, 3
    )

    snooze(1)
    if left_set:

        verify_decrease_disabled(
            names.centralWidget_pbReduce_QPushButton,
            "Left pedal"
        )

    else:

        test.fail(
            "FAIL: Left pedal pulse energy did not reach 0.025 J"
        )

    if right_set:

        verify_decrease_disabled(
            names.centralWidget_pbReduce_QPushButton_4,
            "Right pedal"
        )

    else:

        test.fail(
            "FAIL: Right pedal pulse energy did not reach 0.025 J"
        )

