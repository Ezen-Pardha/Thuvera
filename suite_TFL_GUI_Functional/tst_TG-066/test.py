import names
from common import *

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

def get_preset_names():
    """
    WHEN the preset screen is open,
    THEN read all preset names from the preset table,
    AND return the list of preset names.
    """

    try:
        table = waitForObject(names.apollo_tvPresets_PresetsTable)

        test.log("PRESET TABLE DETAILS")
        test.log("TABLE OBJECT: {}".format(table))

        model = table.model()

        row_count = model.rowCount()
        column_count = model.columnCount()

        test.log("MODEL ROW COUNT: {}".format(row_count))
        test.log("MODEL COLUMN COUNT: {}".format(column_count))
        preset_names = []
        for row in range(row_count):
            for column in range(column_count):
                index = model.index(row, column)
                value = model.data(index, Qt.DisplayRole)
                test.log(
                    "ROW: {}, COLUMN: {}, VALUE: {}".format(
                        row, column, value
                    )
                )
                if value is not None:
                    value = str(value).strip()
                    if value and value not in preset_names:
                        preset_names.append(value)

        test.log("EXISTING PRESETS: {}".format(preset_names))
        return preset_names
    except Exception as error:
        test.fail(
            "FAIL: Unable to read preset names - {}".format(error)
        )
        raise

def preset_exists(preset_name):
    """
    WHEN user need to check whether a preset exists,
    THEN search for the given preset name in the preset list,
    AND return True if it exists or False if it does not.
    """
    try:
        existing_presets = get_preset_names()
        if preset_name.lower() in [
            name.lower() for name in existing_presets
        ]:
            return True
        return False
    except Exception as error:

        test.fail(
            "FAIL: Preset existence check failed - {}".format(error)
        )
        raise

def enter_preset_name(preset_name):
    """
    WHEN user need to enter a preset name,
    THEN click the required letters on the on-screen keyboard,
    AND press Enter after entering the complete name.
    """
    try:
        for char in preset_name.lower():
            if not char.isalpha():
                raise ValueError(
                    "Only alphabetic preset names are supported."
                )
            key_object = getattr(
                names,
                "keyboardFrame_{}_KeyButtonLetter".format(char)
            )
            
            clickButton(waitForObject(key_object))
        clickButton(
            waitForObject(names.keyboardFrame_Enter_KeyButtonEnter)
        )
    except Exception as error:
        test.fail(
            "FAIL: Unable to enter preset name - {}".format(error)
        )
        raise

def create_preset(preset_name, configure_callback=None):
    """
    WHEN user need to create a new preset,
    THEN click Add Preset and enter the preset name,
    AND save the preset.
    WHEN the preset name already exists,
    THEN close the warning popup and cancel the creation.
    AND verify whether the new preset was created successfully.
    """
    try:
        test.log("REQUESTED PRESET CREATION: {}".format(preset_name))
        clickButton(
            waitForObject(names.frToolbar_tbAddPreset_QToolButton)
        )
        mouseClick(
            waitForObject(names.apollo_edName_QLineEdit),
            116, 31,
            Qt.NoModifier,
            Qt.LeftButton
        )
        enter_preset_name(preset_name)
        if configure_callback is not None:
            configure_callback()
        clickButton(
            waitForObject(names.apollo_btSave_QPushButton)
        )
        if object.exists(names.warning_OK_QPushButton):
            test.log(
                "PRESET ALREADY EXISTS: {}".format(preset_name)
            )
            clickButton(
                waitForObject(names.warning_OK_QPushButton)
            )
            clickButton(
                waitForObject(names.apollo_btCancel_QPushButton)
            )
            test.log(
                "Duplicate preset creation cancelled: {}".format(
                    preset_name
                )
            )
            return False
        updated_presets = get_preset_names()
        if preset_exists(preset_name):
            test.passes(
                "PASS: Preset created successfully - {}".format(
                    preset_name
                )
            )
            return True
        test.log(
            "WARNING: Preset not found in table inventory: {}".format(
                preset_name
            )
        )
        test.log(
            "Check diagnostic table logs for actual preset values."
        )
        return False
    except Exception as error:
        test.fail(
            "FAIL: Preset creation failed - {}".format(error)
        )
        raise

