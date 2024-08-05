"""
Programming Python
Desc: Complex numbers as 2D vectors
All right reserved lotus code studios Mar 2021
"""
import math

# defining the coordinates
miami_fl = complex(-80.191788, 25.761681)
san_juan = complex(-66.105721, 18.466333)
hamilton = complex(-64.78303, 32.2949)
city_coord = complex

# calculating the magnitude
z = 3 + 2j
pyt = math.sqrt(z.real**2 + z.imag**2)
# print(pyt)

# geometric center
geometric_center = sum([miami_fl, san_juan, hamilton])/3
# print(geometric_center)

# finding the distance between 2 points
v1 = geometric_center - miami_fl
v2 = geometric_center - san_juan
v3 = geometric_center - hamilton

# translating, flipping, scaling and rotating
triangle = miami_fl, san_juan, hamilton

# translating
# inverts the triangle around the real and imaginary axis
offset = -geometric_center
centered_triangle = [vertex + offset for vertex in triangle]

# flipping
flip_horizontal = [complex(-v.real, v.imag) for v in centered_triangle]
flip_vertical = [complex(v.real, -v.imag) for v in centered_triangle]

# scaling
scaled_triangle = [1.5 * vertex for vertex in centered_triangle]

# rotating