
import names
import test

from squish import *
from common import *


def verify_lithotripsy_assistant_options():
    """
    Verify that the Lithotripsy Assistant Mode screen
    displays the required options.
    """
    try:
        clickButton(waitForObject(names.apollo_tbAssistant_QToolButton,20000))
        test.passes("PASS: Assistant Mode screen opened successfully")
        clickButton(waitForObject(names.frWizardPlace_Lithotripsy_WizardButton,20000))
        test.passes("PASS: Lithotripsy Assistant screen opened")
        location_present = False
        stone_size_present = False
        stone_density_present = False
        try:
            location = waitForObject(names.frWizardPlace_LOCATION_WizardTitle,1000)
            mouseClick(location,128,27,Qt.NoModifier,Qt.LeftButton)
            location_present = True
            test.log("Option: Location")
            test.passes("PASS: Location option is available")
        except Exception as error:
            test.fail("FAIL: Location option is not available - {}".format(error))
        try:
            stone_size = waitForObject(names.frWizardPlace_STONE_SIZE_MM_WizardTitle,1000)
            mouseClick(stone_size,77,19,Qt.NoModifier,Qt.LeftButton)
            stone_size_present = True
            test.log("Option: Stone Size")
            test.passes("PASS: Stone Size option is available")
        except Exception as error:
            test.fail("FAIL: Stone Size option is not available - {}".format(error))
        try:
            stone_density = waitForObject(names.frWizardPlace_STONE_DENSITY_HU_WizardTitle,10000)
            mouseClick(stone_density,162,26,Qt.NoModifier,Qt.LeftButton)
            stone_density_present = True
            test.log("Option: Stone Density")
            test.passes("PASS: Stone Density option is available")
            clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton,20000))
    
        except Exception as error:
            test.fail("FAIL: Stone Density option is not available - {}".format(error))
        all_options_present = (
            location_present
            and stone_size_present
            and stone_density_present
        )

        test.log("Location present: {}".format(location_present))
        test.log("Stone Size present: {}".format(stone_size_present))
        test.log("Stone Density present: {}".format(stone_density_present))
        test.log("Final verification result: {}".format(all_options_present))

        if all_options_present:
            test.passes("PASS: Assistant Mode provides Location, Stone Size, and Stone Density options")
        else:
            test.fail("FAIL: One or more required Assistant Mode options are missing")
        return all_options_present
    except Exception as error:
        test.fail("FAIL: Lithotripsy Assistant Mode verification failed - {}".format(error))
        raise


def main():
    """
    Execute the Lithotripsy Assistant Mode verification test.
    """

    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))
        enterpin()
        test.passes("PASS: Application PIN entered successfully")
        result = verify_lithotripsy_assistant_options()
        test.log("FINAL RESULT - All required options present: {}".format(result))

        if result:
            test.passes("PASS: Lithotripsy Assistant Mode verification completed")
        else:
            test.fail("FAIL: Lithotripsy Assistant Mode verification failed")

    except Exception as error:
        test.fail("FAIL: Main test execution failed - {}".format(error))
        raise
