
import names
import test

from squish import *
from common import *


def verify_soft_tissue_treatment():
    """
    Verify whether Soft Tissue treatment type is present
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
        soft_tissue_present = False

        try:
            soft_tissue = waitForObject(
                names.frWizardPlace_Soft_Tissue_WizardButton,
                5000
            )
            visibility = soft_tissue.visible

            soft_tissue_present = (
                visibility is True
                or str(visibility).lower() == "true"
                or str(visibility) == "1"
            )
        except Exception as error:
            test.log(
                "Soft Tissue object lookup failed: {}".format(
                    error
                )
            )
            soft_tissue_present = False
        test.log("Treatment type: Soft Tissue")
        test.log(
            "Soft Tissue present: {}".format(
                soft_tissue_present
            )
        )
        if soft_tissue_present is True:

            test.passes(
                "PASS: Soft Tissue treatment type is present in Assistant mode"
            )
            clickButton(soft_tissue)

            test.passes(
                "PASS: Soft Tissue treatment type selected successfully"
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
                "FAIL: Soft Tissue treatment type is not present"
            )
            return False
    except Exception as error:
        test.fail(
            "FAIL: Soft Tissue treatment verification failed - {}".format(
                error
            )
        )
        raise

def main():
    """
    Execute the Soft Tissue treatment verification test.
    """

    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))
        enterpin()
        test.passes("PASS: Application PIN entered successfully")
        soft_tissue_status = verify_soft_tissue_treatment()
        test.log("FINAL RESULT - Soft Tissue Present: {}".format(soft_tissue_status))
        if soft_tissue_status is True:
            test.passes("PASS: Soft Tissue verification completed successfully")
        else:
            test.fail("FAIL: Soft Tissue treatment type is unavailable")
    except Exception as error:
        test.fail("FAIL: Main test execution failed - {}".format(
                error
            )
        )
        raise
