from flask import Flask, render_template, json, request, jsonify
from flaskext.mysql import MySQL
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
        rec = user_db.signup(conn,_name,_password,_last_name,_first_name,_zipco,_address,_email,_telephone,_credit)
        if(rec):
            return jsonify({'issignup':True})
        else:
            return jsonify({'issignup':False})
    except Exception as e:
        return jsonify({'error':str(e)})


@application.route('/api/showuser',methods=['POST','GET'])
def showuser():
    conn = mysql.connect()
    try:
        _account_no = request.form['Account_no']
        # _account_no = 1
        rec = user_db.show_customer(conn,_account_no)
        dist = {}
        if(rec == False):
            return jsonify({'error':False})
        dist['Account_no'] = rec[0][0]
        dist['Last_name'] = rec[0][1]
        dist['First_name'] = rec[0][2]
        dist['Address'] = rec[0][3]
        dist['Preference'] = rec[0][5]
        dist['Email'] = rec[0][6]
        dist['Telephone'] = rec[0][8]
        dist['Account_date'] = rec[0][9]
        dist['Zipco'] = rec[0][10]
        dist['Credit'] = rec[0][11]
        return jsonify(dist)
    except Exception as e:
        return jsonify({'error':str(e)}) 


@application.route('/api/edituser',methods=['POST','GET'])
def edituser():
    conn = mysql.connect()
    try:
        _account_no = request.form['Account_no']
        _last_name = request.form['Last_name']
        _first_name = request.form['First_name']
        _zipco = request.form['Zipco']
        _address = request.form['Address']
        _email = request.form['Email']
        _telephone = request.form['Telephone']
        _credit = request.form['Credit']
        _prefer = request.form['Prefer']
        rec = user_db.update_customer(conn,_account_no,_last_name,_first_name,_zipco,_address,_email,_telephone,_credit,_prefer)
        if(rec):
            return jsonify({'isedituser':True})
        else:
            return jsonify({'isedituser':False})
    except Exception as e:
        return jsonify({'error':str(e)})

@application.route('/api/editpass',methods=['POST','GET'])
def editpass():
    conn = mysql.connect()
    try:
        _account_no = request.form['Account_no']
        _password = request.form['Changed_password']
        rec = user_db.update_password(conn,_account_no,_password)
        if(rec):
            return jsonify({'iseditpass':True})
        else:
            return jsonify({'iseditpass':False})
    except Exception as e:
        return jsonify({'error':str(e)})

@application.route('/api/delete',methods=['POST','GET'])
def delete():
    conn = mysql.connect()
    try:
        _account_no = request.form['Account_no']
        rec = user_db.delete_customer(conn,_account_no)
        if(rec):
            return jsonify({'isdelete':True})
        else:
            return jsonify({'isdelete':False})
    except Exception as e:
        return jsonify({'error':str(e)})



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



@application.route('/api/manager/getSalesReport',methods=['POST','GET'])
def get_sales_report():
    conn = mysql.connect()
    try:
        _month = request.form['Month']
        _year = request.form['Year']
        # _month = '3'
        # _year = '2018'
        rec = user_db.sales_report(conn,_month,_year)
        if(rec == False):
            return jsonify({'sales_report':False})
        else:
            return jsonify({'sales_report':rec})
    except Exception as e:
        return jsonify({'error':str(e)})

#finished
@application.route('/api/manager/listAllFlights',methods=['POST','GET'])
def list_all_flights():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
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
            res.append(dic)
    except Exception as e:
        res = ['Search Error']
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
        inputval = request.form["input"]
        typeval = request.form["type"]
        print inputval, typeval
        if typeval=="name":
            cursor.execute("SELECT DISTINCT reservation_no FROM Reservation_Leg WHERE name=%s", (inputval))
            for reservation_no in cursor.fetchall():

                cursor.execute("SELECT DISTINCT name, Reservation.date, total_fare, LegsInfo.idFlight, FlightInfoAll.departure, FlightInfoAll.arrival, Reservation_Leg.trip_no, Reservation.reservation_no FROM Reservation_Leg JOIN Reservation JOIN LegsInfo JOIN FlightInfoAll ON Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idLegs=LegsInfo.idLegs  AND LegsInfo.idFlight=FlightInfoAll.idFlightInfo WHERE name=%s AND Reservation.reservation_no=%s", (inputval, reservation_no[0]))

                dic = {}
                dic["reservation_no"] = reservation_no[0]
                dic["stops"] = {"go":[],"back":[]}
                for data in cursor.fetchall():
                    dic["passenger_info"] = [data[0]]
                    dic["date"] = data[1]
                    dic["isCurrent"] = isDateFuture(data[1])
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
            cursor.execute("SELECT idLegs FROM LegsInfo WHERE flight_no=%s", (inputval))
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
        res = ['Search Error']
    finally:
        cursor.close()
        conn.close()

    return jsonify(res)

