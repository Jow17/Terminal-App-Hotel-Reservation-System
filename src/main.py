import random 
import calendar
import datetime

# Universal variables in list format that will be appended to

user = []
room = []
rn = ["Your room number is:"]
room_pin = ["Your 4 digit room access pin is:"]
checkin =["Your checkin date is:"]
checkout = ["Your checkout date is:"]
room_cost = ["Cost per night: "]

# Function to create a user account
def register():
	print("PLease enter a username and password with at least 6 characters")
	db = open("src/database.txt", "r") 
	username = input("Create a username: ")
	password = input("Create a password: ")
	password1 = input("Confirm your password: ")
	d = []
	f = []
	for i in db:
		a,b = i.split(", ") # Splits username and password
		b = b.strip()
		d.append(a)
		f.append(b)
	data = dict(zip(d, f))
	
	if password != password1:
		print("Passwords do not match! Please re-enter your username and password")
		register()
	else:
		if len(password) < 6:
			print("Password must be at least 6 characters, please try again")
			register()
		elif username in d:
			print("Username already exists! Please re-enter your username and password")
			register()
		else:
			db = open("src/database.txt", "a") 
			db.write(username +", "+ password +"\n") # Appends username and password to database,txt
			print(f"Success! Welcome {username}!")
			user.append(username)
			room_select()
# Function to log into account
def access():
	db = open("src/database.txt", "r")
	username = input("Enter your username: ")
	password = input("Enter your password: ")

	if not len(username or password) <1: # Checks if username and password are already in database.txt
		d = []
		f = []
		for i in db:
			a,b = i.split(", ")
			b = b.strip()
			d.append(a)
			f.append(b)
		data = dict(zip(d, f))
# Error handling for inputs
		try: 
			if data[username]:
				try:
					if password == data[username]:
						print(f"Welcome back {username}! ")
						user.append(username)
					else:
						print("Username or Password is incorrect\n")
						home()
				except:
					print("Username or Password does not exist\n")
					home()
			else:
				print("Username does not exist, please create an account\n")
				home()
		except:
			print("Username does not exist, please create an account\n")
			home()
		finally:
			room_select() # Sends user to room selection function 

# Home function 
def home():
	print("Welcome to Atlas Hotel!")
	print("Login: 1 | Create a new account: 2\n")
	
	number = (input("-> "))

	if number == '1':
		access()
	elif number == '2':
		register()
	else:
		print("Please enter a valid number")
		home()
# Room type selection function
def room_select():
	print("Please select which type of room you would like to stay in?\n")
	print("1. Peasant Quarter")
	print("Price per night: $50\n")
	print("2. Studio Apartment")
	print("Price per night: $75\n")
	print("3. Executive Suite ")
	print("Price per night: $150\n")
	print("4. Presedential Suite")
	print("Price per night: $250\n")
	print("5. Penthouse") 
	print("Price per night: $500\n")

	number = (input("-> ")) 

	if number == '1': 
		print("You've selected Peasant Quarter! On a tight budget huh\n")
		room.append("Room type: Peasant Quarter") # Appends room type to room variable
		room_cost.append(50.00) # Appends cost to cost variable
		show_calendar()
	elif number == '2':
		print("You've selected Studio Apartment: Our most popular room!\n")
		room.append("Room type: Studio Apartment")
		room_cost.append(75.00)
		show_calendar()
	elif number == '3':
		print("You've selected Executive Suite: Great choice! We'll even throw in a free lunch!\n")
		room.append("Room type: Executive Suite")
		room_cost.append(150.00)
		show_calendar()
	elif number == '4':
		print("You've selected Presedential Suite: Someone's on their honeymoon!\n")
		room.append("Room type: Presendential Suite")
		room_cost.append(250.00)
		show_calendar()
	elif number == '5':
		print("You've selected the Penthouse: Wow you must be a VIP\n")
		room.append("Room type: Penthouse")
		room_cost.append (500.00)
		show_calendar()
	else:
		print("Invalid number! Please try again")
		room_select()		
#Display calendar function 
def show_calendar():
    print("Please use this calendar to assist with your reservation")
    print("To skip, enter 0\n")
# Error handling for user inputs    
    while True:
        try: 
            year = int(input("Select year: "))
            
            if year == 0: # Skips to date function if user inputs 0
                set_checkin_date()
                break  
            elif year < 2023:
                print("Year invalid! Please enter a year in or after 2023.")
            else:
                while True:
                    month = int(input("Select month (1-12):"))
                    if 1 <= month <= 12:
                        print(calendar.month(year, month)) # Prints calendar for month and year selected
                        break  
                    else:
                        print("Invalid month! Please enter a valid month (1-12).")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
# Check in date selection function 
def set_checkin_date():
    while True: # Error handling for date inputs
        checkin_date_entry = input("Please enter a check-in date in YYYY-MM-DD format:\n")

        try:
            year, month, day = map(int, checkin_date_entry.split('-')) # Splits input and maps to checkin_date_entry into year, month, day 
            checkin_date = datetime.date(year, month, day)
            today = datetime.date.today()

            if checkin_date < today:
                print("Check-in date cannot be in the past!")
            else:
                checkin.append(checkin_date)# Appends checkin date to checkin variable 
                set_checkout_date()
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
# Check out date selection function 
def set_checkout_date():
    while True: # Error handling for date inputs
        checkout_date_entry = input("Now enter a checkout date in YYYY-MM-DD format:\n")

        try:
            year, month, day = map(int, checkout_date_entry.split('-')) # Splits input and maps to checkout_date_entry into year, month, day 
            checkout_date = datetime.date(year, month, day)
            today = datetime.date.today()

            if checkout_date < today:
                print("Checkout date cannot be in the past!")
            elif checkout_date <= checkin[-1]:
                print("Checkout date cannot be earlier or equal to the check-in date!")
            else:
                checkout.append(checkout_date) # Appends checkout date to checkout variable 
                pin_generator()
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
# Generates 4 digit pin 
def pin_generator():
	pin_number = random.randrange(1000, 9999)
	room_pin.append(pin_number)
	room_number()
# Generates room number
def room_number():
	number = random.randrange(1, 99)
	rn.append(number)
	print_receipt()
# Outputs all reservation details
def print_receipt():
	print("Here are your reservation details!")
	print(user)
	print(room)
	print(rn)
	print(room_pin)
	print(checkin)
	print(checkout)
	print(room_cost)

home()
