import psycopg2
 

class Create:
    def __init__(self):
        self.conn = psycopg2.connect("dbname='my_diary' user='postgres' password='asekenye'")
        self.cur = self.conn.cursor()

    def table(self):
        create_user_table = """ CREATE TABLE users(user_id VARCHAR(255) PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,user_password VARCHAR(20) NOT NULL) """
        self.cur.execute(create_user_table)
        self.conn.commit()
        self.conn.close()

class Users(Create):
    def __init__(self):
        Create.__init__(self)

    def insert_new_user(self, u_id, name, password):
        create = """INSERT INTO my_diary(user_id, user_name,user_password)VALUES(%s,%s,%s);"""
        self.cur.execute(create, (u_id, name, password))
        self.conn.commit()
        return "new user created"

    def get_all_user(self):
        create = """SELECT * FROM my_diary;"""
        self.cur.execute(create)
        result = self.cur.fetchall()
        return result
        return "all users"
        
    


