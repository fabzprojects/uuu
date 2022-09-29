from msilib.schema import File
from flask import Flask, render_template, request, redirect,send_file,  flash, abort, url_for
from kmply import app,db,mail
from kmply import app,db,mail
from kmply import app
from kmply.models import *

from flask_login import login_user, current_user, logout_user, login_required
from random import randint
import os
from PIL import Image
from flask_mail import Message
from io import BytesIO
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
# from datetime import datetime as dt
from datetime import datetime,date
# from datetime import timedelta
from werkzeug.utils import secure_filename


from datetime import datetime, timedelta



@app.route('/customer',methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        address = request.form['address']
        
       
        my_data = Login(name=name,username=email,contact=contact,password=password,address=address,usertype="customer")
        db.session.add(my_data) 

        db.session.commit()
        r="Registered Successfully .Please Login"
        # return redirect('/login')
        return render_template("customer.html",r=r)
        
    else :
        return render_template("customer.html")





@app.route('/delivery',methods=['GET', 'POST'])
def delivery():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        address = request.form['address']
      
        
       
        my_data = Login(name=name,address=address,username=email,contact=contact,password=password,approve="Approve",reject="Reject",usertype="delivery")
        db.session.add(my_data) 

        db.session.commit()
        r="Registered Successfully.Please wait for Confirmation"
        # return redirect('/login')
        return render_template("delivery.html",r=r)
        
    else :
        return render_template("delivery.html")



@app.route('/wholesaler',methods=['GET', 'POST'])
def wholesaler():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        address = request.form['address']
        shop = request.form['shop']
        
       
        my_data = Login(name=name,username=email,shop=shop,contact=contact,password=password,address=address,usertype="wholesaler")
        db.session.add(my_data) 

        db.session.commit()
        r="Registered Successfully .Please Login"
        # return redirect('/login')
        return render_template("wholesaler.html",r=r)
        
    else :
        return render_template("wholesaler.html")







@app.route('/retailer',methods=['GET', 'POST'])
def retailer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        address = request.form['address']
        shop = request.form['shop']
        
       
        my_data = Login(name=name,username=email,shop=shop,contact=contact,password=password,address=address,usertype="retailer")
        db.session.add(my_data) 

        db.session.commit()
        r="Registered Successfully .Please Login"
        # return redirect('/login')
        return render_template("retailor.html",r=r)
        
    else :
        return render_template("retailor.html")






@app.route('/tailor',methods=['GET', 'POST'])
def tailor():
    d=Login.query.filter_by(usertype="retailer").all()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        address = request.form['address']
        ret_id = request.form['ret_id']
        
       
        my_data = Login(name=name,ret_id=ret_id,username=email,contact=contact,approve="Approve",reject="Reject",password=password,address=address,usertype="tailor")
        db.session.add(my_data) 

        db.session.commit()
        r="Registered Successfully.Please wait for Confirmation"
        return render_template("tailor.html",r=r,d=d)
        
    else :
        return render_template("tailor.html",d=d)



@app.route('/customer_index/<id>',methods=['GET', 'POST'])
def customer_index(id):
    return render_template("customer_index.html")



@app.route('/tailor_index/<id>',methods=['GET', 'POST'])
def tailor_index(id):
    return render_template("tailor_index.html")


@app.route('/pay_success',methods=['GET', 'POST'])
def pay_success():
    return render_template("pay_success.html")


@app.route('/wh_pay_success',methods=['GET', 'POST'])
def wh_pay_success():
    return render_template("wh_pay_success.html")



@app.route('/ret_pay_success',methods=['GET', 'POST'])
def ret_pay_success():
    return render_template("ret_pay_success.html")


@app.route('/cod',methods=['GET', 'POST'])
def cod():
    return render_template("cod.html")


@app.route('/wh_cod',methods=['GET', 'POST'])
def wh_cod():
    return render_template("wh_cod.html")



@app.route('/ret_cod',methods=['GET', 'POST'])
def ret_cod():
    return render_template("ret_cod.html")


@app.route('/cancel_prod/<int:id>')
@login_required
def cancel_prod(id):
    delet = Order.query.get_or_404(id)
    uid=delet.uid
    
    try:
        db.session.delete(delet)
        
        db.session.commit()
        return redirect('/orders/'+str(uid))
    except:
        return 'There was a problem deleting that task'



@app.route('/wh_cancel_prod/<int:id>')
@login_required
def wh_cancel_prod(id):
    delet = Order.query.get_or_404(id)
    uid=delet.uid
    
    try:
        db.session.delete(delet)
        
        db.session.commit()
        return redirect('/whol_orders/'+str(uid))
    except:
        return 'There was a problem deleting that task'


@app.route('/wholesaler_index/<id>',methods=['GET', 'POST'])
def wholesaler_index(id):
    return render_template("wholesaler_index.html")



@app.route('/retailor_index/<id>',methods=['GET', 'POST'])
def retailor_index(id):
    return render_template("retailor_index.html")





@app.route('/delivery_index/<id>',methods=['GET', 'POST'])
def delivery_index(id):
    return render_template("delivery_index.html")


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        my_data = Contact(name=name, email=email,message=message,subject=subject)
        db.session.add(my_data) 
        db.session.commit()
        return redirect('/msg')
    return render_template("index.html")



@app.route('/admin_index',methods=['GET', 'POST'])
def admin_index():
    return render_template("admin_index.html")



@app.route('/msg',methods=['GET', 'POST'])
def msg():
    return render_template("msg.html")




@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')




@app.route('/login', methods=["GET","POST"])
def login():

   
    if request.method=="POST":
         username=request.form['username']
         password=request.form['password']
         admin = Login.query.filter_by(username=username, password=password,usertype= 'admin').first()
         tailor=Login.query.filter_by(username=username,password=password, usertype= 'tailor',approve="Approved").first()
         customer=Login.query.filter_by(username=username,password=password, usertype= 'customer').first()
         retailor=Login.query.filter_by(username=username,password=password, usertype= 'retailer').first()
         wholesaler=Login.query.filter_by(username=username,password=password,usertype="wholesaler").first()
         delivery=Login.query.filter_by(username=username,password=password,usertype="delivery",approve="Approved").first()
         if admin:
             login_user(admin)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/admin_index') 
        
             
         elif tailor:
             login_user(tailor)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/tailor_index/'+str(tailor.id))

         
     
         
         elif customer:
             login_user(customer)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/customer_index/'+str(customer.id)) 
         elif retailor:
             login_user(retailor)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/retailor_index/'+str(retailor.id))
         elif wholesaler:
             login_user(wholesaler)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/wholesaler_index/'+str(wholesaler.id))


         elif delivery:
             login_user(delivery)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/delivery_index/'+str(delivery.id))
         else:
             d="Invalid Username or Password!"
             return render_template("login.html",d=d)


    
    return render_template("login.html")





# @app.route('/contact', methods = ['GET','POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         subject = request.form['subject']
#         message = request.form['message']
#         my_data = Contact(name=name, email=email,message=message,subject=subject)
#         db.session.add(my_data) 
#         db.session.commit()
#         return redirect('/login')
#     else :
#         return render_template("index.html")





@app.route('/vw_cus')
def vw_cus():
    d=Login.query.filter_by(usertype="customer").all()
    return render_template("vw_cus.html",d=d)



@app.route('/vw_ret')
def vw_ret():
    d=Login.query.filter_by(usertype="retailer").all()
    return render_template("vw_ret.html",d=d)



@app.route('/vw_whol')
def vw_whol():
    d=Login.query.filter_by(usertype="wholesaler").all()
    return render_template("vw_whol.html",d=d)




@app.route('/vw_tai')
def vw_tai():
    d=Login.query.filter_by(usertype="tailor").all()
    return render_template("vw_tai.html",d=d)

@app.route('/ret_tai/<int:id>')
def ret_tai(id):
    d=Login.query.filter_by(ret_id=id,usertype="tailor",approve="Approved").all()
    return render_template("ret_tai.html",d=d)



@app.route('/vw_del')
def vw_del():
    d=Login.query.filter_by(usertype="delivery").all()
    return render_template("vw_del.html",d=d)



@app.route('/allot_delivery/<int:id>',methods=["GET","POST"])
def allot_delivery(id):
    u=Order.query.filter_by(id=id).first()
    d=Login.query.filter_by(usertype="delivery",approve="Approved").all()
    return render_template("allot_delivery.html",d=d,u=u)


@app.route('/wh_allot_delivery/<int:id>',methods=["GET","POST"])
def wh_allot_delivery(id):
    u=Order.query.filter_by(id=id).first()
    d=Login.query.filter_by(usertype="delivery",approve="Approved").all()
    return render_template("wh_allot_delivery.html",d=d,u=u)


@app.route('/ret_allot_delivery/<int:id>',methods=["GET","POST"])
def ret_allot_delivery(id):
    u=Order.query.filter_by(id=id).first()
    d=Login.query.filter_by(usertype="delivery",approve="Approved").all()
    return render_template("ret_allot_delivery.html",d=d,u=u)


@app.route('/approve_tai/<int:id>')
def approve_tai(id):
    c= Login.query.get_or_404(id)
    c.approve = "Approved"
    c.reject="Reject"
    db.session.commit()
    a_sendmail(c.username)
    return redirect('/vw_tai')




@app.route('/allot/<int:oid>/<int:id>')
def allot(oid,id):
    c= Order.query.get_or_404(oid)
    d=Login.query.get_or_404(id)
    c.did = d.id
    c.al_status="Alloted"
    db.session.commit()
   
    return redirect('/ad_vw_orders')



@app.route('/wh_allot/<int:oid>/<int:id>')
def wh_allot(oid,id):
    c= Order.query.get_or_404(oid)
    d=Login.query.get_or_404(id)
    c.did = d.id
    c.al_status="Alloted"
    db.session.commit()
   
    return redirect('/ad_vw_whol_orders')


@app.route('/ret_allot/<int:oid>/<int:id>')
def ret_allot(oid,id):
    c= Order.query.get_or_404(oid)
    d=Login.query.get_or_404(id)
    c.did = d.id
    c.al_status="Alloted"
    db.session.commit()
   
    return redirect('/ad_vw_ret_orders')





@app.route('/up_del_status/<int:id>', methods=["GET","POST"])
def up_del_status(id):
    c= Order.query.get_or_404(id)
    if request.method=="POST":
        c.del_status = request.form['status']
   
        db.session.commit()
   
        return redirect('/de_vw_ords/'+str(current_user.id))
    else:
        return render_template('up_del_status.html')


@app.route('/cod_del_status/<int:id>', methods=["GET","POST"])
def cod_del_status(id):
    c= Order.query.get_or_404(id)
    if request.method=="POST":
        c.del_status = request.form['status']
        d=request.form['amt']
        if d=="Amount Received":
            c.pstatus="Success"
      

   
        db.session.commit()
   
        return redirect('/de_vw_ords/'+str(current_user.id))
    else:
        return render_template('cod_del_status.html')


@app.route('/reject_tai/<int:id>')
def reject_tai(id):
    c= Login.query.get_or_404(id)
    c.reject = 'Rejected'
    c.approve="Approve"
    db.session.commit()
    r_sendmail(c.username)
    return redirect('/vw_tai')




@app.route('/approve_del/<int:id>')
def approve_del(id):
    c= Login.query.get_or_404(id)
    c.approve = "Approved"
    c.reject="Reject"
    db.session.commit()
    a_sendmail(c.username)
    return redirect('/vw_del')


@app.route('/reject_del/<int:id>')
def reject_del(id):
    c= Login.query.get_or_404(id)
    c.reject = 'Rejected'
    c.approve="Approve"
    db.session.commit()
    r_sendmail(c.username)
    return redirect('/vw_del')




def a_sendmail(username):
    
    msg = Message('Approved Successfully',
                  recipients=[username])
    msg.body = f''' Congratulations , Your  Registeration is approved successfully... Now You can login using username and password '''
    mail.send(msg)

def r_sendmail(username):
  
    msg = Message('Registeration Rejected',
                  recipients=[username])
    msg.body = f''' Sorry , Your  Registeration is rejected. '''
    mail.send(msg)




@login_required
@app.route('/vw_feedbacks',methods=["GET","POST"])
def vw_feedbacks():
    obj = Contact.query.all()
    return render_template("vw_feedbacks.html",obj=obj)


@login_required
@app.route('/manage_product',methods=["GET","POST"])
def manage_product():
    obj = Product.query.all()
    return render_template("manage_product.html",obj=obj)



@login_required
@app.route('/cust_vw_products',methods=["GET","POST"])
def cust_vw_products():
    obj = Product.query.all()
    return render_template("cust_vw_products.html",obj=obj)




@login_required
@app.route('/whol_vw_products',methods=["GET","POST"])
def whol_vw_products():
    obj = Product.query.all()
    return render_template("whol_vw_products.html",obj=obj)



@login_required
@app.route('/ret_vw_products',methods=["GET","POST"])
def ret_vw_products():
    obj = Product.query.all()
    return render_template("ret_vw_products.html",obj=obj)




@app.route('/add_products',methods=['GET', 'POST'])
def add_products():



    if request.method == 'POST':
        
        product = request.form['product']
        cprice = request.form['cprice']
        wprice = request.form['wprice']
        rprice = request.form['rprice']
    
        desc = request.form['desc']
       
        img=request.files['image']
        pic_file = save_picture(img)
        view = pic_file
        print(view)  
        my_data = Product(name=product,image=view,cprice=cprice,wprice=wprice,rprice=rprice,desc=desc)
        db.session.add(my_data) 
        db.session.commit()
        return redirect('/manage_product')
    else:
        return render_template("add_products.html")



@app.route('/edit_prod/<int:id>',methods=['GET', 'POST'])
def edit_prod(id):
    d=Product.query.get_or_404(id)

    if request.method == 'POST':
        d.name = request.form['product']

        d.cprice = request.form['cprice']
        d.wprice = request.form['wprice']
        d.rprice = request.form['rprice']
        d.desc = request.form['desc']

        # img=request.files['image']
        # pic_file = save_picture(img)
        # view = pic_file
        # print(view) 
        # d.image=view 
        
       
        db.session.commit()
        return redirect('/manage_product')

    return render_template("edit_product.html",d=d)


def save_picture(form_picture):
    random_hex = random_with_N_digits(14)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)
    
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



