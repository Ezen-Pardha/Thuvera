import names
from common import *
import test
def main():
    """
    Main execution function for TU-219
    CW preset verification
    """
    test.log("Starting TU-219: CW preset verification")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    test.log("Verifying CW Left preset")
    mouseClick(
        waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel),
        119, 35,
        Qt.NoModifier,
        Qt.LeftButton
    )
    popup = waitForObjectExists(
        names.apollo_aivComboBoxPopup_QTreeView
    )
    sendEvent("QWheelEvent", popup, 233, 203, -120, 0, 2)
    sendEvent("QWheelEvent", popup, 233, 203, -120, 0, 2)
    sendEvent("QWheelEvent", popup, 233, 204, -120, 0, 2)
    item = waitForObjectItem(
        names.apollo_aivComboBoxPopup_QTreeView,
        "Tissue Vaporize (CW)"
    )

    mouseClick(
        item,
        237, 31,
        Qt.NoModifier,
        Qt.LeftButton
    )

    actual_value = waitForObjectExists(
        names.comboBox_lbValue_AutoReducibleFontSizeLabel
    ).text

    expected_value = "Tissue Vaporize (CW)"

    test.compare(
        actual_value,
        expected_value,
        "CW Left preset verification"
    )


    test.log("Verifying CW Right preset")
    mouseClick(
        waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel_2),
        44, 30,
        Qt.NoModifier,
        Qt.LeftButton
    )

    popup = waitForObjectExists(
        names.apollo_aivComboBoxPopup_QTreeView
    )

    sendEvent("QWheelEvent", popup, 169, 219, -120, 0, 2)
    sendEvent("QWheelEvent", popup, 169, 219, -120, 0, 2)
    sendEvent("QWheelEvent", popup, 169, 219, -120, 0, 2)
    item = waitForObjectItem(
        names.apollo_aivComboBoxPopup_QTreeView,
        "Tissue Vaporize (CW)"
    )

    mouseClick(
        item,
        183, 20,
        Qt.NoModifier,
        Qt.LeftButton
    )

    actual_value = waitForObjectExists(
        names.comboBox_lbValue_AutoReducibleFontSizeLabel_2
    ).text

    expected_value = "Tissue Vaporize (CW)"

    test.compare(
        actual_value,
        expected_value,
        "CW Right preset verification"
    )

   