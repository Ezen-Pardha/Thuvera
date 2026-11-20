from common import *
import names

def bph_select_pulse_settings():
    """
    Selects BPH Wizard settings and configures pulse options.

    """

    test.log("PULSE SETTINGS CONFIGURATION STARTED ")

    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    test.log("PASS: Assistant opened")
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    test.log("PASS: BPH Wizard selected")

    clickButton(
        waitForObject(
            names.frWizardPlace_Enucleation_Low_Power_WizardButton
        )
    )
    test.log("PASS: Enucleation Low Power selected")

    clickButton(
        waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton)
    )
    test.log("PASS: ADVANCE settings applied")

    snooze(1)

    test.log("FIRST PULSE SET")

    clickButton(
        waitForObject(names.centralWidget_btShortPulse_ButtonWithClickSound)
    )
    test.log("PASS: Short Pulse selected (First Set)")

    clickButton(
        waitForObject(names.centralWidget_btMiddlePulse_ButtonWithClickSound)
    )
    test.log("PASS: Middle Pulse selected (First Set)")

    clickButton(
        waitForObject(names.centralWidget_btLongPulse_ButtonWithClickSound)
    )
    test.log("PASS: Long Pulse selected (First Set)")
    test.log(" SECOND PULSE SET")

    clickButton(
        waitForObject(names.centralWidget_btShortPulse_ButtonWithClickSound_2)
    )
    test.log("PASS: Short Pulse selected (Second Set)")

    clickButton(
        waitForObject(names.centralWidget_btMiddlePulse_ButtonWithClickSound_2)
    )
    test.log("PASS: Middle Pulse selected (Second Set)")

    clickButton(
        waitForObject(names.centralWidget_btLongPulse_ButtonWithClickSound_2)
    )
    test.log("PASS: Long Pulse selected (Second Set)")

    test.log(" PULSE SETTINGS CONFIGURATION COMPLETED")
    
def main():
    clickButton(
        waitForObject(names.frmPopup_pbAccept_QPushButton)
    )
    enterpin()
    bph_select_pulse_settings()
