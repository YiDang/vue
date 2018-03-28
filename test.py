import random, string
import pymysql
import names
from faker import Faker


DB_PATH = "cs539-sp18.cwvtn5eogw8i.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PORT = 3306
DB_NAME = "cs539_dev"
DB_PASS = "***cs539***"
conn = pymysql.connect(DB_PATH, DB_USER, DB_PASS,DB_NAME)

cursor = conn.cursor()
cursor.execute('SELECT  idLegs,
		idFlight,
		departure_airport,
		arrival_airport,
        SUBSTRING(FlightInfoAll.departure, 5) as departure_city,
        SUBSTRING(FlightInfoAll.arrival, 5) as arrival_city,
        STR_TO_DATE(departure_time, '%h:%i%p') as departure_time,
		STR_TO_DATE(arrival_time, '%h:%i%p') as arrival_time,
		FlightInfoAll.airline,
		FlightInfoAll.duration,
		FlightInfoAll.nextDayArrival,
		FlightInfoAll.price,
		FlightInfoAll.stops,
		FlightInfoAll.total_distance
FROM cs539_dev.LegsInfo join  cs539_dev.FlightInfoAll
On LegsInfo.idFlight = FlightInfoAll.idFlightInfo
where LegsInfo.departure_airport = 'LAX' and LegsInfo.arrival_airport = 'EWR' and LegsInfo.departure_date = '04/05/2018'
order by departure_time ASC;')

for data in cursor.fetchall():
    print data[]
