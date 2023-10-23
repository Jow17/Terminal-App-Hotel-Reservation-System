# import room
import datetime
# import smtplib
# import random 

# room = []
# checkin = []
# checkout = []

# def register():
# 	print("PLease enter a username and password with at least 6 characters")
# 	db = open("src/database.txt", "r")
# 	username = input("Create a username: ")
# 	password = input("Create a password: ")
# 	password1 = input("Confirm your password: ")
# 	d = []
# 	f = []
# 	for i in db:
# 		a,b = i.split(", ")
# 		b = b.strip()
# 		d.append(a)
# 		f.append(b)
# 	data = dict(zip(d, f))
	
# 	if password != password1:
# 		print("Passwords do not match! Please re-enter your username and password")
# 		register()
# 	else:
# 		if len(password) < 6:
# 			print("Password must be at least 6 characters, please try again")
# 			register()
# 		elif username in d:
# 			print("Username already exists! Please re-enter your username and password")
# 			register()
# 		else:
# 			db = open("src/database.txt", "a")
# 			db.write(username +", "+password+"\n")
# 			print(f"Success! Welcome {username}!")

# def access():
# 	db = open("src/database.txt", "r")
# 	username = input("Enter your username: ")
# 	password = input("Enter your password: ")

# 	if not len(username or password) <1:
# 		d = []
# 		f = []
# 		for i in db:
# 			a,b = i.split(", ")
# 			b = b.strip()
# 			d.append(a)
# 			f.append(b)
# 		data = dict(zip(d, f))

# 		try: 
# 			if data[username]:
# 				try:
# 					if password == data[username]:
# 						print(f"Welcome back {username}! ")
# 					else:
# 						print("Username or Password is incorrect")
# 						home()
# 				except:
# 					print("Username or Password does not exist")
# 					home()
# 			else:
# 				print("Username does not exist, please create an account")
# 				home()
# 		except:
# 			print("Username does not exist, please create an account")
# 			home()
# 		finally:
# 			booking()

# def home():
# 	print("Login: 1 | Create a new account: 2\n")
	
# 	number = int(input("-> "))
	
# 	if number == 1:
# 		access()
# 	elif number == 2:
# 		register()
# 	else:
# 		print("Please enter a valid number")
# 		home()

# def booking():
# 	print("Please select which type of room you would like to stay in?")
# 	print("1. Peasant Quarter")
# 	print("2. Studio Apartment")
# 	print("3. Executive Suite ")
# 	print("4. Presendial Suite")
# 	print("5. Penthouse")

# 	number = int(input("-> ")) 

# 	if number == 1: 
# 		print("You've selected Peasant Quarter! On a tight budget huh\n")
# 		room.append("Room type: Peasant Quarter")
# 		set_date()
# 	elif number == 2:
# 		print("You've selected Studio Apartment: Our most popular room!\n")
# 		room.append("Room type: Studio Apartment")
# 		set_date()
# 	elif number == 3:
# 		print("You've selected Executive Suite: Great choice! We'll even throw in a free lunch!\n")
# 		room.append("Room type: Executive Suite")
# 		set_date()
# 	elif number == 4:
# 		print("You've selected Presedential Suite: Someone's on their honeymoon!\n")
# 		room.append("Room type: Presendential Suite")
# 		set_date()
# 	elif number == 5:
# 		print("You've selected the Penthouse: Wow you must be a VIP\n")
# 		room.append("Room type: Penthouse")
# 		set_date()
# 	else:
# 		print("Please enter a valid number")
# 		booking()


def set_date():
	checkin_date_entry = input("Please enter a date in YYYY-MM-DD format: ")
	checkout_date_entry = input("Please enter a month in YYYY-MM-DD format: ")
	year, month, day = map(int, checkin_date_entry.split('-'))
	year, month, day = map(int, checkout_date_entry.split('-'))
	checkin_date = datetime.date(year, month, day)
	checkout_date = datetime.date(year, month, day)

	

	print(checkin_date)
	print(checkout_date)


	
set_date()


# print("Welcome to Atlas Hotel!")

# home()