import random, string
import pymysql
import names
from faker import Faker
from datetime import datetime


def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def random_str(randomlength=8):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])

def random_address_zipco():
    fake = Faker()
    address = fake.address()
    zipco = address.split(' ')[-1]
    return [address,zipco]

def db_conn():
    DB_PATH = "cs539-sp18.cwvtn5eogw8i.us-east-1.rds.amazonaws.com"
    DB_USER = "admin"
    DB_PORT = 3306
    DB_NAME = "cs539_dev"
    DB_PASS = "***cs539***"
    conn = pymysql.connect(DB_PATH, DB_USER, DB_PASS,DB_NAME)
    #conn = pymysql.connect(host='cs539-sp18.cwvtn5eogw8i.us-east-1.rds.amazonaws.com', port=3306, user='admin', passwd='***cs539***',db='cs539_dev')
    return conn



def db_close(conn):
    conn.close()

def db_check(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)

def db_select(sql, conn):
    cursor = conn.cursor()
    try:
    	cursor.execute(sql)
    	result = cursor.fetchall()
        # print result
        cursor.close()
    	return result
    except:
        cursor.close()
    	print "[ERROR]: CANNOT SELECT DATA"
        return False

def db_insert(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return True
    except:
        print "[ERROR]: CANNOT INSERT DATA"
        cursor.close()
        conn.rollback()
        return False

def db_update(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return True
    except:
        print "[ERROR]: CANNOT UPDATE DATA"
        cursor.close()
        conn.rollback()
        return False

def db_delete(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return True
    except:
        print "[ERROR]: CANNOT DELETE DATA"
        cursor.close()
        conn.rollback()
        return False

def check_acccount(conn, name):
    count = "select count(*) from Account_dev where account_name = '%s'" %(name)
    rec = db_select(count,conn)
    if(rec[0][0] == 1):
        return False
    else:
        return True
    return True

def db_account_customer_generater(conn,num):
    for i in range(num):
        number = i+1
        name = random_str(8)
        password = random_str(8)
        sql = "insert into Account_dev(account_no,account_pass,account_name) values(%s, '%s','%s')"%(number,name,password)
        db_insert(sql,conn)
        last_name = names.get_last_name()
        first_name = names.get_first_name()
        address_zipco = random_address_zipco()
        address = address_zipco[0]
        zipco = address_zipco[1]
        email = last_name + first_name + "@gmail.com"
        telephone = random_with_n_digits(10)
        account_date = "03/20/2018"
        sql2 = "insert into Customer_dev(account_no,last_name,fshowirst_name,address,email,telephone,account_date,zipco) values(%s,'%s','%s','%s','%s','%s','%s','%s')"%(number,last_name,first_name,address,email,telephone,account_date,zipco)
        db_insert(sql2,conn)

def create_customer(conn,name, password,last_name,first_name,zipco,address="",email="",telephone="",credit=""):
    count = "select max(account_no) from Account_dev"
    number_ = db_select(count,conn)[0][0]
    number = number_ + 1
    print number
    account_date = ""
    sql = ["insert into Account_dev(account_no,account_pass,account_name) values(%s, '%s','%s')"%(number,password,name),
           "insert into Customer_dev(account_no,last_name,first_name,address,email,telephone,account_date,zipco) values(%s,'%s','%s','%s','%s','%s','%s','%s')"%(number,last_name,first_name,address,email,telephone,account_date,zipco)]
    flag1 = db_insert(sql[0],conn)
    flag2 = db_insert(sql[1],conn)
    print flag1
    print flag2
    if(flag1 and flag2):
        return True
    else:
        return False
    # count = "select count(*) from Account_dev"
    # sql = "insert into Account_dev(account_no,account_pass,account_name) values(%s, '%s','%s')"%(number,name,password)
    # sql2 = "insert into Customer_dev(account_no,last_name,first_name,address,email,telephone,account_date,zipco) values(%s,'%s','%s','%s','%s','%s','%s','%s')"%(number,last_name,first_name,address,email,telephone,account_date,zipco)
def get_account_no(conn,account_name):
    sql = "select account_no from Account_dev where account_name = '%s'"%(account_name)
    rec = db_select(sql,conn)
    if(rec):
        return rec[0][0]
    else:
        return False

def get_account_name(conn,account_no):
    sql = "select account_name from Account_dev where account_no = '%s'"%(account_no)
    rec = db_select(sql,conn)
    if(rec):
        return rec[0][0]
    else:
        return False



def update_customer(conn,account_no,account_password,last_name,first_name,zipco,address="",email="",telephone="",credit="",prefer=""):
    sql = "update Customer_dev set last_name = '%s', first_name = '%s',address = '%s',email  = '%s',telephone = '%s', credit_catd_no  = '%s', preference  = '%s', zipco = '%s', account_date  = '%s' where account_no  = %s"%(last_name,first_name,address,email,telephone,credit,prefer,zipco,"3/18/2018",account_no)
    account_name = get_account_name(conn,account_no)
    flag = db_update(sql,conn)
    flag2 = update_password(conn,account_name,account_password)
    if(flag and flag2):
        return True
    else:
        return False

def update_password(conn,account_name,account_password):
    sql = "update Account_dev set account_pass = '%s' where account_name = '%s'"%(account_password,account_name)
    flag = db_update(sql,conn)
    if(flag):
        return True
    else:
        return False

def delete_customer(conn,account_no):
    sql = "delete from Account_dev where account_no = %s" %(account_no)
    flag = db_update(sql,conn)
    if(flag):
        return True
    else:
        return False

def show_customer(conn,account_no):
    sql = "select * from Customer_dev where account_no = %s" %(account_no)
    rec = db_select(sql,conn) #that is a tuple like this ((xxx,xx,xxx,xxx),(xxx,xxx,xx))
    # if(rec[0][5] == None):
    #      print ("no things")
    # else:
    #     print("there is some thing")
    if(rec):
        return rec
    else:
        return False

def show_password(conn,account_no):
    sql = "select * from Account_dev where account_no = %s" %(account_no)
    rec = db_select(sql,conn) #that is a tuple like this ((xxx,xx,xxx,xxx),(xxx,xxx,xx))
    if(rec):
        return rec
    else:
        return False

def signup(conn,name, password,last_name,first_name,zipco,address="",email="",telephone="",credit=""):
    flag = check_acccount(conn,name)
    if(flag):
        if(create_customer(conn,name, password,last_name,first_name,zipco,address,email,telephone,credit)):
            return True
        else:
            return False
    else:
        return False

def compare_data(date1):
    date_format = '%m/%d/%Y'
    date_formalized = datetime.strptime(date1, date_format)
    #print date_formalized.month

def get_airline_name(conn):
    sql = "SELECT DISTINCT airlineName FROM LegsInfo"
    rec = db_select(sql,conn)
    if(rec):
        return rec
    else:
        return False

def sales_report(conn,month = '3',year = '2018'):
    date = '%' + month + '/%/' + year 
    rec = []
    sql_1 = "SELECT airlineName, count(*) as numberflight FROM Reservation INNER JOIN Reservation_Leg ON Reservation.reservation_no = Reservation_Leg.reservation_no INNER JOIN LegsInfo ON Reservation_Leg.idLegs = LegsInfo.idLegs WHERE Reservation.date LIKE '%s' GROUP BY LegsInfo.airlineName"%(date)
    sql_2 = "SELECT airlineName, CAST(SUM(total_fare) AS DECIMAL(10,2)) as numberflight FROM Reservation INNER JOIN Reservation_Leg ON Reservation.reservation_no = Reservation_Leg.reservation_no INNER JOIN LegsInfo ON Reservation_Leg.idLegs = LegsInfo.idLegs WHERE Reservation.date LIKE '%s' GROUP BY LegsInfo.airlineName"%(date)
    _number_flight = db_select(sql_1,conn)
    _total_flight = db_select(sql_2,conn)
    if(_number_flight and _number_flight):
        for index in range(len(_number_flight)):
            if((_total_flight[index][1] == None) and (_number_flight[index][1] == 0)):
                rec.append(({'name':_total_flight[index][0],'# of flight': 0,'value':0}))
            else:
                rec.append(({'name':_total_flight[index][0],'# of flight': _number_flight[index][1],'value':float(_total_flight[index][1])}))
    else:
        return False
    return rec


def get_delay_flight_detail(conn,start,end):
    #sql = "SELECT *, If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs where CAST(delay AS SIGNED) > 0"
    cursor = conn.cursor()
    cursor.execute("SELECT count(*), If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%m/%d/%Y') DESC, TIME_FORMAT(departure_time, '%h:%i') DESC")
    count = cursor.fetchall()
    #sql = "SELECT count(*), If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%m/%d/%Y') DESC, TIME_FORMAT(departure_time, '%h:%i') DESC"
    cursor.close()

    cursor1 = conn.cursor()
    cursor1.callproc('sp_showDelay', [start, end])
    rec = cursor1.fetchall()
    #sql = "SELECT count(*), If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%m/%d/%Y') DESC, TIME_FORMAT(departure_time, '%h:%i') DESC"
    #sql2 = "SELECT *, If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%m/%d/%Y') DESC, TIME_FORMAT(departure_time, '%h:%i') DESC LIMIT '%s','%s' " %(start,end)
    cursor1.close()
    # count = db_select(sql,conn)
    # rec = db_select(sql2,conn)
    if(rec and count):
        return (count,rec)
    else:
        return False


def get_delay_flight(conn):

    sql = "SELECT *, If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%m/%d/%Y') DESC, TIME_FORMAT(departure_time, '%h:%i') DESC"
    #sql2 = "SELECT *, If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%m/%d/%Y') DESC, TIME_FORMAT(departure_time, '%h:%i') DESC LIMIT '%s','%s' " %(start,end)
    rec = db_select(sql,conn)
    if(rec):
        return rec
    else:
        return False


def test_delay(conn,start,end):
    # sql = "SELECT *, If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%m/%d/%Y') DESC, TIME_FORMAT(departure_time, '%h:%i') DESC"
    sql = "SELECT *, If( CAST(delay AS SIGNED)>0, 'Delayed','On Time') as isDelayed FROM HistoryLegs ORDER BY str_to_date(departure_date, '%%m/%%d/%%Y') DESC, TIME_FORMAT(departure_time, '%%h:%%i') DESC LIMIT %s,%s " %(start,end)
    print sql
    rec = db_select(sql,conn)
    if(rec):
        return rec
    else:
        return False

#sql= SELECT CAST(SUM(total_fare) AS DECIMAL(10,2)) as total FROM Reservation WHERE date LIKE '%3/%/%' AND reservation_no IN (SELECT reservation_no FROM Reservation_Leg WHERE idLegs IN  (SELECT idLegs FROM LegsInfo WHERE airlineName = 'Delta'))
#compare_data("3/18/2017")

# conn = db_conn()
# db_check(conn)
#db_account_customer_generater(conn,100)
#create_customer(conn,"kkk","kkk","xxx","mmm","123123","301 river road","mohanxiao94@gmail.com","7325003789","123123")
#update_password(conn,"kkk","aws")
#update_customer(conn,101,"ooo","ppp","111","111","111","111","111","111")
# tmp = check_acccount(conn,"FxeXPdjE")
# print tmp
#show_customer(conn,1)
# flag = signup(conn,"qqq","qqq","xxx","mmm","123123","301 river road","mohanxiao94@gmail.com","7325003789","123123")
# print flag


# cursor = conn.cursor()
# month = '3'
# year = '2018'
# date = '%' + month + '/%/' + year 
# sql = " SELECT CAST(SUM(total_fare) AS DECIMAL(10,2)) as total FROM Reservation WHERE date LIKE '%s' "%(date)
# cursor.execute(sql)
# result = cursor.fetchall()
# print result[0][0]
#print (sales_report(conn,'3','2018'))
# print ({"aaa":"qwe"})
#db_close(conn)
# _name = 'qqq'
# _password = 'qqq'
# sql = "SELECT account_pass from Account_dev where account_name = '%s'"%(_name)
# # sql = "SELECT account_no,account_name FROM Account_dev where account_name = '%s' and account_pass = '%s'"%(_name,_password)
# rec = db_select(sql,conn)
# print rec
# _name = 1
# sql2 = "select employ_no from Manage_dev where account_no = (select account_no from Account_dev where account_name = '%s')"%(_name)
# manage_Flag = db_select(sql2,conn)
# print manage_Flag
# if manage_Flag:
#     print "good"
# else:
#     print "bad"
# conn = db_conn()
# conn
# #rec = sales_report(conn)
# for i in range(10):
# date = '%' + '3' + '/%/' + '2018'
# sql_2 = "SELECT airlineName, CAST(SUM(total_fare) AS DECIMAL(10,2)) as numberflight FROM Reservation INNER JOIN Reservation_Leg ON Reservation.reservation_no = Reservation_Leg.reservation_no INNER JOIN LegsInfo ON Reservation_Leg.idLegs = LegsInfo.idLegs WHERE Reservation.date LIKE '%s' GROUP BY LegsInfo.airlineName"%(date)
# rec = db_select(sql_2,conn)
# print rec
# date = '%' + '3' + '/%/' + '2018'
# sql_1 = "SELECT airlineName, count(*) as numberflight FROM Reservation INNER JOIN Reservation_Leg ON Reservation.reservation_no = Reservation_Leg.reservation_no INNER JOIN LegsInfo ON Reservation_Leg.idLegs = LegsInfo.idLegs WHERE Reservation.date LIKE '%s' GROUP BY LegsInfo.airlineName"%(date)
# rec = sales_report(conn)
# print(rec)
# for i in range(1000):
#     print(i)
# _number_flight = db_select(sql_1,conn)
# for index in range(len(_number_flight)):
#     print index
# print _number_flight
#     rec = show_customer(conn,1)
#     print rec
# #print rec
# conn = db_conn()
# rec = test_delay(conn,0,10)
# print rec
# db_close(conn)