def edit_preset(old_name, new_name):
    """
    WHEN user need to change an existing preset name,
    THEN find and select the old preset,
    AND replace its name with the new name and save it.
    AND verify whether the preset name was updated successfully.
    """
    try:
        if not preset_exists(old_name):
            test.log(
                "PRESET NOT FOUND: {}".format(old_name)
            )
            return False
        if preset_exists(new_name):
            test.log(
                "PRESET ALREADY EXISTS: {}".format(new_name)
            )
            return False
        test.log(
            "EDITING PRESET: {} -> {}".format(
                old_name, new_name
            )
        )
        clickButton(
            waitForObject(names.frToolbar_tbEditPreset_QToolButton)
        )
        preset_item = waitForObjectItem(
            names.apollo_tvPresets_PresetsTable,
            "*{}*".format(old_name)
        )
        mouseClick(
            preset_item,
            198, 39,
            Qt.NoModifier,
            Qt.LeftButton
        )
        name_field = waitForObject(
            names.apollo_edName_QLineEdit
        )
        name_field.setText(new_name)
        clickButton(
            waitForObject(names.apollo_btSave_QPushButton)
        )
        if object.exists(names.warning_OK_QPushButton):
            clickButton(
                waitForObject(names.warning_OK_QPushButton)
            )
            test.log("WARNING: Preset edit was not accepted.")

            return False
        if preset_exists(new_name):
            test.passes(
                "PASS: Preset edited successfully - {}".format(
                    new_name
                )
            )
            return True
        test.fail(
            "FAIL: Preset edit verification failed - {}".format(
                new_name
            )
        )
        return False
    except Exception as error:

        test.fail(
            "FAIL: Preset edit failed - {}".format(error)
        )
        raise

def delete_preset(preset_name):
    """
    WHEN user need to delete an existing preset,
    THEN select the preset and click Delete,
    AND confirm the deletion.
    AND verify that the preset no longer exists in the preset list.
    """
    try:
        if not preset_exists(preset_name):
            test.log(
                "PRESET NOT FOUND: {}".format(preset_name)
            )
            return False
        test.log(
            "DELETING PRESET: {}".format(preset_name)
        )
        clickButton(
            waitForObject(names.frToolbar_tbDeletePreset_QToolButton)
        )
        preset_item = waitForObjectItem(
            names.apollo_tvPresets_PresetsTable,
            "*{}*".format(preset_name)
        )
        mouseClick(
            preset_item,
            284, 16,
            Qt.NoModifier,
            Qt.LeftButton
        )
        clickButton(
            waitForObject(names.question_OK_QPushButton)
        )
        if not preset_exists(preset_name):

            test.passes(
                "PASS: Preset deleted successfully - {}".format(
                    preset_name
                )
            )

            return True
        test.fail(
            "FAIL: Preset deletion verification failed - {}".format(
                preset_name
            )
        )
        return False
    except Exception as error:

        test.fail(
            "FAIL: Preset deletion failed - {}".format(error)
        )
        raise

def report_preset_inventory():
    """
    WHEN user need to check the available presets,
    THEN get all preset names from the preset table,
    AND display the total number of presets and their names.
    """
    try:
        preset_names = get_preset_names()
        test.log(
            "TOTAL NUMBER OF PRESETS: {}".format(
                len(preset_names)
            )
        )
        test.log(
            "PRESET NAMES: {}".format(preset_names)
        )
        return preset_names
    except Exception as error:
        test.fail(
            "FAIL: Unable to report preset inventory - {}".format(
                error
            )
        )
        raise

def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    create_profile("thuvera")
    clickButton(waitForObject(names.sclProfiles_thuvera_ProfileButton))
    clickButton(waitForObject(names.apollo_btPresets_QPushButton))
    create_preset("soft")
    create_preset("tissue")
    create_preset("soft")
    create_preset("softtissue")
    create_preset("thuvera")
    test.log("REPORTING PRESET INVENTORY")
    report_preset_inventory()
    edit_preset("soft", "softnew")
    # delete_preset("tissue")
    clickButton(waitForObject(names.apollo_btExitProfile_QPushButton))
    clickButton(waitForObject(names.question_YES_QPushButton))
    clickButton(waitForObject(names.sclProfiles_thuvera_ProfileButton)) 
    mouseClick(waitForObject(names.comboBox_lbPixmap_QLabel), 24, 20, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.apollo_frmComboBoxShadow_QFrame), 143, 80, Qt.NoModifier, Qt.LeftButton)
    
    