
# -*- coding: utf-8 -*-

import names
from common import *
import re

LEFT_FREQUENCY = {
    "container": names.apollo_centralWidget_QStackedWidget,
    "name": "lbValue",
    "occurrence": 1,
    "type": "FlashableLabel",
    "visible": 1
}

LEFT_ENERGY = {
    "container": names.apollo_centralWidget_QStackedWidget,
    "name": "lbValue",
    "occurrence": 2,
    "type": "FlashableLabel",
    "visible": 1
}

RIGHT_FREQUENCY = names.centralWidget_lbValue_FlashableLabel_2
RIGHT_ENERGY = names.centralWidget_lbValue_FlashableLabel

def get_value(obj_name, description):

    try:
        obj = waitForObject(obj_name)
        raw_value = str(obj.text).strip()

        match = re.search(r"[-+]?\d+(?:\.\d+)?", raw_value)

        if not match:
            test.fail(
                "FAIL: Unable to read numeric value: " + description
            )
            return None

        return float(match.group())

    except Exception as e:

        test.fail(
            "FAIL: Unable to access " + description + " | " + str(e)
        )
        return None


def verify_change(button_name, value_name, description, direction):

    before = get_value(value_name, description)

    if before is None:
        return

    try:
        clickButton(waitForObject(button_name))
        snooze(1)

        after = get_value(value_name, description)

        if after is None:
            return

        if direction == "decrease":
            result = after < before
            action = "DECREASED"

        else:
            result = after > before
            action = "INCREASED"

        test.verify(
            result,
            "{} {} | Before: {} | After: {}".format(
                description,
                action if result else "NOT " + action,
                before,
                after
            )
        )

    except Exception as e:

        test.fail(
            "FAIL: {} {} | {}".format(
                description,
                direction,
                str(e)
            )
        )


def main():

    
    enterpin()

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))

    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))

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



    verify_change(names.centralWidget_pbReduce_QPushButton,LEFT_ENERGY,"Left Pulse Energy","decrease")

    verify_change(names.centralWidget_pbEnlarge_QPushButton,LEFT_ENERGY,"Left Pulse Energy","increase")

    verify_change(names.centralWidget_pbReduce_QPushButton_2,LEFT_FREQUENCY,"Left Frequency","decrease")

    verify_change(names.centralWidget_pbEnlarge_QPushButton_3,LEFT_FREQUENCY,"Left Frequency","increase")

    verify_change(names.centralWidget_pbReduce_QPushButton_4,RIGHT_ENERGY,"Right Pulse Energy","decrease")

    verify_change(names.centralWidget_pbEnlarge_QPushButton_2,RIGHT_ENERGY,"Right Pulse Energy","increase")

    verify_change(names.centralWidget_pbReduce_QPushButton_3,RIGHT_FREQUENCY,"Right Frequency","decrease")

    verify_change(names.centralWidget_pbEnlarge_QPushButton_4,RIGHT_FREQUENCY,"Right Frequency","increase")
    
    
