import psycopg2
 

class Database:
    def __init__(self):
        self.conn = psycopg2.connect("dbname='my_diary' host='localhost' user='postgres' password='incorrect'")
        self.cur = self.conn.cursor()

    def table(self):
        create_user_table = """ CREATE TABLE Users(user_id SERIAL,
        user_name VARCHAR(100) NOT NULL,user_password VARCHAR(20) NOT NULL) """
        self.cur.execute(create_user_table)
        self.conn.commit()
        self.conn.close()

        create_user_entries = """ CREATE TABLE Entries(entry_id SERIAL,
        title VARCHAR(100) NOT NULL,description VARCHAR(20) NOT NULL) """
        self.cur.execute(create_user_entries)
        self.conn.commit()
        self.conn.close()

class Users(Database):
    def __init__(self):
        Database.__init__(self)

    def insert_new_user(self, user_id, name, password):
        create = """INSERT INTO my_diary(user_id, user_name,user_password)VALUES(%s,%s,%s);"""
        self.cur.execute(create, (user_id, name, password))
        self.conn.commit()
        return True

    def get_user_by_id(self):
        create = """SELECT FROM Users WHERE user_id IN (VALUES(%s)) """
        self.cur.execute(create)
        self.conn.commit()
        return True    

    def get_all_user(self):
        create = """SELECT * FROM my_diary;"""
        self.cur.execute(create)
        self.conn.commit()
        return True 

class Entries(Database):
    def __init__(self):
        Database.__init__(self)

    def insert_new_entry(self, entry_id, title,description):
        create = """INSERT INTO my_diary(entry_id, title,description)VALUES(%s,%s,%s);"""
        self.cur.execute(create)
        self.conn.commit()
        return True 

    def get_entry_by_id(self): 
        create = """SELECT FROM User WHERE entry_id IN (VALUES(%s);"""
        self.cur.execute(create)
        self.conn.commit()
        return True

    def get_all_entries(self):
        create = """SELECT * FROM Entries;"""
        self.cur.execute(create)
        self.conn.commit()
        return True