import room

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
		print("Passwords do not match! Please re-enter your username and password" )
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
						# booking()
					else:
						print("Username or Password is incorrect")
						home()
				except:
					print("Username or Password does not exist")
					home()
			else:
				print("Username does not exist, please create an account")
				home()
		except:
			print("Username does not exist, please create an account")
			home()
	else: 
		print("Please enter a value")
		home()

def home():
	print("Login: 1 | Create a new account: 2\n")
	
	number = int(input("-> "))
	
	if number == 1:
		access()
	elif number == 2:
		register()
	else:
		print("Please enter a valid number")
		home()

def booking():
	print("Please select which type of room you would like to stay in?\n")
	print("""
	   1. Peasant quarters
	   2. Studio apartment 
	   3. Executive suite 
	   4. Presedential suite
	   5. Penthouse 
	   """)
	
	number = int(input) 

	if number == 1: 
		print("You've selected Peasant Quarters!\n")
		
		print 

	if number == 2:
		print("Available room")
	

print("Welcome to Atlas Hotel!")

home()