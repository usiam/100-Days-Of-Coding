import requests, os, datetime

# info needed
date = datetime.datetime(year=2021, month=6, day=23).strftime("%Y%m%d")
pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'usiam'
TOKEN = os.environ.get('TOKEN')
GRAPHID = 'graph1'

# Creating a user

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph
headers = {
    'X-USER-TOKEN': TOKEN
}

graph_params = {
    'id': GRAPHID,
    'name': 'Running Graph',
    'unit': 'Kilometer',
    'type': 'float',
    'color': 'kuro'
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Creating a pixel
pixel_post_params = {
    'date': date,
    'quantity': '5',
}
pixel_post_endpoint = f"{graph_endpoint}/graph1"
# response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)

# Editing an existing pixel
pixel_put_params = {
    'quantity': '0'
}

pixel_put_endpoint = f"{pixel_post_endpoint}/{date}"
response = requests.put(url=pixel_put_endpoint, json=pixel_put_params, headers=headers)

# Deleting an existing pixel
requests.delete(url=pixel_put_endpoint, headers=headers)
