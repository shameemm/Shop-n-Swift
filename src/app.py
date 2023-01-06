import os
from builtins import print

import pyqrcode
from flask import *
from werkzeug.utils import secure_filename

from src.db_connection import *
app = Flask(__name__)
app.secret_key="123"


import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect("/")
        return func()
    return secure_function

@app.route('/')

def main():

    session.clear()
    return render_template("login.html")



@app.route('/addsales',methods=['POST'])
@login_required
def addsales():
    return render_template("addsales.html")

@app.route('/logout')
@login_required
def logout():
    return render_template("login.html")

@app.route('/addstaff',methods=['POST','GET'])
@login_required
def addstaff():
    return render_template("addstaff.html")

@app.route('/adminhome')
@login_required
def adminhome():
    return render_template("admin_index.html")

@app.route('/managesales')
@login_required
def manage_sales():
    qry = "select staffreg.* from staffreg join login on login.id=staffreg.loginid where login.type='sales'"
    res = selectall(qry)
    return render_template("Manage sales.html", sales=res)


@app.route('/saleshome')
@login_required
def saleshome():
    return render_template("sales_index.html")

@app.route('/slviewproduct')
@login_required
def slviewproduct():
    return render_template("sl_view_product.html")

@app.route('/staddproduct')
@login_required
def staddproduct():
    return render_template("st_add_product.html")

@app.route('/stqrallocation')
@login_required
def stqrallocation():
    qry = "select * from product"
    res = selectall(qry)
    return render_template("st_qr_allocation.html", qr=res)

@app.route('/ststockupdation')
@login_required
def ststockupdation():
    qry = "select * from product"
    res = selectall(qry)

    return render_template("st_stock_updation.html", res = res)

@app.route('/storemasterhome')
@login_required
def storemasterhome():
    return render_template("store_index.html")

@app.route('/trackagent')
@login_required
def trackagent():
    qry="SELECT `delivery_agent`.`agent_firstname`,`agent_lastname`,`registration`.`name`,`registration`.`mobile`,`track table`.`latitude`,`longitude` FROM `delivery_agent` JOIN `track table` ON `track table`.`agent_loginid`=`delivery_agent`.`agent_loginid` JOIN `assign_table` ON `assign_table`.`agent_loginid`=`delivery_agent`.`agent_loginid` JOIN `billing` ON `billing`.`billno`=`assign_table`.`bill_id` JOIN `registration` ON `registration`.`loginid`=`billing`.`userid`"
    res=selectall(qry)
    return render_template("track agent.html",val=res)

@app.route('/updatestaff')
@login_required
def updatestaff():
    return render_template("updatestaff.html")

@app.route('/verifycode')
@login_required
def verifycode():
    return render_template("verifycode.html")

@app.route('/viewproductdetails')
@login_required
def viewproductdetails():
    qry = "select * from product"
    res = selectall(qry)
    return render_template("viewproducts.html", products=res)


@app.route('/viewbill')
@login_required
def viewbill():
    qry = "select * from billing"
    res = selectall(qry)
    return render_template("viewbill.html", bill=res)


@app.route('/viewbill2')
@login_required
def viewbill2():
    id = request.args.get('id')
    print("==========",id)
    qry = "SELECT `product`.`productname`,`cart`.`quantity`,`cart`.`price` FROM `billing` JOIN `cart` ON `cart`.`billid`=`billing`.`billno`JOIN`product`ON`product`.`productid`=`cart`.`productid`"
    value = (id)
    res = selectone2(qry,value)
    print(res)
    return render_template("viewbill2.html", bill=res)

@app.route('/viewproducts')
@login_required
def viewproducts():
    qry = "select * from product"
    res = selectall(qry)
    return render_template("viewproducts.html", products=res)

@app.route('/viewproducts2')
@login_required
def viewproducts2():
    qry = "SELECT `product`.*,`product_quantity`.`qty`FROM `product_quantity`JOIN `product`ON`product`.`productid`=`product_quantity`.`pid`"
    res = selectall(qry)
    return render_template("viewproducts2.html",product=res)

@app.route('/storeviewbill')
@login_required
def storeviewbill():
    return render_template("store view bill.html")

