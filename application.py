from flask import Flask, render_template, json, request, jsonify
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import safe_str_cmp
from model import isDateFuture
from datetime import datetime
import model
import user_db
import ast
import test
mysql = MySQL()
application = Flask(__name__,
            static_folder = "./flight/dist/static",
            template_folder = "./flight/dist")

@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


# MySQL configurations
application.config['MYSQL_DATABASE_USER'] = 'admin'
application.config['MYSQL_DATABASE_PASSWORD'] = '***cs539***'
application.config['MYSQL_DATABASE_DB'] = 'cs539_dev'
application.config['MYSQL_DATABASE_HOST'] = 'cs539-sp18.cwvtn5eogw8i.us-east-1.rds.amazonaws.com'
mysql.init_app(application)

# @application.route('/',defaults={'path':''})
# @application.route('/<path:path>')
# def cath_all(path):
#     return render_template("index.html")

# sign up new user
@application.route('/api/signUp',methods=['POST','GET'])
def signUp():
    conn = mysql.connect()
    try:
        _id = request.form['id']
        _password = request.form['password']
        _last_name = request.form['lastName']
        _first_name = request.form['firstName']
        _zipco = request.form['zipCode']
        _address = request.form['address']
        _email = request.form['email']
        _telephone = request.form['telephone']
        _credit = request.form['credit']
        print request.form
        rec = user_db.signup(conn,_id,_password,_last_name,_first_name,_zipco,_address,_email,_telephone,_credit)
        if(rec):
            return jsonify({'isSignUp':True})
        else:
            return jsonify({'isSignUp':False})
    except Exception as e:
        return jsonify({'error':str(e)})

@application.route('/api/showuser',methods=['POST','GET'])
def showuser():
    conn = mysql.connect()
    try:
        _account_name = request.form['id']
        print _account_name
        _account_no = user_db.get_account_no(conn,_account_name)
        account_info =  user_db.show_password(conn,_account_no)
        rec = user_db.show_customer(conn,_account_no)
        print _account_no
        dist = {}
        if(rec == False):
            return jsonify({'error':False})
        dist['id'] =account_info[0][2]
        dist['no'] = rec[0][0]
        dist['password'] =account_info[0][1]
        dist['lastName'] = rec[0][1]
        dist['firstName'] = rec[0][2]
        dist['address'] = rec[0][3]
        dist['preference'] = rec[0][5]
        dist['email'] = rec[0][6]
        dist['telephone'] = rec[0][8]
        dist['account_date'] = rec[0][9]
        dist['zipCode'] = rec[0][10]
        dist['credit'] = rec[0][11]
        return jsonify(dist)
    except Exception as e:
        return jsonify({'error':str(e)})

@application.route('/api/edituser',methods=['POST','GET'])
def edituser():
    conn = mysql.connect()
    try:
        _account_no = request.form['no']
        _account_password = request.form['password']
        _last_name = request.form['lastName']
        _first_name = request.form['firstName']
        _zipco = request.form['zipCode']
        _address = request.form['address']
        _email = request.form['email']
        _telephone = request.form['telephone']
        _credit = request.form['credit']
        _prefer = request.form['preference']
        rec = user_db.update_customer(conn,_account_no,_account_password,_last_name,_first_name,_zipco,_address,_email,_telephone,_credit,_prefer)
        if(rec):
            return jsonify({'isedituser':'Success'})
        else:
            return jsonify({'isedituser':'Fail to edit'})
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
        _account_name = request.form['id']
        _account_no = user_db.get_account_no(conn,_account_name)
        if(_account_name == False):
            return jsonify({'Delete false':False})
        rec = user_db.delete_customer(conn,_account_no)
        if(rec):
            return jsonify({'Successful Delete':True})
        else:
            return jsonify({'Delete false':False})
    except Exception as e:
        return jsonify({'error':str(e)})

# sign up new user
@application.route('/api/isUser',methods=['POST','GET'])
def verifyUser():
    conn = mysql.connect()
    cursor = conn.cursor()
    res={}
    try:
        _name = request.form['id']
        _password = request.form['password']
        if _name and _password:
            sql = "SELECT account_pass from Account_dev where account_name = '%s'"%(_name)
            data = user_db.db_select(sql,conn)
            if (data[0][0] == _password):
                res['validUser'] = True
                sql2 = "select employ_no from Manage_dev where account_no = (select account_no from Account_dev where account_name = '%s')"%(_name)
                manage_Flag = user_db.db_select(sql2,conn)
                if manage_Flag:
                    res['isManager'] = True
                else:
                    res['isManager'] = False
            else:
                res['validUser'] = False
                res['isManager'] = False
            sql = "SELECT account_no,account_name FROM Account_dev where account_name = '%s' and account_pass = '%s'"%(_name,_password)
            rec = user_db.db_select(sql,conn)
            res['no'] = rec[0][0]
            res['id'] = rec[0][1]
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
        _month = request.form['month']
        _year = request.form['year']
        # print _month
        # print _year
        rec = user_db.sales_report(conn,_month,_year)
        # print rec
        if(rec == False):
            return jsonify({'sales_report':False})
        else:
            return jsonify(rec)
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
                dic = {}
                dic["passenger_info"] = []

                cursor.execute("SELECT DISTINCT name, Reservation.date, total_fare, LegsInfo.idFlight, FlightInfoAll.departure, FlightInfoAll.arrival, Reservation_Leg.trip_no, Reservation.reservation_no FROM Reservation_Leg JOIN Reservation JOIN LegsInfo JOIN FlightInfoAll ON Reservation.reservation_no=Reservation_Leg.reservation_no AND Reservation_Leg.idLegs=LegsInfo.idLegs  AND LegsInfo.idFlight=FlightInfoAll.idFlightInfo WHERE name=%s AND Reservation.reservation_no=%s", (inputval, reservation_no[0]))

                dic["reservation_no"] = reservation_no[0]
                dic["stops"] = {"go":[],"back":[]}
                for data in cursor.fetchall():
                    dic["passenger_info"].append({"name":data[0]})
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
                        res[-1]["passenger_info"].append({"name":record[1]})
                    else:
                        dic = {}
                        dic["stops"] = {"go":[],"back":[]}
                        dic["reservation_no"] = record[0]
                        dic["passenger_info"] = []
                        dic["passenger_info"].append({"name":record[1]})
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
        dic['revenue'] = round(revenue,2) if revenue else 0

        res.append(dic)
    except Exception as e:
        print e
        res = ["Search Error"]
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)