#finished
@application.route('/api/manager/getRevList',methods=['POST','GET'])
def get_rev_list():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
    try:
        flight_no = request.form["flight"]
        city = request.form["city"]
        customer = request.form['customer']
        id = request.form["groupby"]
        print id

        dic = {}
        dic["flight"] = ''
        dic["city"] = ''
        dic['customer'] = ''
        dic['mostCustomerRev'] = {}
        if id=='flight':
            cursor.execute("SELECT SUM(booking_fee) FROM Reservation, Reservation_Leg WHERE Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idLegs in (SELECT idLegs From LegsInfo WHERE flight_no=%s);", (flight_no))
            dic["flight"] = flight_no

        elif id=='city':
            cursor.execute("SELECT SUM(booking_fee) FROM Reservation, Reservation_Leg, FlightInfoAll WHERE Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idFlight=FlightInfoAll.idFlightInfo AND arrival LIKE %s ", ('%'+city))
            dic["city"] = city
        else:
            cursor.execute("SELECT SUM(booking_fee) FROM Reservation, Reservation_Leg WHERE Reservation.reservation_no=Reservation_Leg.reservation_no AND name=%s;", (customer))
            dic["customer"] = customer
            most_customer_rev = get_most_rev()
            dic["mostCustomerRev"] = most_customer_rev[0]

        revenue = cursor.fetchone()[0]
        dic['revenue'] = revenue if revenue else 0

        res.append(dic)
    except Exception as e:
        print e
        res = ["Search Error"]
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)

#finished
def get_most_rev():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
    try:
        cursor.execute("SELECT Reservation.account_no, first_name, last_name, SUM(total_fare) as total FROM Reservation, Customer_dev WHERE Reservation.account_no=Customer_dev.account_no GROUP BY account_no ORDER BY total DESC")
        for data in cursor.fetchmany(30):
            dic = {}
            dic["account_no"] = data[0]
            dic["first_name"] = data[1]
            dic["last_name"] = data[2]
            dic["revenue"] = data[3]
            res.append(dic)
    except Exception as e:
        print e
        res = ["Search Error"]
    finally:
        cursor.close()
        conn.close()
    return res

#finished
@application.route('/api/manager/mostActiveFlight',methods=['POST','GET'])
def most_active_flight():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
    try:
        cursor.execute("SELECT flight_no, COUNT(*) as num, airlineCode FROM LegsInfo, Reservation_Leg WHERE LegsInfo.idLegs=Reservation_Leg.idLegs GROUP BY flight_no ORDER BY num DESC")
        for data in cursor.fetchall():
            dic = {}
            dic["flight_no"] = data[0]
            dic["active_number"] = data[1]
            dic["airlineCode"] = data[2]
            res.append(dic)
    except Exception as e:
        print e
        res = ["Search Error"]
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)

#finished
@application.route('/api/manager/listForAirport',methods=['POST','GET'])
def list_for_airports():

    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
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
            res.append(dic)

    except Exception as e:
        print e
        res = ['Search Error']
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)

#finished
@application.route('/api/manager/customerSeated',methods=['POST','GET'])
def get_customer_seated():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
    try:
        flight_no = request.form["flight"]
        cursor.execute("SELECT name FROM Reservation_Leg WHERE idLegs IN (SELECT idLegs FROM LegsInfo WHERE flight_no=%s) AND seat_no!=''", (flight_no))
        dic = {}
        dic["flight_no"] = flight_no
        dic["passengers"] = []
        for data in cursor.fetchall():
            dic["passengers"].append(data[0])
        res.append(dic)
    except Exception as e:
        print e
        res = ["Search Error"]
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)

# Customer booking APIs
@application.route('/api/customer/bookFlight',methods=['POST','GET'])
def book_flight():
    return ""

