import requests, datetime, os

now = datetime.datetime.now()
nutrition_APIKEY = os.environ.get('NUT_APIKEY')
nutrition_APPID = os.environ.get('NUT_APPID')
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheetly_endpoint = 'https://api.sheety.co/a96437876dce61755e1ca0bf709aa1fb/myWorkouts/workouts'

headers = {
    'x-app-id': nutrition_APPID,
    'x-app-key': nutrition_APIKEY,
    'x-remote-user-id': '0'
}

exercise_input = input("What exercises did you do? ")

exercise_params = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 79.4,
    "height_cm": 177.8,
    "age": 21
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercise_data = response.json()['exercises']

for exercise in exercise_data:
    myExercises = {
        'workout': {
            'date': now.strftime("%d/%m/%Y"),
            'time': now.strftime("%H:%M:%S"),  # same as "%X"
            'exercise': exercise['name'].title(),
            'duration': str(exercise['duration_min']),
            'calories': exercise['nf_calories']
        }
    }
    sheet_input = requests.post(url=sheetly_endpoint, json=myExercises)

