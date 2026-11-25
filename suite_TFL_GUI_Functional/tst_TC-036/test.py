import names
import test
from common import *
from squish import *

def read_system_event_log():

    error_codes = []

    test.log(" SYSTEM EVENT LOG VERIFICATION STARTED ")

    try:
        try:
            clickTab(
                waitForObject(names.serviceModeScreen_tabWidget_QTabWidget),
                "System\nEvent Log"
            )

            test.log("PASS: Navigated to System Event Log tab")

        except Exception as e:

            test.fail(
                "FAIL: Unable to navigate to System Event Log: " + str(e)
            )

            return error_codes


        try:

            scroll_bar = waitForObject(names.tableView_QScrollBar)

            scrollTo(scroll_bar, 1)

            test.log("PASS: Scrolled Event Log to position 1")

            scrollTo(scroll_bar, 14)

            test.log("PASS: Scrolled Event Log to position 14")

        except Exception as e:

            test.fail(
                "FAIL: Unable to scroll Event Log: " + str(e)
            )

        try:

            error_header = waitForObject(
                names.error_Code_HeaderViewItem
            )

            mouseClick(
                error_header,
                127,
                21,
                Qt.NoModifier,
                Qt.LeftButton
            )

            test.log("PASS: Clicked Error Code column header")

        except Exception as e:

            test.fail(
                "FAIL: Unable to click Error Code header: " + str(e)
            )

        try:

            scroll_bar = waitForObject(names.tableView_QScrollBar)

            current_obj = scroll_bar
            table = None

            test.log(" EVENT LOG TABLE INSPECTION ")

            for level in range(10):

                if current_obj is None:
                    break

                class_name = str(
                    current_obj.metaObject().className()
                )

                object_name = str(
                    current_obj.objectName
                )

                test.log(
                    "Parent Level " + str(level) +
                    " | Class: " + class_name +
                    " | Object Name: " + object_name
                )

                if class_name == "QTableView":

                    table = castToQObject(current_obj)

                    test.log(
                        "PASS: QTableView object identified"
                    )

                    break

                current_obj = current_obj.parent()

            if table is None:

                test.fail(
                    "FAIL: Unable to identify Event Log QTableView"
                )

            else:
                model = table.model()
                row_count = model.rowCount()
                column_count = model.columnCount()

                test.log(
                    "PASS: Table model accessed successfully"
                )

                test.log(
                    "Total Event Log Rows: " + str(row_count)
                )

                test.log(
                    "Total Event Log Columns: " + str(column_count)
                )


                error_column = -1

                for col in range(column_count):

                    header_value = model.headerData(
                        col,
                        Qt.Horizontal,
                        Qt.DisplayRole
                    )

                    header = str(header_value)

                    test.log(
                        "Column " + str(col) +
                        " : " + header
                    )

                    if header.strip().lower() == "error code":

                        error_column = col

                        break

                if error_column == -1:

                    test.fail(
                        "FAIL: Error Code column not found"
                    )

                else:

                    test.log(
                        "PASS: Error Code column identified"
                    )


                    for row in range(row_count):

                        index = model.index(
                            row,
                            error_column
                        )

                        value = model.data(
                            index,
                            Qt.DisplayRole
                        )

                        if value is None:

                            code = ""

                        else:

                            code = str(value).strip()

                        error_codes.append(code)

                        test.log(
                            "PASS: Row " + str(row + 1) +
                            " | Error Code: " + code
                        )


                    if len(error_codes) == row_count:

                        test.log(
                            "PASS: All Error Code values retrieved successfully"
                        )

                    else:

                        test.fail(
                            "FAIL: Error Code count mismatch"
                        )


                    test.log(
                        "COMPLETE ERROR CODE LIST "
                    )

                    for index, code in enumerate(error_codes):

                        test.log(
                            "Error Code " + str(index + 1) +
                            " : " + code
                        )

                    test.log(
                        "Total Error Codes Retrieved: " +
                        str(len(error_codes))
                    )

        except Exception as e:
            test.fail("FAIL: Unable to read Error Code values: " + str(e))

    except Exception as e:
        test.fail("FAIL: System Event Log verification failed: " + str(e))
    finally:
        try:
            clickButton(
                waitForObject(
                    names.serviceModeScreen_pbExit_QPushButton
                )
            )

            test.log("PASS: Successfully exited Service Mode")
        except Exception as e:
            test.fail("FAIL: Unable to exit Service Mode: " + str(e))
        test.log("SYSTEM EVENT LOG VERIFICATION COMPLETED")

    return error_codes

def main():

    test.log("TC-036 EXECUTION START")

    try:
        clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton,20000))

        test.log("PASS: Initial popup accepted")
    except Exception as e:
        test.fail("FAIL: Unable to accept initial popup: " + str(e))
        return
    try:
        service_mode_login()
        test.log("PASS: Service Mode login completed")
    except Exception as e:
        test.fail("FAIL: Service Mode login failed: " + str(e))
        return
    error_codes = read_system_event_log()
    test.log(
        "Total Error Codes Retrieved: " + str(len(error_codes))
    )
    for index, code in enumerate(error_codes):
        test.log("Retrieved Error Code " + str(index + 1) +" : " + code)
