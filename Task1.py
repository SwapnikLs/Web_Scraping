from bs4 import BeautifulSoup
import requests


urls = [
    "https://ackodrive.com/collection/maruti-suzuki-cars/",
    "https://ackodrive.com/collection/maruti-suzuki-cars/page/2/",
     "https://ackodrive.com/cars/"
]

car_index = 1  

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cars = soup.find_all("div", {"data-testid": "listingcardesktop"})

    for car in cars:
        name_tag = car.find("h2")
        car_name = name_tag.text.strip() 

        car_make = " ".join(car_name.split()[:2])

        for p in car.find_all("p"):
            if "Available in" in p.text and "color" in p.text.lower():
                color_text = p.text.strip()
                break
        else:
            color_text = "Color info not found"

        price_tag = car.find("div", {"data-testid": "car_price"})
        car_price = price_tag.text.strip() if price_tag else "Price not found"

        transmisson_tag = car.find("p", {"data-testid": "car_variant_transmission"})
        transmisson = transmisson_tag.text.strip() if transmisson_tag else "Transmission not found"

        fuel_tag = car.find("p", {"data-testid": "car_variant_fuel_type"})
        fuel = fuel_tag.text.strip() if fuel_tag else "Fuel type not found"

        print(f"Car {car_index}: {car_name}")
        print(f"Car_Make: {car_make}")
        print(f"Price: {car_price}")
        print(f"Fuel Type: {fuel}")
        print(f"Transmission: {transmisson}")
        print(f"{color_text}\n")

        car_index += 1
