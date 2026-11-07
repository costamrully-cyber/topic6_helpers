#Augustine 
#assignment topic6_helper

def calculate_total(price, quantity):
    return price * quantity

def add_vat(price, rate=0.16):
    total = price + (price * rate)
    return round(total, 2)

def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

def is_pass(mark):
    if mark >= 50:
        return True
    else:
        return False

def greet(name):
    print("Hello,", name)

print(calculate_total(250, 4))
print(calculate_total(85.5, 3))

print(add_vat(1000))
print(add_vat(1000, 0.10))
print(add_vat(price=500, rate=0))

marks = [85, 72, 64, 51, 38]
for mark in marks:
    print(mark, get_grade(mark), is_pass(mark))

result = greet("Amina")
print(result)

print(add_vat(calculate_total(250, 4)))