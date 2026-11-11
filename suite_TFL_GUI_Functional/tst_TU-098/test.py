import names
import test
from squish import *
from common import *


def verify_treatment_screen_visible():
    """
    Verify whether the current Lithotripsy treatment screen is visible.
    The mapped Home button is used as an indicator of the
    treatment screen.

    """
    try:
        home_button = waitForObject(names.frWizardPlace_tbHome_QToolButton,10000)
        visibility = home_button.visible
        is_visible = (
            visibility is True
            or str(visibility).lower() == "true"
            or str(visibility) == "1"
        )
        if is_visible:
            test.passes("PASS: Lithotripsy treatment screen is visible")
        else:
            test.fail("FAIL: Lithotripsy treatment screen is not visible")

        return is_visible

    except Exception as error:
        test.fail("FAIL: Treatment screen verification failed - {}".format(error))
        return False


def return_to_home_screen():
    """
    Return from the current treatment screen to the application
    Home screen using the mapped Home button.
    """
    try:
        clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton,20000))
        test.passes("PASS: Returned to application Home screen")
        return True

    except Exception as error:
        test.fail("FAIL: Unable to return to Home screen - {}".format(error))
        return False


def select_lithotripsy_options(
    stone_size,
    stone_density,
    pedal_x=None,
    pedal_y=None,
    profile_x=None,
    profile_y=None
):
    """
    Select stone size and stone density, apply the profile,
    and optionally click the pedal or profile widget.
    """
    try:
        if not verify_treatment_screen_visible():
            return False

        clickButton(waitForObject(stone_size, 20000))

        test.passes("PASS: Stone size selected successfully")

        clickButton(waitForObject(stone_density, 20000))

        test.passes("PASS: Stone density selected successfully")

        clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton,20000))

        test.passes("PASS: Lithotripsy profile applied successfully")

        if pedal_x is not None and pedal_y is not None:
            mouseClick(
                waitForObject(
                    names.centralWidget_wdLeftPedal_PedalSettingsWidget,
                    20000
                ),
                pedal_x,
                pedal_y,
                Qt.NoModifier,
                Qt.LeftButton
            )

            test.log(
                "Pedal settings widget clicked successfully"
            )

        if profile_x is not None and profile_y is not None:
            mouseClick(
                waitForObject(
                    names.apollo_wdProfile_QWidget,
                    20000
                ),
                profile_x,
                profile_y,
                Qt.NoModifier,
                Qt.LeftButton
            )

            test.log("Profile widget clicked successfully")

        return True

    except Exception as error:
        test.fail("FAIL: Lithotripsy option selection failed - {}".format(error))
        return False


def select_medium_soft_without_apply():
    """
    Select Medium stone size and Soft stone density without applying
    the profile, following the recorded test sequence.
    """
    try:
        if not verify_treatment_screen_visible():
            return False

        clickButton(waitForObject(names.frWizardPlace_Medium_6_10_WizardButton,20000))

        test.passes(
            "PASS: Medium stone size selected"
        )

        clickButton(waitForObject(names.frWizardPlace_Soft_500_WizardButton,20000))

        test.passes("PASS: Soft stone density selected")

        clickButton(waitForObject(names.frWizardPlace_tbHome_QToolButton,20000))

        test.passes("PASS: Returned to Home screen")

        return True

    except Exception as error:
        test.fail("FAIL: Medium + Soft selection failed - {}".format(error))
        return False


def exit_current_profile():
    """
    Exit the currently applied Lithotripsy profile and confirm
    the exit dialog.
    """
    try:
        clickButton(waitForObject(names.apollo_btExitProfile_QPushButton,20000))
        clickButton(waitForObject(names.question_YES_QPushButton,20000))
        test.passes("PASS: Lithotripsy profile exited successfully")

        return True

    except Exception as error:
        test.fail("FAIL: Profile exit failed - {}".format(error))
        return False

def execute_lithotripsy_profiles(
    category,
    navigation_function,
    profile_combinations
):
    """
    Execute the supplied Lithotripsy profile combinations for
    Kidney, Ureter, or Bladder.
    """
    try:
        if not verify_treatment_screen_visible():
            return False
        total_profiles = len(profile_combinations)
        for index, combination in enumerate(profile_combinations):

            profile_number = index + 1
            stone_size = combination[0]
            stone_density = combination[1]
            pedal_x = combination[2]
            pedal_y = combination[3]
            profile_x = combination[4]
            profile_y = combination[5]

            test.log("{} PROFILE {}/{}".format(
                    category,
                    profile_number,
                    total_profiles
                )
            )
            if (
                stone_size == names.frWizardPlace_Medium_6_10_WizardButton
                and stone_density == names.frWizardPlace_Soft_500_WizardButton
            ):
                if not select_medium_soft_without_apply():
                    return False

                navigation_function()

                test.passes("PASS: Navigated back to {} Lithotripsy".format(category))

                if not verify_treatment_screen_visible():
                    return False
                continue
            if not select_lithotripsy_options(
                stone_size,
                stone_density,
                pedal_x=pedal_x,
                pedal_y=pedal_y,
                profile_x=profile_x,
                profile_y=profile_y
            ):
                return False
            if not exit_current_profile():
                return False

            if profile_number < total_profiles:
                navigation_function()

                test.passes("PASS: Navigated back to {} Lithotripsy".format(category))

                if not verify_treatment_screen_visible():
                    return False

        test.passes("PASS: All {} {} Lithotripsy combinations completed".format(total_profiles,category))

        return True

    except Exception as error:
        test.fail("FAIL: {} Lithotripsy profile execution failed - {}".format(category,error))
        raise