@app.route('/delete_prod/<int:id>', methods = ['GET','POST'])
@login_required
def delete_prod(id):

    delet = Product.query.get_or_404(id)
  

    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/manage_product')
    except:
        return 'There was a problem deleting that task'

@login_required
@app.route('/ret_vw_det/<id>',methods=["GET","POST"])
def ret_vw_det(id):

    p=Product.query.filter_by(id=id).first()
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']
        product = request.form['product']
        qty = request.form['qty']
        price = request.form['price']
        desc = request.form['desc']
        uid = request.form['uid']
        pid = request.form['pid']
        shop = request.form['shop']
        total=int(price)*int(qty)
        pstatus="null"
        del_status="Not Delivered"
        image=p.image
        my_data = Order(name=name,usertype="retailor",shop=shop,email=email,qty=qty,total=total,address=address,del_status=del_status,image=image,al_status="Allot",pstatus=pstatus,uid=uid,contact=contact,product=product,price=price,desc=desc,pid=pid)
      
        db.session.add(my_data) 
  
        db.session.commit()
     
        # flash("Registered successfully! Please Login..")
        return redirect('/ret_orders/'+str(uid))
        
    else :
        return render_template("ret_vw_det.html",p=p)



@login_required
@app.route('/whol_vw_det/<id>',methods=["GET","POST"])
def whol_vw_det(id):

    p=Product.query.filter_by(id=id).first()
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']
        product = request.form['product']
        qty = request.form['qty']
        price = request.form['price']
        desc = request.form['desc']
        uid = request.form['uid']
        pid = request.form['pid']
        shop = request.form['shop']
        total=int(price)*int(qty)
        pstatus="null"
        del_status="Not Delivered"
        image=p.image
        my_data = Order(name=name,usertype="wholesaler",shop=shop,email=email,qty=qty,total=total,address=address,del_status=del_status,image=image,al_status="Allot",pstatus=pstatus,uid=uid,contact=contact,product=product,price=price,desc=desc,pid=pid)
      
        db.session.add(my_data) 
  
        db.session.commit()
     
        # flash("Registered successfully! Please Login..")
        return redirect('/whol_orders/'+str(uid))
        
    else :
        return render_template("whol_vw_det.html",p=p)


