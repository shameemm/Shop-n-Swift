from flask import *
from src.db_connection import *
app=Flask(__name__)

@app.route("/logincode",methods=['post'])
def logincode():
    uname=request.form['uname']
    password=request.form['password']
    q="select * from login where username=%s and password=%s "
    val=uname,password
    res=selectone2(q, val)
    print(res)
    if res is None:
        return jsonify({'task': 'invalid'})
    else:
        return jsonify({'task': 'success','lid':res[0],'type':res[3]})

@app.route("/registration",methods=['post'])
def parentregistration():
    try:
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        username=request.form['uname']
        password=request.form['password']
        qry = "insert into login values(null,%s,%s,'user')"
        value = (username, password)
        lid = iud(qry, value)
        qry1 = "insert into registration values(null,%s,%s,%s,%s)"
        val = (str(lid), name, mobile, email, )
        iud(qry1, val)

        return jsonify({'task': 'success'})
    except Exception as e:
        return jsonify({'task': 'Already Exist'})

@app.route("/viewbill", methods=['post'])
def viewbill():
     id = request.form['id']
     print(id)
     qry = "select * from billing where userid=%s and status='pending'"
     value = id
     res = androidselectall(qry,value)
     print(res)
     return jsonify(res)

@app.route("/viewmoredetails",methods=['post'])
def viewmoredetails():
    id = request.form['id']
    qry = "SELECT `product`.`productid`,`product`.`productname`,`cart`.`quantity`,`cart`.`price`,cart.cart_id FROM`cart`JOIN`product`ON`cart`.`productid`=`product`.`productid`WHERE`cart`.`billid`= %s"
    value = id
    res = androidselectall(qry,value)
    return jsonify(res)

@app.route("/addrating", methods=['post'])
def addrating():
    id = request.form['id']
    rating = request.form['rating']
    qry = "insert into rating values(null,curdate(),%s,%s)"
    value = id,rating
    iud(qry,value)
    return jsonify({'task': 'success'})

@app.route("/viewrating")
def viewrating():
    qry = "SELECT `registration`.`name`,`rating`.`date`,`rating`.`rating`FROM `rating`JOIN`registration`ON`registration`.`loginid`=`rating`.`userlogin_id`"
    res = androidselectallnew(qry)
    return jsonify(res)

@app.route("/trackorder", methods=['post'])
def trackorder():
     id = request.form['id']
     print(id)
     qry = "SELECT`billing`.*,`track table`.*,`delivery_agent`.`agent_firstname`,`delivery_agent`.`agent_lastname`,`delivery_agent`.`phone`FROM`billing`JOIN`assign_table`ON`billing`.`billno`=`assign_table`.`bill_id`JOIN `delivery_agent` ON `delivery_agent`.`agent_loginid`=`assign_table`.`agent_loginid` JOIN `track table` ON `track table`.`agent_loginid`=`delivery_agent`.`agent_loginid` WHERE `billing`.`userid`=%s"
     value = id
     res = androidselectall(qry,value)
     print(res)
     return jsonify(res)

@app.route("/viewproduct",methods=['post'])
def viewproduct():
    qry = "select * from product"
    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)

@app.route("/cart",methods=['post'])
def cart():
    id = request.form['id']
    billid = request.form['billid']
    pid = request.form['pid']
    qty = request.form['quanity']
    qry = "select price from product where productid=%s"
    value = pid
    res = androidselectall(qry,value)
    price = res[0]
    total = qty*price
    qry1 = "insert into cart values(null,%s,%s,%s,%s,'online')"
    value1 = id,billid,pid,qty,total
    iud(qry1,value1)
    return jsonify({'task': 'success'})


@app.route("/viewcart",methods=['post'])
def viewcart():
    id = request.form['id']
    qry = "SELECT `cart`.*,`product`.`productname`FROM `cart`JOIN`product`ON`cart`.`productid`=`product`.`productid`JOIN `billing`ON `billing`.`billno`=`cart`.`billid`WHERE `billing`.`userid`=%S"
    value = id
    res = androidselectallnew(qry,value)
    return jsonify(res)


