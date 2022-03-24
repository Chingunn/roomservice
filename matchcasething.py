quit_flag: True
match quit_flag :
    case True:
        print("Quitting")
        exit()
    case False:
        print("System is on")
