roman = input("Enter roman:- ")

roman_dict = {
    "M": 1000,
    "CM": 900,
    "D":500 ,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L":50 ,
    "XL": 40 ,
    "X":10 ,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I":1
}


result = 0
temp = max(roman_dict.values())


for i in range(len(roman)):
    if roman[i] in roman_dict:
        if temp < roman_dict[roman[i]]:
            temp =  roman_dict[roman[i]] - temp*2
            result += temp

            temp = roman_dict[roman[i]]
        else:
            result += roman_dict[roman[i]]

            temp = roman_dict.get(roman[i])

print(result)




