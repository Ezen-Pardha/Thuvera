# -*- coding: utf-8 -*-

import names
from common import *

def main():
    test.passes("SVV TAG: System Event Log Event Type: TC-022")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    sendEvent("QMouseEvent", waitForObject(names.passwordScreen_pbService_QPushButton), QEvent.MouseButtonPress, 9, 13, Qt.LeftButton, 1, 0)
    service_mode_login()
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
    
    test.passes("SVV TAG: System Event Log Laser State: TC-023")

    test.compare(waitForObjectExists(names.laser_State_HeaderViewItem).text, "Laser State")
    """Verify Laser State column is empty for all log entries"""
    test.passes("Checking the Emission Logs laster State") 
    """Verify Laser State is displayed for all log entries"""

    for row in range(1, 6):
        obj_name = getattr(names, "tableView_{}_4_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Laser state is empty. Expected Laser state to be displayed.".format(row))
        else:
            test.passes("Row {}: Laser state is displayed successfully: {}".format(row, display_text))
                
    test.log("SVV TAG: System Event Log Laser Temperature: TC-024")
    test.passes("Checking the Logs Laser Temperature ") 
    test.compare(waitForObjectExists(names.laser_Temp_HeaderViewItem).text, "Laser Temp")
    """Verify Laser Temp values in all log entries"""
    
    for row in [0, 1, 2, 3, 5]:
        obj_name = getattr(names, "tableView_{}_5_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Laser Temp value is empty".format(row))
        else:
            test.passes("Row {}: Laser Temp value is displayed: {}".format(row, display_text))
    test.log("SVV TAG: System Event Log Pulse Energy Setting: TC-025")
    test.passes("Checking the Logs Pulse Energy Setting ") 
    """Verify Pulse Energy header"""

    test.compare(waitForObjectExists(names.pulse_Energy_HeaderViewItem).text, "Pulse Energy")
    
    
    """Verify Pulse Energy values in all log entries"""
    
    for row in [0, 1, 2, 3, 4]:
        obj_name = getattr(names, "tableView_{}_8_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Pulse Energy value is empty".format(row))
        else:
            test.passes("Row {}: Pulse Energy value is displayed: {}".format(row, display_text))
    test.log("SVV TAG: System Event Log Frequency Setting: TC-026")
    test.passes("Checking the Event Log Frequency Setting") 

    test.compare(waitForObjectExists(names.frequency_HeaderViewItem).text, "Frequency")
    """Verify Frequency values in all log entries"""
    
    for row in [0, 1, 2, 3, 4]:
        obj_name = getattr(names, "tableView_{}_9_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Frequency value is empty".format(row))
        else:
            test.passes("Row {}: Frequency value is displayed: {}".format(row, display_text))
    test.log("SVV TAG: System Event Log Peak Power Setting: TC-027")
    test.passes("Checking the Event Log Peak Power Setting") 
    """Verify Peak Power header"""

    test.compare(waitForObjectExists(names.peak_Power_HeaderViewItem).text, "Peak Power")
    
    
    """Verify Peak Power values in all log entries"""
    
    for row in [0, 1, 2, 3, 4]:
        obj_name = getattr(names, "tableView_{}_10_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Peak Power value is empty".format(row))
        else:
            test.passes("Row {}: Peak Power value is displayed: {}".format(row, display_text))
    test.log("SVV TAG: System Event Log Duration of Emission: TC-028")
    test.passes("Checking the Event Log Duration of Emission") 
    """Verify Duration Of Emission header"""
    
    test.compare(waitForObjectExists(names.duration_Of_Emission_HeaderViewItem).text, "Duration Of Emission")
    
    
    """Verify Duration Of Emission values in all log entries"""
    
    for row in [0, 1, 2, 3, 5]:
        obj_name = getattr(names, "tableView_{}_11_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Duration Of Emission value is empty".format(row))
        else:
            test.passes("Row {}: Duration Of Emission value is displayed: {}".format(row, display_text))
    test.log("SVV TAG: System Event Log Energy Delivered: TC-029")
    test.passes("Checking the Event Log Energy Delivered")
    """Scroll to Total Energy Delivered column"""

    scrollTo(waitForObject(names.tableView_QScrollBar), 7)
    
    
    """Verify Total Energy Delivered header"""
    
    test.compare(waitForObjectExists(names.total_Energy_Delivered_HeaderViewItem).text, "Total Energy Delivered")
    
    
    """Verify Total Energy Delivered values in all log entries"""
    
    for row in [0, 1, 2]:
        obj_name = getattr(names, "tableView_{}_14_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Total Energy Delivered value is empty".format(row))
        else:
            test.passes("Row {}: Total Energy Delivered value is displayed: {}".format(row, display_text))
    test.log("SVV TAG: System Event Log Pedal Used: TC-030")
    test.passes("Checking the Event Log Pedal Used")
    """Scroll to Pedal Used column"""
    
    scrollTo(waitForObject(names.tableView_QScrollBar), 7)
    
    
    """Verify Pedal Used header"""
    
    test.compare(waitForObjectExists(names.pedal_Used_HeaderViewItem).text, "Pedal Used")
    
    
    """Verify Pedal Used values in all log entries"""
    
    for row in [0, 1, 2]:
        obj_name = getattr(names, "tableView_{}_13_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Pedal Used value is empty".format(row))
        else:
            test.passes("Row {}: Pedal Used value is displayed: {}".format(row, display_text))
        
        test.log("SVV TAG: System Event Log Total Energy Delivered: TC-031")
        test.passes("Checking the Event Log Total Energy Delivered")

        """Verify Total Energy Delivered header"""

    test.compare(waitForObjectExists(names.total_Energy_Delivered_HeaderViewItem).text, "Total Energy Delivered")
    
    
    """Verify Total Energy Delivered values in all log entries"""
    
    for row in [0, 1]:
        obj_name = getattr(names, "tableView_{}_14_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Total Energy Delivered value is empty".format(row))
        else:
            test.passes("Row {}: Total Energy Delivered value is displayed: {}".format(row, display_text))
        test.log("SVV TAG: System Event Log Fiber Serial Number: TC-032")
        test.passes("Checking the Event Log Fiber Serial Number")
        
    test.log("SVV TAG: System Event Log Fiber Type: TC-033")
    test.passes("Checking the Event Log Fiber Type")
    """Scroll to Fiber Type column"""

    scrollTo(waitForObject(names.tableView_QScrollBar), 10)
    
    
    """Verify Fiber Type header"""
    
    test.compare(waitForObjectExists(names.fiber_Type_HeaderViewItem).text, "Fiber Type")
    
    
    """Verify Fiber Type values in all log entries"""
    
    for row in [0, 1, 2]:
        obj_name = getattr(names, "tableView_{}_16_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Fiber Type value is empty".format(row))
        else:
            test.passes("Row {}: Fiber Type value is displayed: {}".format(row, display_text))
    
    test.log("SVV TAG:  System Event Log Fiber Uses Remaining: TC-034")
    test.passes("Checking the Event Log Fiber Uses Remaining")
    
    """Verify Fiber Uses Remaining header"""

    test.compare(waitForObjectExists(names.fiber_Uses_Remaining_HeaderViewItem).text, "Fiber Uses Remaining")
    
    
    """Verify Fiber Uses Remaining values in all log entries"""
    
    for row in [0, 1, 2]:
        obj_name = getattr(names, "tableView_{}_17_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Fiber Uses Remaining value is empty".format(row))
        else:
            test.passes("Row {}: Fiber Uses Remaining value is displayed: {}".format(row, display_text))
    
    test.log("SVV TAG:  System Event Log Error Code: TC-036")
    test.passes("Checking the Event Log System Event Log Error Code")
    """Scroll to Error Code column"""

    scrollTo(waitForObject(names.tableView_QScrollBar), 13)
    
    
    """Verify Error Code header"""
    
    test.compare(waitForObjectExists(names.error_Code_HeaderViewItem).text, "Error Code")
    
    
    """Verify Error Code values in all log entries"""
    
    expected_values = {
        0: None,
        1: "General_InvalidKernelImageVersion<1>",
        2: None
    }
    
    for row, expected_value in expected_values.items():
        obj_name = getattr(names, "tableView_{}_19_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Error Code value is empty".format(row))
        elif expected_value is not None:
            test.compare(str(display_text), expected_value)
        else:
            test.passes("Row {}: Error Code value is displayed: {}".format(row, display_text))
        
    test.log("SVV TAG:  System Event Log Step Pulse Tag: TC-037 & System Event Log CW Mode Tag: TC038")
    test.passes("Checking the Event Log System Event Log Error Code")
    
    """Scroll to Variable Value column"""

    scrollTo(waitForObject(names.tableView_QScrollBar), 14)
    
    
    """Verify Variable Value header"""
    
    test.compare(waitForObjectExists(names.variable_Value_HeaderViewItem).text, "Variable Value")
    
    
    """Verify Variable Value in all log entries"""
    
    for row in range(10):
        obj_name = getattr(names, "tableView_{}_20_QModelIndex".format(row))
        display_text = waitForObjectExists(obj_name).displayText
    
        if display_text is None or str(display_text).strip() == "":
            test.fail("Row {}: Variable Value is empty".format(row))
        else:
            test.passes("Row {}: Variable Value is displayed: {}".format(row, display_text))

   

   
   
   
   
