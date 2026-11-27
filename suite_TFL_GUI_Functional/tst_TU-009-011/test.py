# -*- coding: utf-8 -*-

import names
from common import *

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))
    """Verify Default Laser Settings are loaded"""
    
    profile_name = str(waitForObjectExists(names.apollo_lbProfileName_QLabel).text)
    
    if profile_name == "DEFAULT":
        test.passes("Default Laser settings are loaded and verified")
    else:
        test.fail("Default Laser settings are not loaded. Actual profile: {}".format(profile_name))
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.apollo_YES_QPushButton))
