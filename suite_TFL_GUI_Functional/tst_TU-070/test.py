
import names
from common import *

def main():
    enterpin()
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    test.compare(waitForObjectExists(names.apollo_wdTopBar_TopBar).visible, True)
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    mouseClick(waitForObject(names.apollo_lbScreenTitle_QLabel), 590, 24, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.apollo_lbScreenTitle_QLabel).visible, True)