
from common import *
import names


def verify_button_selection(previous_button, current_button):

    previous = waitForObject(previous_button)
    current = waitForObject(current_button)

    test.verify(
        current.checked == True,
        "PASS: Current button is highlighted"
    )

def verify_lithotripsy_button_selection():

    lithotripsy = waitForObject(names.frWizardPlace_Lithotripsy_WizardButton)
    clickButton(lithotripsy)

    test.verify(
        lithotripsy.checked == True,
        "PASS: Lithotripsy is highlighted after selection"
    )

    kidney = waitForObject(names.frWizardPlace_Kidney_WizardButton)
    clickButton(kidney)

    verify_button_selection(
        names.frWizardPlace_Lithotripsy_WizardButton,
        names.frWizardPlace_Kidney_WizardButton
    )


def select_options():
    """
    Selection verification:
    Each new option should become highlighted when selected.
    The previously selected option in the same category should
    no longer be highlighted.
    """

    clickButton(waitForObject(names.frWizardPlace_Ureter_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Bladder_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Small_6_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Medium_6_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Large_10_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Unknown_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_500_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Hard_1000_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Unknown_WizardButton_2))
    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Incision_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enucleation_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enucleation_Low_Power_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton))



def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    test.imagePresent("Assistant_page")
    verify_lithotripsy_button_selection()
    select_options()
