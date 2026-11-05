import names
from squish import *
from common import *
def main():

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    doubleClick(waitForObject(names.wdKeypad_pushButton_0_QPushButton), 79, 43, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.wdKeypad_pushButton_0_QPushButton), 79, 43, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    clickButton(waitForObject(names.apollo_btSettings_QPushButton))
    mouseClick(waitForObject(names.frmComboBox_cbLang_QComboBox), 479, 7, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Español (Spain)"), 182, 33, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.frmComboBox_cbLang_QComboBox, "Español (Spain)"), 182, 33, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.apollo_btHome_QPushButton))
    mouseClick(waitForObject(names.apollo_lbProfileTitle_QLabel), 24, 13, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbProfileName_QLabel), 43, 8, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbLasingTimeTitle_QLabel), 21, 15, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbTotalEnergyTitle_QLabel), 37, 16, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbFiberDiameterTitle_QLabel), 13, 13, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbUsesLeftTitle_QLabel), 39, 15, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_lbExpirationTitle_QLabel), 27, 11, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget), 407, 457, Qt.NoModifier, Qt.LeftButton)

    # --------------------------------------------------
    # Localization Validation
    # --------------------------------------------------

    validate_localization(

        objects=[

            waitForObject(names.apollo_lbProfileTitle_QLabel),
                
            waitForObject(names.apollo_lbProfileName_QLabel),
                
            waitForObject(names.apollo_lbLasingTimeTitle_QLabel),
                
            waitForObject(names.apollo_lbTotalEnergyTitle_QLabel),
                
            waitForObject(names.apollo_lbFiberDiameterTitle_QLabel),
                
            waitForObject(names.apollo_lbUsesLeftTitle_QLabel),
                
            waitForObject(names.apollo_lbExpirationTitle_QLabel),
                
            waitForObject(names.centralWidget_PulseModeWidget_PulseModeWidget)
        ],

        screen_name="Home Screen",

        expected_strings=[
            "DEFAULT",
            "PROFILE",
            "LASING TIME",
            "TOTAL Kj",
            "FIBER (μm)",
            "USES LEFT",
            "EXPIRATION"
        ],
    )
    
    
    
    