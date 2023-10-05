import requests

API_KEY = 'AIzaSyAfcXobkxe14CbAut0snQBNiSWBo3F-wvw'

address = 'VMWW+WF Barotac Nuevo, Iloilo'

params = {
    'key' : API_KEY,
    'address' : address
}

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

response = requests.get(base_url, params=params).json()

# print(response['results'])


if response['status'] == 'OK':
    geometry = response['results'][0]['geometry']
    lat = geometry['location']['lat']
    lng = geometry['location']['lng']

print(lat, lng)
