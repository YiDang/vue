from flask import Flask, render_template, json, request, jsonify
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import safe_str_cmp
from model import isDateFuture
from datetime import datetime
import pdb
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
    conn = mysql.connect()
    cursor = conn.cursor()
    res = {}
    try:
        _name = request.form['Name']
        _password = request.form['Password']
        if _name and _password:
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_hashed_password))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                res['success'] = True
                res['exist'] = False
                return jsonify(res)
            else:
                ## user name exist
                return jsonify({'error':str(data[0])})
        else:
            return jsonify({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        return jsonify({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

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

#finished
@application.route('/api/manager/listAllFlights',methods=['POST','GET'])
def list_all_flights():
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

#finished
@application.route('/api/manager/listReservation',methods=['POST','GET'])
def list_reservation():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
    try:
        name = request.form["username"]
        flight_no = request.form["flight_no"]
        if name:
            cursor.execute("SELECT DISTINCT reservation_no FROM Reservation_Leg WHERE name=%s", (name))
            for reservation_no in cursor.fetchall():

                cursor.execute("SELECT DISTINCT name, Reservation.date, total_fare, LegsInfo.idFlight, FlightInfoAll.departure, FlightInfoAll.arrival, Reservation_Leg.trip_no, Reservation.reservation_no FROM Reservation_Leg JOIN Reservation JOIN LegsInfo JOIN FlightInfoAll ON Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idLegs=LegsInfo.idLegs  AND LegsInfo.idFlight=FlightInfoAll.idFlightInfo WHERE name=%s AND Reservation.reservation_no=%s", (name, reservation_no[0]))

                dic = {}
                dic["reservation_no"] = reservation_no[0]
                dic["stops"] = {"go":[],"back":[]} 
                for data in cursor.fetchall():
                    dic["passenger_info"] = [data[0]]
                    dic["date"] = data[1]
                    dic["price"] = data[2]
                    trip_no = data[6]
                    idFlight = data[3]
                    if trip_no==1:
                        dic["departure"] = data[4]
                        dic["arrival"] = data[5]
                    reservation_no = data[7]
                    dic["isCurrent"] = isDateFuture(data[1])

                    cursor.execute("SELECT * FROM LegsInfo WHERE idFlight=%s", (idFlight))
                    for legdata in cursor.fetchall():
                        legInfo = {}
                        legInfo["departure_airport"] = legdata[4]
                        legInfo["departure_time"] = legdata[5]
                        legInfo["arrival_airport"] = legdata[7]
                        legInfo["arrival_time"] = legdata[8]
                        if trip_no==1:
                            dic["stops"]["go"].append(legInfo)
                        else:
                            dic["stops"]["back"].append(legInfo)

                res.append(dic)
        else:
            cursor.execute("SELECT idLegs FROM LegsInfo WHERE flight_no=%s", (flight_no))
            LegsId = []
            for data in cursor.fetchall():
                LegsId.append(data[0])

            for idLegs in LegsId:
                reservation_no_set = set()
                cursor.execute("SELECT Reservation.reservation_no, name, Reservation.date, Reservation.total_fare, trip_no, LegsInfo.departure_airport, LegsInfo.arrival_airport, LegsInfo.departure_time, LegsInfo.arrival_time FROM Reservation_Leg, Reservation, LegsInfo WHERE Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idLegs=LegsInfo.idLegs AND LegsInfo.idLegs=%s", (idLegs))

                for record in cursor.fetchall():
                    reservation_no = record[0]
                    if reservation_no in reservation_no_set:
                        res[-1]["passenger_info"].append(record[1])
                    else:
                        dic = {}
                        dic["stops"] = {"go":[],"back":[]}
                        dic["reservation_no"] = record[0]
                        dic["passenger_info"] = [record[1]]
                        reservation_no_set.add(reservation_no)
                        dic["date"] = record[2]
                        dic["price"] = record[3]
                        trip_no = record[4]
                        dic["departure"] = record[5]
                        dic["arrival"] = record[6]
                        leg = {}
                        leg["departure_time"] = record[7]
                        leg["arrival_time"] = record[8]
                        leg["departure_airport"] = record[5]
                        leg["arrival_airport"] = record[6]
                        if trip_no==1:
                            dic["stops"]["go"].append(leg)
                        else:
                            dic["stops"]["back"].append(leg)
                        res.append(dic)

    except Exception as e:
        print e
        res["error"] = 'Search Error'
    finally:
        cursor.close()
        conn.close()

    return jsonify(res)

@application.route('/api/manager/getRevList',methods=['POST','GET'])
def get_rev_list():
    return ""

@application.route('/api/manager/mostCustomerRev',methods=['POST','GET'])
def get_most_rev():
    return ""

@application.route('/api/manager/mostActiveFlight',methods=['POST','GET'])
def most_active_flight():
    return ""

#finished
@application.route('/api/manager/listForAirport',methods=['POST','GET'])
def list_for_airports():
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
        cursor.execute('SELECT Distinct name,ssn,reservation_no from Reservation natural join Reservation_Leg natural join LegsInfo where account_no = %s;',[account_no])
        res["passenger_info"] = []

        for data in cursor.fetchall():
            if(data[2] not in res.keys()):
                res[data[2]] = {}
                res[data[2]]['passenger_info'] = []
                res[data[2]]['stops'] = {}
                res[data[2]]['stops']['go'] = []
                res[data[2]]['stops']['back'] = []
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
    return ""



if __name__ == "__main__":
    application.debug = True
    application.run()
