import names
import test
from squish import *
from common import *
def verify_page(object_name, page_name):
    """
    WHEN a page or UI element is expected to be visible,
    THEN verify that its mapped object exists.
    """
    try:
        waitForObject(object_name, 20000)
        test.passes("PASS: {} is present".format(page_name))
        return True

    except Exception as error:
        test.fail(
            "FAIL: {} verification failed - {}".format(
                page_name, error        # Verify Settings Page
            )
        )
        raise
    
def home_page():
    """
    WHEN the Default Profile Home Page is required,
    THEN select the Default Profile and open its main page.
    """
    try:
        test.log("Opening Default Profile Home Page")

        clickButton(
            waitForObject(names.sclProfiles_Default_ProfileButton)
        )

        mouseClick(
            waitForObject(names.apollo_wdProfile_QWidget),
            545, 34,
            Qt.NoModifier,
            Qt.LeftButton
        )

        verify_page(
            names.apollo_wdProfile_QWidget,
            "Default Profile Home Page"
        )

        test.passes("PASS: Default Profile Home Page opened")
        return True

    except Exception as error:
        test.fail("FAIL: Home Page - {}".format(error))
        raise


def pedal_settings_page():
    """
    WHEN the Pedal Settings Page is required,
    THEN open Pedal Settings and verify its UI object.
    """
    try:
        test.log("Opening Pedal Settings Page")

        mouseClick(
            waitForObject(
                names.centralWidget_wdLeftPedal_PedalSettingsWidget
            ),
            284, 27,
            Qt.NoModifier,
            Qt.LeftButton
        )

        verify_page(
            names.centralWidget_wdLeftPedal_PedalSettingsWidget,
            "Pedal Settings Page"
        )

        test.passes("PASS: Pedal Settings Page opened")
        return True

    except Exception as error:
        test.fail("FAIL: Pedal Settings Page - {}".format(error))
        raise


def presets_page():
    """
    WHEN the Presets Page is required,
    THEN select the Default Profile and open Presets.
    """
    try:
        test.log("Opening Presets Page")

        clickButton(
            waitForObject(names.sclProfiles_Default_ProfileButton)
        )

        clickButton(
            waitForObject(names.apollo_btPresets_QPushButton)
        )

        mouseClick(
            waitForObject(names.apollo_lbScreenTitle_QLabel),
            611, 15,
            Qt.NoModifier,
            Qt.LeftButton
        )

        verify_page(
            names.apollo_lbScreenTitle_QLabel,
            "Presets Page"
        )

        test.passes("PASS: Presets Page opened")
        return True

    except Exception as error:
        test.fail("FAIL: Presets Page - {}".format(error))
        raise


def treatmentlogs_page():
    """
    WHEN the Treatment Logs Page is required,
    THEN select the Default Profile and open Treatment Logs.
    """
    try:
        test.log("Opening Treatment Logs Page")

        clickButton(
            waitForObject(names.sclProfiles_Default_ProfileButton)
        )

        clickButton(
            waitForObject(names.apollo_btTreatmentLogs_QPushButton)
        )

        mouseClick(
            waitForObject(names.apollo_lbHeader_QLabel),
            537, 17,
            Qt.NoModifier,
            Qt.LeftButton
        )

        verify_page(
            names.apollo_lbHeader_QLabel,
            "Treatment Logs Page"
        )

        test.passes("PASS: Treatment Logs Page opened")
        return True

    except Exception as error:
        test.fail("FAIL: Treatment Logs Page - {}".format(error))
        raise


def settings_page():
    """
    WHEN the Settings Page is required,
    THEN open Settings and verify Speaker Volume and Display Brightness.
    """
    try:
        test.log("Opening Settings Page")

        clickButton(
            waitForObject(names.sclProfiles_Default_ProfileButton)
        )

        clickButton(
            waitForObject(names.apollo_btSettings_QPushButton)
        )

        mouseClick(
            waitForObject(names.apollo_lbHeader_QLabel),
            256, 27,
            Qt.NoModifier,
            Qt.LeftButton
        )

        verify_page(
            names.apollo_lbHeader_QLabel,
            "Settings Page"
        )
        verify_page(
            names.centralWidget_lbVolume_QLabel,
            "Speaker Volume"
        )
        verify_page(
            names.centralWidget_lbBrightness_QLabel,
            "Display Brightness"
        )

        test.passes(
            "PASS: Settings Page contains Speaker Volume "
            "and Display Brightness"
        )

        return True

    except Exception as error:
        test.fail("FAIL: Settings Page - {}".format(error))
        raise


def utilities_page():
    """
    WHEN the Utilities Page is required,
    THEN select the Default Profile and open Utilities.
    """
    try:
        test.log("Opening Utilities Page")

        clickButton(
            waitForObject(names.sclProfiles_Default_ProfileButton)
        )

        clickButton(
            waitForObject(names.apollo_btUtilities_QPushButton)
        )

        mouseClick(
            waitForObject(names.apollo_lbHeader_QLabel),
            101, 16,
            Qt.NoModifier,
            Qt.LeftButton
        )

        verify_page(
            names.apollo_lbHeader_QLabel,
            "Utilities Page"
        )

        test.passes("PASS: Utilities Page opened")
        return True

    except Exception as error:
        test.fail("FAIL: Utilities Page - {}".format(error))
        raise


def exit_page():
    """
    WHEN an opened Default Profile page needs to be closed,
    THEN click Exit Profile and confirm using YES.
    """
    try:
        test.log("Exiting Current Profile Page")

        clickButton(
            waitForObject(names.apollo_btExitProfile_QPushButton)
        )

        clickButton(
            waitForObject(names.question_YES_QPushButton)
        )

        test.passes("PASS: Current Profile Page exited successfully")
        return True

    except Exception as error:
        test.fail("FAIL: Exiting Current Page - {}".format(error))
        raise


def exit_home_page():
    """
    WHEN the Default Profile Home Page needs to be exited,
    THEN select the profile and confirm the exit.
    """
    try:
        test.log("Exiting Default Profile Home Page")

        clickButton(
            waitForObject(names.sclProfiles_Default_ProfileButton)
        )

        clickButton(
            waitForObject(names.apollo_btExitProfile_QPushButton)
        )

        mouseClick(
            waitForObject(names.question_TextLabel_QLabel),
            113, 21,
            Qt.NoModifier,
            Qt.LeftButton
        )

        mouseClick(
            waitForObject(names.apollo_Question_MessageBox),
            70, 86,
            Qt.NoModifier,
            Qt.LeftButton
        )

        clickButton(
            waitForObject(names.question_YES_QPushButton)
        )

        test.passes(
            "PASS: Default Profile Home Page exited"
        )
        return True

    except Exception as error:
        test.fail(
            "FAIL: Exiting Default Profile Home Page - {}".format(error)
        )
        raise

def main():
    """Navigate through and verify all Default Profile pages."""
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
        enterpin()
        home_page()
        pedal_settings_page()
        exit_page()
        presets_page()
        exit_page()
        treatmentlogs_page()
        exit_page()
        settings_page()
        exit_page()
        utilities_page()
        exit_page()
        exit_home_page()
        test.passes("PASS: All Default Profile pages navigated successfully")
        test.log("DEFAULT PROFILE PAGE TEST COMPLETED")
    except Exception as error:
        test.fail("FAIL: Default Profile Page Test - {}".format(error))
        raise
