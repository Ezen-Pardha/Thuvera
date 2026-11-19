import names
from squish import *
from common import *


def verify_profile_reduce_settings():
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    test.imagePresent("TU-075_left")
    test.imagePresent("TU-075_Right")
    for _ in range(9):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_2))

    sendEvent(
        "QMouseEvent",
        waitForObject(names.centralWidget_pbReduce_QPushButton_2),
        QEvent.MouseButtonPress,
        46, 35,
        Qt.LeftButton, 1, 0
    )

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
    test.imagePresent("TU-075_Right")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))

    test.log("Profile reduce settings verification completed.")
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_vaporize_hemostasis()
    verify_profile_reduce_settings()

