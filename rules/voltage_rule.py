def check_voltage(voltage):
    if voltage  > 250:
        return "High_Voltage_fault"
    elif voltage < 180:
        return "Low_Voltage_fault"
    else:
        return "Normal"