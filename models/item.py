from db import db

#here our ItemModel extended db.model what it means is : It tell Sqlalchemy  this class here
#is going to save in our db, reteriving from db. So basically it will create mapping between
#db and object 
class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
 
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # this column is used to map stores table with items table using store_id & id column
    #below will seees that we have a store_id and therefore we can find a store in database that 
    #matches store_id. Now every ItemModel has a property store that is the store that matches
    #store_id in its id 
    store = db.relationship('StoreModel')

    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name' : self.name, 'price' : self.price}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() 
        # select * from items where name = name limit 1
        #here cls = ItemModel it is a class which is a type of sqlalchemy model, cls.query is 
        #query builder which means Select * from items , now filter by is parameter to filter 
        #data , we can filter on more than one column by again adding filter_by 
        #the above statement is returning an ItemModel object which contains self.name 
        # & self.price

#for upserting data 
    def save_to_db(self):
        # the session in this instance is collection of objects that we are going to add to 
        # database. We can multiple objects and can write them at once. so below statement insert/add 
        # object provided in database
        db.session.add(self)
        # below statement commit in db 
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
