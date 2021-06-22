'''
Project 3: Rabbits Rabbits Rabbits
CS 1400-601
Jessica Reece
March 5, 2021
'''
file = open("rabbits.csv", "w")
#create variables
month = 1
adults = 1
babies = 0
total = adults + babies
file.write("#Table of rabbit pairs\n")
file.write("Month, Adults, Babies, Total\n")
file.write(f"{month}, {adults}, {babies}, {total}\n")
while total < 500:
    month += 1
    babies = adults
    adults = total
    total = adults + babies
    file.write(f"{month}, {adults}, {babies}, {total}\n")
file.write(f"#Cages will run out in month: {month}")
file.close()