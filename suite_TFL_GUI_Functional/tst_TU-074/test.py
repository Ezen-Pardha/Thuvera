import names
from squish import *
from common import *


def verify_profile_dropdown_and_reduce_settings():
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel),
               8, 24, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("TU_076_left")

    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame),
               684, 109, Qt.NoModifier, Qt.LeftButton)
    test.log("RIGHT dropdown was closed.")

    mouseClick(waitForObject(names.comboBox_lbValue_AutoReducibleFontSizeLabel_2),
               127, 41, Qt.NoModifier, Qt.LeftButton)
    test.imagePresent("TU_076_Right")

    mouseClick(waitForObject(names.frmComboBoxHeader_lbPixmap_QLabel),
               32, 37, Qt.NoModifier, Qt.LeftButton)
    test.log("Dropdown selection completed.")
    for _ in range(3):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton_3))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_YES_QPushButton))

    test.imagePresent("TU-075")

    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))

    test.log("Profile dropdown and reduce settings verification completed.")


def verify_soft_tissue_vaporize_hemastasis_profile():
    clickButton(waitForObject(names.apollo_tbAssistant_QToolButton))

    clickButton(waitForObject(names.frWizardPlace_Soft_Tissue_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_Vaporize_Hemostasis_WizardButton))
    clickButton(waitForObject(names.frWizardPlace_ADVANCE_WizardApplyButton))
    for _ in range(3):
        clickButton(waitForObject(names.centralWidget_pbReduce_QPushButton))
    test.imagePresent("Exit_mode")
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    test.imagePresent("TU-075_frequency")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
    test.log("Soft Tissue Vaporize/Hemostasis profile verification completed.")
    
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    navigate_to_vaporize_hemostasis()
    verify_profile_dropdown_and_reduce_settings()
    verify_soft_tissue_vaporize_hemastasis_profile()
    
    
    
