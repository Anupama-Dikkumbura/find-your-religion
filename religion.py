q1 = input("How many gods do you want to worship(none,one,more): ")
if q1=='none':
    q2 = input("Are you Rich and Insane(yes or no): ")
    if q2 == 'yes' or 'YES' or 'Yes':
        print("You should be a Scientologist")
    elif q2== 'no' or 'NO' or 'No':
        print("You shold be an Atheist")
    else:
        print("wrong input !!!!!")
elif q1 == 'one':
    q3 = input("How do you feel about Bacon(love or mehh): ")
    if q3=='love':
        q4  = input("Are you a naturally annoying person(yes or no): ")
        if q4 == 'yes' or 'YES' or 'Yes':
            q5 = input("Do you think underware can be magical(yes or no): ")
            if q5=='yes' or 'YES' or 'Yes':
                print("You should be a Mormon")
            elif q5=='no' or 'NO' or 'No':
                print("You should be a Jehovah's witness")
            else:
                print("wrong input !!!!!")
        elif q4=='no' or 'NO' or 'No':
            print("You shoukd be a boring, generic Christian")
        else:
            print("wrong input !!!!!")
    elif q3=='mehh':
        q6 = input("How do you feel about Hummus(love or mehh): ")
        if q6=='love':
            print("You should be a Muslim")
        elif q6=='mehh':
            print("You should be Jewish")
        else:
            ("wrong input !!!!!")
    else:
        ("wrong input !!!!!")
elif q1=='more':
    q7=input("Do you want to be Reincarnated(yes or no): ")
    if q7=='yes' or 'YES' or 'Yes':
        q8= input("Do you own a Black Cat(yes or no): ")
        if q8=='yes' or 'YES' or 'Yes':
            print("You should be a wiccan")
        elif q8=='no' or 'NO' or 'No':
            q9=input("Do you prefer Indian takeout or Chinese Takeout (indian or chinese): ")
            if q9=='indian':
                print("You should be a Hindu")
            elif q9=='chinese':
                print("You should be a Buddhist")
            else:
                print("wrong input !!!!!")
        else:
            print("wrong input !!!!!")

    elif q7=='no' or 'NO' or 'No':
        print("You should follow the Mayan Religion")
    else:
        print("wrong input !!!!!")

else:
    print("wrong input !!!!!")
