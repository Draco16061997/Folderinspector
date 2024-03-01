import sqlite3
import config
import File
from datetime import datetime


class BD_init():
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(self.path)
        self.c = self.db.cursor()



class AddBD(BD_init):
    def writheBd(self, list):
        today = datetime.today()

        exept = []

        count = 0

        for i in list:
            try:
                self.c.execute(f"SELECT Name FROM tags WHERE Name  = '{i[1]}'")
                if self.c.fetchone() is None:
                    self.c.execute(f"INSERT INTO tags VALUES (?, ?, NULL)", (i[0], i[1]))

                    count += 1
            except:
                exept.append(i)
                print(i)

        self.db.commit()

        with open (f"{config.path}/_ERROR.txt", 'a') as file:
            for i in exept:
                file.write(today.strftime("%Y-%m-%d")+'__'+i[0]+'\n')
        print(f'UPDATE TABLE FROM tags ADD {count} RECORDS')


if __name__ == '__main__':
    bd = AddBD(config.db)
    folder = File.Folder(config.path)
    bd.writheBd(folder.getListFiles())
