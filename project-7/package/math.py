# import math as m

# def calculate_factorial(n):
#     if n < 0:
#         return "Factorial not defined for negative numbers."
#     return m.factorial(n)

# def compound_interest(p, r, t):
#     # standard formula: A = P * (1 + R/100)^T
#     amount = p * ((1 + r / 100) ** t)
#     return round(amount, 2)

# # Direct run test code
# if __name__ == "__main__":
#     print("Testing custom math utilities directly.")

import math

def factorial(n):
    return math.factorial(n)

def compound_interest(p, r, t):
    amount = p * ((1 + r / 100) ** t)
    return round(amount, 2)

def trig_values(angle):
    a = math.radians(angle)
    return {
        "sin": round(math.sin(a), 4),
        "cos": round(math.cos(a), 4),
        "tan": round(math.tan(a), 4)
    }

def area_circle(r):
    return round(math.pi * r * r, 2)

def area_rectangle(l, w):
    return round(l * w, 2)