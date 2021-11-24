## use a list to remember a 1d map

# [x] [ ] [x] [ ] [x] [ ] 
# 0 - free
# 1 - occupied

parking = [0, 0, 0, 1, 0, 0, 1]
# index

index_to_park = int(input("Where ?"))

# HW 1 --- check if index is NOT OUT of RANGE !!!
if index_to_park >= 0 and index_to_park < len(parking) :
#if index_to_park >= 0 and index_to_park <= 6 :
#    parking
    if parking[index_to_park] == 1:
        print("Occupied !!! ")
    else:
        print("You can park there !!! ")

    parking[index_to_park] = 1

    for index in range(0, len(parking)):
        if parking [index] == 1:
            print(index, "[x] ", end="" )
        elif parking[index] == 0:
            print(index, "[ ] ", end="")

else:
   print("You can NOT PARK there ")


"""
if parking[index_to_park] == 1:
    print("Occupied !!! ")
else:
    print("You can park there !!! ")

parking[index_to_park] = 1

for index in range(0, len(parking)):
    if parking [index] == 1:
        print(index, "[x] " )
    elif parking[index] == 0:
        print(index, "[ ] ",)
"""


