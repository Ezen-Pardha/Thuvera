import names
import test
from squish import *
from common import *

def verify_all_hemostasis_profiles():
    """
    Execute the recorded Vaporize, Tumor, and Incision Hemostasis
    profile test sequences.
    """
    try:
        test.log("VAPORIZE HEMOSTASIS ")

        clickButton(waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton))
        test.passes("PASS: Vaporize Hemostasis selected")

        clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
        test.passes("PASS: Vaporize Hemostasis profile applied")

        mouseClick(
            waitForObject(
                names.centralWidget_wdLeftPedal_PedalSettingsWidget
            ),
            584, 19, Qt.NoModifier, Qt.LeftButton
        )
        test.passes("PASS: Vaporize Hemostasis pedal configured")

        clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))

        clickButton(waitForObject(names.question_YES_QPushButton))
        test.passes("PASS: Vaporize Hemostasis profile exited")
        test.log("========== TUMOR HEMOSTASIS ==========")
        navigate_to_tumor_hemostasis()
        test.passes("PASS: Navigated to Tumor Hemostasis")
        clickButton(waitForObject(names.frWizardPlace_Tumor_Hemostasis_WizardButton))
        test.passes("PASS: Tumor Hemostasis selected")
        clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
        test.passes("PASS: Tumor Hemostasis profile applied")
        mouseClick(
            waitForObject(
                names.centralWidget_wdLeftPedal_PedalSettingsWidget
            ),
            585, 11, Qt.NoModifier, Qt.LeftButton
        )
        test.passes("PASS: Tumor Hemostasis pedal configured")
        clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
        clickButton(waitForObject(names.question_YES_QPushButton))
        test.passes("PASS: Tumor Hemostasis profile exited")
        test.log("INCISION HEMOSTASIS ")
        navigate_to_incision_hemostasis()
        test.passes("PASS: Navigated to Incision Hemostasis")
        clickButton(waitForObject(names.frWizardPlace_Incision_Hemostasis_WizardButton))
        test.passes("PASS: Incision Hemostasis selected")
        clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
        test.passes("PASS: Incision Hemostasis profile applied")
        mouseClick(
            waitForObject(names.centralWidget_standby_QWidget),
            597, 6, Qt.NoModifier, Qt.LeftButton
        )
        test.passes("PASS: Incision Hemostasis standby configured")
        clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
        clickButton(waitForObject(names.question_YES_QPushButton))
        test.passes("PASS: Incision Hemostasis profile exited")
        test.passes("PASS: All three Hemostasis profiles completed successfully")
        return True

    except Exception as error:
        test.fail("FAIL: Hemostasis profile verification failed - {}".format(error))
        raise
    
def main():
    """
    Accept the initial popup, enter the PIN, and execute
    all Hemostasis profile tests.
    """
    test.log("This TC softTissues And SubCategory")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_vaporize_hemostasis()
    verify_all_hemostasis_profiles()
