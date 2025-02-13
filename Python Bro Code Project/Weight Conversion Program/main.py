# Python Weight converter

def weight_converter():
    print()
    try:
        weight = float(input("Enter your weight: "))
        unit = input("Kilograms or Pound: (K/LB): ").upper()

        if unit == "K":
            weight *= 2.205
            unit = "Kilo"
            print(f"Weight: {round(weight,2)} in {unit} \n")
        elif unit == "LB":
            weight /= 2.205
            unit = "Pounds"
            print(f"Weight: {round(weight,2)} in {unit} \n")
        else:
            print(f"Weight: {unit} was NOT VALID!\n")
    except:
        print("Invalid Entry!")
        print("Please enter your weight in numbers!\n")
        weight_converter()

weight_converter()