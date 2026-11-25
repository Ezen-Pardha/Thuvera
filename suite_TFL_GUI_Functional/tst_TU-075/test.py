import names
from squish import *
from common import *


def verify_profile_reduce_settings():
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
    clickButton(waitForObject(names.apollo_YES_QPushButton))

    test.log("Profile reduce settings verification completed.")
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_vaporize_hemostasis()
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    test.compare(waitForObjectExists(names.centralWidget_comboBox_ComboBox).visible, True)
    test.compare(waitForObjectExists(names.centralWidget_comboBox_ComboBox_2).visible, True)
    verify_profile_reduce_settings()


