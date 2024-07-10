from duffel_api import Duffel
import json


def initializate():
	global duffelClient
	try:
		with open('tokens.json') as tokens:
			duffel_access_token = json.load(tokens)['duffelToken']
	except FileNotFoundError:
		return 'Ошибка при попытке открыть файл с настройками'

	try:
		duffelClient = Duffel(access_token = duffel_access_token)
	except:
		return 'Ошибка при попытке подключиться к OpenAI'

	return 'Duffel подключен'


def get_avia_tickets(iata_from, iata_to, date):
	slices = [
	{
	"origin": iata_from,
	"destination": iata_to,
	"departure_date": date,
	},
	]
	offer_request = (
		duffelClient.offer_requests.create()
		.passengers([{"type": "adult"}])
		.slices(slices)
		.execute()
	)
	offers = list(duffelClient.offers.list(offer_request.id))
	offers_data = []
	for offer in offers:
		print(offer.slices[0].segments)
		print('\n\n\n')
		offers_data.append({'id': offer.id, 'owner': {'id': offer.owner.id, 'name': offer.owner.name, 'iata_code': offer.owner.iata_code, 'logo_symbol_url': offer.owner.logo_symbol_url, 'logo_lockup_url': offer.owner.logo_lockup_url}, 'slices': [], 'total_amount': offer.total_amount, 'total_currency': offer.total_currency})
		for i in range(len(offer.slices)):
			# print(offer.slices[i].segments)
			offers_data[-1]['slices'].append({'origin': {'id': offer.slices[i].origin.id, 'name': offer.slices[i].origin.name, 'type': offer.slices[i].origin.type, 'iata_city_code': offer.slices[i].origin.iata_city_code, 'iata_country_code': offer.slices[i].origin.iata_country_code, 'city_name': offer.slices[i].origin.city_name}, 'destination': {'id': offer.slices[i].destination.id, 'name': offer.slices[i].destination.name, 'type': offer.slices[i].destination.type, 'iata_city_code': offer.slices[i].destination.iata_city_code, 'iata_country_code': offer.slices[i].destination.iata_country_code, 'city_name': offer.slices[i].destination.city_name}, 'segments': []})
			for j in range(len(offer.slices[i].segments)):
				offers_data[-1]['slices'][-1]['segments'].append({'id': offer.slices[i].segments[j].id, 'aircraft': {'id': offer.slices[i].segments[j].aircraft.id, 'iata_code': offer.slices[i].segments[j].aircraft.iata_code, 'name': offer.slices[i].segments[j].aircraft.name}, 'arriving_at': offer.slices[i].segments[j].arriving_at, 'departing_at': offer.slices[i].segments[j].departing_at, 'origin': {'id': offer.slices[i].segments[j].origin.id, 'name': offer.slices[i].segments[j].origin.name, 'iata_code': offer.slices[i].segments[j].origin.iata_code, 'iata_country_code': offer.slices[i].segments[j].origin.iata_country_code, 'latitude': offer.slices[i].segments[j].origin.latitude, 'longitude': offer.slices[i].segments[j].origin.longitude, 'time_zone': offer.slices[i].segments[j].origin.time_zone}, 'destination': {'id': offer.slices[i].segments[j].destination.id, 'name': offer.slices[i].segments[j].destination.name, 'iata_code': offer.slices[i].segments[j].destination.iata_code, 'iata_country_code': offer.slices[i].segments[j].destination.iata_country_code, 'latitude': offer.slices[i].segments[j].destination.latitude, 'longitude': offer.slices[i].segments[j].destination.longitude, 'time_zone': offer.slices[i].segments[j].destination.time_zone}})