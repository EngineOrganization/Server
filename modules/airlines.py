from duffel_api import Duffel
import json


def initializate():

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
		.return_offers()
		.execute()
	)
	offers = offer_request.offers
	offers_data = [] # [{'id': id, 'slices': [origin': {'id': id, 'name': name, 'type': type, 'iata_city_code': iata_city_code, 'iata_country_code': iata_country_code, 'city_name': city_name}, 'arriving_at': arriving_at, 'departing_at': departing_at, destination: {'id': id, 'name': name, 'type': type, 'iata_city_code': iata_city_code, 'iata_country_code': iata_country_code, 'city_name': city_name}], 'owner': {'id': id, 'name': name, 'iata_code': iata_code, 'logo_symbol_url': logo_symbol_url, 'logo_lockup_url': logo_lockup_url}}]
	for offer in offers:
		print(offer.slices[0].segments)
		print('\n\n\n')
		offers_data.append({'id': offer.id, 'owner': {'id': offer.owner.id, 'name': offer.owner.name, 'iata_code': offer.owner.iata_code, 'logo_symbol_url': offer.owner.logo_symbol_url, 'logo_lockup_url': offer.owner.logo_lockup_url}, 'slices': [], 'total_amount': offer.total_amount, 'total_currency': offer.total_currency})
		for i in range(len(offer.slices)):
			# print(offer.slices[i].segments)
			offers_data[-1]['slices'].append({'origin': {'id': offer.slices[i].origin.id, 'name': offer.slices[i].origin.name, 'type': offer.slices[i].origin.type, 'iata_city_code': offer.slices[i].origin.iata_city_code, 'iata_country_code': offer.slices[i].origin.iata_country_code, 'city_name': offer.slices[i].origin.city_name}, 'destination': {'id': offer.slices[i].destination.id, 'name': offer.slices[i].destination.name, 'type': offer.slices[i].destination.type, 'iata_city_code': offer.slices[i].destination.iata_city_code, 'iata_country_code': offer.slices[i].destination.iata_country_code, 'city_name': offer.slices[i].destination.city_name}})

	print(offers_data)