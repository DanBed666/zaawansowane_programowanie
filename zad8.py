import requests


class Brewery:

    def __init__(self, name, brewery_type, street, city, state, phone):
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.phone = phone

    def __str__(self) -> str:
        return f"Browar o nazwie {self.name} typu {self.brewery_type}" \
               f" na ulicy {self.street} w mieście {self.city} położonym" \
               f"w stanie {self.state}. Numer telefonu to {self.phone}"


def get_20_breweries_request(number):

    req = requests.get(f"https://api.openbrewerydb.org/"
                       f"breweries/random?size={number}").json()
    get_elements(req)


def get_breweries_by_city_request(city):

    req = requests.get(f"https://api.openbrewerydb.org/breweries?"
                       f"by_city={city}&per_page=20").json()

    get_elements(req)


def get_elements(req):

    breweries_list = []

    for brewery in req:
        new_brewery = Brewery(brewery["name"], brewery["brewery_type"],
                              brewery["street"], brewery["city"],
                              brewery["state"], brewery["phone"])
        breweries_list.append(new_brewery)

    for number, brewery in enumerate(breweries_list):
        print(f"{number + 1}. {brewery.__str__()}")


if __name__ == '__main__':
    get_20_breweries_request(20)
    print()
    get_breweries_by_city_request("chicago")
