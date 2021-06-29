#Import local 'datamanager' module to allow '\data' path acquisition
import datamanager
#Import local 'credentialchecker' module to allow user credential checking
import credentialchecker

#Define restartcheck function, asks user if they want to restart application
#Continues while loop if 'Y'
#Breaks out of while loop if 'N'
def restartcheck():
    """Asks user if they want to log out or restart. Returns True if 'Y' and False if 'N'"""
    if (input("\nWould you like to restart? (Y/N): ").upper() == "Y"):
        print ("Restarting...\n")  
        return True
    else:
        print("")
        return False

#Define maxareacheck function. Takes in the directory path to 'maxarea.txt'.
#Checks if 'maxarea.txt' contents are of numerical type. If not, sets to default value of 4.
def maxareacheck(maxarea_dir):
    """Check if the contents of the 'maxarea.txt' file can be converted into float.
If not, overwrite the contents of 'maxarea.txt' to the default value of 4"""
    maxareafile = open(maxarea_dir, "r").read()

    if not (maxareafile.isdigit()):
        print ("Max area has not been set to a valid number.")
        print ("Setting max area (and maxarea.txt) to the default value of 4.\n")
        open(maxarea_dir, "w").write("4")
        return 4
    else:
       return maxareafile

#Define function containing the main code to be called in a while loop
#Allows main code to be run indefinitely until user wants to quit
def mainloop():
    """The Main Code loop. Gets all desired input from user and performs the neccessary checks and calculations"""
    #Use datamanager to get an error checked path to 'maxarea.txt' file
    #Check if the contents of the 'maxarea.txt' file can be converted into float
    #If not, overwrite the contents of 'maxarea.txt' to the default value of 4
    maxarea = maxareacheck(datamanager.get_maxarea())
    
    #Get length from user input
    length = input ("What is the length of the room?: ")
    
    #Check if length input string can be converted into float
    #If not, print an error and ask user if they want to restart
    if not(length.isdigit()):
        print ("You must enter a valid number for the room length.")
        return restartcheck()
    
    #Get width from user input
    width = input ("What is the width of the room?: ")
    
    #Check if width input string can be converted into float
    #If not, print an error and ask user if they want to restart
    if not (width.isdigit()):
        print ("You must enter a valid number for the room width.")
        return restartcheck()
    
    #Convert the length and width input types to float
    #Multiply length and width floats to find the area
    calculatedarea = float(length) * float(width)
    
    #Display calculated area to user
    print ("\nThe area of the room is: " + str(calculatedarea) + " sq meters.")
    
    #Print error message if the calculated area is greater than max area
    if (calculatedarea > float(maxarea)): 
        print("We're sorry, but the specified room size is unavailable. Please enter a different room size.")

    #restartcheck one last time
    return restartcheck()

#Declare login and menu loop bools before starting main while loop 
loginloop = True
menuloop = True

#Call mainloop until username is empty (user has selected to quit)
while (True):
    #Call logincheck until the user has logged in
    while(loginloop):
        if (credentialchecker.logincheck()):
            #When user is logged in, set menuloop to True
            loginloop = False
            menuloop = True

    #If username is set to "", break the loop as the user has selected to quit
    if(credentialchecker.username == ""):
        break

    while (menuloop):
        #If the current userpermissions are "admin", run admin code while menuloop True
        if (credentialchecker.userpermissions == "admin"):
                admininput = input("What would you like to do?: \nSet Max Area (M)   Calculate Area (C)   Log Out (L)\n").upper()

                #If admin enters "M", get new max area and perform error checks before setting it
                if (admininput == "M"):
                    #Get new max area input from admin user
                    newarea = input("\nPlease enter a new maximum area size: ")

                    #If newarea is a valid numerical type, write it to 'maxarea.txt'
                    #If not, print an error message
                    if(newarea.isdigit()):
                        open(datamanager.get_maxarea(), "w").write(newarea)
                        print("Max area has been set to " + newarea + "\n")
                    else:
                        print("Max area must be set to a valid number.\n")

                #If admin enters "C", set adminloop false to exit admin menu and continue with area calculator code
                if (admininput == "C"):
                    print("")
                    menuloop = False
                
                #If admin enters "L", set menuloop false to exit admin menu, and loginloop true to send user back to login prompt
                if (admininput == "L"):
                    print("Logging out...\n")
                    menuloop = False
                    loginloop = True

        #If the current userpermissions are "user", run user code while menuloop True
        if (credentialchecker.userpermissions == "user"):
                userinput = input("What would you like to do?: \nCalculate Area (C)   Log Out (L)\n").upper()
                
                #If user enters "C", set userloop false to exit user menu and continue with area calculator code
                if (userinput == "C"):
                    print("")
                    userloop = False

                #If user enters "L", set menuloop false to exit user menu, and loginloop true to send user back to login prompt
                if (userinput == "L"):
                    print("Logging out...\n")
                    menuloop = False
                    loginloop = True
                 
    #If looplogin has been set to true before mainloop function, ignore mainloop function and continue to rerun logincheck function
    if (loginloop):
       continue

    #mainloop function always returns the results of restartcheck function
    if not mainloop():
        #If restartcheck returns False, set menuloop to True
        menuloop = True

        #If user is a guest, set the loginloop to true to send user back to login prompt, ignoring user and admin menus.
        if(credentialchecker.userpermissions == "guest"):
            loginloop = True
