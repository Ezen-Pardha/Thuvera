# -*- coding: utf-8 -*-

import names
from common import *

def main():
    
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    
    clickButton(waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    type(waitForObject(names.editFrame_edEditText_QLineEdit), "Test1")
    clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))
    
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    
    mouseClick(waitForObject(names.comboBox_lbLogo_QLabel),
               9, 46, Qt.NoModifier, Qt.LeftButton)
    
    mouseClick(waitForObjectItem(
        names.apollo_aivComboBoxPopup_QTreeView,
        "Kidney Dust (High)"
    ), 255, 24, Qt.NoModifier, Qt.LeftButton)
    
    """Set pulse energy to 0.4 J"""
    for i in range(14):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))
    
    """Adjust frequency"""
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    
    """Verify pulse energy"""
    pulse_energy = str(waitForObjectExists(
        names.centralWidget_lbValue_FlashableLabel_3
    ).text)
    
    if pulse_energy == "0.4":
        test.passes("Pulse Energy is set to 0.4 J")
    else:
        test.fail("Pulse Energy mismatch. Actual: " + pulse_energy)
    
    """Verify frequency"""
    frequency = str(waitForObjectExists(
        names.centralWidget_lbValue_FlashableLabel_4
    ).text)
    
    if frequency == "5":
        test.passes("Frequency is set to 5 Hz")
    else:
        test.fail("Frequency mismatch. Actual: " + frequency) 
    
    """Verify left pedal power"""
    power = str(waitForObjectExists(
        names.centralWidget_lbPowerValue_FlashableLabel
    ).text)
    
    if power == "2.0":
        test.passes("Left pedal average power is set to 2.0 W")
    else:
        test.fail("Left pedal average power mismatch. Actual: " + power)
        
    
    """ Attempt to decrease Pulse Energy and verify values"""

    

    reduce_button = waitForObject(names.centralWidget_pbReduce_QPushButton)
    
    for i in range(5):
        if reduce_button.isEnabled():
            clickButton(reduce_button)
            snooze(1)
    
            pulse_energy = str(waitForObjectExists(
                names.centralWidget_lbValue_FlashableLabel_3
            ).text)
    
            test.passes(
                "Pulse Energy after Reduce attempt " + str(i + 1) +
                " is: " + pulse_energy + " J"
            )
    
        else:
            test.passes(
                "Pulse Energy cannot be decreased further. Minimum value: " +
                str(waitForObjectExists(
                    names.centralWidget_lbValue_FlashableLabel_3
                ).text) + " J"
            )
            break
    
    
    
    # Increase Frequency until Average Power reaches 60 W
    
    increase_button = waitForObject(
        names.centralWidget_pbEnlarge_QPushButton_3
    )
    
    for i in range(50):
    
        if not increase_button.isEnabled():
            test.fail("Frequency Increase button is disabled")
            break
    
        clickButton(increase_button)
        snooze(0.5)
    
        pulse_energy = str(waitForObjectExists(
            names.centralWidget_lbValue_FlashableLabel_3
        ).text)
    
        frequency = str(waitForObjectExists(
            names.centralWidget_lbValue_FlashableLabel_4
        ).text)
    
        average_power = float(str(waitForObjectExists(
            names.centralWidget_lbPowerValue_FlashableLabel
        ).text))
    
        test.log(
            "Attempt " + str(i + 1) +
            " | Pulse Energy: " + pulse_energy +
            " J | Frequency: " + frequency +
            " Hz | Average Power: " + str(average_power) + " W"
        )
    
        if abs(average_power - 60.0) < 0.001:
            test.passes("Average Power reached 60 W")
            break
    else:
        test.fail("Average Power did not reach 60 W")
    
    # Final verification
    test.compare(
        float(str(waitForObjectExists(
            names.centralWidget_lbPowerValue_FlashableLabel
        ).text)),
        60.0,
        "Final Average Power is 60 W"
    )
    
    
    
    # Set right pedal Pulse Energy to 0.4 J
    
    for i in range(14):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_3))
    
    
    # Adjust right pedal Frequency
    
    clickButton(waitForObject(names.centralWidget_pbEnlarge_QPushButton_4))
    clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_4))
    
    
    # Verify right pedal Pulse Energy
    
    pulse_energy = str(waitForObjectExists(
        names.centralWidget_lbValue_FlashableLabel
    ).text)
    
    if pulse_energy == "0.4":
        test.passes("Right pedal Pulse Energy is set to 0.4 J")
    else:
        test.fail("Right pedal Pulse Energy mismatch. Actual: " + pulse_energy)
    
    
    # Verify right pedal Frequency
    
    frequency = str(waitForObjectExists(
        names.centralWidget_lbValue_FlashableLabel_2
    ).text)
    
    if frequency == "5":
        test.passes("Right pedal Frequency is set to 5 Hz")
    else:
        test.fail("Right pedal Frequency mismatch. Actual: " + frequency)
    
    
    # Verify right pedal Average Power
    
    power = str(waitForObjectExists(
        names.centralWidget_lbPowerValue_FlashableLabel_2
    ).text)
    
    if power == "2.0":
        test.passes("Right pedal Average Power is set to 2.0 W")
    else:
        test.fail("Right pedal Average Power mismatch. Actual: " + power)
    
    
    # Attempt to decrease right pedal Pulse Energy
    
    reduce_button = waitForObject(
        names.centralWidget_pbReduce_QPushButton_4
    )
    
    for i in range(5):
        if reduce_button.isEnabled():
            clickButton(reduce_button)
            snooze(1)
    
            pulse_energy = str(waitForObjectExists(
                names.centralWidget_lbValue_FlashableLabel
            ).text)
    
            test.passes(
                "Right pedal Pulse Energy after Reduce attempt " +
                str(i + 1) + " is: " + pulse_energy + " J"
            )
        else:
            test.passes(
                "Right pedal Pulse Energy reached minimum value: " +
                str(waitForObjectExists(
                    names.centralWidget_lbValue_FlashableLabel
                ).text) + " J"
            )
            break
    
    
    # Increase right pedal Frequency until Average Power reaches 60 W
    
    increase_button = waitForObject(
        names.centralWidget_pbEnlarge_QPushButton_4
    )
    
    for i in range(50):
    
        if not increase_button.isEnabled():
            test.fail("Right pedal Frequency Increase button is disabled")
            break
    
        clickButton(increase_button)
        snooze(0.5)
    
        pulse_energy = str(waitForObjectExists(
            names.centralWidget_lbValue_FlashableLabel
        ).text)
    
        frequency = str(waitForObjectExists(
            names.centralWidget_lbValue_FlashableLabel_2
        ).text)
    
        average_power = float(str(waitForObjectExists(
            names.centralWidget_lbPowerValue_FlashableLabel_2
        ).text))
    
        test.log(
            "Right pedal attempt " + str(i + 1) +
            " | Pulse Energy: " + pulse_energy +
            " J | Frequency: " + frequency +
            " Hz | Average Power: " + str(average_power) + " W"
        )
    
        if abs(average_power - 60.0) < 0.001:
            test.passes("Right pedal Average Power reached 60 W")
            break
    else:
        test.fail("Right pedal Average Power did not reach 60 W")
    
    
    # Final right pedal Average Power verification
    
    test.compare(
        float(str(waitForObjectExists(
            names.centralWidget_lbPowerValue_FlashableLabel_2
        ).text)),
        60.0,
        "Right pedal Average Power is 60 W"
    )
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    clickButton(waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Test1_ProfileButton))
    snooze(5)
    clickButton(waitForObject(names.question_OK_QPushButton))    
