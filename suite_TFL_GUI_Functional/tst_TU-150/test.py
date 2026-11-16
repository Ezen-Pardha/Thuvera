import names
from common import *
def get_preset_rows():
    """
    Read every displayed row from the preset table.
    """
    try:
        table = waitForObject(names.apollo_tvPresets_PresetsTable)
        model = table.model()
        row_count = model.rowCount()
        column_count = model.columnCount()
        preset_rows = {}
        test.log("PRESET TABLE DETAILS")
        test.log("MODEL ROW COUNT: {}".format(row_count))
        test.log("MODEL COLUMN COUNT: {}".format(column_count))
        for row in range(row_count):
            row_values = []

            for column in range(column_count):
                index = model.index(row, column)
                value = model.data(index, Qt.DisplayRole)

                if value is None:
                    value = ""
                else:
                    value = str(value).strip()

                row_values.append(value)

            preset_name = ""

            for value in row_values:
                if value:
                    preset_name = value
                    break

            if preset_name:
                preset_rows[preset_name] = row_values
                test.log(
                    "PRESET ROW: {} | VALUES: {}".format(
                        preset_name, row_values
                    )
                )

        test.log("TOTAL PRESETS READ: {}".format(len(preset_rows)))
        return preset_rows

    except Exception as error:
        test.fail(
            "FAIL: Unable to read preset table rows - {}".format(error)
        )
        raise


def get_preset_names():
    """Return the preset names currently displayed in the preset table."""
    preset_rows = get_preset_rows()
    preset_names = list(preset_rows.keys())

    test.log("EXISTING PRESETS: {}".format(preset_names))
    return preset_names


def get_preset_row_data(preset_name):
    """
    Return all displayed column values for one preset.
    """
    try:
        preset_rows = get_preset_rows()

        for current_name in preset_rows.keys():
            if current_name.lower() == preset_name.lower():
                return preset_rows[current_name]

        test.log("PRESET ROW NOT FOUND: {}".format(preset_name))
        return None

    except Exception as error:
        test.fail(
            "FAIL: Unable to read values for preset {} - {}".format(
                preset_name, error
            )
        )
        raise


def preset_exists(preset_name):
    """Return True if the specified preset is present in the table."""
    try:
        existing_presets = get_preset_names()

        for existing_name in existing_presets:
            if existing_name.lower() == preset_name.lower():
                return True

        return False

    except Exception as error:
        test.fail(
            "FAIL: Preset existence check failed - {}".format(error)
        )
        raise


def click_preset_row(preset_name, x=52, y=24, click_twice=False):
    """
    Select a preset row using the recorded table-item coordinates.
    """
    preset_item = waitForObjectItem(
        names.apollo_tvPresets_PresetsTable,
        preset_name
    )

    mouseClick(
        preset_item,
        x, y,
        Qt.NoModifier,
        Qt.LeftButton
    )

    if click_twice:
        mouseClick(
            preset_item,
            x, y,
            Qt.NoModifier,
            Qt.LeftButton
        )

def enter_preset_name(preset_name):
    """
    Enter a preset name using the on-screen alphabetic keyboard.
    """
    try:
        for char in preset_name.lower():
            if not char.isalpha():
                raise ValueError(
                    "Only alphabetic preset names are supported: {}".format(
                        preset_name
                    )
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
            "FAIL: Unable to enter preset name {} - {}".format(
                preset_name, error
            )
        )
        raise


def create_preset(preset_name, configure_callback=None):
    """
    Create a preset.
    """
    try:
        test.log("REQUESTED PRESET CREATION: {}".format(preset_name))

        if preset_exists(preset_name):
            test.log(
                "PRESET ALREADY EXISTS; CREATION SKIPPED: {}".format(
                    preset_name
                )
            )
            return False

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
                "WARNING: Preset already exists or could not be saved: {}".format(
                    preset_name
                )
            )

            clickButton(
                waitForObject(names.warning_OK_QPushButton)
            )

            if object.exists(names.apollo_btCancel_QPushButton):
                clickButton(
                    waitForObject(names.apollo_btCancel_QPushButton)
                )

            return False

        if preset_exists(preset_name):
            test.passes(
                "PASS: Preset created successfully - {}".format(
                    preset_name
                )
            )
            return True

        test.fail(
            "FAIL: Preset was not found after creation - {}".format(
                preset_name
            )
        )
        return False

    except Exception as error:
        test.fail(
            "FAIL: Preset creation failed for {} - {}".format(
                preset_name, error
            )
        )
        raise

