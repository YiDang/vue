import random, string
import pymysql
import names
from faker import Faker


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
    	return result
    except:
    	print "[ERROR]: CANNOT SELECT DATA"
        return False

def db_insert(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        print "[ERROR]: CANNOT INSERT DATA"
        conn.rollback()
        return False

def db_update(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        print "[ERROR]: CANNOT UPDATE DATA"
        conn.rollback()
        return False

def db_delete(sql, conn):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        print "[ERROR]: CANNOT DELETE DATA"
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
        sql2 = "insert into Customer_dev(account_no,last_name,first_name,address,email,telephone,account_date,zipco) values(%s,'%s','%s','%s','%s','%s','%s','%s')"%(number,last_name,first_name,address,email,telephone,account_date,zipco)
        db_insert(sql2,conn)

def create_customer(conn,name, password,last_name,first_name,zipco,address="",email="",telephone="",credit=""):
    count = "select count(*) from Account_dev"
    number_ = db_select(count,conn)[0][0]
    number = number_ + 1
    account_date = ""
    sql = ["insert into Account_dev(account_no,account_pass,account_name) values(%s, '%s','%s')"%(number,name,password),
           "insert into Customer_dev(account_no,last_name,first_name,address,email,telephone,account_date,zipco) values(%s,'%s','%s','%s','%s','%s','%s','%s')"%(number,last_name,first_name,address,email,telephone,account_date,zipco)]
    flag1 = db_insert(sql[0],conn)
    flag2 = db_insert(sql[1],conn)
    if(flag1 and flag2):
        return True
    else:
        return False
    # count = "select count(*) from Account_dev"
    # sql = "insert into Account_dev(account_no,account_pass,account_name) values(%s, '%s','%s')"%(number,name,password)
    # sql2 = "insert into Customer_dev(account_no,last_name,first_name,address,email,telephone,account_date,zipco) values(%s,'%s','%s','%s','%s','%s','%s','%s')"%(number,last_name,first_name,address,email,telephone,account_date,zipco)

def update_customer(conn,account_no,last_name,first_name,zipco,address="",email="",telephone="",credit="",prefer=""):
    sql = "update Customer_dev set last_name = '%s', first_name = '%s',address = '%s',email  = '%s',telephone = '%s', credit_catd_no  = '%s', preference  = '%s', zipco = '%s', account_date  = '%s' where account_no  = %s"%(last_name,first_name,address,email,telephone,credit,prefer,zipco,"3/18/2018",account_no)
    flag = db_update(sql,conn)
    if(flag):
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

def signup(conn,name, password,last_name,first_name,zipco,address="",email="",telephone="",credit=""):
    flag = check_acccount(conn,name)
    if(flag):
        if(create_customer(conn,name, password,last_name,first_name,zipco,address,email,telephone,credit)):
            return True
        else:
            return False
    else:
        return False


conn = db_conn()
db_check(conn)
#db_account_customer_generater(conn,100)
#create_customer(conn,"kkk","kkk","xxx","mmm","123123","301 river road","mohanxiao94@gmail.com","7325003789","123123")
#update_password(conn,"kkk","aws")
#update_customer(conn,101,"ooo","ppp","111","111","111","111","111","111")
# tmp = check_acccount(conn,"FxeXPdjE")
# print tmp
#show_customer(conn,1)
# flag = signup(conn,"qqq","qqq","xxx","mmm","123123","301 river road","mohanxiao94@gmail.com","7325003789","123123")
# print flag
db_close(conn)