@app.route('/storeviewbill2')
@login_required
def storeviewbill2():
    return render_template("store view bill2.html")


@app.route('/viewstaff')
@login_required
def viewstaff():
    qry = "select * from staffreg"
    res = selectall(qry)
    return render_template("viewstaff.html",staff=res)

@app.route('/viewrating')
@login_required
def viewrating():
    qry = "SELECT `registration`.`name`,`rating`.`date`,`rating`.`rating`FROM `rating`JOIN`registration`ON`registration`.`loginid`=`rating`.`userlogin_id`"
    res = selectall(qry)
    return render_template("viewrating.html", rating = res)

@app.route('/adddeliveryagent',methods=['post'])
@login_required
def adddeliveryagent():
    return render_template("adddeliveryagent.html")

@app.route('/deliveryagenttable')
@login_required
def deliveryagenttable():
    qry = "select * from delivery_agent"
    res = selectall(qry)
    return render_template("deliveryagenttable.html", dagent=res)

@app.route('/viewassignedjob')
@login_required
def viewassignedjob():
    qry="SELECT `billing`.`billno`,`billing`.`date`,`delivery_agent`.`agent_firstname`,`delivery_agent`.`agent_lastname`,`registration`.`name`,`registration`.`mobile`,`registration`.`email`,`assign_table`.`assign_id` FROM `assign_table` JOIN `billing` ON `assign_table`.`bill_id`=`billing`.`billno` JOIN `delivery_agent` ON `delivery_agent`.`agent_loginid`=`assign_table`.`agent_loginid` JOIN `registration` ON `registration`.`loginid`=`billing`.`userid`"
    res = selectall(qry)
    return render_template("view assigned job.html", res=res)
@app.route('/addwork',methods=['post'])
@login_required
def addwork():
    qry = "select * from delivery_agent"
    res = selectall(qry)
    qry1 = "SELECT * FROM billing WHERE `billing`.`billno` NOT IN(SELECT `bill_id` FROM `assign_table`) "
    res1 = selectall(qry1)



    return render_template("add work.html", agent=res, bill=res1)

@app.route('/login', methods=['post'])

def login():
    un = request.form['username']
    pswd = request.form['password']
    qry = "select * from login where username = %s and password = %s"
    values = (un, pswd)
    res = selectone2(qry, values)
    if res is None:
        return'''<script> alert ("Invalid Username & Password"); window.location="/"</script>'''
    elif res[3]=="admin":
        session['lid']=res[0]
        return redirect("/adminhome")

    elif res[3]=="store":
        session['lid'] = res[0]
        return redirect("/storemasterhome")
    elif res[3]=="sales":
        session['lid'] = res[0]
        return redirect("/saleshome")
    else:
        return '''<script> alert ("Invalid Username & Password"); window.location="/"</script>'''


@app.route('/registerstaff', methods=['post'])
@login_required
def registerstaff():
    try:
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        gender = request.form['radio']
        place = request.form['place']
        pin = request.form['pin']
        phone = request.form['phone']
        email = request.form['email']
        uname = request.form['uname']
        password = request.form['password']
        qry = "insert into login values(null,%s,%s,'store')"
        value = (uname, password)
        id = iud(qry, value)
        qry1 = "insert into staffreg values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value1 = (fname,lname,age,gender,place,phone,pin,email,str(id))
        iud(qry1, value1)
        return '''<script> alert ("registration success"); window.location="/adminhome"</script>'''
    except Exception as e:
        return '''<script> alert ("Already Exist"); window.location="/viewstaff"</script>'''

@app.route('/addproduct', methods=['post'])
@login_required
def addproduct():
    pname = request.form['pname']
    mfgd = request.form['mfgd']
    expd = request.form['expd']
    price = request.form['price']
    image = request.files['image']
    file = secure_filename(image.filename)
    image.save(os.path.join("static/product_image", file))
    qry = "insert into product values(null,%s,%s,%s,%s,%s)"

    value = (pname, mfgd, expd, price,file)
    iud(qry, value)
    return '''<script> alert ("Product Added"); window.location="/viewproducts"</script>'''



