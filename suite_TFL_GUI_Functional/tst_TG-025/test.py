# -*- coding: utf-8 -*-

import names
from common import *


def verify_result(description, condition):
    if condition:
        test.passes(description)
    else:
        test.fail(description)


def main():

    enterpin()

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))

    # Step 1: Open Assistant Mode
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    snooze(1)

    verify_result(
        "Assistant Mode screen displayed",
        waitForObjectExists(names.frWizardPlace_Lithotripsy_WizardButton).visible
    )

    # Lithotripsy - Kidney - Small 6
    clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Kidney_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Small_6_WizardButton))

    mouseClick(
        waitForObject(names.frWizardPlace_Title_QLabel),
        299, 35, Qt.NoModifier, Qt.LeftButton
    )

    advance = waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton)
    verify_result("Lithotripsy - Advance button enabled", advance.enabled)

    clickButton(advance)
    snooze(2)

    verify_result(
        "Lithotripsy - Treatment screen displayed",
        waitForObjectExists(names.centralWidget_wdLeftPedal_PedalSettingsWidget).visible
    )

    mouseClick(
        waitForObject(names.centralWidget_wdLeftPedal_PedalSettingsWidget),
        562, 131, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.centralWidget_wdRightPedal_PedalSettingsWidget),
        105, 129, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))

    # Soft Tissue - Tumor Hemostasis
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostasis_WizardButton))

    mouseClick(
        waitForObject(names.frWizardPlace_Title_QLabel),
        104, 32, Qt.NoModifier, Qt.LeftButton
    )

    advance = waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton)
    verify_result("Soft Tissue - Advance button enabled", advance.enabled)

    clickButton(advance)
    snooze(2)

    verify_result(
        "Soft Tissue - Treatment screen displayed",
        waitForObjectExists(names.centralWidget_wdLeftPedal_PedalSettingsWidget).visible
    )

    mouseClick(
        waitForObject(names.centralWidget_lbHeader_QLabel_2),
        266, 6, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.centralWidget_wdRightPedal_PedalSettingsWidget),
        134, 131, Qt.NoModifier, Qt.LeftButton
    )

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))

    # BPH - Enucleation Low Power
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Enucleation_Low_Power_WizardButton))

    mouseClick(
        waitForObject(names.frWizardPlace_Title_QLabel),
        137, 33, Qt.NoModifier, Qt.LeftButton
    )

    advance = waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton)
    verify_result("BPH - Advance button enabled", advance.enabled)

    clickButton(advance)
    snooze(2)

    verify_result(
        "BPH - Treatment screen displayed",
        waitForObjectExists(names.centralWidget_wdLeftPedal_PedalSettingsWidget).visible
    )

    mouseClick(
        waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget),
        431, 2, Qt.NoModifier, Qt.LeftButton
    )

    mouseClick(
        waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget_2),
        204, 7, Qt.NoModifier, Qt.LeftButton
    )