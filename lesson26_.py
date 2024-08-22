from math import pi

#ex1
def area(r, alpha): #O(1)
    degree_to_radian = alpha * pi / 180
    return f"{(pi * r ** 2) * degree_to_radian / 360:.2f}"


#ex2
_roman = {1: 'I',
          2: 'II',
          3: 'III',
          4: 'IV',
          5: 'V',
          6: 'VI',
          7: 'VII',
          8: 'VIII',
          9: 'IX',
          10: 'X',
          50: 'L',
          100: 'C',
          500: 'D',
          1000: 'M'}


def expanded_form(number):
    list_number = list(str(number))
    # check = []
    count = len(list_number)-1
    for element in range(len(list_number)):
        d = list_number[element] + (count * "0")
        if d[0] != "0":
            yield int(d)
            # check.append(d)
        count -= 1


def main(num):

    roman_number = ""
    for k in expanded_form(num):
        if k in _roman:
            roman_number += _roman[k]
        #_________K <= 59____________
        elif 19 < k < 40:
            roman_number += (k // 10) * "X"
        elif k == 40:
            roman_number += "XL"
        #_________K <= 199 ___________
        elif 59 < k < 90:
            roman_number += "L" + (k - 50) // 10 * "X"
        elif k == 90:
            roman_number += "XC"
        #_________K <= 599____________
        elif 199 < k < 400:
            roman_number += (k // 100) * "C"
        elif k == 400:
            roman_number += "CD"
        #_________K <= 999____________
        elif 599 < k < 900:
            roman_number += "D" + (k - 500) // 100 * "C"
        elif k == 900:
            roman_number += "CM"
        #_________K >= 3000___________
        elif 1000 < k <= 3000:
            roman_number += k // 1000 * "M"
    return roman_number


# while True:
#     user = input("Arabic To Roman: ")
#     if user == "":
#         break
#     print(main(user))


#ex3
def filter_maximum_len(array: list) -> list: #O(n)
    return list(filter(lambda x: len(x) == len(max(array, key=len)), array))

