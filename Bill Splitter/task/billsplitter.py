import random
# write your code here
friendList = {}

friends_number = int(input("Enter the number of friends joining (including you):"))
if friends_number < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(friends_number):
        name = input()
        friendList[name]=0

    totalBillValueUP = int(input("Enter the total bill value:"))


    if 'Yes' == input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:"):
        luckyOne = random.choice(list(friendList.keys()))
        print(luckyOne + " is the lucky one!")

        blik = round(totalBillValueUP/(friends_number-1),2)
        for k in friendList:
            friendList[k] = blik
        friendList[luckyOne]=0
        print(friendList)

    else:
        print("No one is going to be lucky")
        for k in friendList:
            friendList[k] = round(totalBillValueUP/friends_number,2)
        print(friendList)