@login_required
@app.route('/vw_det/<id>',methods=["GET","POST"])
def vw_det(id):

    p=Product.query.filter_by(id=id).first()
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']
        product = request.form['product']
        qty = request.form['qty']
        price = request.form['price']
        desc = request.form['desc']
        uid = request.form['uid']
        pid = request.form['pid']
        total=int(price)*int(qty)
        pstatus="null"
        del_status="Not Delivered"
        image=p.image
        my_data = Order(name=name,usertype="customer",email=email,qty=qty,total=total,address=address,del_status=del_status,image=image,al_status="Allot",pstatus=pstatus,uid=uid,contact=contact,product=product,price=price,desc=desc,pid=pid)
      
        db.session.add(my_data) 
  
        db.session.commit()
     
        # flash("Registered successfully! Please Login..")
        return redirect('/orders/'+str(uid))
        
    else :
        return render_template("vw_det.html",p=p)




@login_required
@app.route('/st_tai/<id>/<tid>',methods=["GET","POST"])
def st_tai(id,tid):

    d=Order.query.filter_by(id=id).first()
    m=Login.query.filter_by(id=tid).first()
    if request.method=="POST":
        product = request.form['product']
        qty = request.form['qty']
        height = request.form['height']
        bust = request.form['bust']
        waist = request.form['waist']
        hips = request.form['hips']
        sleeve = request.form['sleeve']
        neck = request.form['neck']
        desc = request.form['desc']
        tid = m.id
        img=request.files['image']
        pic_file = save_picture(img)
        view = pic_file
        print(view)  
        d.st="Order Placed"
        my_data = StitchOrder(product=product,qty=qty,height=height,bust=bust,waist=waist,hips=hips,sleeve=sleeve,neck=neck,desc=desc,tid=tid,image=view)
      
        db.session.add(my_data) 
  
        db.session.commit()
     
        # flash("Registered successfully! Please Login..")
        return redirect('/st_order/'+str(tid))
        
    else :
        return render_template("st_tai.html",d=d)



