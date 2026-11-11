import names
import test
from squish import *
from common import *

def verify_lithotripsy_treatment():
    """
    Verify whether Lithotripsy treatment type is present
    in Assistant mode.
    """
    try:
        clickButton(
            waitForObject(
                names.apollo_tbAssistant_QToolButton,
                20000
            )
        )
        test.log("Assistant mode opened successfully")
        lithotripsy_present = False
        try:
            lithotripsy = waitForObject(
                names.frWizardPlace_Lithotripsy_WizardButton,
                5000
            )
            visibility = lithotripsy.visible
            lithotripsy_present = (
                visibility is True
                or str(visibility).lower() == "true"
                or str(visibility) == "1"
            )
        except Exception as error:
            test.log(
                "Lithotripsy object lookup failed: {}".format(
                    error
                )
            )

            lithotripsy_present = False
        test.log("Treatment type: Lithotripsy")
        test.log(
            "Lithotripsy present: {}".format(
                lithotripsy_present
            )
        )

        if lithotripsy_present is True:

            test.passes(
                "PASS: Lithotripsy treatment type is present in Assistant mode"
            )

            clickButton(lithotripsy)
            test.log(
                "Selected treatment type: Lithotripsy"
            )

            test.passes(
                "PASS: Lithotripsy treatment type selected successfully"
            )
            clickButton(
                waitForObject(
                    names.frWizardPlace_tbHome_QToolButton,
                    20000
                )
            )
            test.passes(
                "PASS: Returned to Home screen successfully"
            )
            return True
        else:
            test.fail(
                "FAIL: Lithotripsy treatment type is not present"
            )
            return False
    except Exception as error:
        test.fail(
            "FAIL: Lithotripsy verification failed - {}".format(
                error
            )
        )
        raise

def main():
    """
    Execute Lithotripsy treatment verification.
    """
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))
        enterpin()
        lithotripsy_status = verify_lithotripsy_treatment()
        test.log("Treatment type: Lithotripsy")
        test.log("FINAL RESULT - Lithotripsy Present: {}".format(lithotripsy_status))
        if lithotripsy_status is True:
            test.passes("PASS: Lithotripsy treatment verification completed successfully")
        else:
            test.fail("FAIL: Lithotripsy treatment type is unavailable")
    except Exception as error:
        test.fail("FAIL: Main test execution failed - {}".format(error))
        raise
