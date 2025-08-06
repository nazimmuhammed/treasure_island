print("welcome to ticket fair station!!!!")
height=int(input("may ik the hight of yours?"))
fare=0
if(height>=150):
    print("Congratsss!! you are weclome to our adventurous ride")
    age=int(input("enter your age sir/maam"))
    if(age<12):
        fare=5
        print("childs fare is $5")
    elif(age<=18):
        fare =12
        print("teens fare is $12")
    else:
        fare=18
        print("for adults its $18")
    no_of_members=int(input('noww we need you to enter no of memebers in your grp!!!'))
    if(no_of_members==2):
        print("perfect!! you can sitt in the tow seatersss ride!!!")
    elif(no_of_members==3):
        print("you can sit in the three seater ridess!!!")
    
    else:
        print("no prob!! we can split you guys guys in pairs and have adjacent coaches")
    response=input("enter Y if you guys need a crazzyy fam photo or N if not")
    if(response=="Y"):

        fare=fare+3
        total_fare=fare*no_of_members
        print(f"heyy you total fare with an addtion of 3 dollars is {total_fare}")
    else:
        total_fare=fare*no_of_members
        print(f"no worries your total fare is {total_fare}")
    print("thanku for your lovely time hope to see you soonn!!!")
else:
    print("sorry guys next time when you become 150 cm !!!")

    
