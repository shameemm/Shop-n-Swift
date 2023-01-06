import pymysql
def selectall(qry):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shopnswift')
    cmd = con.cursor()
    cmd.execute(qry)
    res = cmd.fetchall()
    con.commit()
    return res

def selectall2(qry, value):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shopnswift')
    cmd = con.cursor()
    cmd.execute(qry, value)
    res = cmd.fetchall()
    con.commit()
    return res

def selectone(qry):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shopnswift')
    cmd = con.cursor()
    cmd.execute(qry)
    res = cmd.fetchone()
    con.commit()
    return res

def selectone2(qry, value):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shopnswift')
    cmd = con.cursor()
    cmd.execute(qry, value)
    res = cmd.fetchone()
    con.commit()
    return res

def iud(qry, values):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='shopnswift')
    cmd = con.cursor()
    cmd.execute(qry, values)
    res = cmd.lastrowid
    con.commit()
    return res

def androidselectall(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='shopnswift')
    cmd=con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

def androidselectallnew(q):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='shopnswift')
    cmd=con.cursor()
    cmd.execute(q)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
