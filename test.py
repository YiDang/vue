import model

# @application.route('/api/customer/bookFlight',methods=['POST','GET'])
def book_flight(go, back):
    conn = model.db_conn()
    cursor = conn.cursor()
    try:
    	_account_no = 1
    	_dep_date = go['date']
    	_reserv_date = model.get_today()
    	_book_fare = 1
    	_total_fare = _book_fare * 1.1
    	_trip_no = 
    	# INSERT INTO RESERVATION TABLE
    	cursor.execute('SELECT MAX(reservation_no) From Reservation')
    	_reservation_no =  cursor.fetchone()[0] + 1
    	cursor.execute('INSERT INTO Reservation VALUES (%s, %s, %s, %s, %s)',[_reservation_no,_account_no,_book_fare, _total_fare, _dep_date, _reserv_date])
    	# INSERT INTO RESERVATION_LEG TABLE
    	for t in range (_trip_no): # 1 or 2
    		flight_id = 1
    		passenger_info = []
    		stops = []
    		_booking_fare = 
    		for p in range(len(passenger_info)):
    			passenger = passenger_info[p]
    			for leg in range(len(stops)):
    				idLegs = stops[leg]['idLegs']
    				cursor.execute('INSERT INTO Reservation_Leg VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',[_reservation_no], idLegs, passenger['ssn'],passenger['name'], flight_id, 4, "Y", "", t)
    except Exception as e:
    	print e
    finally: 
		cursor.close()
		conn.close()

