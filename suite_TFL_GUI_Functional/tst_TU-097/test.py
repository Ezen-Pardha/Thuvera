import names
import test
from squish import *
from common import *

def verify_bph_pedal_options():
    """
    Verify that the BPH Assistant Mode screen provides
    Left Pedal and Right Pedal options.
    """

    try:
        clickButton(waitForObject(names.apollo_tbAssistant_QToolButton,20000))
        test.passes("PASS: Assistant Mode screen opened successfully")

        clickButton(waitForObject(names.frWizardPlace_BPH_WizardButton,20000))
        test.passes("PASS: BPH Assistant screen opened successfully")
        pedal_options_present = False
        try:
            pedal_title = waitForObject(names.frWizardPlace_LEFT_PEDAL_RIGHT_PEDAL_WizardTitle,10000)

            mouseClick(
                pedal_title,
                115,
                20,
                Qt.NoModifier,
                Qt.LeftButton
            )

            test.passes("PASS: Left Pedal click executed successfully")
            mouseClick(
                pedal_title,
                359,
                22,
                Qt.NoModifier,
                Qt.LeftButton
            )
            test.passes("PASS: Right Pedal click executed successfully")
            pedal_options_present = True

        except Exception as error:
            test.fail("FAIL: BPH pedal option verification failed - {}".format(error))
        test.log("BPH Left Pedal and Right Pedal options present: {}".format(pedal_options_present))

        clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton,20000))
        test.passes("PASS: Returned to Home screen successfully")
        if pedal_options_present:
            test.passes("PASS: BPH pedal option verification completed")
        else:
            test.fail("FAIL: BPH pedal option verification failed")

        return pedal_options_present
    except Exception as error:
        test.fail("FAIL: BPH pedal verification failed - {}".format(error))
        raise

def main():
    """
    Execute the BPH pedal option verification test.
    """
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))
        enterpin()
        result = verify_bph_pedal_options()
        test.log("FINAL RESULT - BPH pedal options present: {}".format(result))

        if result:
            test.passes("PASS: BPH pedal verification completed successfully")
        else:
            test.fail("FAIL: BPH pedal verification failed")

    except Exception as error:
        test.fail("FAIL: Main test execution failed - {}".format(error))
        raise