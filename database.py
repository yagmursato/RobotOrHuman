import psycopg2

class db_add():
    def __init__(self):
        connection = psycopg2.connect("dbname='robotorhuman_db' user='postgres' host='192.168.31.247' password='qazwsx'")
        self.connection = connection.cursor()


    def insert_human(self,word,count):
        self.connection.execute("insert into human (word,count) VALUES ('{}',{}); COMMIT ;".format(word,count))


    def insert_robot(self,word,count):
        self.connection.execute("insert into robot (word,count) VALUES ('{}',{}); COMMIT ;".format(word,count))

    def human_count(self, word):
        self.connection.execute("select count from human where word = '{}' ".format(str(word)))
        count = self.connection.fetchall()
        return count[0][0]

    def robot_count(self,word):
        self.connection.execute("select count from robot where word = '{}'".format(str(word)))
        count = self.connection.fetchall()
        return count[0][0]