import datetime
import smtplib
import random 
import calendar

room = []
room_pin = ["Your 4 digit pin is:"]
checkin = ["Check in date:"]
checkout = ["Check out date:"]
total_cost = []
room_cost = []
total_days = []

def register():
	print("PLease enter a username and password with at least 6 characters")
	db = open("src/database.txt", "r")
	username = input("Create a username: ")
	password = input("Create a password: ")
	password1 = input("Confirm your password: ")
	d = []
	f = []
	for i in db:
		a,b = i.split(", ")
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
			db.write(username +", "+password+"\n")
			print(f"Success! Welcome {username}!")
			booking()

def access():
	db = open("src/database.txt", "r")
	username = input("Enter your username: ")
	password = input("Enter your password: ")

	if not len(username or password) <1:
		d = []
		f = []
		for i in db:
			a,b = i.split(", ")
			b = b.strip()
			d.append(a)
			f.append(b)
		data = dict(zip(d, f))

		try: 
			if data[username]:
				try:
					if password == data[username]:
						print(f"Welcome back {username}! ")
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
			booking()

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

def booking():
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
			room.append("Room type: Peasant Quarter")
			room_cost.append(50)
			show_calendar()
	elif number == '2':
		print("You've selected Studio Apartment: Our most popular room!\n")
		room.append("Room type: Studio Apartment")
		room_cost.append(75)
		show_calendar()
	elif number == '3':
		print("You've selected Executive Suite: Great choice! We'll even throw in a free lunch!\n")
		room.append("Room type: Executive Suite")
		room_cost.append(150)
		show_calendar()
	elif number == '4':
		print("You've selected Presedential Suite: Someone's on their honeymoon!\n")
		room.append("Room type: Presendential Suite")
		room_cost.append(250)
		show_calendar()
	elif number == '5':
		print("You've selected the Penthouse: Wow you must be a VIP\n")
		room.append("Room type: Penthouse")
		room_cost.append(500)
		show_calendar()
	else:
		print("Invalid number! Please try again")
		booking()		

def show_calendar():
    print("Please use this calendar to assist with your reservation")
    print("To skip, enter 0\n")
    
    while True:
        try: 
            yy = int(input("Select year: "))
            
            if yy == 0:
                set_checkin_date()
                break  # Exit the loop
            elif yy < 2023:
                print("Year invalid! Please enter a year in or after 2023.")
            else:
                while True:
                    mm = int(input("Select month (1-12): "))
                    if 1 <= mm <= 12:
                        print(calendar.month(yy, mm))
                        break  # Exit the inner loop
                    else:
                        print("Invalid month! Please enter a valid month (1-12).")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def set_checkin_date():
    while True:
        checkin_date_entry = input("Please enter a check-in date in YYYY-MM-DD format:\n")

        try:
            year, month, day = map(int, checkin_date_entry.split('-'))
            checkin_date = datetime.date(year, month, day)
            today = datetime.date.today()

            if checkin_date < today:
                print("Check-in date cannot be in the past!")
            else:
                checkin.append(checkin_date)
                set_checkout_date()
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def set_checkout_date():
    while True:
        checkout_date_entry = input("Now enter a checkout date in YYYY-MM-DD format:\n")

        try:
            year, month, day = map(int, checkout_date_entry.split('-'))
            checkout_date = datetime.date(year, month, day)
            today = datetime.date.today()

            if checkout_date < today:
                print("Checkout date cannot be in the past!")
            elif checkout_date <= checkin[-1]:
                print("Checkout date cannot be earlier or equal to the check-in date!")
            else:
                checkout.append(checkout_date)
                pin_generator()
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def pin_generator():
	pin_number = random.randrange(1000, 9999)
	room_pin.append(pin_number)

	


home()

