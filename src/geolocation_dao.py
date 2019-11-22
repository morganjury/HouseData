#create table geolocation (
#    postcode varchar(10) not null primary key,
#    latitude float,
#    longitude float,
#    updated timestamp not null default now()
#);
import pandas

column_names = ["Postcode","Latitude","Longitude","Updated"]

class GeoLocationDao:
    
    def __init__(self, connection):
        self.conn = connection
        self.cursor = connection.cursor()

    def insert(self, postcode, latitude, longitude):
        if type(postcode) != str:
            raise Exception("")
        if type(latitude) != float:
            raise Exception("")
        if type(longitude) != float:
            raise Exception("")
        postcode = postcode.replace(" ","")
        self.cursor.execute("INSERT INTO geolocation (postcode, latitude, longitude) VALUES ('"
                      + str(postcode) + "','"
                      + str(latitude) + "','"
                      + str(longitude) + "')")
        self.conn.commit()
    
    def get(self, postcode):
        if type(postcode) != str:
            raise Exception("")
        postcode = postcode.replace(" ","")
        self.cursor.execute("SELECT * FROM geolocation WHERE postcode='" + str(postcode) + "'")
        for row in self.cursor:
            return row
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM geolocation")
        return self.get_results(self)
    
    def get_within_range(self, min_latitude, max_latitude, min_longitude, max_longitude):
        self.cursor.execute("SELECT * FROM geolocation WHERE (latitude BETWEEN " + min_latitude + " AND " + max_latitude + ") AND (longitude BETWEEN " + min_longitude + " AND " + max_longitude + ")")
        return self.get_results(self)
    
    def get_results(self):
        results = pandas.DataFrame(columns=column_names)
        for row in self.cursor:
            results = results.append({
                    column_names[0] : str(row[0]), 
                    column_names[1] : float(row[1]), 
                    column_names[2] : float(row[2]), 
                    column_names[3] : row[3]
                    }, ignore_index = True)
        return results