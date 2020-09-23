import math

radius = int(input("Please, enter a radius:"))

print(f"radius = {radius}")

print(f"\nCircle:\nArea = {math.pi*radius**2}\nCircumference = {2*math.pi*radius}\n")

print(f"\nSphere:\nVolume = {(4/3)*math.pi*radius**3}\nSurface area = {4*math.pi*radius**2}\n")