@app.route('/deliveryagent', methods=['post'])
@login_required
def deliveryagent():
    try:
        fname = request.form['fname']
        lname = request.form['lname']
        place = request.form['place']

        pin = request.form['pin']
        phone = request.form['phone']
        email = request.form['email']
        uname = request.form['uname']
        password = request.form['password']
        qry = "insert into login values(null,%s,%s,'dagent')"
        value = (uname, password)
        id = iud(qry, value)
        qry1 = "insert into delivery_agent values(null,%s,%s,%s,%s,%s,%s,%s)"
        value1 = ( str(id),fname, lname,place, pin, phone, email)
        iud(qry1, value1)
        return '''<script> alert ("registration success"); window.location="/deliveryagenttable"</script>'''
    except Exception as e:
        return '''<script> alert ("Already Exist"); window.location="/adddeliveryagent"</script>'''
@app.route('/assign_work', methods=['post'])
@login_required
def assign_work():
    billid = request.form['billid']
    agent = request.form['agent']
    qry = "insert into assign_table values(null,%s,%s,'Assigned',curdate())"
    value = (billid,agent)
    iud(qry,value)
    return '''<script> alert ("Work Assigned"); window.location="/viewassignedjob"</script>'''
@app.route('/delete_work')
@login_required
def delete_work():
    id = request.args.get('id')
    qry = "delete from assign_table where assign_id = %s"
    value = (id)
    iud(qry,value)
    return '''<script> alert ("work Deleted"); window.location="/viewassignedjob"</script>'''

@app.route('/delete_staff')
@login_required
def delete_staff():
    id = request.args.get('id')
    qry = "delete from staffreg where staffid = %s"
    value = (id)
    iud(qry,value)
    return '''<script> alert ("Staff Deleted"); window.location="/viewstaff"</script>'''

@app.route('/add_sales',methods=['post'])
@login_required
def add_sales():
    try:
        fname = request.form['fname']
        lname = request.form['lname']
        age=request.form['age']
        place = request.form['place']
        gender = request.form['radiobutton']
        pin = request.form['pin']
        phone = request.form['phone']
        email = request.form['email']
        uname = request.form['uname']
        password = request.form['password']
        qry = "insert into login values(null,%s,%s,'sales')"
        value = (uname, password)
        id = iud(qry, value)
        qry1 = "insert into staffreg values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value1 = ( fname, lname,age,gender, place,  phone,pin, email,str(id))
        iud(qry1, value1)
        return '''<script> alert ("Sales added"); window.location="/managesales"</script>'''
    except Exception as e:
        return '''<script> alert ("Sales added"); window.location="/addsales"</script>'''


@app.route('/delete_product')
@login_required
def delete_product():
    id = request.args.get('id')
    qry = "delete from product where productid = %s"
    value = (id)
    iud(qry,value)
    return '''<script> alert ("Product Deleted"); window.location="/viewproducts"</script>'''

@app.route('/edit_product')
@login_required
def edit_product():
    id = request.args.get('id')
    session['pid']=id
    qry = "select * from product where productid=%s"
    value =(id)
    res = selectone2(qry,value)
    print(res)
    return render_template("edit_product.html", products=res)

@app.route('/update_product', methods=['post'])
@login_required
def update_product():
    pname = request.form['pname']
    mfgd = request.form['mfgd']
    expd = request.form['expd']
    price = request.form['price']
    image = request.files['image']
    file = secure_filename(image.filename)
    image.save(os.path.join("static/product_image", file))
    qry = "update product set productname=%s, mfgdate=%s, expdate=%s, price=%s, productimage=%s where productid = %s"

    value = (pname, mfgd, expd, price, file,str(session['pid']))
    iud(qry, value)
    return '''<script> alert ("Product Updated"); window.location="/viewproducts"</script>'''

@app.route('/edit_staff')
@login_required
def edit_staff():
    id = request.args.get('id')
    session['sid'] = id
    qry = "select * from staffreg where staffid = %s"
    value =(id)
    res = selectone2(qry,value)
    print(res)
    return render_template("edit_staff.html", staff=res)

