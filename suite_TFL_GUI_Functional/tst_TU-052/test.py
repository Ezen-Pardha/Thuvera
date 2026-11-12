# -*- coding: utf-8 -*-

import names
from common import *
import re

def get_value(label):
    return str(waitForObjectExists(label).text).strip()


def get_numeric_value(value):
    match = re.search(r"-?\d+(?:\.\d+)?", value)

    if not match:
        raise Exception("Unable to read numeric value: " + value)

    return float(match.group())


def verify_adjustment(description, button, label):

    try:
        before = get_value(label)

        
        for i in range(2):
            clickButton(waitForObject(button))
            snooze(0.5)

        after = get_value(label)

        old_value = get_numeric_value(before)
        new_value = get_numeric_value(after)

        result = (
            description
            + " | Before: " + before
            + " | After: " + after
        )

        if new_value > old_value:
            test.passes(result)
        else:
            test.fail(result)

    except Exception as error:
        test.fail(description + " | Error: " + str(error))


def main():

    # Login
    enterpin()

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))

    
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))

    snooze(2)

    
    left_pedal = waitForObjectExists(
        names.centralWidget_wdLeftPedal_PedalSettingsWidget
    )

    right_pedal = waitForObjectExists(
        names.centralWidget_wdRightPedal_PedalSettingsWidget
    )

    if left_pedal.visible and right_pedal.visible:
        test.passes("Treatment screen displayed")
    else:
        test.fail("Treatment screen not displayed")

    
    left_frequency = {"container": names.apollo_centralWidget_QStackedWidget,"name": "lbValue","type": "FlashableLabel","occurrence": 1,"visible": 1}

    left_energy = {"container": names.apollo_centralWidget_QStackedWidget,"name": "lbValue","type": "FlashableLabel","occurrence": 2,"visible": 1}

    right_frequency = {"container": names.apollo_centralWidget_QStackedWidget,"name": "lbValue","type": "FlashableLabel","occurrence": 3,"visible": 1}

    right_energy = {"container": names.apollo_centralWidget_QStackedWidget,"name": "lbValue","type": "FlashableLabel","occurrence": 4,"visible": 1}

   
    verify_adjustment("Left pedal pulse energy adjustment",names.centralWidget_pbEnlarge_QPushButton,left_energy)   
    verify_adjustment("Left pedal frequency adjustment",names.centralWidget_pbEnlarge_QPushButton_3,left_frequency)   
    verify_adjustment("Right pedal pulse energy adjustment",names.centralWidget_pbEnlarge_QPushButton_2,right_energy)
    verify_adjustment("Right pedal frequency adjustment",names.centralWidget_pbEnlarge_QPushButton_4,right_frequency)
    
    