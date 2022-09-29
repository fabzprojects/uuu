from enum import unique
from ssl import _create_unverified_context
from kmply import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol


@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))






class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    shop = db.Column(db.String(200))
    approve = db.Column(db.String(200))
    reject = db.Column(db.String(200))
    ret_id= db.Column(db.String(200))





class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    email= db.Column(db.VARCHAR)
    subject= db.Column(db.VARCHAR)
    message= db.Column(db.String(200))



class StitchOrder(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tid = db.Column(db.String(200))
    product= db.Column(db.VARCHAR)
    qty= db.Column(db.VARCHAR)
    height= db.Column(db.String(200))
    bust= db.Column(db.String(200))
    hips= db.Column(db.String(200))
    waist= db.Column(db.String(200))
    sleeve= db.Column(db.String(200))
    neck= db.Column(db.String(200))
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    desc = db.Column(db.String(200))
    status= db.Column(db.String(200),default='Pending')
    





class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    cprice = db.Column(db.String(200))
    wprice = db.Column(db.String(200))
    rprice = db.Column(db.String(200))
    desc = db.Column(db.String(200))





class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    pid=db.Column(db.String(200))
    did=db.Column(db.String(200))
    qty=db.Column(db.String(200))
    shop=db.Column(db.String(200))
    usertype=db.Column(db.String(200))
    total=db.Column(db.String(200))
    al_status=db.Column(db.String(200))
    del_status=db.Column(db.String(200))
    m_status=db.Column(db.String(200))
    uid=db.Column(db.String(200))
    mode=db.Column(db.String(200))
    product = db.Column(db.String(200))
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    st = db.Column(db.String(20),  default='Place Stitching Order')
    address= db.Column(db.String(200))
    price = db.Column(db.String(200))
    desc = db.Column(db.String(200))
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    pstatus= db.Column(db.String(200))
    cardno = db.Column(db.String(200),unique=True)
    amount =db.Column(db.String(200))
    cvv=db.Column(db.String(200))
    month=db.Column(db.String(200))
    year=db.Column(db.String(200))
    