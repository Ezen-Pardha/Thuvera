from common import *
import names
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

  
def edit_profile(profile_name):
    """
    Edit an existing profile using the supplied profile name.
    """
    try:
        if not profile_name or not profile_name.strip():
            raise ValueError("Profile name cannot be empty")

        profile_name = profile_name.strip()
        clickButton(waitForObject(names.frToolbar_tbEditProfile_QToolButton))
        clickButton(waitForObject(names.sclProfiles_gemini_ProfileButton))
        clickButton(waitForObject(names.sclProfiles_gemini_ProfileButton))
        clickButton(waitForObject(names.editFrame_tbClear_QToolButton))
        for character in profile_name.lower():

            if character == " ":
                raise ValueError(
                    "Space character mapping is not configured"
                )

            key_object_name = (
                "keyboardFrame_{}_KeyButtonLetter".format(character)
            )

            key_object = getattr(names, key_object_name)

            clickButton(waitForObject(key_object))

        clickButton(waitForObject(names.keyboardFrame_Enter_KeyButtonEnter))

        clickButton(waitForObject(names.warning_OK_QPushButton))

        clickButton(waitForObject(names.keyboardFrame_Cancel_KeyButtonCancel))

        test.passes(
            "PASS: Profile edited successfully. New name: {}".format(profile_name)
        )

        return True

    except Exception as error:
        test.fail(
            "FAIL: Profile editing failed for '{}': {}".format(
                profile_name, error
            )
        )
        raise
 

def create_blank_profile():
    """
    Create a blank profile.
    """
    try:
        clickButton(
            waitForObject(names.frToolbar_tbAddProfile_QToolButton)
        )

        clickButton(
            waitForObject(names.keyboardFrame_Enter_KeyButtonEnter)
        )

        sendEvent(
            "QMouseEvent",
            waitForObject(names.warning_OK_QPushButton),
            QEvent.MouseButtonPress,
            132, 32,
            Qt.LeftButton,
            1,
            0
        )

        sendEvent(
            "QMouseEvent",
            waitForObject(names.warning_OK_QPushButton),
            QEvent.MouseButtonRelease,
            149, -71,
            Qt.LeftButton,
            0,
            0
        )

        mouseClick(
            waitForObject(names.warning_TextLabel_QLabel),
            458, 56,
            Qt.NoModifier,
            Qt.LeftButton
        )

        clickButton(
            waitForObject(names.warning_OK_QPushButton)
        )

        clickButton(
            waitForObject(names.keyboardFrame_Cancel_KeyButtonCancel)
        )

        test.passes("PASS: Blank profile created successfully")
        return True

    except Exception as error:
        test.fail(
            "FAIL: Blank profile creation failed - {}".format(error)
        )
        raise

def main():
    test.log("This TC contain TU-366 to TU-TU-370")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    create_profile("thuvera")
    create_profile("gemini")
    create_blank_profile()
    edit_profile("thuvera")
