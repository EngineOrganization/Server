import socket
import requests
import json
import firebase_admin
from firebase_admin import db
import math
import geopy.distance
import hashlib
import modules.openAI as OpenAI
import modules.airlines as Airlines


# places = {}
# countries = {}
# iata_codes_response = requests.get('https://api.travelpayouts.com/data/ru/cities.json?_gl=1*tkywyh*_ga*MTE1MTg3MDkzOS4xNzE5NTczNTQ2*_ga_1WLL0NEBEH*MTcyMDE5MTIwMS42LjEuMTcyMDE5MTU3OS42MC4wLjA.')
# iata_codes = json.loads(iata_codes_response.text)

# for city in iata_codes:
# 	if (city['country_code'] not in places):
# 		places[city['country_code']] = {}
# 	places[city['country_code']][str(city['name']).replace('/', '|').replace('[', '').replace(']', '')] = city['code']

# countries_response = requests.get(f'https://restcountries.com/v3.1/alpha?codes={','.join(map(str, list(places.keys())))}')

# for country in json.loads(countries_response.text):
# 	countries[country['cca2']] = {'name': country['translations']['rus']['common'], 'flag': country['flags']['svg'], 'cities': places[country['cca2']]}


# HOST = ''
# PORT = 4048

# cred = firebase_admin.credentials.Certificate('engine-4a21e-firebase-adminsdk-k46l1-738b7b8021.json')
# firebase_app = firebase_admin.initialize_app(cred, {
# 	'databaseURL': 'https://engine-4a21e-default-rtdb.europe-west1.firebasedatabase.app/'
# 	})


# ref = db.reference('places/countries')
# ref.set(countries)
# ref.push()



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# 	s.bind((HOST, PORT))
# 	s.listen(10)
# 	while True:
# 		conn, addr = s.accept()
# 		with conn:
# 			print('Connected by', addr)
# 			while True:
# 				data = conn.recv(1024)
# 				if not data:
# 					break
# 				ans = json.loads(data.decode('utf-8'))
# 				print(ans)
# 				if (ans['type'] == 1):
# 					print(countries)
# 					conn.sendall(json.dumps(countries).encode('utf-8'))
# 				elif (ans['type'] == 2):
# 					print(places[ans['data']])
# 					conn.sendall(json.dumps(places[ans['data']][0:30]).encode('utf-8'))
# 				elif (ans['type'] == 3):
# 					for i in range(5):
# 						ref = db.reference(f'/users/{ans['uid']}/generated_tours/{i}')
# 						chatgpt_out = get_chatgpt(ans['countryTo'], ans['cityTo'], ans['activity'], ans['people'], ans['priorities'], ans['countDay'], ans['budget'])
# 						print(chatgpt_out)
# 						ref.set(json.loads(chatgpt_out))
# 						info = {'countryTo': ans['countryTo'], 'cityTo': ans['cityTo'], 'countryOf': ans['countryOf'], 'cityOf': ans['cityOf'], 'countDay': ans['countDay'], 'budget': ans['budget'], 'priorities': ans['priorities'], 'travelDate': ans['travelDate']}
# 						ref.update(info)
# 						data_migrations = get_migrations(places_codes[ans['countryOf']][ans['cityOf']], places_codes[ans['countryTo']][ans['cityTo']], ans['travelDate'])
# 						ref.update(data_migrations)
# 						print(data_migrations)
# 						ref.push()

# 	if (country['title'] in places):
# 		count += 1
# 		countries_copy.remove(country['title'])
# 		print(len(country['regions'][0]['settlements']))

# for country in countries_copy:
# 	del places[country]


if __name__ == '__main__':
	print(OpenAI.initializate())
	print(Airlines.initializate())