"""
This program is by Altai and Chingun
"""
confirm = "N"
while confirm == "N":
    #Delivery function
    #guest list
    guest_list = {'altai': 112,'chingun':123,'vertador':124}
    
    #asking name
    name = input('What is your name? ')
    print('Hello', name)
    name = name.lower()
    
    #asking room number
    room_num = int(input('What is your room number? '))
    print('Room number', room_num)
    
    #determining if the info is correct
    if room_num == guest_list[name]:
        print("info correct")
    else:
        print("Sorry, wrong room number")
        while room_num != guest_list[name]:
            name = input('What is your name? ')
            print('Hello', name)
    
            room_num = int(input('What is your room number? '))
            print('Room number', room_num)
            
            if room_num == guest_list[name]:
                print("info correct")
                break
            
    #the menu
    appetizers = ('Fish Chips','Chicken Nuggets','Spring Rolls','None')
    main_course = ('BQQ Steak','Pork Chop','Salmon', 'None')
    dessert = ('Icecream','Pudding','Cake', 'None')
    
    #the menu
    appetizers = ('Fish Chips','Chicken Nuggets','Spring Rolls','None')
    main_course = ('BQQ Steak','Pork Chop','Salmon', 'None')
    dessert = ('Icecream','Pudding','Cake', 'None')
    
    #appetizer choice
    print('We have the following as appetizers')
    for dish in appetizers:
        print(dish)
    chosen_appetizer = input("Which one would you like? ")
    
    
    #checking if info correct
    if chosen_appetizer in(appetizers):
            print("info correct")
    
    while chosen_appetizer not in(appetizers):
        if chosen_appetizer in(appetizers):
            print("info correct")
            break
        else:
            print(" ")
            print("error, input not accepted. (check your spelling and capitalization)")
            print('We have the following as appetizers')
            for dish in appetizers:
                print(dish)
            print(" ")
            chosen_appetizer = input("Which one would you like? ")
            
    #Main course
    print('We have the following as main courses')
    for dish in main_course:
        print(dish)
    chosen_main_course = input("Which one would you like? ")
    
    
    #checking if info correct
    if chosen_main_course in(main_course):
            print("info correct")
    
    while chosen_main_course not in(main_course):
        if chosen_main_course in(main_course):
            print("info correct")
            break
        else:
            print(" ")
            print("error, input not accepted. (check your spelling and capitalization)")
            print('We have the following as main courses')
            for dish in main_course:
                print(dish)
            print(" ")
            chosen_main_course = input("Which one would you like? ")
    
    #dessert choosing
    print('We have the following as desserts')
    for dish in dessert:
        print(dish)
    chosen_dessert = input("Which one would you like? ")
    
    
    #checking if info correct
    if chosen_dessert in(dessert):
            print("info correct")
    
    while chosen_dessert not in(dessert):
        if chosen_dessert in(dessert):
            print("info correct")
            break
        else:
            print(" ")
            print("error, input not accepted. (check your spelling and capitalization)")
            print('We have the following as dessert')
            for dish in dessert:
                print(dish)
            print(" ")
            chosen_dessert = input("Which one would you like? ")
    
    #Delivery function
    delivery_times = ("9 AM","10 AM","11 AM","12 PM","1 PM", "2 PM", "3 PM", "4 PM","5 PM", "6 PM", "7 PM", "8 PM" )
    #delivery time function
    
    print('available times: ')
    for time in delivery_times:
        print(time)
    chosen_time = input("what time should it be delivered? ")
        
        #checking if info correct
    if chosen_time in(delivery_times):
            print("info correct")
    while chosen_time not in(delivery_times):
        if chosen_time in(delivery_times):
            print("info correct")
            break
        else:
            print(" ")
            print("error, input not accepted. (check your spelling and capitalization)")
            print('available times')
            for time in delivery_times:
                print(time)
            chosen_time = input("What time should it be delivered? ")
    
    print('confirm order:', (chosen_appetizer), ",", (chosen_main_course), ",", (chosen_dessert), "at", (chosen_time), "to room", (room_num), "ordered by",(name))
    confirm = input("confirm? Y/N ")
    if confirm == "Y":
        print("Your order is no confirmed")
        break
    elif confirm == "N":
        print('')
    else: 
        print("Incorrect input")
        confirm = input("confirm? Y/N ")
