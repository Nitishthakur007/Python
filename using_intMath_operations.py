def integer_math(Side, Radius):
    AreaSquare = 4 * Side
    VolumeCube = Side ** 3
    AreaCircle = 3.14 * (Radius ** 2)
    VolumeSphere = 4/3 * (3.14 * (Radius ** 3))
    Square  = str(round(AreaSquare,2))
    Cube = str(round(VolumeCube, 2))
    Circle = str(round(AreaCircle, 2))
    Sphere = str(round(VolumeSphere, 2))
    print("Area of Square is " + Square)
    print("Volume of Cube is " + Cube)
    print("Area of Circle is " + Circle)
    print("Volume of Sphere is " + Sphere)


integer_math(5,7)






