#Import local 'datamanager' module to allow '\data' path acquisition
import datamanager
#Import Regular Expression ('re') module to allow precise string checking
import re

#Login Functions##############################################################
def usernamecheck():
		"""Checks if the username is more than 5 chars, and only contains letters, numbers, or underscores.
Returns True or False"""
		if (username == "NULL"):
			print("Invalid username: Cannot use 'NULL' as a username.\n")
			return False
		if (username == "Guest"):
				print("Invalid username: Cannot use 'Guest' as a username.\n")
				return False

		if re.match("^[a-zA-Z0-9_]{5,}$", username):
			return True
		else:
			print("Invalid username: Must be at least 5 characters, and can only contain letters, numbers, or underscores.\n")
			return False

def passwordcheck(password):
		"""Checks if the password is more than 5 chars. 
Returns True or False"""
		if len(password) >= 5:
			return True
		else:
			print("Invalid password: Must be at least 5 characters.\n")
			return False

def existingusercheck(userdata):
		"""Checks if the input username is already in the userdata file, and if user entry is in valid format.
If valid, returns username, password, user permissions, and user area."""
		for line in userdata:
			if (len(line) > 1 and line.split()[0] == username):
				if (len(line.split()) == 3):
					return line.split()[0], line.split()[1], line.split()[2]
				else:
					print("Invalid userdata: Userdata entry format is invalid. Cannot retrieve userdata.\n")
					return "NULL", "", ""
		return "", "", ""
##############################################################################

def logincheck():
	"""Prompts user to log in, create account, or continue as guest. Performs format and duplicate entry checks on user input.
Returns True if login is found, and False if login is not found."""

	#Get userdata path from datamanager
	userdata_dir = datamanager.get_userdata()

	if (input("Would you like to log in? (Y/N): ").upper() == "Y"):
		#Declare a global username variable
		#This means all refernces to username in this scope will be set to the same variable
		#This also allows us to reference username from outside this script
		global username

		#Get user input and set current username to this
		username = input("\nPlease enter a username: ")

		#Checks if username fits min char limit and no special characters.
		#Continues loop if username fails check
		if not (usernamecheck()):
			return False

		#Open userdata in read mode and check if it contains the current username
		userdata_r = open(userdata_dir, "r")
		usercheckdata = existingusercheck(userdata_r)

		#Declare an int for password entry attempts and set to 3
		attempts = 3

		#End login check if NULL username is found. 
		#NULL username is only found when userdata for a user is in an invalid format.
		if (usercheckdata[0] == "NULL"):
			return False

		#If the entered username has been found in userdata
		if (usercheckdata[0] != ""):
			#Loop password entry until attemps are 0 and count down attemps each loop
			while attempts > 0:
				#Declare promptstring to show password attempt amount on input prompt
				promptstring = "Please enter a password: "

				if attempts < 3:
					promptstring = "Please enter a password " + "(" + str(attempts) + " attempts remaining): "

				#If password matches the password in the userdata file, allow entry with current username.
				#If not, either count down attempts or end current login check
				if (input(promptstring) == usercheckdata[1]):
					#Set the global variable userpermissions to the current permissions from userdata
					#Allows us to reference the current userpermissions from outside this script
					global userpermissions 
					userpermissions = usercheckdata[2]

					print("\nWelcome, " + username + "!\n")
					return True

				else:
					print("Invalid password: Password does not match.\n")
					if attempts <= 1:
						return False
					else:
						attempts -= 1
		#If no username was found in userdata, end current login check
		else:
			print("Invalid username: User not found.\n")
			return False

	elif (input("Would you like to create an account? (Y/N): ").upper() == "Y"):
		#Run username entry loop until valid username is entered or user wants to quit
		while (True):
			#Get input from user for new username
			username = input("\nPlease enter a username: ")

			#Check if username is valid, prompt user to end account creation if not
			if not (usernamecheck()):
				if(input("Do you still want to create an account? (Y/N): ").upper() == "Y"):
					continue
				else:
					return False
			
			#Open userdata in read mode and check if username already exists
			userdata_r = open(userdata_dir, "r")
			usercheckdata = existingusercheck(userdata_r)

			#If a username is found, prompt user to end account creation or reenter a username
			if (usercheckdata[0] != ""):
				print("Invalid username: Username already exists.")
				if(input("Do you still want to create an account? (Y/N): ").upper() == "Y"):
					continue
				else:
					return False

			#If no existing username is found, run password entry loop until valid password or user wants to quit
			while (True):
				#Get input from user for new password
				password = input("Please enter a password: ")

				#Check if password is valid, and prompt user to end account creation if not
				if (passwordcheck(password)):
					#Write the username and password to the userdata file. User permissions are set to user by default. 
					#User permissions can be set to admin by adnother admin after creation.
					userdata_w = open(userdata_dir, "a").write("\n" + username + " " + password + " " + "user")
					print(username + ", your account was created! Please log in to continue.\n")
					return False
				elif(input("Do you still want to create an account? (Y/N): ").upper() == "Y"):
					continue
				else:
					return False

	elif (input("Would you like to continue as Guest? (Y/N): ").upper() == "Y"):
		#If user doesn't log in or create an account, they can continue as a "Guest" user
		print("\nContinuing as Guest.\n")
		username = "Guest"
		userpermissions = "guest"
		return True

	else:
		#If user wants to quit the program, they can continue as a "" user
		#This allows us to know when to exit the program in the main module
		username = ""
		print("Exiting program...")
		return True
