import names
from squish import *
from common import *
  
def verify_profile_dropdown_and_cancel_settings():

    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbLogo_QLabel),
               41, 28, Qt.NoModifier, Qt.LeftButton)
    test.log("First dropdown opened.")

    mouseClick(waitForObject(names.frmComboBoxHeader_lbLogo_QLabel),
               41, 27, Qt.NoModifier, Qt.LeftButton)
    test.log("Second dropdown opened.")
    for _ in range(3):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_3))

    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    test.log("Clicked CANCEL on the exit popup. The profile values were not changed.")

    for _ in range(3):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))

    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_NO_QPushButton))
    test.log("Clicked CANCEL on the exit popup. The profile values were not changed.")

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))

    mouseClick(waitForObject(names.apollo_Question_MessageBox),
               96, 86, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.apollo_YES_QPushButton))

    test.log("Profile dropdown and reduce settings verification completed.")  
  
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_vaporize_hemostasis()
    verify_profile_dropdown_and_cancel_settings()