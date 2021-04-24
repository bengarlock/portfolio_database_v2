import requests
import json
import passwords

def pull_resy_data():
    url = "https://api.resy.com/2/venues?location_id=ny"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'ResyAPI api_key="' + passwords.return_api_key() + '"'
    }
    data = requests.get(url, headers=headers)
    data = json.loads(data.text)
    return data


def pull_local_api():
    url = "https://bengarlock.com/api/v1/resy/restaurants/"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'ResyAPI api_key="' + passwords.return_api_key() + '"'
    }
    data = requests.get(url, headers=headers)
    data = json.loads(data.text)
    return data


def format_resy_data():
    resy_data = pull_resy_data()
    package = []

    for item in resy_data:
        restaurant = {
            "restaurant_name": item["name"],
            "resy_id": str(item["id"]["resy"]),
            "neighborhood": item["location"]["neighborhood"],
            "url": item["contact"]["url"]
        }
        package.append(restaurant)
    return package


def format_local_api_data():
    local_api_data = pull_local_api()
    for restaurant in local_api_data:
        restaurant.pop("id", None)
        restaurant.pop("created_at", None)
        restaurant.pop("updated_at", None)

    return local_api_data


def update_api():
    resy_api_data = format_resy_data()
    local_api_data = format_local_api_data()

    new_restaurants = [i for i in resy_api_data if i not in local_api_data]
    dead_restaurants = [i for i in local_api_data if i not in resy_api_data]

    for restaurant in dead_restaurants:
        url = "https://bengarlock.com/api/v1/resy/restaurants/?resy_id=" + str(restaurant["resy_id"])
        fetch_resy_search = requests.get(url).json()
        response = requests.delete(url="https://bengarlock.com/api/v1/resy/restaurants/" + str(fetch_resy_search[0]["id"]) + "/")
        print(response.status_code)

    for restaurant in new_restaurants:
        url = "https://bengarlock.com/api/v1/resy/restaurants/?resy_id=" + str(restaurant["resy_id"])
        fetch_resy_search = requests.get(url).json()

        if not fetch_resy_search:
            print("create")
            payload = {
                "restaurant_name": restaurant["restaurant_name"],
                "resy_id": restaurant["resy_id"],
                "neighborhood": restaurant["neighborhood"],
                "url": restaurant["url"]
            }

            response = requests.post(url="https://bengarlock.com/api/v1/resy/restaurants/", json=payload)
            print(response.status_code)

        else:
            print("update")
            print(restaurant)
            url = "https://bengarlock.com/api/v1/resy/restaurants/" + str(fetch_resy_search[0]["id"]) + "/"

            headers = {
                'Content-Type': 'application/json',
                'Accepts': 'application/json'
            }

            payload = {
                "restaurant_name": restaurant["restaurant_name"],
                "resy_id": restaurant["resy_id"],
                "neighborhood": restaurant["neighborhood"],
                "url": restaurant["url"]
            }
            response = requests.patch(url=url, json=payload, headers=headers)
            print(response.status_code)


update_api()
