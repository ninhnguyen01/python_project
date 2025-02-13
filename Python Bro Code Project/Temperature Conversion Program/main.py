# Python Temperature Conversion 

def temp_converter():
    print()
    try:
        unit = input("Is temperature in Celsius or Fahrenheit?: (C/F): ").upper()
        temp = float(input("Enter the temperature: "))
        
        if unit == "C":
            temp = (temp * 9/5) + 32
            print(f"Temperature in Fahrenheit: {round(temp,2)} °F \n")
        elif unit == "F":
            temp = (temp - 32) * 5/9
            print(f"Temperature in Celsius: {round(temp,2)} °C \n")
        else:
            print("Invalid Entry!")
            print("Please enter temperature in Celsius or Fahrenheit!\n")
            temp_converter()

    except:
        print("Error with temperature entry! Exiting program...\n")        

temp_converter()