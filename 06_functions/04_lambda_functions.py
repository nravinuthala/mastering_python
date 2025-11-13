# circ = 56
circ = lambda side1, side2, side3: side1 + side2 + side3


# print(circ(34, 45, 67))

# def circ(side1, side2, side3):
#     return side1 + side2 + side3

# circ = lambda side1, side2, side3: side1 + side2 + side3

print((lambda side1, side2, side3: side1 + side2 + side3)(34, 45, 67))