# Delivery Agent

# @app.route("/loginagent",methods=['post'])
# def loginagent():
#     uname=request.form['username']
#     password=request.form['password']
#     q="select * from login where username=%s and password=%s "
#     val=uname,password
#     res=selectone2(q, val)
#     if res is None:
#         return jsonify({'task': 'invalid'})
#     else:
#         return jsonify({'task': 'success','lid':res[0],'type':res[3]})

@app.route("/viewwork",methods=['post'])
def viewwork():
    id = request.form['id']
    print(id)
    qry = "SELECT `billing`.`billno`,`assign_table`.`date`,`registration`.*,`assign_table`.`assign_id`FROM `billing`JOIN`cart`ON`billing`.`billno`=`cart`.`billid`JOIN`assign_table`ON`assign_table`.`bill_id`=`cart`.`billid` JOIN `registration` ON `registration`.`loginid`=`billing`.`userid`WHERE `agent_loginid`= %s and assign_table.status !='delivered'"
    val = id
    res = androidselectall(qry,val)
    print(res)
    return jsonify(res)

@app.route("/updatestatus",methods=['post'])
def updatestatus():
    id = request.form['assignid']
    status = request.form['status']
    print(id,status)
    qry = "update assign_table set status=%s where assign_id=%s"
    val =(status,id)
    iud(qry,val)
    return jsonify({'task': 'success'})

@app.route("/updateloc",methods=['post'])
def updateloc():
    id =request.form['lid']
    print(id)
    latitude = request.form['lati']
    longitude = request.form['longi']
    print(latitude,longitude)
    qry1="select * from `track table` where agent_loginid=%s"
    val1= id
    res=selectone2(qry1,val1)
    if res is not None:
        qry = "update `track table` set latitude=%s,longitude=%s where agent_loginid=%s"
        val =  latitude, longitude,id
        iud(qry,val)
    else:
        qry="INSERT INTO `track table` VALUES(NULL,%s,%s,%s)"
        val=id,latitude,longitude
        iud(qry,val)
    return jsonify({'result': 'success'})

@app.route('/purstart',methods=['get','post'])
def purstart():
    print(request.form)
    id=request.form['uid']
    qry = "INSERT INTO`billing` values(null,'0',%s,'0','pending')"
    val = id;
    billno = iud(qry,val)

    return jsonify({'task': str(billno)})

@app.route('/prodtl',methods=['POST'])
def prodtl():
    pid=request.form['productid']
    print(pid)
    qry = "SELECT * FROM product where productid=%s"
    value = pid
    print(qry)
    print(value)
    res = androidselectall(qry,value)
    print(res)
    return jsonify(res)

@app.route('/addtocart',methods=['post'])
def addtocart():
    print(request.form)
    pid=request.form['pid']
    billid=request.form['billid']
    qty=request.form['qty']
    price=request.form['price']
    type = request.form['type']
    print(pid)
    amt=int(qty)*int(price)
    qry = "SELECT `product_quantity`.`qty` FROM`product_quantity`JOIN`product`ON`product`.`productid`=`product_quantity`.`pid`WHERE `product`.`productid`=%s"
    val=(pid)
    r=selectone2(qry,val)
    print(r)
    orgqunty = int(r[0])
    if orgqunty < int(qty):
        return jsonify({'task': "Out of stock"})
    else:
        qry="INSERT INTO cart values(null, %s, %s, %s, %s, %s) "
        value = (billid, pid,qty,amt,type)
        iud(qry,value)
        qry1="UPDATE `product_quantity` SET `qty`=`qty`-%s  WHERE `pid`=%s"
        value1 = (qty,pid)
        iud(qry1,value1)
        return jsonify({'task': "success"})

