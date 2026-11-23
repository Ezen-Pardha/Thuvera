import names
from common import *

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

def delete_preset(preset_name):

    try:
        test.log("========== DELETE PRESET ==========")
        test.log("REQUESTED PRESET: {}".format(preset_name))

        # Step 1: Verify preset exists
        if not preset_exists(preset_name):
            test.fail(
                "FAIL: Preset not found - {}".format(preset_name)
            )
            return False

        # Step 2: Click Delete Preset button
        clickButton(
            waitForObject(
                names.frToolbar_tbDeletePreset_QToolButton
            )
        )

        # Step 3: Move mouse
        sendEvent(
            "QMoveEvent",
            waitForObject(names.apollo_MainWindow),
            113, 133, 570, 164
        )

        # Step 4: Scroll preset table
        table = waitForObject(
            names.apollo_tvPresets_PresetsTable
        )

        sendEvent("QWheelEvent", table, 414, 346, -120, 0, 2)
        sendEvent("QWheelEvent", table, 416, 349, -120, 0, 2)
        sendEvent("QWheelEvent", table, 416, 351, -120, 0, 2)
        sendEvent("QWheelEvent", table, 416, 353, -120, 0, 2)
        sendEvent("QWheelEvent", table, 416, 355, -120, 0, 2)
        sendEvent("QWheelEvent", table, 416, 355, -120, 0, 2)

        # Step 5: Select preset twice
        mouseClick(
            waitForObjectItem(
                names.apollo_tvPresets_PresetsTable,
                preset_name
            ),
            153, 39,
            Qt.NoModifier,
            Qt.LeftButton
        )

        mouseClick(
            waitForObjectItem(
                names.apollo_tvPresets_PresetsTable,
                preset_name
            ),
            153, 39,
            Qt.NoModifier,
            Qt.LeftButton
        )

        # Step 6: Click confirmation text label
        mouseClick(
            waitForObject(names.question_TextLabel_QLabel_2),
            101, 3,
            Qt.NoModifier,
            Qt.LeftButton
        )

        # Step 7: Click first OK button
        clickButton(
            waitForObject(names.question_OK_QPushButton_2)
        )

        # Step 8: Click second OK button
        clickButton(
            waitForObject(names.question_OK_QPushButton)
        )

        test.log("ALL DELETE CONFIRMATION ACTIONS COMPLETED")

        snooze(2)

        # Step 9: Verify deletion
        if not preset_exists(preset_name):

            test.passes(
                "PASS: PRESET DELETED SUCCESSFULLY - {}".format(
                    preset_name
                )
            )

            return True

        test.fail(
            "FAIL: PRESET DELETION VERIFICATION FAILED - {}".format(
                preset_name
            )
        )

        return False

    except Exception as error:

        test.fail(
            "FAIL: Preset deletion failed for {} - {}".format(
                preset_name, error
            )
        )
        raise
def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    enterpin()
    open_default_profile_presets()
    create_preset("soft")
    create_preset("tissue")
    create_preset("soft")
    create_preset("softtissue")
    create_preset("thuvera")
    test.log("REPORTING PRESET INVENTORY")
    report_preset_inventory()
    edit_preset("soft", "softnew")
    delete_preset("tissue")
    
    
