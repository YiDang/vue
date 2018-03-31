import model
import pdb

# @application.route('/api/customer/bookFlight',methods=['POST','GET'])
def book_flight(go, back, account_no, passengers):
    conn = model.db_conn()
    cursor = conn.cursor()
    try:
        _account_no = account_no
    	_dep_date = go['date']
    	_reserv_date = model.get_today()
        _book_fare = go['price']
    	_book_fare +=  back['price'] if back != None else 0
        _book_fare *= len(passengers)
    	_total_fare = _book_fare * 1.1
    	_trip_no = 2 if back!=None else 1
        _trips = [go, back]

    	# INSERT INTO RESERVATION TABLE
    	cursor.execute('SELECT MAX(reservation_no) From Reservation')
    	_reservation_no =  cursor.fetchone()[0] + 1
    	cursor.execute('INSERT INTO Reservation VALUES (%s, %s, %s, %s, %s, %s)',[_reservation_no,_account_no,_book_fare, _total_fare, _dep_date, _reserv_date])
        
    	# # # INSERT INTO RESERVATION_LEG TABLE
    	for t in range (_trip_no): # 1 or 2
    	   flight_id = _trips[t]['flight_id']
    	   # passenger_info = passengers[t]
    	   stops = _trips[t]['stops']
    	   for p in range(len(passengers)):
                passenger = passengers[p]
    	        for leg in range(len(stops)):
                    idLegs = stops[leg]['legs']
                    cursor.execute('INSERT INTO Reservation_Leg VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',[_reservation_no, idLegs, passenger['ssn'],passenger['name'], flight_id, 4, "Y", 1, t])

    except Exception as e:
    	print  e
    	return jsonify({"result":False,"message":"Error: Cannot Complete Booking"})
    finally: 
		cursor.close()
		conn.commit()
		conn.close()
		return jsonify({"result":True, "message":"Booking Completed"})


