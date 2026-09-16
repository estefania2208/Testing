import math
coordinate_x = float(input("Enter coordinate x: "))
coordinate_y = float(input("Enter coordinate y: "))
distance = math.hypot(coordinate_x,coordinate_y)
if distance <= 50:
    x= "Safe zone"
elif distance > 50 and distance <= 100:
    x = "Caution zone"
elif distance > 100 and distance <= 150:
    x = "Return to base"
elif distance > 150:
    x = "Out of range"
print(round(distance,2))
print(x)
