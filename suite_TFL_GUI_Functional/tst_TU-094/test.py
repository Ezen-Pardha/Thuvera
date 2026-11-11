import names
import test
from squish import *
from common import *

def verify_bph_treatment():
    """
    Verify whether the BPH treatment type is present
    in Assistant mode.
    """
    try:
        clickButton(waitForObject(names.apollo_tbAssistant_QToolButton,20000))
        test.log("Assistant mode opened successfully")
        bph_present = False
        try:
            bph_button = waitForObject(names.frWizardPlace_BPH_WizardButton,5000)
            visibility = bph_button.visible
            bph_present = (
                visibility is True
                or str(visibility).lower() == "true"
                or str(visibility) == "1"
            )
        except Exception as error:
            test.log("BPH object lookup failed: {}".format(error))
            bph_present = False
        test.log("Treatment type: BPH")
        test.log("BPH present: {}".format(bph_present))
        if bph_present:
            test.passes("PASS: BPH treatment type is present in Assistant mode")
            clickButton(bph_button)
            test.passes("PASS: BPH treatment type selected successfully")
            clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton,20000))
            test.passes("PASS: Returned to Home screen successfully")
            return True
        else:
            test.fail("FAIL: BPH treatment type is not present")
            return False
    except Exception as error:
        test.fail(
            "FAIL: BPH treatment verification failed - {}".format(
                error
            )
        )
        raise

def main():
    """
    Execute the BPH treatment verification test.
    """
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))
        enterpin()
        bph_status = verify_bph_treatment()
        test.log("BPH present: {}".format(bph_status))
        if bph_status:
            test.passes("PASS: BPH verification completed successfully")
        else:
            test.fail("FAIL: BPH treatment type is unavailable")
    except Exception as error:
        test.fail("FAIL: Main test execution failed - {}".format(error))
        raise