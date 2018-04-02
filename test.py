import model
import pdb


def searchFlight(_dep, _arr, _date):
    print _dep, _arr, _date
    conn = model.db_conn()
    cursor = conn.cursor()
    conn_2 = model.db_conn()
    cursor_2 = conn_2.cursor()
    res_final = []
    res_list = []
    try:
        _db_date = model.get_db_date(_date)
        flight_id = []
        flight_dict = {}
        i = 0
        cursor.execute("SELECT idFlightInfo,departure,arrival,duration,nextDayArrival,stops,price, total_distance FROM  cs539_dev.FlightInfoAll where SUBSTRING(FlightInfoAll.departure, 1, 3) = %s and SUBSTRING(FlightInfoAll.arrival,  1, 3) = %s ; ", [_dep, _arr] )
        for data in cursor.fetchall():
            if(data):
                flight_id.append(data[0])
                flight_dict[data[0]] = i
                res_list.append({})
                res_list[flight_dict[data[0]]]['flight_id'] = data[0]
                res_list[flight_dict[data[0]]]['departure'] = data[1]
                res_list[flight_dict[data[0]]]['arrival'] = data[2]
                dur = data[3].split(" ")
                res_list[flight_dict[data[0]]]['duration'] =  dur[0] + dur[1][0] + " " + dur[2] + dur[3][0] + " " + dur[4] + dur[5][0]
                res_list[flight_dict[data[0]]]['next_day_arr'] = data[4]
                res_list[flight_dict[data[0]]]['stop_count'] = data[5]
                res_list[flight_dict[data[0]]]['price'] = round(model.get_fair(data[6],_date),2)
                res_list[flight_dict[data[0]]]['total_distance'] = data[7]
                res_list[flight_dict[data[0]]]['stops'] = []
                res_list[flight_dict[data[0]]]['date'] = _date  
                i+=1   
        for fid in flight_id:
            # print fid
            isFull = False
            cursor.execute('SELECT  idFlight,idLegs,distance,duration,departure_airport,departure_time,arrival_airport,arrival_time,flight_no,airlineName,airlineCode from cs539_dev.LegsInfo where idFlight = %s and departure_date = %s;',[fid,_db_date])
            stop = 1
            res_list[flight_dict[fid]]['Full'] = False
            for data in cursor.fetchall():
                if(data and not isFull):
                    dict = {}
                    dict['stop'] = stop
                    dur = data[3].split(" ")
                    dict['duration'] = dur[0] + dur[1][0] + " " + dur[2] + dur[3][0] + " " + dur[4] + dur[5][0]
                    dict['departure_airport'] = data[4]
                    dict['departure_time'] = data[5]
                    dict['arrival_airport'] = data[6]
                    dict['arrival_time'] = data[7]
                    dict['flight_no'] = data[8]
                    dict['airlineName'] = data[9]
                    dict['airlineCode'] = data[10]
                    dict['distance'] = data[2]
                    dict['legs'] = data[1]
                    cursor_2.callproc('sp_isFlightFull',(_date,fid,data[1],0))
                    data_2 = cursor_2.fetchone()
                    isFull, totalBooked, capacity = data_2[0], data_2[1], data_2[2]
                    if(isFull):
                        res_list[flight_dict[fid]]['Full'] = True
                        break
                    res_list[flight_dict[fid]]['stops'].append(dict)
                    stop += 1
        for fid in flight_id:
            if(len(res_list[flight_dict[fid]]['stops']) >= 1 and not res_list[flight_dict[fid]]['Full']):
                res_final.append(res_list[flight_dict[fid]])    
    except Exception as e:
        print e
        return ""
    finally:
        cursor.close()
        conn.close()
        cursor_2.close()
        conn_2.close()
        return res_final

def search_hot_flight(_dep, _arr, _date):
    conn = model.db_conn()
    cursor = conn.cursor()
    hot_Flight_Id = None
    res_list = []
    _db_date = model.get_db_date(_date)
    cursor.callproc('sp_getHotFlight',(_dep,_arr,_date))

    for data in cursor.fetchall():
        if(data):
            hot_Flight_Id = data[0]
            print "hot flight ", hot_Flight_Id
    if(hot_Flight_Id==None):
        return res_list 
    else:
        res_list.append({})
        cursor.execute("SELECT idFlightInfo,departure,arrival,duration,nextDayArrival,stops,price, total_distance FROM  cs539_dev.FlightInfoAll where idFlightInfo = %s limit 1;", [hot_Flight_Id] )

        for data in cursor.fetchall():
            if(data):
                res_list[0]['flight_id'] = data[0]
                res_list[0]['departure'] = data[1]
                res_list[0]['arrival'] = data[2]
                dur = data[3].split(" ")
                res_list[0]['duration'] = dur[0] + dur[1][0] + " " + dur[2] + dur[3][0] + " " + dur[4] + dur[5][0]
                res_list[0]['next_day_arr'] = data[4]
                res_list[0]['stop_count'] = data[5]
                res_list[0]['price'] = round(model.get_fair(data[6],_date),2)
                res_list[0]['total_distance'] = data[7]
                res_list[0]['stops'] = []
                res_list[0]['date'] = _date

        cursor.execute('SELECT  idFlight,idLegs,distance,duration,departure_airport,departure_time,arrival_airport,arrival_time,flight_no,airlineName,airlineCode from cs539_dev.LegsInfo where idFlight = %s and departure_date = %s ;',[hot_Flight_Id,_db_date])
        stop = 1
        for data in cursor.fetchall():
            if(data):
                dict = {}
                dict['stop'] = stop
                dur = data[3].split(" ")
                dict['duration'] = dur[0] + dur[1][0] + " " + dur[2] + dur[3][0] + " " + dur[4] + dur[5][0]
                dict['departure_airport'] = data[4]
                dict['departure_time'] = data[5]
                dict['arrival_airport'] = data[6]
                dict['arrival_time'] = data[7]
                dict['flight_no'] = data[8]
                dict['airlineName'] = data[9]
                dict['airlineCode'] = data[10]
                dict['distance'] = data[2]
                dict['legs'] = data[1]
                res_list[0]['stops'].append(dict)
                stop += 1
    conn.close()
    cursor.close()
    return res_list