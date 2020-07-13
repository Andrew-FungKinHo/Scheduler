import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY,
            event_date text,
            dayInWeek text,
            start_time text,
            end_time text,
            event_name text,
            remarks text
            )""")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM schedule")
        rows = self.cur.fetchall()
        return rows

    def insert(self, event_date, dayInWeek, start_time, end_time, event_name, remarks):

        self.cur.execute("INSERT INTO schedule VALUES (NULL, ?, ?, ?, ?, ?, ?)",
            (event_date, dayInWeek, start_time, end_time, event_name, remarks))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM schedule WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, event_date, dayInWeek, start_time, end_time, event_name, remarks):
        self.cur.execute("UPDATE schedule SET event_date = ?, dayInWeek = ?, start_time = ?, end_time = ?, event_name = ?, remarks = ? WHERE id = ?",
                         (event_date, dayInWeek, start_time, end_time, event_name, remarks, id))
        self.conn.commit()

    def sort(self):
        self.cur.execute("SELECT * FROM schedule ORDER BY event_date ASC")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

# db = Database('store.db')
# db.insert("2020-07-14","Tuesday","20:00","21:00","Meet the people of JP Morgan","get link from gmail")
# db.insert("2020-07-25", "Saturday", "09:30", "11:30","FinTech Track: Hong Kong Monetary Authority (morning)", "reply email to Cyberport to sign up")
# db.insert("2020-07-25", "Saturday", "14:30", "16:30","Smart-Living Track: Hong Kong Broadband Network", "reply email to Cyberport to sign up")



# import sqlite3

# conn = sqlite3.connect(':memory:')
# # conn = sqlite3.connect('schedule.db')

# c = conn.cursor()

# c.execute("""CREATE TABLE schedule (
#             id INTEGER PRIMARY KEY,
#             event_date text,
#             dayInWeek text,
#             start_time text,
#             end_time text,
#             event_name text,
#             remarks text
#             )""")


# # c.execute("INSERT INTO schedule VALUES (NULL, ?, ?, ?, ?, ?, ?)",('12/7/2020','Saturday','14:00','15:00','CUPP Webinar','compulsory'))
# # (event_date, dayInWeek, start_time, end_time, event_name, remarks))

# c.execute("INSERT INTO schedule VALUES (NULL, ?, ?, ?, ?, ?, ?)", ('2020-07-12','Saturday','14:00','15:00','CUPP Webinar','compulsory'))
# c.execute("INSERT INTO schedule VALUES (NULL, ?, ?, ?, ?, ?, ?)", ('2020-06-30','Saturday','14:00','15:00','CUPP Webinar','compulsory'))
# c.execute("INSERT INTO schedule VALUES (NULL, ?, ?, ?, ?, ?, ?)", ('2020-07-12','Saturday','14:00','15:00','CUPP Webinar','compulsory'))
# conn.commit()

# # c.execute("SELECT * FROM schedule WHERE event_name='CUPP Webinar'")
# c.execute("SELECT * FROM schedule")
# print(c.fetchall())
# conn.commit()

# # c.execute("SELECT DATE('event_date') FROM schedule")
# # conn.commit()

# c.execute("SELECT event_date FROM schedule ORDER BY event_date ASC")

# print(c.fetchall())
# conn.commit()

# conn.close()

