import requests


data = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean").json()
question_data = data['results']
