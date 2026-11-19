import names
from squish import *
from common import *

def verify_profile_dropdowns():
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel),
               34, 27, Qt.NoModifier, Qt.LeftButton)

    test.log("LEFT dropdown opened.")
    test.imagePresent("TU_076_left")

    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame),
               665, 158, Qt.NoModifier, Qt.LeftButton)

    test.log("LEFT dropdown was closed.")
    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel_2),
               53, 37, Qt.NoModifier, Qt.LeftButton)

    test.log("RIGHT dropdown opened.")
    test.imagePresent("TU_076_Right")

    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame),
               676, 118, Qt.NoModifier, Qt.LeftButton)

    test.log("RIGHT dropdown was closed.")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))

    mouseClick(waitForObject(names.apollo_Question_MessageBox),
               100, 129, Qt.NoModifier, Qt.LeftButton)

    clickButton(waitForObject(names.apollo_YES_QPushButton))

    test.log("Profile dropdown verification completed.")
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_vaporize_hemostasis()
    verify_profile_dropdowns()