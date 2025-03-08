"""
Module for computing the circumference, area, and volume of a circle or sphere based on user input.

This script prompts the user for a radius value and then calculates:
- The circumference of a circle.
- The area of a circle.
- The volume of a sphere.

Functions:
    - circumference_of_circle(): Computes the circumference of a circle given the radius.
    - area_of_circle(): Computes the area of a circle given the radius.
    - volume_of_sphere(): Computes the volume of a sphere given the radius.

Example Usage:
    $ python circle_calculations.py
    Please enter the radius of your circle/sphere: 5
    The circumference of a circle with a radius of 5.0 is 31.4159
    The area of a circle with a radius of 5.0 is 78.5398
    The volume of a sphere with a radius of 5.0 is 523.5988

Author: Ike Iloegbu
License: MIT
"""
import math

def get_radius():
    """
    Prompts the user to enter the radius of the circle or sphere.
    
    Returns:
        float: The user-provided radius.
    """
    return float(input("Please enter the radius of your circle/sphere:  "))

def circumference_of_circle(r):
    """
    Computes the circumference of a circle given the radius.
    
    Args:
        r (float): Radius of the circle.
    
    Returns:
        float: Circumference of the circle.
    """
    return 2 * math.pi * r

def area_of_circle(r):
    """
    Computes the area of a circle given the radius.
    
    Args:
        r (float): Radius of the circle.
    
    Returns:
        float: Area of the circle.
    """
    return math.pi * r**2

def volume_of_sphere(r):
    """
    Computes the volume of a sphere given the radius.
    
    Args:
        r (float): Radius of the sphere.
    
    Returns:
        float: Volume of the sphere.
    """
    return (4/3) * math.pi * r**3

if __name__ == "__main__":
    radius = get_radius()
    print(f"The circumference of a circle with a radius of {radius} is {circumference_of_circle(radius):.4f}")
    print(f"The area of a circle with a radius of {radius} is {area_of_circle(radius):.4f}")
    print(f"The volume of a sphere with a radius of {radius} is {volume_of_sphere(radius):.4f}")