@login_required
@app.route('/orders/<id>',methods=["GET","POST"])
def orders(id):
    d=Order.query.filter_by(uid=id,pstatus="null").all()
   
    return render_template("orders.html",d=d)



@login_required
@app.route('/whol_orders/<id>',methods=["GET","POST"])
def whol_orders(id):
    d=Order.query.filter_by(uid=id,pstatus="null").all()
   
    return render_template("whol_orders.html",d=d)




@login_required
@app.route('/ret_orders/<id>',methods=["GET","POST"])
def ret_orders(id):
    d=Order.query.filter_by(uid=id,pstatus="null").all()
   
    return render_template("ret_orders.html",d=d)



@login_required
@app.route('/ad_vw_orders',methods=["GET","POST"])
def ad_vw_orders():
    d=Order.query.filter_by(m_status="fill",usertype="customer").all()
   
    return render_template("ad_vw_orders.html",d=d)



@login_required
@app.route('/ad_vw_whol_orders',methods=["GET","POST"])
def ad_vw_whol_orders():
    d=Order.query.filter_by(m_status="fill",usertype="wholesaler").all()
   
    return render_template("ad_vw_whol_orders.html",d=d)



@login_required
@app.route('/ad_vw_ret_orders',methods=["GET","POST"])
def ad_vw_ret_orders():
    d=Order.query.filter_by(m_status="fill",usertype="retailor").all()
   
    return render_template("ad_vw_ret_orders.html",d=d)





