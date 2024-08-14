# string, integer, float, boolean

jedi = "Obiwan Kenobi"
print(jedi[0])
print(jedi[-1])  # it works also backwards
print(jedi[2] + jedi[3])

# formatted strings
print(f"Who doesn't use his original first name anymore? {jedi}")

print(123_456_789)
print(1.34)
print(453_332 + 2.33)

print(type(jedi))
print(type(False))
print(type(1.33))
print(type(999_999))

# type casting
print(int("123") + int("321"))
print(type(bool("True")))
print(str(321))

# math
print(33 + 21)
print(33 - 21)
print(33 * 21)
print(33 / 21)  # returns float
print(33 // 21)  # return int, loosing accuracy
print(33 ** 21)  # 33 to the power of 21

# PEMDAS order
# parenthesses, exponents, multiplication, division, addition, subtraction
print(3 * 3 + 3 / 3 - 3)  # 7
print(3 * (3 + 3) / 3 - 3)  # 3

# BMI calculation, weight divided by the height squared
bmi = 86 / 1.75 ** 2
print(bmi)
print(round(bmi, 2))
