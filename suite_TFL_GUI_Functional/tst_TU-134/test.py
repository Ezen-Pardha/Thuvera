import test
import names
from common import *


def verify_add_presets_screen_sidebar():
    """Open the Add Presets screen and verify that the sidebar is not displayed."""
    try:
        mouseDrag(
            waitForObject(names.apollo_wdProfile_QWidget),
            712,
            1,
            -296,
            10,
            1,
            Qt.LeftButton
        )
        clickButton(
            waitForObject(
                names.frToolbar_tbAddPreset_QToolButton,
                20000
            )
        )

        mouseClick(
            waitForObject(names.apollo_centralWidget_QWidget_2),
            1035,
            602,
            Qt.NoModifier,
            Qt.LeftButton
        )
        if object.exists(names.apollo_sidebar_QWidget):
            sidebar = waitForObject(
                names.apollo_sidebar_QWidget,
                20000
            )

            if sidebar.visible:
                test.fail(
                    "FAIL: Sidebar is displayed on the Add Presets screen"
                )
                return False

        test.passes(
            "PASS: Sidebar is not displayed on the Add Presets screen"
        )
        return True

    except Exception as error:
        test.fail(
            "FAIL: Add Presets screen sidebar verification failed - {}".format(
                error
            )
        )
        raise


def main():
    test.log("This TC contains TU-134 to TU-135")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_presets()
    verify_add_presets_screen_sidebar()