#finished
@application.route('/api/manager/getDomestic', methods=['POST','GET'])
def get_airport_domestic():
    conn = mysql.connect()
    cursor = conn.cursor()
    res = []
    try:
        depart = request.form['depart']
        arrival = request.form['destination']
        cursor.execute("SELECT Country FROM Airports_dev WHERE IATA=%s;", (depart))
        country_depart = cursor.fetchone()[0]
        cursor.execute("SELECT Country FROM Airports_dev WHERE IATA=%s;", (arrival))
        country_arrival = cursor.fetchone()[0]
        dic = {}
        if country_depart==country_arrival:
            dic['domestic'] = True
        else:
            dic['domestic'] = False
        res.append(dic)
    except Exception as e:
        print e
        res = ['Search Error']
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
            dic["revenue"] = round(data[3],2)
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
        date = request.form["date"]
        cursor.execute("SELECT name FROM Reservation_Leg JOIN Reservation USING (reservation_no) WHERE idLegs IN (SELECT idLegs FROM LegsInfo WHERE flight_no=%s) AND seat_no<>'' AND date=%s", (flight_no, date))
        for data in cursor.fetchall():
            res.append({"name":data[0]})
    except Exception as e:
        print e
        res = ["Search Error"]
    finally:
        cursor.close()
        conn.close()
    return jsonify(res)


@application.route('/api/manager/delay',methods=['POST','GET'])
def delay():
    conn = mysql.connect()
    try:
        rec = user_db.get_delay_flight(conn)
        _delay = []
        if(rec == False):
            return jsonify({'error':False})
        for index in range(len(rec)):
            dist = {}
            dist['idLegs'] = rec[index][0]
            dist['idFlight'] = rec[index][1]
            dist['distance'] = rec[index][2]
            dist['duration'] = rec[index][3]
            dist['departure_airport'] = rec[index][4]
            dist['departure_time'] = rec[index][5]
            dist['departure_date'] = rec[index][6]
            dist['arrival_airport'] = rec[index][7]
            dist['arrival_time'] = rec[index][8]
            dist['arrival_date'] = rec[index][9]
            dist['flight_no'] = rec[index][10]
            dist['plane'] = rec[index][11]
            dist['plane_code'] = rec[index][12]
            dist['airlinename'] = rec[index][13]
            dist['airline_code'] = rec[index][14]
            dist['delay'] = rec[index][15]
            dist['isdelay'] = rec[index][16]
            _delay.append(dist)
        return jsonify(_delay)
    except Exception as e:
        return jsonify({'error':str(e)})

# Customer booking APIs
@application.route('/api/customer/bookFlight',methods=['POST','GET'])
def book_flight():
    go  = json.loads((request.form['go']))
    back = json.loads((request.form['back']))
    account_no = request.form['account_no']
    passengers = json.loads(request.form['passengers'])
    # print  account_no, passengers[0]
    return model.book_flight(go,back,account_no,passengers)


@application.route('/api/customer/searchFlight',methods=['POST','GET'])
def searchFlight():
    _dep = request.form['depart']
    _arr = request.form['destination']
    _roundtrip = request.form['trip']
    _date1 = request.form['date1']
    _date2 = None  
    go_exist = False
    back_exist = False 
    if(_roundtrip == '1'):
        _date2 = request.form['date2']
    res_all = []
    while (not go_exist):
        res = test.searchFlight(_dep, _arr, _date1)
        if(len(res)<1):
            _date1 = model.get_next_day(_date1)
        else:
            go_exist = True
            res_all.append(res)
    while(_date2!=None and not back_exist):
        res = test.searchFlight(_arr, _dep, _date2)
        if(len(res)<1):
            _date2 = model.get_next_day(_date2)
        else:
            back_exist = True
            res_all.append(res)

    res_all[0] = test.search_hot_flight(_dep,_arr,_date1) + res_all[0]
    if(_date2 != None):        
        res_all[1] = test.search_hot_flight(_arr,_dep,_date1) + res_all[1]
    return jsonify(res_all)


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
                    print data[2]
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

        cursor.execute('SELECT distinct departure_airport,arrival_airport,departure_time,arrival_time,flight_no, airlineCode, airlineName, booking_fee, total_fare, trip_no, duration ,distance, date, reservation_no , seat_no  from Reservation natural join Reservation_Leg natural join LegsInfo where account_no = %s;',[account_no])
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
        print "Length of serach result", len(res_list)
        return jsonify(res_list)

@application.route('/api/customer/getHistory',methods=['POST','GET'])
def get_history():
    return ""

@application.route('/api/customer/getBestSeller',methods=['POST','GET'])
def get_best_seller():
    return ""


if __name__ == "__main__":
    application.run(debug=True)


