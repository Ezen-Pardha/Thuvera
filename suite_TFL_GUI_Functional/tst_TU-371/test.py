import names
from common import *
import test

def create_profile(profile_name):
    """
    Create a new profile, handle existing-profile warnings, and report the result.
    """
    try:
        test.log("Creating profile: {}".format(profile_name))

        clickButton(
            waitForObject(names.frToolbar_tbAddProfile_QToolButton)
        )

        for char in profile_name.lower():
            if not char.isalpha():
                raise ValueError(
                    "Only alphabetic profile names are supported."
                )

            key_object = getattr(
                names,
                "keyboardFrame_{}_KeyButtonLetter".format(char)
            )

            clickButton(waitForObject(key_object))

        clickButton(
            waitForObject(names.keyboardFrame_Enter_KeyButtonEnter)
        )

        if object.exists(names.warning_OK_QPushButton):

            clickButton(
                waitForObject(names.warning_OK_QPushButton)
            )

            clickButton(
                waitForObject(names.keyboardFrame_Cancel_KeyButtonCancel)
            )

            test.log(
                "PROFILE ALREADY EXISTS: {}".format(profile_name)
            )

            return False

        test.passes(
            "PASS: Profile creation submitted - {}".format(profile_name)
        )

        return True

    except Exception as error:
        test.fail(
            "FAIL: Profile creation failed - {}".format(error)
        )
        raise

def edit_thuvera_profile():
    """
    Edit the Thuvera profile.

    """
    try:
        clickButton(waitForObject(
            names.frToolbar_tbEditProfile_QToolButton
        ))
        test.passes("PASS: Click Edit Profile")

        clickButton(waitForObject(
            names.sclProfiles_thuvera_ProfileButton
        ))
        test.passes("PASS: Select Thuvera Profile")

        clickButton(waitForObject(
            names.editFrame_tbClear_QToolButton
        ))
        test.passes("PASS: Clear Profile")

        clickButton(waitForObject(
            names.keyboardFrame_Enter_KeyButtonEnter
        ))
        test.passes("PASS: Press Enter")

        mouseClick(
            waitForObject(names.warning_TextLabel_QLabel),
            406, 94,
            Qt.NoModifier,
            Qt.LeftButton
        )
        test.passes("PASS: Click Warning Message")

        clickButton(waitForObject(
            names.warning_OK_QPushButton
        ))
        test.passes("PASS: Confirm Warning")

        clickButton(waitForObject(
            names.keyboardFrame_Cancel_KeyButtonCancel
        ))
        test.passes("PASS: Cancel Keyboard")

        test.passes(
            "PASS: Thuvera profile editing completed successfully"
        )
        return True

    except Exception as error:
        test.fail(
            "FAIL: Thuvera profile editing failed - {}".format(error)
        )
        raise


def main():
    test.log("This TC contain TU-371")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    create_profile("thuvera")
    edit_thuvera_profile()