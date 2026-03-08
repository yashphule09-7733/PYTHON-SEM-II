import shapes

print("Choose a shape to find area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    r = float(input("Enter radius of circle: "))
    area = shapes.area_circle(r)
    print("Area of Circle =", area)

elif choice == 2:
    L = float(input("Enter length of rectangle: "))
    w = float(input("Enter width of rectangle: "))
    area = shapes.area_rectangle(L, w)
    print("Area of Rectangle =", area)

elif choice == 3:
    L = float(input("Enter length of triangle: "))
    w = float(input("Enter width of triangle: "))
    area = shapes.area_triangle(L, w)
    print("Area of Triangle =", area)

else:
    print("Invalid choice")