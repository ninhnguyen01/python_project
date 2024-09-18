# 1. Input: two locations (“from” and “to”) each defined by a pair of latitude/longitude coordinates
# 2. Output: The midpoint on the shortest path between these two locations on the surface of the Earth

# import package
import haversine as hs
from haversine import Unit

# You will enter name, latitude and longitude of each location in the function during execution of code for input
# Use the function below to calculate the distance between the 2 points
def haversine_formula():
    # Check your FROM location name before input
    # Check your FROM location point before input
    from_location_name = str(input("Enter 1st location name: ")) # sample - Lyon
    location_point_x = float(input("Enter x point: ")) # sample (45.7597)
    location_point_y = float(input("Enter y point: ")) # sample (4.8422)
    from_location_point = (location_point_x,location_point_y) 
    print(f"The 1st location is {from_location_name} and the latitude/longitude are {from_location_point}")
    print('\n')
    
    # Check your TO location name before input
    # Check your TO location point before input
    to_location_name = str(input("Enter 2nd location name: ")) # sample - Paris
    location_point_x2 = float(input("Enter x point: ")) # (48.8567)
    location_point_y2 = float(input("Enter y point: ")) # (2.3508)
    to_location_point = (location_point_x2, location_point_y2)
    print(f"The 2nd location is {to_location_name} and the latitude/longitude are {to_location_point}")
    print('\n')
    
    # Calculate distance between the 2 points with haversine formula
    # Change the parameter in "unit" for distance conversion: Unit.Miles, Unit.METERS, Unit.KILOMETERS, etc 
    midpoint_in_miles = hs.haversine(from_location_point,to_location_point, unit=Unit.MILES)
    print(f"The distance between {from_location_name} to {to_location_name} in MILES is: ",midpoint_in_miles)
    print('\n')
    # Sample result in miles: ~244

    midpoint_in_km = hs.haversine(from_location_point,to_location_point, unit=Unit.KILOMETERS)
    print(f"The distance between {from_location_name} to {to_location_name} in KILOMETERS is: ",midpoint_in_km)
    print('\n')
    # Sample result in kilometers: ~392

# Call the main function to call the haversine_formula function
if __name__ == '__main__':
    def main():
        haversine_formula()
    
    main()