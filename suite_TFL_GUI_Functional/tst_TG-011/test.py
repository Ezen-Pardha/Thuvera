import names
from common import *

def verify_invalid_passcode():
    """Enter invalid passcode and log invalid notification."""
    try:
        for i in range(4):
            clickButton(
                waitForObject(names.wdKeypad_pushButton_5_QPushButton)
            )
        test.log("Entered invalid passcode: 5555")

        mouseClick(
            waitForObject(names.passwordScreen_mInvalidPassNotif_QLabel),
            297, 50, Qt.NoModifier, Qt.LeftButton
        )

        test.log("INVALID PASSCODE: Application displayed invalid passcode notification.")

        test.passes("PASS: Invalid passcode notification verified.")

    except Exception as error:
        test.log("INVALID PASSCODE CHECK FAILED: {}".format(error))
        test.fail(
            "FAIL: Invalid passcode verification - {}".format(error)
        )
        raise
 
def main():
    """
    GIVEN the display has been launched.
    WHEN the user enters an invalid passcode, the application displays an "Invalid Passcode" pop-up message.
    AND WHEN the user enters the correct passcode the application successfully logs in and navigates to the home screen.
    """
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    verify_invalid_passcode()
    enterpin()
    exit_default_profile()
    
    

     