@login_required
@app.route('/de_vw_ords/<int:id>',methods=["GET","POST"])
def de_vw_ords(id):
    d=Order.query.filter_by(did=id).all()
   
    return render_template("de_vw_ords.html",d=d)





@login_required
@app.route('/pay_mode/<id>',methods=["GET","POST"])
def pay_mode(id):
    d=Order.query.filter_by(id=id).first()
    if request.method == 'POST':
        pay_mode =  request.form['pay_mode']
        d.mode=request.form['pay_mode']
        d.m_status="fill"
       
        db.session.commit()
        if pay_mode=="Cash On Delivery":
            d.pstatus="cod"
            db.session.commit()

            return redirect('/cod')
        else:
            return redirect('/buy_now/'+str(d.id))
   
        
   
    return render_template("pay_mode.html",d=d)



@login_required
@app.route('/ret_pay_mode/<id>',methods=["GET","POST"])
def ret_pay_mode(id):
    d=Order.query.filter_by(id=id).first()
    if request.method == 'POST':
        pay_mode =  request.form['pay_mode']
        d.mode=request.form['pay_mode']
        d.m_status="fill"
       
        db.session.commit()
        if pay_mode=="Cash On Delivery":
            d.pstatus="cod"
            db.session.commit()

            return redirect('/ret_cod')
        else:
            return redirect('/ret_buy_now/'+str(d.id))
   
        
   
    return render_template("ret_pay_mode.html",d=d)