def verify_all_kidney_lithotripsy_profiles():
    """
    Execute all 10 recorded Kidney Lithotripsy combinations.
    """
    profiles = [
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            585, 22, None, None
        ),
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            579, 24, None, None
        ),
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 501, 31
        ),
        (
            names.frWizardPlace_Unknown_WizardButton,
            names.frWizardPlace_Unknown_WizardButton_2,
            None, None, 547, 28
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            None, None, None, None
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            585, 29, None, None
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 563, 57
        ),
        (
            names.frWizardPlace_Large_10_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            None, None, None, None
        ),
        (
            names.frWizardPlace_Large_10_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            587, 24, None, None
        ),
        (
            names.frWizardPlace_Large_10_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 568, 54
        )
    ]

    return execute_lithotripsy_profiles(
        "KIDNEY",
        navigate_to_kidney_lithotripsy,
        profiles
    )


def verify_all_ureter_lithotripsy_profiles():
    """
    Execute all 10 recorded Ureter Lithotripsy combinations.
    """
    profiles = [
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            585, 22, None, None
        ),
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            579, 24, None, None
        ),
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 501, 31
        ),
        (
            names.frWizardPlace_Unknown_WizardButton,
            names.frWizardPlace_Unknown_WizardButton_2,
            None, None, 547, 28
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            None, None, None, None
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            585, 29, None, None
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 563, 57
        ),
        (
            names.frWizardPlace_Large_10_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            None, None, None, None
        ),
        (
            names.frWizardPlace_Large_10_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            587, 24, None, None
        ),
        (
            names.frWizardPlace_Large_10_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 568, 54
        )
    ]

    return execute_lithotripsy_profiles(
        "URETER",
        navigate_to_ureter_lithotripsy,
        profiles
    )

def verify_all_bladder_lithotripsy_profiles():
    """
    Execute all 8 Bladder Lithotripsy combinations supplied
    in the recorded test sequence.
    """
    profiles = [
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            585, 22, None, None
        ),
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            579, 24, None, None
        ),
        (
            names.frWizardPlace_Small_6_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 501, 31
        ),
        (
            names.frWizardPlace_Unknown_WizardButton,
            names.frWizardPlace_Unknown_WizardButton_2,
            None, None, 547, 28
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            None, None, None, None
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Medium_500_1000_WizardButton,
            585, 29, None, None
        ),
        (
            names.frWizardPlace_Medium_6_10_WizardButton,
            names.frWizardPlace_Hard_1000_WizardButton,
            None, None, 563, 57
        ),
        (
            names.frWizardPlace_Large_10_WizardButton,
            names.frWizardPlace_Soft_500_WizardButton,
            None, None, None, None
        )
    ]

    return execute_lithotripsy_profiles(
        "BLADDER",
        navigate_to_bladder_lithotripsy,
        profiles
    )



def main():
    """
    Execute Kidney, Ureter, and Bladder Lithotripsy tests.
    """
    test.log("This TC is relate to Lithotripsy SubCategories")
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))
        enterpin()
        test.log("STARTING KIDNEY LITHOTRIPSY TESTS")
        navigate_to_kidney_lithotripsy()
        if not verify_treatment_screen_visible():
            test.fail(
                "FAIL: Kidney Lithotripsy screen is not visible"
            )
            return
        kidney_result = verify_all_kidney_lithotripsy_profiles()
        if not kidney_result:
            test.fail(
                "FAIL: Kidney Lithotripsy tests failed"
            )
            return
        test.passes("PASS: Kidney Lithotripsy tests completed")
        navigate_to_ureter_lithotripsy()
        if not verify_treatment_screen_visible():
            test.fail("FAIL: Ureter Lithotripsy screen is not visible")
            return
        ureter_result = verify_all_ureter_lithotripsy_profiles()
        if not ureter_result:
            test.fail(
                "FAIL: Ureter Lithotripsy tests failed"
            )
            return
        test.passes("PASS: Ureter Lithotripsy tests completed")
        test.log("STARTING BLADDER LITHOTRIPSY TESTS ")
        navigate_to_bladder_lithotripsy()
        if not verify_treatment_screen_visible():
            test.fail("FAIL: Bladder Lithotripsy screen is not visible")
            return
        bladder_result = verify_all_bladder_lithotripsy_profiles()
        if not bladder_result:
            test.fail("FAIL: Bladder Lithotripsy tests failed")
            return
        test.passes("PASS: Bladder Lithotripsy tests completed")
        test.log("Kidney Lithotripsy result: {}".format(kidney_result))

        test.log("Ureter Lithotripsy result: {}".format(ureter_result))

        test.log("Bladder Lithotripsy result: {}".format(bladder_result))

        if kidney_result and ureter_result and bladder_result:
            test.passes("PASS: All Kidney, Ureter, and Bladder Lithotripsy tests completed successfully")
        else:
            test.fail("FAIL: One or more Lithotripsy test groups failed")

    except Exception as error:
        test.fail("FAIL: Main test execution failed - {}".format(error))
        raise
