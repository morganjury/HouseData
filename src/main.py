import pyodbc
import geolocation_dao
import price_paid_dao
import postcodes_io
import pandas

file_location = "../files/"
driver = "PostgreSQL Unicode(x64)"
database = "housedata"
username = "postgres"
password = "postgres"
server = "localhost"
port = "5432"
conn = pyodbc.connect(
        "driver={"+driver+"};database="+database+";username="+username
        +";password="+password+";server="+server+";port="+port+";"
    )
geolocationdao = geolocation_dao.GeoLocationDao(conn)
pricepaiddao = price_paid_dao.PricePaidDao(conn)

def populate_lat_lon(postcode):
    if type(postcode) != str: return
    if geolocationdao.get(postcode) == None:
        api_result = postcodes_io.get_lat_lon(postcode)
        if api_result[1] != None: geolocationdao.insert(api_result[0], api_result[1], api_result[2])

def load_file(file_path, column_names):
    file_contents = pandas.read_csv(file_path, names=column_names)
    for entry in file_contents.values:
        populate_lat_lon(entry[column_names.index("Postcode")])
#        pricepaiddao.insert(entry)

#load_file(file_location+"pp-monthly-update-new-version.csv", price_paid_dao.column_names)

import graph
results = geolocationdao.get_all()
graph.plot("Longitude", "Latitude", results["Longitude"], results["Latitude"])
print(results.corr())

conn.close()