@login_required
@app.route('/up_st_status/<id>',methods=["GET","POST"])
def up_st_status(id):
    d=StitchOrder.query.filter_by(id=id).first()
    if request.method == 'POST':
   
        d.status=request.form['status']
       
       
        db.session.commit()
       
        return redirect('/vw_st_ords/'+str(d.tid))
  
   
        
   
    return render_template("up_st_status.html")


@login_required
@app.route('/wh_pay_mode/<id>',methods=["GET","POST"])
def wh_pay_mode(id):
    d=Order.query.filter_by(id=id).first()
    if request.method == 'POST':
        pay_mode =  request.form['pay_mode']
        d.mode=request.form['pay_mode']
        d.m_status="fill"
       
        db.session.commit()
        if pay_mode=="Cash On Delivery":
            d.pstatus="cod"
            db.session.commit()

            return redirect('/wh_cod')
        else:
            return redirect('/wh_buy_now/'+str(d.id))
   
        
   
    return render_template("wh_pay_mode.html",d=d)


@login_required
@app.route('/ords/<id>',methods=["GET","POST"])
def ords(id):
    d=Order.query.filter_by(uid=id,m_status="fill").all()
   
    return render_template("ords.html",d=d)





@login_required
@app.route('/cust_vw_receipt/<id>',methods=["GET","POST"])
def cust_vw_receipt(id):
    d=Order.query.filter_by(id=id).first()
   
    return render_template("cust_vw_receipt.html",d=d)




