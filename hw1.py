def SortTri(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b == c:
                return 'Equilateral Triangle'
            return "Isosceles Triangle"
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Right Triangle"
        if a != b != c:
            return "Scalene Triangle"
    else:
        return "Length error!!"

