# Python Compound Interest Calculator in Dollars

def interest_calculator():
    principle = 0
    rate = 0
    time = 0
    entry = True
    
    try:
        while entry:
            principle = float(input("Enter the principle amount: "))
            print()
            if principle <= 0:
                print("Principle can't be less than or equal to 0!")
            else:
                break
            
        while entry:
            rate = float(input("Enter the rate: "))
            print()
            if rate <= 0:
                print("Rate can't be less than or equal to 0!")
            else:
                break

        while entry:     
            time = int(input("Enter the time in year(s): "))     
            print() 
            if time < 1:
                print("Time can't be less than 1 year!")   
            else:
                break
        
        total = principle * pow(1 + rate/100,time)
        print(f"Balance after {time} year(s): ${total:.2f}\n")

    except:
        print("Something went wrong! Exiting program...\n")

interest_calculator()