@application.route('/api/customer/searchFlight',methods=['POST','GET'])
def searchFlight():
    conn = mysql.connect()
    cursor = conn.cursor()
    res_final_list = []
    # try:
    _dep = request.form['departure']
    _arr = request.form['arrival']
    _roundtrip = request.form['roundtrip']
    _date1 = model.get_db_date(request.form['date1'])
    print _date1
    _date2 = None
    if(_roundtrip == 1):
        _date2 = model.get_db_date(request.form['date2'])
    dep = [_dep,_arr]
    arr = [_arr,_dep]
    dates = [_date1,_date2]
    loop = 1
    if(_roundtrip == 1):
        loop = 2
    for i in range(loop):
        ii = 0
        flight_id = []
        flight_dict = {}
        res_list = []
        loop_dep = dep[i]
        loop_arr = arr[i]
        loop_date = dates[i]

        res_tmp = []
        cursor.execute("SELECT idFlightInfo,departure,arrival,duration,nextDayArrival,stops,price, total_distance FROM  cs539_dev.FlightInfoAll where SUBSTRING(FlightInfoAll.departure, 1, 3) = %s and SUBSTRING(FlightInfoAll.arrival,  1, 3) = %s ;", [loop_dep, loop_arr] )
        for data in cursor.fetchall():
            if(data):
                flight_id.append(data[0])
                flight_dict[data[0]] = ii
                res_list.append({})
                res_list[flight_dict[data[0]]]['flight_id'] = data[0]
                res_list[flight_dict[data[0]]]['departure'] = data[1]
                res_list[flight_dict[data[0]]]['arrival'] = data[2]
                res_list[flight_dict[data[0]]]['duration'] = data[3]
                res_list[flight_dict[data[0]]]['next_day_arr'] = data[4]
                res_list[flight_dict[data[0]]]['stops'] = data[5]
                res_list[flight_dict[data[0]]]['price'] = model.get_fair(data[6],_date1)
                res_list[flight_dict[data[0]]]['total_distance'] = data[7]
                res_list[flight_dict[data[0]]]['stops'] = []
                ii+=1

        for fid in flight_id:
            cursor.execute('SELECT  idFlight,idLegs,distance,duration,departure_airport,departure_time,arrival_airport,arrival_time,flight_no,airlineName,airlineCode from cs539_dev.LegsInfo where idFlight = %s and departure_date = %s ;',[fid,loop_date])
            stop = 1
            for data in cursor.fetchall():
                if(data):
                    dict = {}
                    dict['stop'] = stop
                    dict['duration'] = data[3]
                    dict['departure_airport'] = data[4]
                    dict['departure_time'] = data[5]
                    dict['arrival_airport'] = data[6]
                    dict['arrival_time'] = data[7]
                    dict['flight_no'] = data[8]
                    dict['airlineName'] = data[9]
                    dict['airlineCode'] = data[10]
                    dict['distance'] = data[2]
                    res_list[flight_dict[data[0]]]['stops'].append(dict)
                    stop += 1
        for fid in flight_id:
            if(len(res_list[flight_dict[fid]]['stops']) < 1):
                res_list[flight_dict[fid]] = None
        res_final_list.append(res_list)
# except Exception as e:
#     print e
#     res['error'] = 'Search Error'
# finally:
    cursor.close()
    conn.close()
    return jsonify(res_final_list)

    # return ""

# Finished
# Get Reservation by account_no
@application.route('/api/customer/getReserv',methods=['POST','GET'])
def get_reserv():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = {}
    res_list = []
    try:
        account_no = request.form['account_no']
        cursor.execute('SELECT DISTINCT name,ssn,Reservation.reservation_no, FlightInfoAll.departure, FlightInfoAll.arrival FROM Reservation_Leg JOIN Reservation JOIN LegsInfo JOIN FlightInfoAll ON Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idLegs=LegsInfo.idLegs AND LegsInfo.idFlight=FlightInfoAll.idFlightInfo WHERE Reservation.account_no= %s;',[account_no])
        # res_no = []
        res_dict = {}

        i = 0;
        for data in cursor.fetchall():
            if(data):
                if(data[2] not in res_dict.keys()):
                    res_list.append({})
                    res_dict[data[2]] = i
                    res_list[res_dict[data[2]]]['id'] = data[2]
                    res_list[res_dict[data[2]]]['passenger_info'] = []
                    res_list[res_dict[data[2]]]['stops'] = {}
                    res_list[res_dict[data[2]]]['stops']['go'] = []
                    res_list[res_dict[data[2]]]['stops']['back'] = []
                    res_list[res_dict[data[2]]]['RoundTrip'] = "One Way"
                    i+=1

                res_list[res_dict[data[2]]]['Departure'] = data[3]
                res_list[res_dict[data[2]]]['Arrival'] = data[4]
                temp = {}
                temp['name'] = data[0]
                temp['ssn'] = data[1]
                res_list[res_dict[data[2]]]["passenger_info"].append(temp)

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
                j = res_dict[data[13]]
                if(isDateFuture(data[12])):
                    res_list[j]['isFuture']= True
                else:
                    res_list[j]['isFuture']= False
                res_list[j]['price']= data[8]
                if(data[9]==1):
                    res_list[j]['stops']['go'].append(dict)
                else:
                    res_list[j]['stops']['back'].append(dict)
                    res_list[j]['RoundTrip'] = "RoundTrip"
    except Exception as e:
        res['error'] = 'Search Error'
    finally:
        cursor.close()
        conn.close()
        return jsonify(res_list)

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
# @application.route('/api/searchFlight',methods=['POST','GET'])
# def search_flight():
#     roundtrip = False
#     if(request.form['roundtrip']==True){
#         roundtrip = True
#     }
#     date = []
#     date.append()
#
#     return ""

if __name__ == "__main__":
    application.run(host='172.31.221.55',debug=True,)
