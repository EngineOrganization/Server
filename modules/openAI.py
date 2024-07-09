from openai import OpenAI
import json


def initializate():

	try:
		with open('tokens.json') as tokens:
			openAIToken = json.load(tokens)['openAIToken']
	except FileNotFoundError:
		return 'Ошибка при попытке открыть файл с настройками'

	try:
		client = OpenAI(api_key = openAIToken)
	except:
		return 'Ошибка при попытке подключиться к OpenAI'

	return 'OpenAI подключен'


def get_chatgpt(country, city, activity, people, priorities, countDay, budget):
	activity = str(int(float(activity)))
	text = 'Составь пожалуйста маршрут путешествия по ' + country + ' ' + city + '. Путешествие должно быть расчитано на человека, степень активности которого оценивается в ' + activity + 'из 10. Количество путешественников: ' + people + '. Также нужно, чтобы путешествие совпадало со следующими приоритетами: ' + priorities + '. Путешествие должно продлиться ' + countDay + '. Каждый день должно быть не менее ' + activity + 'действий. Бюджет для путешествия оценивается как ' + budget + """. Также для каждого действия выводи широту и долготу места.Путешествие должно быть представлено в виде json на английском языке. Проверь, чтобы json полностью был рабочим. Пример ответа:
	{
		"Trip": {
			"Day 1": {
				"Action 1": {
					name: "walk in park",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				},
				"Action 2": {
					name: "dinner in restaurant",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				},
				"Action """ + activity + """": { 
					name: "ravel to mountains",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				}
			},
			"Day 2": {
				"Action 1": {
					name: "walk in park",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				},
				"Action 2": {
					name: "dinner in restaurant",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				},
				"Action """ + activity + """": { 
					name: "ravel to mountains",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				}
			}
			"Day """ + countDay + """": {
				"Action 1": {
					name: "walk in park",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				},
				"Action 2": {
					name: "dinner in restaurant",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				},
				"Action """ + activity + """": { 
					name: "ravel to mountains",
					lat: 68,
					lon: 68,
					info: "Информация о месте"
				}
			}
		}
	}
	"""
	messages = [ {"role": "user", "content": text} ]
	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages = messages
	)
	return response.choices[0].message.content

