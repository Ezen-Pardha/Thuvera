import names
from common import *

def read_numeric_value(object_name, description):
    """
    Read and log the displayed value from a UI label.
    """
    obj = waitForObject(object_name)
    value = str(obj.text).strip()
    test.log(description + ": " + value)
    return value

def open_preset_dropdown():
    """
    Open the preset dropdown and locate its popup tree view.

    Returns:
        The preset popup QTreeView object.
    """

    mouseClick(
        waitForObject(names.centralWidget_comboBox_ComboBox),
        207, 35, Qt.NoModifier, Qt.LeftButton
    )

    popup = waitForObject(
        names.apollo_aivComboBoxPopup_QTreeView
    )

    test.log("PASS: Preset dropdown opened successfully")

    return popup

def verify_user_defined_preset_selection():
    """
    Verify Soft and Tissues user-defined presets.
    """
    clickButton(
        waitForObject(names.sclProfiles_Default_ProfileButton)
    )
    popup = open_preset_dropdown()
    scrollTo(
        waitForObject(names.aivComboBoxPopup_QScrollBar),
        51
    )

    mouseDrag(
        waitForObject(names.aivComboBoxPopup_QScrollBar),
        5, 99, 69, -528, 1, Qt.LeftButton
    )

    popup = waitForObject(
        names.apollo_aivComboBoxPopup_QTreeView
    )
    for i in range(3):
        sendEvent(
            "QWheelEvent",
            popup,
            346, 328,
            -120, 0, 2
        )
    mouseClick(
        waitForObjectItem(
            names.apollo_aivComboBoxPopup_QTreeView,
            "soft"
        ),
        164, 13, Qt.NoModifier, Qt.LeftButton
    )
    value_1 = read_numeric_value(
        names.centralWidget_lbValue_FlashableLabel_4,
        "Soft Preset Value 1"
    )
    mouseClick(
        waitForObject(names.centralWidget_comboBox_ComboBox),
        323, 25, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObjectItem(
            names.apollo_aivComboBoxPopup_QTreeView,
            "soft"
        ),
        187, 61, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.centralWidget_comboBox_ComboBox),
        197, 48, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObjectItem(
            names.apollo_aivComboBoxPopup_QTreeView,
            "tissues"
        ),
        193, 34, Qt.NoModifier, Qt.LeftButton
    )
    value_2 = read_numeric_value(
        names.centralWidget_lbValue_FlashableLabel_3,
        "Tissues Preset Value 1"
    )

    value_3 = read_numeric_value(
        names.centralWidget_lbValue_FlashableLabel_4,
        "Tissues Preset Value 2"
    )

    power_value = read_numeric_value(
        names.centralWidget_lbPowerValue_FlashableLabel,
        "Tissues Preset Power"
    )
    test.log("USER DEFINED PRESET VALUES")

    preset_values = [
        ("Soft Preset Value", value_1),
        ("Tissues Preset Value 1", value_2),
        ("Tissues Preset Value 2", value_3),
        ("Tissues Preset Power", power_value)
    ]
    for description, value in preset_values:

        if value and value.lower() != "null":
            test.log(description + ": " + value)
    clickButton(
        waitForObject(names.apollo_btExitProfile_QPushButton)
    )

    clickButton(
        waitForObject(names.question_YES_QPushButton)
    )

def read_system_event_log_values():
    """
    Read and log the first five rows of the System Event Log
    """
    table = waitForObject(
        names.tabSystemEventLog_tableView_QTableView
    )

    model = table.model()

    required_columns = [
        "ID",
        "Date/Time",
        "Event Type",
        "Scope",
        "Error Code",
        "Variable Value",
        "Wireless Pedal Connected"
    ]
    row_count = min(model.rowCount(), 5)
    column_count = model.columnCount()
    column_indexes = {}

    for col in range(column_count):

        header = model.headerData(col, Qt.Horizontal)

        if header is not None:

            header = str(header).strip()

            if header in required_columns:
                column_indexes[header] = col

    test.log("SYSTEM EVENT LOG - FIRST 5 ROWS")
    for row in range(row_count):

        row_values = []

        for header in required_columns:

            if header not in column_indexes:
                continue

            index = model.index(
                row,
                column_indexes[header]
            )

            value = model.data(index)

            if value is None:
                continue

            value = str(value).strip()

            if value and value.lower() != "null":
                row_values.append(
                    header + ": " + value
                )

        if row_values:

            test.log(" Row " + str(row + 1) + " ")

            for item in row_values:
                test.log(item)

    test.log("END OF SYSTEM EVENT LOG")


def verify_system_event_log():
    """
    Open and inspect the System Event Log in Service Mode.
    """

    clickTab(
        waitForObject(
            names.serviceModeScreen_tabWidget_QTabWidget
        ),
        "System\nEvent Log"
    )
    mouseClick(
        waitForObject(names.iD_HeaderViewItem),
        2, 17, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.date_Time_HeaderViewItem),
        44, 17, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.event_Type_HeaderViewItem),
        49, 16, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.tableView_QHeaderView),
        328, 16, Qt.NoModifier, Qt.LeftButton
    )
    scrollTo(
        waitForObject(names.tableView_QScrollBar),
        6
    )

    scrollTo(
        waitForObject(names.tableView_QScrollBar),
        12
    )

    scrollTo(
        waitForObject(names.tableView_QScrollBar),
        14
    )

    mouseClick(
        waitForObject(names.error_Code_HeaderViewItem),
        132, 8, Qt.NoModifier, Qt.LeftButton
    )
    mouseClick(
        waitForObject(names.variable_Value_HeaderViewItem),
        64, 16, Qt.NoModifier, Qt.LeftButton
    )
    read_system_event_log_values()
    clickButton(
        waitForObject(names.serviceModeScreen_pbExit_QPushButton)
    )

def main():
    test.log("This TC contains TC-057 to TC-061")

    clickButton(
        waitForObject(names.frmPopup_pbAccept_QPushButton)
    )
    enterpin()
    test.log("Verification of User Defined Presets")
    verify_user_defined_preset_selection()
    try:

        context = currentApplicationContext()
        context.detach()
        snooze(3)
        test.log("AUT context detached successfully")
    except Exception as error:
        test.log(
            "Error while closing AUT: " + str(error)
        )
    startApplication("run.sh")
    snooze(5)
    test.passes("Apollo AUT restart command executed successfully")
    clickButton(
        waitForObject(names.frmPopup_pbAccept_QPushButton)
    )
    test.log("Verification of Service Mode")
    service_mode_login()
    test.log("Verification of System Event Log")
    verify_system_event_log()
