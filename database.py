import sqlite3
import datetime


class Account(object):

    @staticmethod
    def _current_time():
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def __init__(self, account_name):
        self.account_name = account_name
        self.db = sqlite3.connect(f"{self.account_name}.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)


    # ====================== COURSES =======================#
    def create(self, list_name):
        try:
            self.db.execute("CREATE TABLE IF NOT EXISTS {} (code TEXT PRIMARY KEY NOT NULL, title TEXT NOT NULL,"
                            "creditHour INTEGER NOT NULL, grade INTEGER NOT NULL, date_created TEXT NOT NULL)".format(list_name))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def insert(self, list_name, code, title, creditHour, grade):
        try:
            date_created = self._current_time()
            self.db.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?)".format(list_name), (code, title, creditHour, grade, date_created))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def update(self, list_name, code, modified_title, modified_creditHour, modified_grade):
        try:
            self.db.execute("UPDATE {} SET title=?, creditHour=?, grade=? WHERE (code=?)".format(list_name), (modified_title, modified_creditHour, modified_grade, code))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def delete(self, list_name, code):
        try:
            self.db.execute("DELETE FROM {} WHERE (code=?)".format(list_name), (code,))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def load(self, list_name):
        list_items = {}
        cursor = self.db.execute("SELECT code, title, creditHour, grade, date_created FROM {}".format(list_name))
        row = cursor.fetchall()
        if row:
            for item in row:
                list_items[item[0]] = [item[1], item[2], item[3]]
            return list_items


    # ====================== PROFILE =======================#
    def create_profile(self, list_name):
        try:
            self.db.execute("CREATE TABLE IF NOT EXISTS {} (fName TEXT NOT NULL, mName TEXT, lName TEXT NOT NULL, gender TEXT,"
                            "dateOfBirth TEXT, nationality TEXT, placeOfBirth TEXT, languages TEXT, "
                            "bloodGroup TEXT, matric TEXT NOT NULL, date_created TEXT NOT NULL, PRIMARY KEY(fName, matric))".format(list_name))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def insert_profile(self, list_name, fName, mName, lName, gender, dateOfBirth, nationality, placeOfBirth, languages, bloodGroup, matric):
        try:
            date_created = self._current_time()
            self.db.execute("INSERT INTO {} (fName, mName, lName, gender, dateOfBirth, nationality, placeOfBirth,"
                            "languages, bloodGroup, matric, date_created) VALUES (?, ?, ?, ?, ?, "
                            "?, ?, ?, ?, ?, ?)".format(list_name), (fName, mName, lName, gender, dateOfBirth,
                                                                    nationality, placeOfBirth, languages, bloodGroup, matric, date_created))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def update_profile(self, list_name, fName, mName, lName, gender, dateOfBirth, nationality, placeOfBirth, languages, bloodGroup, matric):
        try:
            self.db.execute("UPDATE {} SET mName=?, gender=?, dateOfBirth=?, nationality=?, placeOfBirth=?, languages=?,"
                            "bloodGroup=? WHERE (matric=?)".format(list_name), (mName, gender, dateOfBirth, nationality, placeOfBirth, languages, bloodGroup, matric))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def delete_profile(self, list_name, matric):
        try:
            self.db.execute("DELETE FROM {} WHERE (matric=?)".format(list_name), (matric,))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def load_profile(self, list_name):
        list_items = {}
        keys = ['First Name', 'Middle Name', 'Surname', 'Gender', 'Date of Birth', 'Nationality', 'Place of Birth', 'Languages', 'Blood Group', 'Matriculation Number']
        cursor = self.db.execute("SELECT fName, mName, lName, gender, dateOfBirth, nationality, "
                                 "placeOfBirth, languages, bloodGroup, matric FROM {}".format(list_name))
        row = cursor.fetchone()
        if row:
            for i in range(len(keys)):
                list_items[keys[i]] = row[i]
            return list_items


    #==================== PROGRAMME ======================#
    def create_prog(self, list_name):
        try:
            self.db.execute("CREATE TABLE IF NOT EXISTS {} (programme TEXT PRIMARY KEY NOT NULL, date_created TEXT NOT NULL)".format(list_name))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def insert_prog(self, list_name, programme):
        try:
            date_created = self._current_time()
            self.db.execute("INSERT INTO {} (programme, date_created) VALUES (?, ?)".format(list_name), (programme, date_created))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def update_prog(self, list_name, programme):
        try:
            self.db.execute("UPDATE {} SET programme=?".format(list_name), (programme,))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def delete_prog(self, list_name, programme):
        try:
            self.db.execute("DELETE FROM {} WHERE (programme=?)".format(list_name), (programme,))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def load_prog(self, list_name):
        programme = ""
        cursor = self.db.execute("SELECT programme FROM {}".format(list_name))
        row = cursor.fetchone()
        if row:
            programme = row[0]
            return programme


    #==================== LOGIN ======================#
    def create_login(self, list_name):
        try:
            self.db.execute("CREATE TABLE IF NOT EXISTS {} (username PRIMARY KEY NOT NULL, password TEXT NOT NULL)".format(list_name))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def insert_login(self, list_name, username, password):
        try:
            self.db.execute("INSERT INTO {} (username, password) VALUES (?, ?)".format(list_name), (username, password))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def update_login(self, list_name, username, password):
        try:
            self.db.execute("UPDATE {} SET password=? WHERE (username=?)".format(list_name), (password, username))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def delete_login(self, list_name, username):
        try:
            self.db.execute("DELETE FROM {} WHERE (username=?)".format(list_name), (username,))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def load_login(self, list_name):
        login = {}
        cursor = self.db.execute("SELECT username, password FROM {}".format(list_name))
        row = cursor.fetchall()
        if row:
            for item in row:
                login[item[0]] = item[1]
            return login

    #==================== PHOTO ======================#
    def create_photo(self, list_name):
        try:
            self.db.execute("CREATE TABLE IF NOT EXISTS {} (photo BLOB PRIMARY KEY NOT NULL, date_created TEXT NOT NULL)".format(list_name))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def insert_photo(self, list_name, photo):
        try:
            date_created = self._current_time()
            self.db.execute("INSERT INTO {} (photo, date_created) VALUES (?, ?)".format(list_name), (photo, date_created))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def update_photo(self, list_name, photo):
        try:
            self.db.execute("UPDATE {} SET photo=?".format(list_name), (photo,))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def delete_photo(self, list_name, photo):
        try:
            self.db.execute("DELETE FROM {} WHERE (photo=?)".format(list_name), (photo,))
        except:
            self.db.rollback()
        else:
            self.db.commit()

    def load_photo(self, list_name):
        photo = None
        cursor = self.db.execute("SELECT photo FROM {}".format(list_name))
        row = cursor.fetchone()
        if row:
            photo = row[0]
            return photo



    #==================== GENERAL ======================#
    def load_tables(self):
        tables = []
        cursor = self.db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        row = cursor.fetchall()
        if row:
            for table_name in row:
                tables.append(table_name[0])
            return tables

    def drop(self, list_name):
        try:
            self.db.execute("DROP TABLE {}".format(list_name))
        except:
            print("cannot delete")
            self.db.rollback()
        else:
            self.db.commit()


if __name__ == '__main__':
    bruno = Account("Ben")
    # bruno.create("monday")
    # bruno.insert('monday', 'ENG141', 'English', '2', '60')
    # print(bruno.load('monday'))
    # t = bruno.load_tables()
    # print(t)
    
    # bruno.create_profile("profile")
    # bruno.insert_profile("profile", 'fName', 'mName', 'lName', 'gender', 'dateOfBirth', 'nationality', 'placeOfBirth', 'languages', 'bloodGroup', 'matric', 'password')
    # print(bruno.load_profile("profile"))

    # bruno.create_login('login')
    # bruno.insert_login('login', 'chris', 'xc90')
    print(bruno.load_login('login'))
    logins = bruno.load_login('login')
    if 'chris' in logins and logins['chris']=='xc90':
        print('yes')


    bruno.db.close()