def edit_preset(old_name, new_name):
    """
    Edit an existing preset name.
    """
    try:
        if not preset_exists(old_name):
            test.fail(
                "FAIL: Cannot edit preset; preset not found - {}".format(
                    old_name
                )
            )
            return False

        if old_name.lower() != new_name.lower() and preset_exists(new_name):
            test.fail(
                "FAIL: Cannot rename preset; new name already exists - {}".format(
                    new_name
                )
            )
            return False

        test.log(
            "EDITING PRESET: {} -> {}".format(old_name, new_name)
        )

        clickButton(
            waitForObject(names.frToolbar_tbEditPreset_QToolButton)
        )

        preset_item = waitForObjectItem(
            names.apollo_tvPresets_PresetsTable,
            old_name
        )

        mouseClick(
            preset_item,
            198, 39,
            Qt.NoModifier,
            Qt.LeftButton
        )

        name_field = waitForObject(names.apollo_edName_QLineEdit)
        name_field.setText(new_name)

        clickButton(
            waitForObject(names.apollo_btSave_QPushButton)
        )

        if object.exists(names.warning_OK_QPushButton):
            clickButton(
                waitForObject(names.warning_OK_QPushButton)
            )
            test.fail(
                "FAIL: Preset edit was rejected - {}".format(new_name)
            )
            return False

        if preset_exists(new_name) and not preset_exists(old_name):
            test.passes(
                "PASS: Preset renamed successfully - {} to {}".format(
                    old_name, new_name
                )
            )
            return True

        if preset_exists(new_name):
            test.log(
                "PRESET WITH NEW NAME IS PRESENT: {}".format(new_name)
            )
            return True

        test.fail(
            "FAIL: Preset edit verification failed - {}".format(new_name)
        )
        return False

    except Exception as error:
        test.fail(
            "FAIL: Preset edit failed for {} - {}".format(
                old_name, error
            )
        )
        raise


def capture_created_preset_values(preset_names):
    """
    Capture the table values immediately after creation and BEFORE editing.
    """
    created_values = {}

    test.log("CAPTURING ORIGINAL PRESET VALUES")

    for preset_name in preset_names:
        row_values = get_preset_row_data(preset_name)

        if row_values is None:
            test.fail(
                "FAIL: Could not capture created values for {}".format(
                    preset_name
                )
            )
            continue

        created_values[preset_name] = list(row_values)

        test.log(
            "CREATED PRESET VALUES - {}: {}".format(
                preset_name, row_values
            )
        )

    return created_values


def verify_edited_preset_values(created_preset_values):

    presets_to_verify = [
        ("soft", "softnew", 52, 24),
        ("tissue", "tissuenew", 72, 20),
        ("softi", "soft", 22, 29)
    ]

    all_presets_edited = True

    test.log("STARTING PRESET VALUE COMPARISON")

    for original_name, current_name, x, y in presets_to_verify:

        test.log(
            "VERIFYING PRESET: {} -> {}".format(
                original_name, current_name
            )
        )

        original_values = created_preset_values.get(original_name)

        if original_values is None:
            test.fail(
                "FAIL: Original values not found for {}".format(
                    original_name
                )
            )
            all_presets_edited = False
            continue

        try:
            click_preset_row(
                current_name,
                x,
                y,
                click_twice=True
            )

            current_values = get_preset_row_data(current_name)

            test.log(
                "CREATED VALUES - {}: {}".format(
                    original_name, original_values
                )
            )

            test.log(
                "CURRENT VALUES - {}: {}".format(
                    current_name, current_values
                )
            )

            if current_values is None:
                test.fail(
                    "FAIL: Unable to read current values for {}".format(
                        current_name
                    )
                )
                all_presets_edited = False
                continue

            if original_values != current_values:

                test.passes(
                    "PASS: PRESET VALUES GOT EDITED - {}".format(
                        current_name
                    )
                )

                test.log("OLD VALUES: {}".format(original_values))
                test.log("NEW VALUES: {}".format(current_values))

            else:

                test.fail(
                    "FAIL: PRESET VALUES WERE NOT CHANGED - {}".format(
                        current_name
                    )
                )

                all_presets_edited = False

        except Exception as error:

            test.fail(
                "FAIL: Verification failed for {} - {}".format(
                    current_name, error
                )
            )

            all_presets_edited = False

    if all_presets_edited:
        test.passes(
            "PASS: All selected preset values got edited successfully"
        )
    else:
        test.fail(
            "FAIL: One or more preset values were not edited"
        )

    return all_presets_edited

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
    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
        enterpin()
        open_default_profile_presets()
        presets_to_create = [
            "soft",
            "tissue",
            "softi",
            "softtissue",
            "thuvera"
        ]

        for preset_name in presets_to_create:
            create_preset(preset_name)


        created_preset_values = capture_created_preset_values(
            presets_to_create
        )

        edit_preset("soft", "softnew")
        edit_preset("tissue", "tissuenew")
        edit_preset("softi", "soft")
        edit_preset("thuvera", "Thuvera")
        verify_edited_preset_values(created_preset_values)

        report_preset_inventory()

    except Exception as error:
        test.fail(
            "FAIL: Preset management main flow failed - {}".format(error)
        )
        raise