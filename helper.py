import tkinter as tk
import tkinter.messagebox
import datetime
from db import Database

# compute the day in a week 
def day_in_a_week(day,month,year):
	week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
	day=datetime.date(int(year),int(month),int(day)).weekday()
	return week_days[day]

# date validation
def is_valid_date(day,month,year):
	isValidDate = True
	try :
	    datetime.datetime(int(year),int(month),int(day))
	except ValueError :
	    isValidDate = False
	return isValidDate

# time validation
def is_valid_time(hour,minute):
	isValidTime = True
	try :
	    datetime.time(int(hour),int(minute))
	except ValueError :
	    isValidTime = False
	return isValidTime

def input_validation(day,month,year,start_hour,start_minute,end_hour,end_minute,event_name,remarks):
	# raise error if missing input
	if day == '' or month == '' or year == '' or start_hour == '' or start_minute == '' or end_hour == '' or end_minute == '' or event_name == '':
		tk.messagebox.showwarning('Required Fields', 'Please include all required fields')
		return False
	# raise error if invalid date input	
	if is_valid_date(day,month,year) == False:
		tk.messagebox.showwarning('Invalid Date Format', 'Please input a valid date')
		return False
	# raise error if invalid time input
	if is_valid_time(start_hour,start_minute) == False or is_valid_time(end_hour,end_minute) == False:
		tk.messagebox.showwarning('Invalid Time Format', 'Please input a valid time')
		return False
	# raise error if end time precedes start time
	if (datetime.time(int(start_hour),int(start_minute)) < datetime.time(int(end_hour),int(end_minute))) == False:
		tk.messagebox.showwarning('Invalid Time Format', 'End Time precedes or equal Start Time in time')
		return False


# import sqlite3
# from db import Database

# conn = sqlite3.connect('store.db')
# c = conn.cursor()

# c.execute("INSERT INTO schedule VALUES (NULL, ?, ?, ?, ?, ?, ?)", ('2020-06-30','Saturday','14:00','15:00','CUPP Webinar','compulsory'))

# c.execute("SELECT * FROM schedule")
# print(c.fetchall())
# conn.commit()

# print("\n")

# c.execute("SELECT * FROM schedule ORDER BY event_date ASC")
# print(c.fetchall())
# conn.commit()

# c.close()
# conn.close()


# db = Database('store.db')
# for row in db.fetch():
# 	print(row)

# db.sort()
# print("\n")

# for row in db.fetch():
# 	print(row)