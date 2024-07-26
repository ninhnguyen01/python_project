# Requirements:

# Assignment: Write a module/package in Python that implements a function with the following characteristics:

# 1. Input: two locations (“from” and “to”) each defined by a pair of latitude/longitude coordinates
# 2. Output: The midpoint on the shortest path between these two locations on the surface of the Earth
# 3. Bonus points: Returning a path of N coordinates evenly spaced along the path
# Include documentation on how to run the module/package.

# import package
from geopy.distance import geodesic as GD, great_circle as GC

# Enter name, latitude and longitude of each location in the function during execution of code for input

# Use haversine_formula function below to calculate the distance between the 2 points
def geodisc_formula():
    # Check your FROM location name before input
    # Check your FROM location point before input
    from_location_name = str(input("Enter 1st location name: ")) # sample - Lyon
    location_point_x = float(input("Enter x point: ")) # sample (45.7597)
    location_point_y = float(input("Enter y point: ")) # sample (4.8422))
    from_location_point = (location_point_x,location_point_y) 
    print(f"The 1st location is {from_location_name} and the latitude/longitude are {from_location_point}")
    
    # Check your TO location name before input
    # Check your TO location point before input
    to_location_name = str(input("Enter 2nd location name: ")) # sample - Paris
    location_point_x2 = float(input("Enter x point: ")) # 48.8567
    location_point_y2 = float(input("Enter y point: ")) # 2.3508
    to_location_point = (location_point_x2, location_point_y2)
    print(f"The 2nd location is {to_location_name} and the latitude/longitude are {to_location_point}")
    
    # Calculate distance between the 2 points with "geodisc" method
    midpoint_in_miles = GD(from_location_point,to_location_point).miles
    print(f"The distance between {from_location_name} to {to_location_name} in MILES with GEODISC method is: ",midpoint_in_miles)
    # Sample result in miles: ~244

    midpoint_in_km = GD(from_location_point,to_location_point).kilometers
    print(f"The distance between {from_location_name} to {to_location_name} in KILOMETERS with GEODISC method is: ",midpoint_in_km)
    # Sample result in kilometers: ~392

    # Calculate distance between the 2 points with "great circle" method
    midpoint_in_miles = GC(from_location_point,to_location_point).miles
    print(f"The distance between {from_location_name} to {to_location_name} in MILES with GREAT CIRCLE method is: ",midpoint_in_miles)
    # Sample result in miles: ~244

    midpoint_in_km = GC(from_location_point,to_location_point).kilometers
    print(f"The distance between {from_location_name} to {to_location_name} in KILOMETERS with GREAT CIRCLE method is: ",midpoint_in_km)
    # Sample result in kilometers: ~392

# Call the main function to call the geodisc_formula function
def main():
    geodisc_formula()
    
main()
