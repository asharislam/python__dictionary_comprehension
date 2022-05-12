###### Dictionary comprehension #########
"""name_age = {
    "ijhar": 30,
    "hasan": 40,
    "majhar": 30
}"""
##################################
"""num_dict ={}
for num in range(1, 30):
    num_dict[num] = num **3
print(num_dict)"""
############## short ###############
"""num_dict_comp = { number: number**3 for number in range(1,30) if number % 2 == 0 }
print(num_dict_comp)
############"""

"""num_dict_comp = { number: number**3 if number % 2 == 0 else "Odd" for number in range(1,30)}
print(num_dict_comp)
"""

######### if age is odd or not##############
name_age = {
    "ijhar": 45,
    "hasan": 40,
    "majhar": 30,
    "elias": 25
}
age_dict = { name:"old" if age >= 40 else "yang" for name, age in name_age.items()}
print(age_dict)

