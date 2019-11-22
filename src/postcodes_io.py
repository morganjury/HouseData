import requests

def get_lat_lon(postcode):
    if type(postcode)!=str:
        raise Exception("")
    postcode = postcode.replace(" ","")
    response = requests.get("http://api.postcodes.io/postcodes/" + postcode)
    if str(response.json()["status"]) == "200":
        return [postcode, response.json()["result"]["latitude"], response.json()["result"]["longitude"]]
    else:
        return [postcode, None, None]