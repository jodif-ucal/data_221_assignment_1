from math import pi

def circle_area_coverage(radius_of_circle_1, radius_of_circle_2):
    if radius_of_circle_1 < 0 or radius_of_circle_2 < 0:
        print("Invalid argument(s). Both radii must be positive.")
        return None

    area_of_circle_1 = pi * (radius_of_circle_1**2)
    area_of_circle_2 = pi * (radius_of_circle_2**2)
    larger_circle_area = max(area_of_circle_1, area_of_circle_2)
    smaller_circle_area = min(area_of_circle_1, area_of_circle_2)

    return (smaller_circle_area/larger_circle_area) * 100

circle_area_coverage_percentage = circle_area_coverage(3, 2)
print(f"Percentage: {circle_area_coverage_percentage:.2f}")