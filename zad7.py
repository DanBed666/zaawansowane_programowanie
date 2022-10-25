import requests


def get_breweries(number):

    # wyswietlenie 30 pierwszych nazw browarów
    req = requests.get(f"https://api.openbrewerydb.org/"
                       f"breweries/random?size={number}").json()
    for number, brewery in enumerate(req):
        print(f"{number + 1}. {brewery['name']}")


if __name__ == '__main__':
    get_breweries(30)