@app.route('/update_staff', methods=['post'])
@login_required
def update_staff():
    fname = request.form['fname']
    lname = request.form['lname']
    age = request.form['age']
    gender = request.form['radio']
    place = request.form['place']

    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']


    qry = "update staffreg set fname=%s,lname=%s, age=%s, gender=%s, place=%s, pin=%s, phone=%s,email=%s where staffid =%s"
    value = (fname,lname,age,gender,place,pin,phone,email,str(session['sid']))
    iud(qry, value)
    return '''<script> alert ("registration success"); window.location="/viewstaff"</script>'''

@app.route('/delete_agent')
@login_required
def delete_agent():
    id = request.args.get('id')
    qry = "delete from delivery_agent where agentid = %s"
    value = (id)
    iud(qry,value)
    return '''<script> alert ("agent Deleted"); window.location="/deliveryagenttable"</script>'''

@app.route('/edit_agent')
@login_required
def edit_agent():
    id = request.args.get('id')
    session['daid'] = id
    qry = "select * from delivery_agent where agentid = %s"
    value =(id)
    res = selectone2(qry,value)
    print(res)
    return render_template("edit_dagent.html", agent=res)

@app.route('/updateagent',methods=['post'])
@login_required
def update_agent():
    fname = request.form['fname']
    lname = request.form['lname']
    place = request.form['place']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    qry = "update delivery_agent set agent_firstname=%s,agent_lastname=%s, place=%s, pin=%s, phone=%s,email=%s where agentid =%s"
    value = (fname,lname,place,pin,phone,email,str(session['daid']))
    iud(qry, value)
    return '''<script> alert ("registration success"); window.location="/deliveryagenttable"</script>'''

@app.route('/delete_sales')
@login_required
def delete_sales():
    id = request.args.get('id')
    qry = "delete from staffreg where staffid = %s"
    value = (id)
    iud(qry,value)
    return '''<script> alert ("sales Deleted"); window.location="/managesales"</script>'''

@app.route('/edit_sales')
@login_required
def edit_sales():
    id = request.args.get('id')
    session['sid'] = id
    qry = "select * from staffreg where staffid = %s"
    value =(id)
    res = selectone2(qry,value)
    print(res)
    return render_template("editsales.html", sales=res)

@app.route('/update_sales', methods=['post'])
@login_required
def update_sales():
    fname = request.form['fname']
    lname = request.form['lname']
    age = request.form['age']
    gender = request.form['radiobutton']
    place = request.form['place']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    qry = "update staffreg set fname=%s,lname=%s, age=%s, gender=%s, place=%s, pin=%s, phone=%s,email=%s where staffid =%s"
    value = (fname,lname,age,gender,place,pin,phone,email,str(session['sid']))
    iud(qry, value)
    return '''<script> alert ("registration success"); window.location="/managesales"</script>'''

@app.route("/stockupdate", methods = ['post'])
@login_required
def stockupdate():
    pname = request.form['pname']
    mfgd = request.form['mfgd']
    expd = request.form['expd']
    price = request.form['price']
    quantity = request.form['qty']
    qry = "update product set mfgdate=%s, expdate=%s, price=%s where productid = %s "
    value = (mfgd,expd,price,pname)
    iud(qry,value)
    qry1 = "select * from product_quantity where pid = %s"
    val=(pname)
    res=selectone2(qry1,val)
    if res is None:
        qry ="insert into product_quantity values(%s,%s)"
        value =(pname,quantity)
        iud(qry,value)
    else:
        qry = "update product_quantity set qty=%s where  pid=%s"
        val = (quantity,pname)
        iud(qry,val)
    return '''<script> alert ("registration success"); window.location="/storemasterhome"</script>'''

@app.route("/qr_generate")
@login_required
def qr_generate():
    id = request.args.get('id')
    big_code = pyqrcode.create(str(id), error='L', version=27, mode='binary')
    qrs = "./static/qr_code/" + str(id) + ".png"
    # img_name = str(id) + ".png"
    big_code.png(qrs, scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    return '''<script> alert ("QR Code Generated"); window.location="/storemasterhome"</script>'''

@app.route('/slviewproducts')
@login_required
def slviewproducts():
    qry = "SELECT `product`.*,`product_quantity`.`qty`FROM `product_quantity`JOIN `product`ON`product`.`productid`=`product_quantity`.`pid`"
    res = selectall(qry)
    return render_template("sl_view_product.html",product=res)






app.run(debug=True)
