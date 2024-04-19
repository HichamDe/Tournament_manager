from .connector import Connector


class Player:
    def __init__(self, full_name="jhon", phone="doe", email="jhon.doe@gmail.com", rating=10):
        self.fullname = full_name
        self.phone = phone
        self.email = email
        self.rating = rating

    def create(self):
        try:
            db = Connector()
            db.cursor.execute("INSERT INTO player (fullname,rating,phone,email) VALUES (?,?,?,?)",(self.fullName, self.phone, self.email, self.rating))
            db.connect.commit()
            db.cursor.close()
            
        except:
            return -1

    def read(id):
        try:
            db = Connector()

            data = db.cursor.execute("SELECT * FROM player WHERE id = ?",(id)).fetchone()
            db.connect.commit()
            db.connect.close()
            
            return data
        except:
            return -1

    def update(self,id):
        try:
            db = Connector()

            db.cursor.execute("UPDATE player SET fullName = ? , rating = ? , phone = ? , email = ? WHERE id = ?;",(self.fullname,self.rating,self.phone,self.email,id))
            db.connect.commit()
            db.connect.close()

        except:
            return -1

    def delete(id):
        try:
            db = Connector()
            db.cursor.execute("DELETE FROM  player WHERE id = ? ", (id))

            db.connect.commit()
            db.connect.close()
            
            return id

        except:
            return -1

    def readAll():
        try:
            db = Connector()

            data = db.cursor.execute("SELECT * FROM player").fetchall()
            db.connect.commit()
            db.connect.close()

            return data
        except:
            return -1
