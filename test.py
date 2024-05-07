months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}


print(months.items())
name_value ={}

for v, k in months.items():
    name_value[k] = v


print (name_value['February'])

name_value = {v: k for k, v in months.items()}