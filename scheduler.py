import tkinter as tk
import tkinter.messagebox
from helper import *
# import TkTreectrl as treectrl
import datetime
from db import Database

db = Database('store.db')

HEIGHT = 500
WIDTH = 850
DEFAULT_YEAR = str(datetime.datetime.now().year)

def sort_events():
	schedule_list.delete(0,'end')
	# i = 1
	for row in db.sort():
		# entry_list = list(row)
		# entry_list[0] = i
		# row = tuple(entry_list)
		# i += 1
		schedule_list.insert('end', row)

def populate_list():
	schedule_list.delete(0,'end')
	# i = 1
	# for row in db.sort():
	# 	# entry_list = list(row)
	# 	# entry_list[0] = i
	# 	# row = tuple(entry_list)
	# 	# i += 1
	# 	schedule_list.insert('end', row)
	for row in db.fetch():
		schedule_list.insert('end', row)

# collect data from all entries
def submit_entry():
	day = day_entry.get()
	month = month_entry.get()
	year = year_entry.get()
	start_hour = start_hour_entry.get()
	start_minute = start_minute_entry.get()
	end_hour = end_hour_entry.get()
	end_minute = end_minute_entry.get()
	event_name = event_name_entry.get()
	remarks = remarks_entry.get()

	if (input_validation(day,month,year,start_hour,start_minute,end_hour,end_minute,event_name,remarks) == False):
		return

	date = datetime.date(int(year),int(month),int(day))
	dayInWeek = day_in_a_week(day,month,year)
	start_time = datetime.datetime(int(year), int(month), int(day),int(start_hour), int(start_minute))
	end_time = datetime.datetime(int(year), int(month), int(day), int(end_hour), int(end_minute))

	db.insert(date,dayInWeek,"{:02d}:{:02d}".format(start_time.hour, start_time.minute),"{:02d}:{:02d}".format(end_time.hour, end_time.minute),event_name,remarks)
	schedule_list.delete(0,'end')
	schedule_list.insert('end', (date,dayInWeek,"{:02d}:{:02d}".format(start_time.hour, start_time.minute),"{:02d}:{:02d}".format(end_time.hour, end_time.minute),event_name,remarks))
	
	clear_data()
	populate_list()

def update_entry():
	# add error message if not selected (please select an item to update)

	day = day_entry.get()
	month = month_entry.get()
	year = year_entry.get()
	start_hour = start_hour_entry.get()
	start_minute = start_minute_entry.get()
	end_hour = end_hour_entry.get()
	end_minute = end_minute_entry.get()
	event_name = event_name_entry.get()
	remarks = remarks_entry.get()

	if (input_validation(day,month,year,start_hour,start_minute,end_hour,end_minute,event_name,remarks) == False):
		return

	date = datetime.date(int(year),int(month),int(day))
	dayInWeek = day_in_a_week(day,month,year)
	start_time = datetime.datetime(int(year), int(month), int(day),int(start_hour), int(start_minute))
	end_time = datetime.datetime(int(year), int(month), int(day), int(end_hour), int(end_minute))

	db.update(selected_item[0],date,dayInWeek,"{:02d}:{:02d}".format(start_time.hour, start_time.minute),"{:02d}:{:02d}".format(end_time.hour, end_time.minute),event_name,remarks)
	clear_data()
	populate_list()

def delete_entry():
	db.remove(selected_item[0])
	clear_data()
	populate_list()

# clear all entry fields
def clear_data():
	try:
		day_entry.delete(0, 'end')
		month_entry.delete(0, 'end')
		# year_entry.delete(0, 'end')
		start_hour_entry.delete(0, 'end')
		start_minute_entry.delete(0, 'end')
		end_hour_entry.delete(0, 'end')
		end_minute_entry.delete(0, 'end')
		event_name_entry.delete(0, 'end')
		remarks_entry.delete(0, 'end')
		
		index = schedule_list.curselection()[0]
		schedule_list.select_clear(index)
	except IndexError:
		pass
	

def select_item(event):
	try:
		global selected_item
		index = schedule_list.curselection()[0]
		selected_item = schedule_list.get(index)

		date = datetime.datetime.strptime(selected_item[1], "%Y-%m-%d")
		start_time = selected_item[3].split(":")
		end_time = selected_item[4].split(":")

		day_entry.delete(0,'end')
		day_entry.insert('end',date.day)
		month_entry.delete(0,'end')
		month_entry.insert('end',date.month)
		year_entry.delete(0,'end')
		year_entry.insert('end',date.year)
		start_hour_entry.delete(0,'end')
		start_hour_entry.insert('end',start_time[0])
		start_minute_entry.delete(0,'end')
		start_minute_entry.insert('end',start_time[1])
		end_hour_entry.delete(0,'end')
		end_hour_entry.insert('end',end_time[0])
		end_minute_entry.delete(0,'end')
		end_minute_entry.insert('end',end_time[1])
		event_name_entry.delete(0,'end')
		event_name_entry.insert('end',selected_item[5])
		remarks_entry.delete(0,'end')
		remarks_entry.insert('end',selected_item[6])

	except IndexError:
		pass

