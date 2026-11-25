# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    sendEvent("QMouseEvent", waitForObject(names.passwordScreen_pbService_QPushButton), QEvent.MouseButtonPress, 9, 13, Qt.LeftButton, 1, 0)
    clickButton(waitForObject(names.wdKeypad_pushButton_7_QPushButton, 275587))
    clickButton(waitForObject(names.wdKeypad_pushButton_4_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_1_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_4_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_7_QPushButton))
    clickTab(waitForObject(names.serviceModeScreen_tabWidget_QTabWidget), "System\nEvent Log")
    event_types = [
    names.tableView_0_2_QModelIndex,
    names.tableView_1_2_QModelIndex,
    names.tableView_2_2_QModelIndex,
    names.tableView_3_2_QModelIndex,
    names.tableView_4_2_QModelIndex,
        ]
    for index, event_object in enumerate(event_types, 1):
        event_type = waitForObjectExists(event_object).displayText
        test.log("Event Log {}: {}".format(index, event_type))
    
    
    
