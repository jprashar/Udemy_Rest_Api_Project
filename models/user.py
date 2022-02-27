from db import db 

#here our UserModel extended db.model what it means is : It tell Sqlalchemy  this class here
#is going to save in our db, reteriving from db. So basically it will create mapping between
#db and object 
class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,username,password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username = username).first()
        
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