root = tk.Tk()
root.title("Event Scheduler")

# root.geometry('700x350')

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
# 80c1ff
frame = tk.Frame(root,bg='#fff373')
frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

# first row
label = tk.Label(frame,text="My Schedule",bg='#fff373',font=("Fixedsys", "15"))
label.place(relx=0.33,rely=0,relwidth=0.33,relheight=0.075)

# second row (date, start_time and end_time)
date_text = tk.StringVar()
date_label = tk.Label(frame, text=' Date:',font=("Fixedsys", "8") )
date_label.place(relx=0, rely=0.1,relwidth=0.1)

day_entry = tk.Entry(frame,bg='#e7ecf2')
day_entry.place(relx=0.15, rely=0.1,relwidth=0.04)

space1 = tk.Label(frame, text='/',font=("Fixedsys", "8"))
space1.place(relx=0.2,rely=0.1,relwidth=0.02)

month_entry = tk.Entry(frame,bg='#e7ecf2')
month_entry.place(relx=0.23,rely=0.1,relwidth=0.04)

space2 = tk.Label(frame, text='/',font=("Fixedsys", "8"))
space2.place(relx=0.28,rely=0.1,relwidth=0.02)

year_entry = tk.Entry(frame, bg='#e7ecf2')
year_entry.insert(0, DEFAULT_YEAR)
year_entry.place(relx=0.31,rely=0.1,relwidth=0.08)

start_time_text = tk.StringVar()
start_time_label = tk.Label(frame, text=' From :',font=("Fixedsys", "8"))
start_time_label.place(relx=0.5,rely=0.1,relwidth=0.1)

start_hour_entry = tk.Entry(frame,bg='#e7ecf2')
start_hour_entry.place(relx=0.65, rely=0.1,relwidth=0.04)

colon1 = tk.Label(frame, text=':')
colon1.place(relx=0.7,rely=0.1,relwidth=0.02)

start_minute_entry = tk.Entry(frame, bg='#e7ecf2')
start_minute_entry.place(relx=0.73,rely=0.1,relwidth=0.04)

end_time_text = tk.StringVar()
end_time_label = tk.Label(frame, text='To',font=("Fixedsys", "8"))
end_time_label.place(relx=0.78, rely=0.1,relwidth=0.05)

end_hour_entry = tk.Entry(frame,bg='#e7ecf2')
end_hour_entry.place(relx=0.865, rely=0.1,relwidth=0.04)

colon2 = tk.Label(frame, text=':')
colon2.place(relx=0.915,rely=0.1,relwidth=0.02)

end_minute_entry = tk.Entry(frame, bg='#e7ecf2')
end_minute_entry.place(relx=0.945, rely=0.1,relwidth=0.04)

# third row (event name and remarks)
event_name_text = tk.StringVar()
event_name_label = tk.Label(frame, text=' Event Name:',font=("Fixedsys", "8"))
event_name_label.place(relx=0,rely=0.2,relwidth=0.2)
event_name_entry = tk.Entry(frame,bg='#e7ecf2')
event_name_entry.place(relx=0.21,rely=0.2,relwidth=0.6)

remarks_text = tk.StringVar()
remarks_label = tk.Label(frame, text=' Remarks:',font=("Fixedsys", "8"))
remarks_label.place(relx=0,rely=0.3,relwidth=0.15)
remarks_entry = tk.Entry(frame,bg='#e7ecf2')
remarks_entry.place(relx=0.21,rely=0.3,relwidth=0.75)

# Display schedule
schedule_list = tk.Listbox(frame, width=50)
schedule_list.place(relx=0.02,rely=0.4, relwidth=0.8,relheight=0.55)

# Create scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.place(relx=0.82,rely=0.4,relheight=0.55)

# Set scroll to listbox
schedule_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=schedule_list.yview)

schedule_list.bind('<<ListboxSelect>>', select_item)

# Submit an entry 
submit_btn = tk.Button(frame,text="Submit",bg='#37eb34',command=submit_entry,width=7)
submit_btn.place(relx=0.88,rely=0.45)

# Update an entry
update_btn = tk.Button(frame,text="Update",bg='#34e1eb',command=update_entry,width=7)
update_btn.place(relx=0.88,rely=0.55)

# Delete an entry
delete_btn = tk.Button(frame,text="Delete",bg='#eb4c34',command=delete_entry,width=7)
delete_btn.place(relx=0.88,rely=0.65)

# Clear all fields
clear_btn = tk.Button(frame,text="Clear",bg='#fff',command=clear_data,width=7)
clear_btn.place(relx=0.88,rely=0.75)

# Sort all events
sort_btn = tk.Button(frame,text="Sort",bg='#fff',command=sort_events,width=7)
sort_btn.place(relx=0.88,rely=0.85)

populate_list()

# unable to resize
# root.resizable(width='FALSE', height='FALSE')

root.mainloop()

# root.geometry('700x350')

# change overall fonts

