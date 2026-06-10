from rules.voltage_rule import check_voltage

def main():
    print("EEE Fault Detection System — v0.1")

    with open("data/sample.csv", "r") as file:
        next(file)  # Skip header

        for row in file:
            row = row.strip().split(",")

            voltage = int(row[0])

            result = check_voltage(voltage)

            print(f"Voltage: {voltage} -> {result}")

main()