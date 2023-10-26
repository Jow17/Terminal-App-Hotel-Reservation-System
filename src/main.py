import datetime
import smtplib
import random 
import calendar

room = []
room_pin = []
checkin = []
checkout = []
cost = []

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
	print("welcome to Atlas Hotel!")
	print("Login: 1 | Create a new account: 2\n")
	
	number = int(input("-> "))
	
	if number == 1:
		access()
	elif number == 2:
		register()
	else:
		print("Please enter a valid number")
		home()
	#Add error handling for non integer inputs

def booking():
	print("Please select which type of room you would like to stay in?")
	print("1. Peasant Quarter")
	print("Price per night: $50\n")
	print("2. Studio Apartment")
	print("Price per night: $75\n")
	print("3. Executive Suite ")
	print("Price per night: $150\n")
	print("4. Presendial Suite")
	print("Price per night: $250\n")
	print("5. Penthouse") 
	print("Price per night: $500\n")


	number = int(input("-> ")) 

	if number == 1: 
		print("You've selected Peasant Quarter! On a tight budget huh\n")
		room.append("Room type: Peasant Quarter")
		show_calendar()
	elif number == 2:
		print("You've selected Studio Apartment: Our most popular room!\n")
		room.append("Room type: Studio Apartment")
		show_calendar()
	elif number == 3:
		print("You've selected Executive Suite: Great choice! We'll even throw in a free lunch!\n")
		room.append("Room type: Executive Suite")
		show_calendar()
	elif number == 4:
		print("You've selected Presedential Suite: Someone's on their honeymoon!\n")
		room.append("Room type: Presendential Suite")
		show_calendar()
	elif number == 5:
		print("You've selected the Penthouse: Wow you must be a VIP\n")
		room.append("Room type: Penthouse")
		show_calendar()
	else:
		print("Please enter a valid number")
		booking()
#Add error handling for non integer inputs

def show_calendar():
	print("Please use this calendar to assist with you reservation")
	print("To skip press 0")
	yy = int(input("Select year: "))
	mm = int(input("Select month: "))
	if yy == 0:
		set_checkin_date()
	elif yy < 2023:
		print("Year invalid! PLease try again!")
		show_calendar()
	else:
		print(calendar.month(yy,mm))
		show_calendar()

def set_checkin_date():
	checkin_date_entry = input("Please enter a checkin date in YYYY-MM-DD format:\n")
	
	year, month, day = map(int, checkin_date_entry.split('-'))
	checkin_date = datetime.date(year, month, day)

	today = datetime.date.today()
	this_year = today.year 
	this_month = today.month
	this_day = today.day

	if year < this_year:
		print("Year is invalid!")
		set_checkin_date()
	elif year == this_year and month < this_month:
		print("Month is invalid!")
		set_checkin_date()
	elif month == this_month and day < this_day:
		print("Day is invalid!")
		set_checkin_date()
	else:
		checkin.append(checkin_date) 
		set_checkout_date()
# Add error handling for invalid than 1 -12 months
# Add error handling for invalid day input 

def set_checkout_date():
	checkout_date_entry = input("Now enter a checkout date in YYYY-MM-DD format:\n")
	
	year, month, day = map(int, checkout_date_entry.split('-'))
	checkout_date = datetime.date(year, month, day)

	today = datetime.date.today()
	this_year = today.year 
	this_month = today.month
	this_day = today.day

	if year < this_year:
		print("Year is invalid!")
		set_checkout_date()
	elif year == this_year and month < this_month:
		print("Month is invalid!")
		set_checkout_date()
	elif month == this_month and day < this_day:
		print("Day is invalid!")
		set_checkout_date()
	elif checkout_date == checkin:
		print("Checkout date cannot be the same as checkin date!")
		set_checkout_date()
	else:
		checkout.append(checkout_date) 
		pin_generator()
# Add error handling for invalid than 1 -12 months
# Add error handling for invalid day input 

def pin_generator():
	pin_number = random.randrange(1000, 9999)
	room_pin.append(pin_number)
		
home()


