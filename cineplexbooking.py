confirm = "N"
doot = "Y"
while confirm == "N":
    while doot == "Y":
        def welcomeandquestions():
            #Welcome message
            print("Welcome to the Cineplex")

            #asking user for info
            user_name= input("What is your name? ")
            user_phone= ''

            #validating phone number
            
            while not user_phone.isnumeric():
                user_phone= input("what is the valid phone number? ")
                if not user_phone.isnumeric():
                    print("bad phonenumber") 
        welcomeandquestions()  

        #movie selection
        print ("1 = batman")
        print ("2 = Masha and the Bear")
        print ("3 = Pororo")
        def movies (movie):
            movie = movie.lower()
            match movie:
                case '1':
                    return 'Batman'
                case '2':
                    return 'Masha and the Bear'
                case '3':
                    return 'Pororo'
                case _:
                    return 'Unidentified movie'
        
        movie = input("Which movie? ")
        print (movies(movie))

        while (movies(movie)) == 'Unidentified movie':
            if (movies(movie)) != 'Unidentified movie':
                print("info correct")
                break
            else:
                print(" ")
                print("error, input not accepted.")
                print ("1 = batman")
                print ("2 = Masha and the Bear")
                print ("3 = Pororo")
                movie = input("Which movie? ")
                print (movies(movie))

    
        #Picking time

        print ("1 = Morning")
        print ("2 = Noon")
        print ("3 = Evening")
        def times (time):
            mtime = time.lower()
            match time:
                case '1':
                    return 'Morning'
                case '2':
                    return 'Noon'
                case '3':
                    return 'Evening'
                case _:
                    return 'Invalid time'
                                
        time = input("What Time? ")
        print (times(time))

        while (times(time)) == 'Invalid time':
            if (times(time)) != 'Invalid time':
                print("info correct")
                break
            else:
                print(" ")
                print("error, input not accepted.")
                print ("1 = Morning")
                print ("2 = Noon")
                print ("3 = Evening")
                time = input("What Time? ")
                print (times(time))

        #booking seat
        available_seats = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)', ]
        print (available_seats)
        def seats (seat):
            seat = seat.lower()
            match seat:
                case '1':
                    return 0
                case '2':
                    return 1
                case '3':
                    return 2
                case '4':
                    return 3
                case '5':
                    return 4
                case '6':
                    return 5
                case '7':
                    return 6
                case '8':
                    return 7
                case '9':
                    return 8
                case '10':
                    return 9
                case _:
                    return 'Invalid seat'
                    
        #seat validation            
        seat = input("Which Seat? ")
        if (seats(seat)) == 'Invalid seat':
            while (seats(seat)) == 'Invalid seat':
                seat = input("Which Seat? ")
                if (seats(seat)) != 'Invalid seat':
                    available_seats[seats(seat)] = "(X)"
                    break
                else:
                    print(" ")
                    print("error, input not accepted.")
                    print(" ")
                    print (available_seats)
                    seat = input("Which Seat? ")
                    print(" ")
                    
        available_seats[seats(seat)] = "(X)"
        print(available_seats)

        #confirming booking
        print('confirm order: movies: ', (movies(movie)), ", time:", (times(time)), ", seats:", (available_seats), )
        confirm = input("confirm? Y/N ")
        
        if confirm == "Y":
            print("Your seat has been confirmed\n")
            """ doot = input("book seat? Y/N ")
            if doot == "N":"""
            break
        elif confirm == "N":
            while confirm == 'N':
                print()
                doot = input("book again? Y/N ")
                if doot == "N":
                    confirm == "Y"
                    print("thank you")
                    break
                elif doot == "Y":
                    break
                else:
                    print("invalid input")
        else: 
            print("Invalid input")
            confirm = input("confirm? Y/N ")