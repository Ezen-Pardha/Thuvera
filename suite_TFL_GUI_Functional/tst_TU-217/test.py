from squish import *
import test
import names
from common import *

def click_and_report(object_name, description):
    try:
        clickButton(waitForObject(object_name, 10000))
        test.log("PASS: " + description)
        return True

    except Exception as e:
        test.log("FAIL: " + description + " | Error: " + str(e))
        return False

def change_pulse_width(button_name, description):

    test.log("Changing " + description + " ")

    try:
        obj = waitForObject(button_name, 10000)

        try:
            previous_value = str(obj.text)
        except:
            previous_value = "Not Available"

        clickButton(obj)
        snooze(1)

        try:
            updated_value = str(obj.text)
        except:
            updated_value = "Not Available"

        test.log("PASS: " + description + " button clicked")
        test.log("Previous Value: " + previous_value)
        test.log("Updated Value: " + updated_value)

        if previous_value != updated_value:
            test.log("PASS: " + description + " value changed successfully")
        else:
            test.log("INFO: No text change detected")

        return True

    except Exception as e:
        test.log("FAIL: " + description + " | Error: " + str(e))
        return False



def exit_profile():

    test.log("EXIT PROFILE")

    if click_and_report(
        names.apollo_btExitProfile_QPushButton,
        "Exit Profile"
    ):

        click_and_report(
            names.question_YES_QPushButton,
            "Confirm YES to exit profile"
        )


def execute_soft_tissue_procedure(procedure_name, procedure_description,
                                  pulse_buttons):


    test.log("STARTING PROCEDURE: " + procedure_description)
    if not click_and_report(
        names.apollo_tbAssistant_QToolButton,
        "Open Assistant"
    ):
        return

    if not click_and_report(
        names.frWizardPlace_Soft_Tissue_WizardButton,
        "Select Soft Tissue"
    ):
        return

    if not click_and_report(
        procedure_name,
        "Select " + procedure_description
    ):
        return

    if not click_and_report(
        names.frWizardPlace_ADVANCE_WizardApplyButton,
        "Apply " + procedure_description
    ):
        return

    test.log(" PULSE WIDTH VERIFICATION")

    for button_name, description in pulse_buttons:

        change_pulse_width(
            button_name,
            description
        )

    exit_profile()
    test.log("COMPLETED PROCEDURE: " + procedure_description)


def main():
    test.log("PULSE WIDTH AUTOMATION TEST STARTED")
    if not click_and_report(
        names.frmPopup_pbAccept_QPushButton,
        "Accept Initial Popup"
    ):
        return
    try:
        enterpin()

    except Exception as e:
        test.log("FAIL: PIN entry failed | Error: " + str(e))
        return

    execute_soft_tissue_procedure(
        names.frWizardPlace_Vaporize_Hemostasis_WizardButton,
        "Vaporize Hemostasis",
        [
            (
                names.centralWidget_btShortPulse_ButtonWithClickSound,
                "Short Pulse"
            ),
            (
                names.centralWidget_btLongPulse_ButtonWithClickSound,
                "Long Pulse"
            )
        ]
    )
    execute_soft_tissue_procedure(
        names.frWizardPlace_Tumor_Hemostasis_WizardButton,
        "Tumor Hemostasis",
        [
            (
                names.centralWidget_btShortPulse_ButtonWithClickSound,
                "Short Pulse 1"
            ),
            (
                names.centralWidget_btLongPulse_ButtonWithClickSound,
                "Long Pulse 1"
            ),
            (
                names.centralWidget_btShortPulse_ButtonWithClickSound_2,
                "Short Pulse 2"
            ),
            (
                names.centralWidget_btLongPulse_ButtonWithClickSound_2,
                "Long Pulse 2"
            )
        ]
    )

    execute_soft_tissue_procedure(
        names.frWizardPlace_Incision_Hemostasis_WizardButton,
        "Incision Hemostasis",
        [
            (
                names.centralWidget_btShortPulse_ButtonWithClickSound,
                "Short Pulse 1"
            ),
            (
                names.centralWidget_btLongPulse_ButtonWithClickSound,
                "Long Pulse 1"
            ),
            (
                names.centralWidget_btShortPulse_ButtonWithClickSound_2,
                "Short Pulse 2"
            ),
            (
                names.centralWidget_btLongPulse_ButtonWithClickSound_2,
                "Long Pulse 2"
            )
        ]
    )
