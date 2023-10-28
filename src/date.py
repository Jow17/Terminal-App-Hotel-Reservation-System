# class date:
#     year = 0
#     month = 0
#     day = 0

#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
    

#     def check_if_valid(self):
#         if self.year >=2023 and self.year<9999:
#             if self.month >0 and self.month<13:
#                 if self.day>0 and self.day<31:
#                     return True
#         else:
#             return False
    
    # def getDates():
# 	y1 = int(input("Year of Check In: "))
# 	m1 = int(input("Year of Check In: "))
# 	d1= int(input("Year of Check In: "))

# 	# checkout date
# 	y2 = int(input("Year of Check In: "))
# 	m2 = int(input("Year of Check In: "))
# 	d2 = int(input("Year of Check In: "))

# 	checkin = Date(y1,m1,d1)
# 	checkout = Date(y2,m2,d2)


# def total_duration_of_stay():
# 	if(checkin.check_if_valid() and checkout.check_if_valid()):
# 		if checkin.year == checkout.year:
# 			if checkin.month == checkout.month:
# 				return checkout.day - checkin.day
# 			else:
# 				return (30-checkin.day) + checkout.day
# 		else:

# from datetime import datetime

# # Prompt the user for a date and time in a specific format
# date_string = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")

# try:
#     # Parse the user input into a datetime object
#     user_datetime = datetime.strptime(date_string, '%Y-%m-%d')

#     # Print the parsed datetime
#     print("Parsed datetime:", user_datetime)
# except ValueError:
#     print("Invalid date and time format. Please use YYYY-MM-DD HH:MM:SS.")
    
from datetime import datetime

date_string = "2023-10-30"
date_format = "%Y-%m-%d"

parsed_date = datetime.strptime(date_string, date_format)
print(parsed_date)



    

