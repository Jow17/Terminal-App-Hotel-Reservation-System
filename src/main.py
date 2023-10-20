def register():
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
	# data = dict(zip(d, f))
	
	if password != password1:
		("Passwords do not match! Please re-enter your username and password" )
		register()
	else:
		if len(password) <= 6:
			print("Password must be at least 6 characters, please try again")
			register()
		elif username in d:
			print("Username already exists! Please re-enter your username and password")
			register()
		else:
			db = open("src/database.txt", "a")
			db.write(username +", "+password+"\n")
			print(f"Success! Welcome {username}!")


print("""Hello! Welcome to Atlas Hotel!   
Please enter your login details or create an account""")    


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
						print("Login success! Welcome")
						print(f"Welcome back{username}! ")
					else:
						print("Password or Username incorrect")
				except:
					print("Password or Username incorrect")
			else:
				print("Username does not exist")
		except:
			print("Username or password doesnt exst")
	else:
		print("Please enter a value")

def home(option = None):
	option = input("Login | Create an account:")
	if option == "Login":
		access()
	elif option == "Create an account":
		register()
	else:
		print("Please enter a valid option")
		home()
	
	
home()