@app.route('/newpur',methods=['post'])
def newpur():
    # pid=request.form['pid']
    Billid=request.form['billid']
    print(Billid)
    # qty=request.form['qty']
    # price=request.form['price']
    # amt=int(qty)*int(price)
    # print(amt)

    # cmd.execute("SELECT `QTY` FROM product WHERE `ID`='"+pid+"'")
    # r=cmd.fetchone()
    # orgqunty=int(r[0])
    # if orgqunty < int(qty) :
    #     return jsonify({'task': "Out of stock"})
    # else:
    #     cmd.execute("INSERT INTO `billitems` VALUES(NULL,'"+Billid+"','"+pid+"','"+qty+"','"+str(amt)+"')")
    #     cmd.execute("UPDATE `product` SET `QTY`=`QTY`-'" + qty + "'  WHERE `ID`='" + pid + "'")
    qry = "SELECT SUM(price) FROM `cart`  WHERE billid=%s"
    value = Billid
    s=selectone2(qry,value)
    print(s)
    if s is not None:
            tot=s[0]
            print(str(tot))
            qry = "UPDATE `billing` SET `totalprice`=%s, date = curdate() WHERE billno=%s"
            val=(tot,Billid)
            iud(qry,val)
    return jsonify({'task': "success"})

@app.route("/addaddress", methods=['post'])
def addaddress():
    billid = request.form['billid']
    print(billid)
    name = request.form['name']
    phone = request.form['phone']
    post = request.form['post']
    email = request.form['email']
    print(email)
    qry = "insert into delivery_address values(null,%s,%s,%s,%s,%s)"
    value = (billid, name, phone, post, email)
    iud(qry, value)
    return jsonify({'task': 'success'})

@app.route("/deleteitem",methods=['post'])
def deleteitem():

    cartid=request.form['cartid']
    billno = request.form['billno']
    print(billno)
    qry="SELECT COUNT(*) FROM `cart`  WHERE `cart`.`billid`=%s"
    res=selectone2(qry,billno)
    print(res)
    if int(res[0])==1:
        qry = "DELETE  FROM `billing` WHERE `billno`=%s"
        value = (billno)
        iud(qry, value)
        qry = "DELETE  FROM cart WHERE cart_id=%s"
        value = (cartid)
        iud(qry, value)
    else:

        qry4 = "SELECT `price` FROM `cart` WHERE `cart_id`=%s"
        val4 = (str(cartid))
        res2 = selectone2(qry4, val4)
        qry = "DELETE  FROM cart WHERE cart_id=%s"
        value = (cartid)
        iud(qry, value)
        qry3="SELECT `totalprice` FROM `billing` WHERE `billing`.`billno`=%s"
        val3=str(billno)
        res1=selectone2(qry3,val3)
        total=res1[0]

        available=int(total)-int(res2[0])
        qry2="UPDATE `billing` SET `billing`.`totalprice`=%s WHERE `billno`=%s"
        val=(int(available),billno)
        iud(qry2,val)


    return jsonify({'task': 'success'})

@app.route("/bankdetails", methods=['post'])
def bankdetails():
    lid = request.form['lid']
    print(lid)
    bname = request.form['bname']
    ifsc = request.form['ifsc']
    key = request.form['key']
    acno = request.form['acno']
    billno = request.form['billno']
    print(bname,ifsc,key,acno,billno)
    qry = "select * from bank_account where  user_lid=%s and bankname=%s and ifsc=%s and keyno=%s and accountno=%s"
    value = (lid,bname,ifsc,key,str(acno))
    print(value)
    res = selectone2(qry,value)
    print(res)
    if res is None:
        return jsonify({'task': 'invalid'})
    else:
        id=res[0]
        amt=res[6]
        qry="select totalprice from billing where billno = %s"
        value = billno
        s=selectone2(qry,value)
        pr=s[0]
        if(amt<pr):
            return jsonify({'task': 'insufficent'})
        else:
            blce=amt-pr
            qry = "update  bank_account set cash = %s where bankid=%s"
            value = blce,id
            iud(qry,value)
            qry1= "update billing set status ='paid' where billno=%s"
            value1 = billno
            iud(qry1,value1)

            return jsonify({'task': 'success'})


app.run(host="192.168.43.16", port=5000)





