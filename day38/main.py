import requests,os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


WEIGHT_KG = 56
HEIGHT_CM = 172
AGE = 26

APP_ID =os.getenv("APP_ID")
API_KEY=os.getenv("API_KEY")
SHEETY_USERNAME=os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD=os.getenv("SHEETY_PASSWORD")

syndigo_exercise_end_point ="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint ="https://api.sheety.co/367ffde77ec7d42b766bec5c03fade4a/myWorkouts/workouts"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

user_input=input("Tell me what exercises you did: ")
today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

exercise_json_body ={
    "query":user_input,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}


syndigo_response = requests.post(url=syndigo_exercise_end_point, json=exercise_json_body, headers=headers)
syndigo_response.raise_for_status()
result = syndigo_response.json()


for exercise in result['exercises']:
    type_of_exercise = exercise['name'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    sheety_json_body ={
    "workout":{
        "date":formatted_date,
        "time":time,
        "exercise":type_of_exercise,
        "duration":duration,
        "calories":calories,
    }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_json_body,auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
    sheety_response.raise_for_status()
    print(sheety_response.status_code)

