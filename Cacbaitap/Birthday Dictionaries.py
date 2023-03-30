birthday = {
    "ayaka" : "Ayaka birthday is 28/10/2003", #Dont Know Year:p
    "hutao" : "Hutao birthday is 15/7/2003",  #Dont Know Year:p
    "raidenShogun" : " Ei birthday is 26/6/2000" #Dont Know Year:p
}



print("Welcome to the birthday dictionary. We know the birthdays of:")
print("Hutao \nAyaka \nRaidenShogun")
print("Who's birthday do you want to look up?")
choose = input()
if choose == "ayaka":
    print(birthday["ayaka"])
elif choose == "hutao":
    print(birthday["hutao"])
elif choose == "raidenshogun":
    print(birthday["raidenShogun"])
