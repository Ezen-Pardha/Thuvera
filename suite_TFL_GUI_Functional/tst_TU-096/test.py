import names
import test
from squish import *
from common import *


def verify_soft_tissue_pedal_options():
    """
    Verify that the Soft Tissue Assistant Mode screen
    provides Left Pedal and Right Pedal options.
    """

    try:
        clickButton(waitForObject(names.apollo_tbAssistant_QToolButton,20000))
        test.passes("PASS: Assistant Mode screen opened successfully")
        clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton,20000))
        test.passes("PASS: Soft Tissue Assistant screen opened")
        pedal_options_present = False
        try:
            pedal_title = waitForObject(names.frWizardPlace_LEFT_PEDAL_RIGHT_PEDAL_WizardTitle,10000)
            test.log("Option: Left Pedal")
            mouseClick(
                pedal_title,
                108,
                18,
                Qt.NoModifier,
                Qt.LeftButton
            )
            test.passes("PASS: Left Pedal option is available")
            test.log("Option: Right Pedal")
            mouseClick(
                pedal_title,
                372,
                16,
                Qt.NoModifier,
                Qt.LeftButton
            )
            test.passes("PASS: Right Pedal option is available")
            pedal_options_present = True
        except Exception as error:
            test.fail("FAIL: Pedal option verification failed - {}".format(error))
        test.log("Left Pedal and Right Pedal options present: {}".format(pedal_options_present))
        clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton,20000))
        test.passes("PASS: Returned to Home screen successfully"
        )
        if pedal_options_present:
            test.passes("PASS: Soft Tissue provides Left Pedal and Right Pedal options")
        else:
            test.fail(
                "FAIL: Soft Tissue pedal options are not available"
            )
        return pedal_options_present
    except Exception as error:
        test.fail("FAIL: Soft Tissue pedal verification failed - {}".format(error))
    raise

def main():
    """
    Execute the Soft Tissue pedal option verification test.
    """
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))
        enterpin()
        result = verify_soft_tissue_pedal_options()
        test.log("FINAL RESULT - Both pedal options present: {}".format(result))
        
        if result:
            test.passes("PASS: Soft Tissue pedal verification completed"
            )
            
        else:
            test.fail("FAIL: Soft Tissue pedal verification failed")

    except Exception as error:
        test.fail("FAIL: Main test execution failed - {}".format(error))
        raise
