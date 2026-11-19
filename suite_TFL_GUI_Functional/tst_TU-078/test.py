# -*- coding: utf-8 -*-
import names
from squish import *
from common import *


def verify_reduce_profile_mode():

    clickButton(
        waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton)
    )

    clickButton(
        waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton)
    )
    mouseClick(
        waitForObject(names.apollo_wdProfile_QWidget),
        538, 53,
        Qt.NoModifier,
        Qt.LeftButton
    )
    for i in range(6):
        clickButton(
            waitForObject(names.centralWidget_pbReduce_QPushButton)
        )

    test.imagePresent("Exit_mode")

    clickButton(waitForObject(names.apollo_YES_QPushButton))
    test.imagePresent("custom_widget")
    for i in range(4):
        clickButton(
            waitForObject(names.centralWidget_pbReduce_QPushButton_2)
        )
    sendEvent(
        "QMouseEvent",
        waitForObject(names.centralWidget_pbReduce_QPushButton_2),
        QEvent.MouseButtonPress,
        45, 43,
        Qt.LeftButton,
        1, 0
    )

    for i in range(4):
        clickButton(
            waitForObject(names.centralWidget_pbReduce_QPushButton_4)
        )
    test.imagePresent("Exit_mode")

    clickButton(waitForObject(names.apollo_YES_QPushButton))
    test.imagePresent("custom_widget",{"occurrence": 2})
    clickButton(
        waitForObject(names.apollo_btExitProfile_QPushButton)
    )

    clickButton(
        waitForObject(names.apollo_YES_QPushButton)
    )



def verify_ureter_medium_profile():
    clickButton(
        waitForObject(names.apollo_tbAssistant_QToolButton)
    )
    clickButton(
        waitForObject(names.frWizardPlace_Lithotripsy_WizardButton)
    )

    clickButton(
        waitForObject(names.frWizardPlace_Ureter_WizardButton)
    )

    clickButton(
        waitForObject(names.frWizardPlace_Medium_6_10_WizardButton)
    )

    clickButton(
        waitForObject(names.frWizardPlace_Medium_500_1000_WizardButton)
    )

    clickButton(
        waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton)
    )
    for i in range(4):
        clickButton(
            waitForObject(names.centralWidget_pbReduce_QPushButton_2)
        )
    test.imagePresent("Exit_mode")

    clickButton(
        waitForObject(names.apollo_YES_QPushButton)
    )
    test.imagePresent("custom_widget")
    
    for i in range(6):
        clickButton(
            waitForObject(names.centralWidget_pbReduce_QPushButton_3)
        )
    test.imagePresent("Exit_mode")

    clickButton(
        waitForObject(names.apollo_YES_QPushButton)
    )
    test.imagePresent("custom_widget",{"occurrence": 2})

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_ureter_lithotripsy()

    clickButton(waitForObject(names.frWizardPlace_Medium_6_10_WizardButton))
    verify_reduce_profile_mode()
    verify_ureter_medium_profile()

    # test.breakpoint()
    
