from math import pi

def circle_area_coverage(radius_of_circle_1, radius_of_circle_2):
    #Impossible for the radius of a circle to be less than or equal to 0
    if radius_of_circle_1 <= 0 or radius_of_circle_2 <= 0:
        print("Invalid argument(s). Both radii must be positive.")
        return None #Returning None to end the function early

    area_of_circle_1 = pi * (radius_of_circle_1**2)
    area_of_circle_2 = pi * (radius_of_circle_2**2)
    larger_circle_area = max(area_of_circle_1, area_of_circle_2) #The bigger value is stored in larger_circle_area
    smaller_circle_area = min(area_of_circle_1, area_of_circle_2) #Same as above, but the smaller value is stored

    #Multiplying by 100 in order to have it in some percentage form
    return (smaller_circle_area/larger_circle_area) * 100

#To test the function
circle_area_coverage_percentage = circle_area_coverage(3, 2)
print(f"Percentage: {circle_area_coverage_percentage:.2f}")