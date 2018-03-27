from flask import Flask, render_template, json, request, jsonify
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import safe_str_cmp
from model import isDateFuture
from datetime import datetime
import model
import user_db
mysql = MySQL()
application = Flask(__name__)

# MySQL configurations
application.config['MYSQL_DATABASE_USER'] = 'admin'
application.config['MYSQL_DATABASE_PASSWORD'] = '***cs539***'
application.config['MYSQL_DATABASE_DB'] = 'cs539_dev'
application.config['MYSQL_DATABASE_HOST'] = 'cs539-sp18.cwvtn5eogw8i.us-east-1.rds.amazonaws.com'
mysql.init_app(application)



def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username


header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))



@application.route('/',methods=['POST','GET'])
def home():
    return "hello"

# sign up new user
@application.route('/api/signUp',methods=['POST','GET'])
def signUp():
    # conn = mysql.connect()
    # cursor = conn.cursor()
    # res = {}
    # try:
    #     _name = request.form['Name']
    #     _password = request.form['Password']
    #     if _name and _password:
    #         _hashed_password = generate_password_hash(_password)
    #         cursor.callproc('sp_createUser',(_name,_hashed_password))
    #         data = cursor.fetchall()
    #         if len(data) is 0:
    #             conn.commit()
    #             res['success'] = True
    #             res['exist'] = False
    #             return jsonify(res)
    #         else:
    #             ## user name exist
    #             return jsonify({'error':str(data[0])})
    #     else:
    #         return jsonify({'html':'<span>Enter the required fields</span>'})
    # except Exception as e:
    #     return jsonify({'error':str(e)})
    # finally:
    #     cursor.close()
    #     conn.close()
    conn = mysql.connect()
    try:
        _name = request.form['Name']
        _password = request.form['Password']
        _last_name = request.form['Last_name']
        _first_name = request.form['First_name']
        _zipco = request.form['Zipco']
        _address = request.form['Address']
        _email = request.form['Email']
        _telephone = request.form['Telephone']
        _credit = request.form['Credit']
        rec = user_db.signup(conn,,_name,_password,_last_name,_first_name,_zipco,_address,_email,_telephone,_credit)
        if(rec):
            return jsonify({'issignup':True})
        else:
            return jsonify({'issignup':False})
    except Exception as e:
        return jsonify({'error':str(e)})


# @application.route('/api/showuser',methods=['POST','GET'])
# def showuser():
    





# sign up new user
@application.route('/api/isUser',methods=['POST','GET'])
def verifyUser():
    conn = mysql.connect()
    cursor = conn.cursor()
    res={}
    try:
        _name = request.form['Name']
        _password = request.form['Password']
        if _name and _password:
            _hashed_password = generate_password_hash(_password)
            cursor.execute('SELECT password from Account where name = %s;',[_name])
            for data in cursor.fetchall():
                if data and check_password_hash(data[0],_password):
                    conn.commit()
                    # is a valid user with name and password
                    res['validUser'] = True
                    cursor.callproc('sp_isManager',(_name,_hashed_password))
                    data = cursor.fetchall()
                    if len(data) is 0:
                        conn.commit()
                        res['isManager'] = True
                    else:
                        res['isManager'] = False
                else:
                    res['validUser'] = False
                    res['isManager'] = False
        else:
            res['validUser'] = False
            res['isManager'] = False
    except Exception as e:
        res['validUser'] = False
        res['isManager'] = False
    finally:
        cursor.close()
        conn.close()
        return jsonify(res)




@application.route('/api/manager/editUser',methods=['POST','GET'])
def edit_user():
    return ""

@application.route('/api/manager/getSalesReport',methods=['POST','GET'])
def get_sales_report():
    return ""

@application.route('/api/manager/listAllFlights',methods=['POST','GET'])
def list_all_flights():
<<<<<<< HEAD
    return ""
=======
    conn = mysql.connect()
    cursor = conn.cursor()
    res = {}
    id = 1
    try:
        cursor.execute("SELECT flight_no, departure_airport, arrival_airport, departure_time, arrival_time, duration, airlineCode FROM LegsInfo GROUP BY flight_no")
        for data in cursor.fetchall():
            dic = {}
            dic["flight_no"] = data[0]
            dic["departure_airport"] = data[1]
            dic["arrival_airport"] = data[2]
            dic["departure_time"] = data[3]
            dic["arrival_time"] = data[4]
            dic["duration"] = data[5]
            dic["airlineCode"] = data[6]
            res[id] = dic
            id += 1
    except Exception as e:
        res["error"] = 'Search Error'
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)
>>>>>>> f83738b3bb133478f0018e244064d0c40f1341a4

@application.route('/api/manager/listReservation',methods=['POST','GET'])
def list_reservation():
    return ""

@application.route('/api/manager/getRevList',methods=['POST','GET'])
def get_rev_list():
    return ""

@application.route('/api/manager/mostCustomerRev',methods=['POST','GET'])
def get_most_rev():
    return ""

@application.route('/api/manager/mostActiveFlight',methods=['POST','GET'])
def most_active_flight():
    return ""

@application.route('/api/manager/listForAirport',methods=['POST','GET'])
def list_for_airports():
<<<<<<< HEAD
    return ""
