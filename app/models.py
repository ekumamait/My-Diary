import psycopg2
 

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='my_diary', host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def table(self):
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users(user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(100) NOT NULL,user_password VARCHAR(20) NOT NULL) """
        self.cur.execute(create_user_table)
        self.conn.commit()

        create_user_entries = """ CREATE TABLE IF NOT EXISTS Entries(entry_id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,description VARCHAR(20) NOT NULL, date VARCHAR(100) NOT NULL) """
        self.cur.execute(create_user_entries)
        self.conn.commit()
        self.conn.close()

class Users():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='my_diary', host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def insert_new_user(self, user_name, user_password):
        create = """INSERT INTO Users(user_name, user_password) VALUES ('{0}', '{1}');""".format(user_name, user_password)
        self.cur.execute(create, (user_name, user_password))
        self.conn.commit()
        return True

    def get_user_by_id(self):
        create = """SELECT FROM Users WHERE user_id IN (VALUES('{0}')) """
        self.cur.execute(create)
        self.conn.commit()
        return True    

    def get_all_user(self):
        create = """SELECT * FROM Users;"""
        self.cur.execute(create)
        self.conn.commit()
        return True 

class Entries():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='my_diary', host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def insert_new_entry(self, title, description, date):
        create = """INSERT INTO Entries (title, description, date) VALUES ('{0}', '{1}', '{2}')""".format(title, description, date)        
        self.cur.execute(create)
        self.conn.commit()
        return True 

    def get_entry_by_id(self, entry_id): 
        create = """SELECT * FROM Entries WHERE entry_id='{}'""".format(entry_id)
        self.cur.execute(create)
        entries = self.cur.fetchall()      
        return entries

    def get_all_entries(self):
        create = """SELECT * FROM Entries;"""
        self.cur.execute(create)
        entries = self.cur.fetchall() 
        return entries

    def edit_entry(self, entry_id, title, description):
        create =  """UPDATE Entries SET title='{0}',  description='{1}' WHERE entry_id='{2}'""".format(title, description, entry_id)
        self.cur.execute(create)
        return True   

    def delete_entry(self, entry_id):
        create = """DELETE FROM Entries WHERE entry_id='{}'""".format(entry_id)
        self.cur.execute(create)
        return True    

    # import pdb;pdb.set_trace()
