# -*- coding: utf-8 -*-

import names
import re




def get_value(object_name):
    obj = waitForObjectExists(object_name)
    return str(obj.text).strip()


def numeric_value(value):
    match = re.search(r"-?\d+(?:\.\d+)?", value)

    if not match:
        raise Exception("Unable to read numeric value: " + value)

    return float(match.group())


def verify_value(description, before, after, operation):
    old_value = numeric_value(before)
    new_value = numeric_value(after)

    result = (
        description + " (" + operation + ")"
        + " | Before: " + before
        + " | After: " + after
    )

    if operation == "+":
        passed = new_value > old_value
    else:
        passed = new_value < old_value

    if passed:
        test.passes(result)
        return True
    else:
        test.fail(result)
        return False




def adjust_parameter(description, button, value_label, operation):

    before = get_value(value_label)

    clickButton(waitForObject(button))
    snooze(1)

    after = get_value(value_label)

    return verify_value(
        description,
        before,
        after,
        operation
    )


def test_parameter(description, plus_button, minus_button, value_label):

    plus_result = adjust_parameter(
        description,
        plus_button,
        value_label,
        "+"
    )

    minus_result = adjust_parameter(
        description,
        minus_button,
        value_label,
        "-"
    )

    return plus_result and minus_result




def main():

  
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))

    
    for i in range(4):
        clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))

    
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))

    snooze(2)

   
    mouseClick(
        waitForObject(names.centralWidget_lbValue_FlashableLabel),
        20, 91,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget),
        537, 140,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.centralWidget_lbHeader_QLabel),
        57, 6,
        Qt.NoModifier,
        Qt.LeftButton
    )

    snooze(2)

   

    left_frequency = {
        "container": names.apollo_centralWidget_QStackedWidget,
        "name": "lbValue",
        "type": "FlashableLabel",
        "occurrence": 1,
        "visible": 1
    }

    right_frequency = {
        "container": names.apollo_centralWidget_QStackedWidget,
        "name": "lbValue",
        "type": "FlashableLabel",
        "occurrence": 3,
        "visible": 1
    }

    left_energy = {
        "container": names.apollo_centralWidget_QStackedWidget,
        "name": "lbValue",
        "type": "FlashableLabel",
        "occurrence": 2,
        "visible": 1
    }

    right_energy = {
        "container": names.apollo_centralWidget_QStackedWidget,
        "name": "lbValue",
        "type": "FlashableLabel",
        "occurrence": 4,
        "visible": 1
    }

    

    frequency_results = []

    frequency_results.append(
        test_parameter(
            "Left pedal frequency",
            names.centralWidget_pbEnlarge_QPushButton_3,
            names.centralWidget_pbReduce_QPushButton_2,
            left_frequency
        )
    )

    frequency_results.append(
        test_parameter(
            "Right pedal frequency",
            names.centralWidget_pbEnlarge_QPushButton_4,
            names.centralWidget_pbReduce_QPushButton_3,
            right_frequency
        )
    )

    if all(frequency_results):
        test.passes("Frequency Operating Parameter Adjustment Provided")
    else:
        test.fail("Frequency Operating Parameter Adjustment Provided")

  

    energy_results = []

    energy_results.append(
        test_parameter(
            "Left pedal pulse energy",
            names.centralWidget_pbEnlarge_QPushButton,
            names.centralWidget_pbReduce_QPushButton,
            left_energy
        )
    )

    energy_results.append(
        test_parameter(
            "Right pedal pulse energy",
            names.centralWidget_pbEnlarge_QPushButton_2,
            names.centralWidget_pbReduce_QPushButton_4,
            right_energy
        )
    )

    if all(energy_results):
        test.passes("Pulse Energy Operating Parameter Adjustment Provided")
    else:
        test.fail("Pulse Energy Operating Parameter Adjustment Provided")