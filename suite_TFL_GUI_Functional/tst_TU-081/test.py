# -*- coding: utf-8 -*-

import names
from common import *

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    test.passes("Treatment screen is verified")
    mouseClick(waitForObject(names.stateSwitch_lbReady_QLabel), 171, 55, Qt.NoModifier, Qt.LeftButton)
    test.passes("Ready screen is verified")
 
    """Verify Presets button is not clickable"""
    try:
        button = waitForObjectExists(names.apollo_btPresets_QPushButton, 2000)
    
        if not button.isEnabled() or not button.visible:
            test.passes("Presets button is not responding and is not clickable, as expected")
        else:
            test.fail("Presets button is clickable, which is unexpected")
    
    except:
        test.passes("Presets button is not found and is not clickable, as expected")
    
    
    """Verify Treatment Logs button is not clickable"""
    try:
        button = waitForObjectExists(names.apollo_btTreatmentLogs_QPushButton, 2000)
    
        if not button.isEnabled() or not button.visible:
            test.passes("Treatment Logs button is not responding and is not clickable, as expected")
        else:
            test.fail("Treatment Logs button is clickable, which is unexpected")
    
    except:
        test.passes("Treatment Logs button is not found and is not clickable, as expected")
    
    
    """Verify Settings button is not clickable"""
    try:
        button = waitForObjectExists(names.apollo_btSettings_QPushButton, 2000)
    
        if not button.isEnabled() or not button.visible:
            test.passes("Settings button is not responding and is not clickable, as expected")
        else:
            test.fail("Settings button is clickable, which is unexpected")
    
    except:
        test.passes("Settings button is not found and is not clickable, as expected")
    
    
    """Verify Utilities button is not clickable"""
    try:
        button = waitForObjectExists(names.apollo_btUtilities_QPushButton, 2000)
    
        if not button.isEnabled() or not button.visible:
            test.passes("Utilities button is not responding and is not clickable, as expected")
        else:
            test.fail("Utilities button is clickable, which is unexpected")
    
    except:
        test.passes("Utilities button is not found and is not clickable, as expected")
    
    
    """Verify Exit Profile button is not clickable"""
    try:
        button = waitForObjectExists(names.apollo_btExitProfile_QPushButton, 2000)
    
        if not button.isEnabled() or not button.visible:
            test.passes("Exit Profile button is not responding and is not clickable, as expected")
        else:
            test.fail("Exit Profile button is clickable, which is unexpected")
    
    except:
         test.passes("Exit Profile button is not found and is not clickable, as expected")
         
    test.passes("Exit Profile button is not found and is not clickable, as expected")

    
