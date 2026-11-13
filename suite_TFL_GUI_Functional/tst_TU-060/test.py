
# -*- coding: utf-8 -*-

import names
from common import *



TARGET_FREQUENCY = 1.0
MAX_ATTEMPTS = 20

def get_frequency(obj_name, description):

    try:
        obj = waitForObject(obj_name)
        raw_value = str(obj.text).strip()

        frequency = float(raw_value)

        test.log(
            "{} frequency: {} Hz".format(
                description, frequency
            )
        )

        return frequency

    except Exception as e:

        test.fail(
            "FAIL: Unable to read {} frequency: {}".format(
                description, str(e)
            )
        )

        return None

def set_frequency_to_minimum(
        slider_name, value_name, description):

    try:

        slider = waitForObject(slider_name)

        
        mouseDrag(
            slider,
            190, 52,
            -148, -3,
            1,
            Qt.LeftButton
        )

        snooze(1)

        frequency = get_frequency(
            value_name, description
        )

        if frequency is None:
            return False

        attempts = 0

        
        while frequency > TARGET_FREQUENCY and attempts < MAX_ATTEMPTS:

            slider = waitForObject(slider_name)

            mouseDrag(
                slider,
                100, 50,
                -10, 0,
                1,
                Qt.LeftButton
            )

            snooze(0.5)

            frequency = get_frequency(
                value_name, description
            )

            if frequency is None:
                return False

            attempts += 1

        result = abs(frequency - TARGET_FREQUENCY) < 0.0001

        test.verify(
            result,
            "{} frequency set to 1 Hz | Actual: {} Hz".format(
                description, frequency
            )
        )

        return result

    except Exception as e:

        test.fail(
            "FAIL: Unable to set {} frequency: {}".format(
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
            "{} frequency decrease button disabled | Enabled: {}".format(
                description, enabled_status
            )
        )

    except Exception as e:

        test.fail(
            "FAIL: {} decrease button verification: {}".format(
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

        waitForObject(
            names.apollo_centralWidget_QStackedWidget
        )

        test.verify(
            True,
            "Treatment screen displayed successfully"
        )

    except Exception as e:

        test.fail(
            "Treatment screen not displayed: " + str(e)
        )

        return



    left_set = set_frequency_to_minimum(
        names.centralWidget_wdSlider_Slider_3,
        names.centralWidget_lbValue_FlashableLabel_2,
        "Left pedal"
    )

    right_set = set_frequency_to_minimum(
        names.centralWidget_wdSlider_Slider_4,
        names.centralWidget_lbValue_FlashableLabel_2,
        "Right pedal"
    )

    snooze(1)

    if left_set:

        verify_decrease_disabled(
            names.centralWidget_pbReduce_QPushButton_2,
            "Left pedal"
        )

    else:

        test.fail(
            "FAIL: Left pedal frequency did not reach 1 Hz"
        )



    if right_set:

        verify_decrease_disabled(
            names.centralWidget_pbReduce_QPushButton_3,
            "Right pedal"
        )

    else:

        test.fail(
            "FAIL: Right pedal frequency did not reach 1 Hz"
        )

   
