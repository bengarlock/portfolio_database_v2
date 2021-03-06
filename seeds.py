import requests
from datetime import timedelta, date
import json
from faker import Faker
import random

url = "http://127.0.0.1:8000/api/v1/tablehost/"
#url = "https://bengarlock.com/api/v1/tablehost/"
today = date.today()
books = []


def create_root_user():
    print("Creating Root User...")
    obj = {
        "first_name": '',
        "last_name": '',
        "phone_number": '',
        "guest_notes": '',
        "root_user": True,
        "slot": '1',
    }
    requests.post(url + "guests/", obj)


def create_restaurant():
    print("Creating Restaurant...")
    obj = {
        "name": 'ilili',
    }
    requests.post(url + "restaurants/", obj)


def create_books(date_cap):
    print("Creating Books...")
    index = 0
    while index <= date_cap:
        date = today + timedelta(days=index)
        print(date)
        obj = {
            "date": date,
            "restaurant_id": 1,
            "slots": [],
        }
        book = requests.post(url=url + "books/", data=obj)
        r = book.content.decode('UTF-8')
        res = json.loads(r)
        books.append(res["id"])
        index += 1


def create_slots(array):
    print("Creating Slots...")
    for book_id in array:
        times = [
            '5:00 PM', '5:15 PM', '5:30 PM', '5:45 PM',
            '6:00 PM', '6:15 PM', '6:30 PM', '6:45 PM',
            '7:00 PM', '7:15 PM', '7:30 PM', '7:45 PM',
            '8:00 PM', '8:15 PM', '8:30 PM', '8:45 PM',
        ]

        for time in times:
            party_sizes = [2, 2, 4, 6]
            for party_size in party_sizes:
                obj = {
                    "booked": False,
                    "time": time,
                    "party_size": party_size,
                    "status": '',
                    "reservation_notes"
                    "tables": [],
                    "book": book_id,
                    "guest": 1
                }
                data = requests.post(url + "slots/", data=obj)
                print(data.text)


def create_guests(data_cap):
    print("Creating Guest Records...")
    index = 0
    while index < data_cap:
        notes_array = [
            "Likes Expensive wine.",
            "Friend of the owner",
            "Friend of Employee",
            "Prefers a Booth Table",
            "Dirty Martini with extra olive",
            "Likes table 10",
            "VIP",
        ]

        fake = Faker()
        name = fake.name().split()
        first_name = name[0]
        last_name = name[1]
        phone_number = fake.phone_number()

        notes = "Works for " + str(fake.company()) + " " + notes_array[random.randint(0, len(notes_array) - 1)]

        obj = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "guest_notes": notes,
            "active": True,
        }

        guest = requests.post(url + "guests/", data=obj)
        print(guest.text)
        index += 1


def create_tables():
    print("Creating Tables...")
    tables = [
        {"class_name": "two-top-horizontal", "position_left": "102px", "position_top": "40px", "name": "1",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "168px", "position_top": "40px", "name": "2",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "234px", "position_top": "40px", "name": "3",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "300px", "position_top": "40px", "name": "4",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "364px", "position_top": "40px", "name": "5",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "430px", "position_top": "40px", "name": "6",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "40px", "position_top": "120px", "name": "7",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "40px", "position_top": "180px", "name": "8",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "40px", "position_top": "240px", "name": "9",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "40px", "position_top": "300px", "name": "10",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "40px", "position_top": "360px", "name": "11",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "two-top-horizontal", "position_left": "40px", "position_top": "420px", "name": "12",
         "restaurant_id": 1, "status": "done"},
        {"class_name": "fourTop", "position_left": "140px", "position_top": "150px", "name": "14", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "210px", "position_top": "150px", "name": "15", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "280px", "position_top": "150px", "name": "16", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "350px", "position_top": "150px", "name": "17", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "420px", "position_top": "150px", "name": "18", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "140px", "position_top": "250px", "name": "19", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "210px", "position_top": "250px", "name": "20", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "280px", "position_top": "250px", "name": "21", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "350px", "position_top": "250px", "name": "22", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "420px", "position_top": "250px", "name": "23", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "140px", "position_top": "350px", "name": "24", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "210px", "position_top": "350px", "name": "25", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "280px", "position_top": "350px", "name": "26", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "350px", "position_top": "350px", "name": "27", "restaurant_id": 1,
         "status": "done"},
        {"class_name": "fourTop", "position_left": "420px", "position_top": "350px", "name": "28", "restaurant_id": 1,
         "status": "done"},
    ]
    for table in tables:
        table = requests.post(url + "tables/", data=table)
        print(table.content)


def create_reservations(limit):
    print("Booking Reservations...")
    index = 0
    while index < limit:
        slot_id = random.randint(1, 7000)
        guest_id = random.randint(1, 1000)

        obj = {
            "booked": True,
            "status": "booked",
            "guest": int(guest_id)
        }

        updated_slot = requests.put(url + "slots/" + str(slot_id) + "/", data=obj)
        print(url + "slots/" + str(slot_id))
        index += 1


# create_books(100)
# create_root_user()
# create_restaurant()
# create_slots(array=books)
create_guests(1000)
# create_tables()
# create_reservations(limit=2000)
