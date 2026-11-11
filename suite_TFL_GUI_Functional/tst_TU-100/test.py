import names
from common import *

def verify_enucleation_hemostasis_profiles():
    """
    Execute the recorded Enucleation Hemostasis and BPH
    Enucleation Low Power profile sequences.
    """
    try:
        test.log(" ENUCLEATION HEMOSTASIS")
        clickButton(waitForObject(names.frWizardPlace_Enucleation_Hemostasis_WizardButton))
        test.passes("PASS: Enucleation Hemostasis selected")
        clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
        test.passes("PASS: Enucleation Hemostasis profile applied")
        mouseClick(
            waitForObject(
                names.centralWidget_wdLeftPedal_PedalSettingsWidget
            ),
            572, 5, Qt.NoModifier, Qt.LeftButton
        )
        test.passes("PASS: Enucleation Hemostasis pedal configured")
        clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
        clickButton(waitForObject(names.question_YES_QPushButton))
        test.passes("PASS: Enucleation Hemostasis profile exited")
        test.log("BPH ENUCLEATION LOW POWER ")
        navigate_to_bph_enucleation_hemostasis()
        test.passes("PASS: Navigated to BPH Enucleation Hemostasis")
        clickButton(waitForObject(names.frWizardPlace_Enucleation_Low_Power_WizardButton))
        test.passes("PASS: First Enucleation Low Power selection completed")
        clickButton(waitForObject(names.frWizardPlace_Enucleation_Low_Power_WizardButton))
        test.passes("PASS: Second Enucleation Low Power selection completed")
        clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
        test.passes("PASS: Enucleation Low Power profile applied")
        mouseClick(
            waitForObject(
                names.centralWidget_wdLeftPedal_PedalSettingsWidget
            ),
            498, 8, Qt.NoModifier, Qt.LeftButton
        )
        test.passes("PASS: Enucleation Low Power pedal configured")

        sendEvent(
            "QMoveEvent",
            waitForObject(names.apollo_MainWindow),
            151, 149, 758, 181
        )
        test.passes("PASS: Recorded mouse-move event sent")
        clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
        clickButton(waitForObject(names.question_YES_QPushButton))
        test.passes("PASS: Enucleation Low Power profile exited")
        test.passes("PASS: Both Enucleation Hemostasis profiles completed successfully")
        return True

    except Exception as error:
        test.fail("FAIL: Enucleation Hemostasis profile verification failed - {}".format(error))
        raise


def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_bph_enucleation_hemostasis()
    verify_enucleation_hemostasis_profiles()
    