=======
    conn = mysql.connect()
    cursor = conn.cursor()
    res = {}
    weekdaydic = {0:'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}
    try:
        airport = request.form["airportCode"]
        cursor.execute("SELECT flight_no, departure_airport, departure_time, departure_date, arrival_airport, arrival_time, arrival_date, airlineName, duration, distance, plane FROM HistoryLegs WHERE departure_airport=%s", (airport))
        id = 1
        for data in cursor.fetchall():
            dic = {}
            date_format = '%m/%d/%Y'
            dic["flight_no"] = data[0]
            dic["departure_airport"] = data[1]
            dic["departure_time"] = data[2]
            dic["departure_weekday"] = weekdaydic[datetime.strptime(data[3],date_format).weekday()]
            dic["arrival_airport"] = data[4]
            dic["arrival_time"] = data[5]
            dic["arrival_weekday"] = weekdaydic[datetime.strptime(data[6],date_format).weekday()]
            dic["airlineName"] = data[7]
            dic["duration"] = data[8]
            dic["distance"] = data[9]
            dic["plane"] = data[10]
            res[id] = dic
            id += 1

    except Exception as e:
        res['error'] = 'Search Error'
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)
>>>>>>> f83738b3bb133478f0018e244064d0c40f1341a4

# Customer booking APIs
@application.route('/api/customer/bookFlight',methods=['POST','GET'])
def book_flight():
    return ""



# Finished
# Get Reservation by account_no
@application.route('/api/customer/getReserv',methods=['POST','GET'])
def get_reserv():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = {}
    try:
        account_no = request.form['account_no']
        cursor.execute('SELECT DISTINCT name,ssn,Reservation.reservation_no, FlightInfoAll.departure, FlightInfoAll.arrival FROM Reservation_Leg JOIN Reservation JOIN LegsInfo JOIN FlightInfoAll ON Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idLegs=LegsInfo.idLegs AND LegsInfo.idFlight=FlightInfoAll.idFlightInfo WHERE Reservation.account_no= %s;',[account_no])
        res_no = []
        for data in cursor.fetchall():
            if(data):
                if(data[2] not in res.keys()):
                    res_no.append(data[2])
                    res[data[2]] = {}
                    res[data[2]]['passenger_info'] = []
                    res[data[2]]['stops'] = {}
                    res[data[2]]['stops']['go'] = []
                    res[data[2]]['stops']['back'] = []
                res[data[2]]['Departure'] = data[3]
                res[data[2]]['Arrival'] = data[4]
                temp = {}
                temp['name'] = data[0]
                temp['ssn'] = data[1]
                res[data[2]]["passenger_info"].append(temp)
        cursor.execute('SELECT distinct departure_airport,arrival_airport,departure_time,arrival_time,flight_no, airlineCode, airlineName, booking_fee, total_fare, trip_no, duration ,distance, date, reservation_no   from Reservation natural join Reservation_Leg natural join LegsInfo where account_no = %s;',[account_no])
        for data in cursor.fetchall():
                dict = {}
                dict['departure_airport'] = data[0]
                dict['arrival_airport'] = data[1]
                dict['departure_time'] = data[2]
                dict['arrival_time'] = data[3]
                dict['flight_no'] = data[4]
                dict['airlineCode'] = data[5]
                dict['airlineName'] = data[6]
                dict['booking_fee'] = data[7]
                dict['total_fare'] = data[8]
                res[data[13]]['price']= data[8]
                # dict['trip_no'] = data[9]
                dict['duration'] = data[10]
                dict['distance'] = data[11]
                dict['date'] = data[12]
                if(data[9]==1):
                    res[data[13]]['stops']['go'].append(dict)
                else:
                    res[data[13]]['stops']['back'].append(dict)
    except Exception as e:
        res['error'] = 'Search Error'
    finally:
        cursor.close()
        conn.close()
        return jsonify(res)

# Finished
# Get Travel Initary
# @application.route('/api/customer/getTravelInit',methods=['POST','GET'])
# def get_init():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     res = {}
#     count = 1
#     try:
#         reservation_no = request.form['reservation_no']
#         cursor.execute('SELECT departure_airport,arrival_airport,departure_time,arrival_time,flight_no, airlineCode, airlineName, booking_fee, total_fare, class, seat_no, trip_no, duration ,distance, date, reservation_no  from Reservation natural join Reservation_Leg natural join LegsInfo where reservation_no = %s;',[reservation_no])
#         for data in cursor.fetchall():
#             if(data):
#                 res[count] = []
#                 dict = {}
#                 dict['departure_airport'] = data[0]
#                 dict['arrival_airport'] = data[1]
#                 dict['departure_time'] = data[2]
#                 dict['arrival_time'] = data[3]
#                 dict['flight_no'] = data[4]
#                 dict['airlineCode'] = data[5]
#                 dict['airlineName'] = data[6]
#                 dict['booking_fee'] = data[7]
#                 dict['total_fare'] = data[8]
#                 dict['class'] = data[9]
#                 dict['seat_no'] = data[10]
#                 dict['trip_no'] = data[11]
#                 dict['duration'] = data[12]
#                 dict['distance'] = data[13]
#                 dict['date'] = data[14]
#                 res[count].append(dict)
#                 count = count + 1
#     except Exception as e:
#         res['error'] = 'Search Error'
#     finally:
#         cursor.close()
#         conn.close()
#         return jsonify(res)

@application.route('/api/customer/getHistory',methods=['POST','GET'])
def get_history():
    return ""

@application.route('/api/customer/getBestSeller',methods=['POST','GET'])
def get_best_seller():
    return ""

#
# Customer booking APIs
@application.route('/api/searchFlight',methods=['POST','GET'])
def search_flight():
    roundtrip = False
    if(request.form['roundtrip']==True){
        roundtrip = True
    }
    date = []
    date.append()

    return ""

if __name__ == "__main__":
    application.debug = True
    application.run()
