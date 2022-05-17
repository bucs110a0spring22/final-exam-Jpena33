import requests

class Location():

 def __init__(self,city,state,country,zipcode,lat,lon):
  self.city = city
  self.state = state
  self.country = country
  self.zipcode = zipcode
  self.lat = lat
  self.lon = lon

 def __str__():
  url = 'http://www.mapquestapi.com/geocoding/v1/address?key=I85AhGVT3L9IRJwxltKpJ0EhJGxZNLx7&location=binghamton'
  r = requests.get(url)
  data = r.json()['results'][0]
  location = data['locations'][0]

  city = location['adminArea5']
  state = location['adminArea3']
  country = location['adminArea1']
  zipcode = location['postalCode']
  lat = location['latLng']['lat']
  lon = location['latLng']['lon']

  print('City :',city)
  print('State :',state)
  print('Country :',country)
  print('Postal Code :',)