@login_required
@app.route('/ret_vw_receipt/<id>',methods=["GET","POST"])
def ret_vw_receipt(id):
    d=Order.query.filter_by(id=id).first()
   
    return render_template("ret_vw_receipt.html",d=d)


@login_required
@app.route('/whol_vw_receipt/<id>',methods=["GET","POST"])
def whol_vw_receipt(id):
    d=Order.query.filter_by(id=id).first()
   
    return render_template("whol_vw_receipt.html",d=d)



@login_required
@app.route('/wh_ords/<id>',methods=["GET","POST"])
def wh_ords(id):
    d=Order.query.filter_by(uid=id,m_status="fill").all()
   
    return render_template("wh_ords.html",d=d)



@login_required
@app.route('/ret_ords/<id>',methods=["GET","POST"])
def ret_ords(id):
    d=Order.query.filter_by(uid=id,m_status="fill").all()
   
    return render_template("ret_ords.html",d=d)



@login_required
@app.route('/st_order/<id>',methods=["GET","POST"])
def st_order(id):
    m=Login.query.filter_by(id=id).first()
    d=Order.query.filter_by(uid=current_user.id,pstatus="Success",del_status="Delivered").all()
   
    return render_template("st_order.html",d=d,m=m)



@login_required
@app.route('/vw_st_ords/<id>',methods=["GET","POST"])
def vw_st_ords(id):
    d=StitchOrder.query.filter_by(tid=id,status="Pending").all()
    
   
    return render_template("vw_st_ords.html",d=d)



@login_required
@app.route('/send_noti/<id>',methods=["GET","POST"])
def send_noti(id):
 
    m=Login.query.filter_by(id=current_user.id).first()
    r=Login.query.filter_by(id=m.ret_id).first()
    if request.method=="POST":
        message=request.form['message']
        msg_sendmail(r.username,message)
        g="Message Sent Successfully"
        return render_template("send_noti.html",u=g)

    
   
    return render_template("send_noti.html")



def msg_sendmail(username,message):
    
    msg = Message('Message',
                  recipients=[username])
    msg.body = f''' {message}'''
    mail.send(msg)




@login_required
@app.route('/wrks/<id>',methods=["GET","POST"])
def wrks(id):
    d=StitchOrder.query.filter_by(tid=id,status="Completed").all()
    
   
    return render_template("wrks.html",d=d)


@app.route('/buy_now/<int:id>',methods=["GET","POST"])
def buy_now(id):
    c= Order.query.get_or_404(id)
    if request.method == 'POST':
        c.cardno =  request.form['cardno']
        c.month =  request.form['month']
        c.year =  request.form['year']
        c.cvv =  request.form['cvv']
        c.amount =  request.form['amount']
        c.pstatus="Success"
        
        db.session.commit()
   
        return redirect('/pay_success')
    else:
        return render_template('buy_now.html',c=c)




@app.route('/wh_buy_now/<int:id>',methods=["GET","POST"])
def wh_buy_now(id):
    c= Order.query.get_or_404(id)
    if request.method == 'POST':
        c.cardno =  request.form['cardno']
        c.month =  request.form['month']
        c.year =  request.form['year']
        c.cvv =  request.form['cvv']
        c.amount =  request.form['amount']
        c.pstatus="Success"
        
        db.session.commit()
   
        return redirect('/wh_pay_success')
    else:
        return render_template('wh_buy_now.html',c=c)




@app.route('/ret_buy_now/<int:id>',methods=["GET","POST"])
def ret_buy_now(id):
    c= Order.query.get_or_404(id)
    if request.method == 'POST':
        c.cardno =  request.form['cardno']
        c.month =  request.form['month']
        c.year =  request.form['year']
        c.cvv =  request.form['cvv']
        c.amount =  request.form['amount']
        c.pstatus="Success"
        
        db.session.commit()
   
        return redirect('/ret_pay_success')
    else:
        return render_template('ret_buy_now.html',c=c)




