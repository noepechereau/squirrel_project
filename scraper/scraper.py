import requests

websites = {
    "resources": {
        "football": "https://www.winamax.fr/paris-sportifs/sports/1",
    },
    "sofascore": {
        "gold": "https://www.sofascore.com/betting-tips-today/football",
    }
}


def get_winamax_page(url):
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.141 Safari/537.36"
    })
    return response.text


def get_sofascore_page(url):
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    })
    return response.text


def get_json(url):
    html = get_sofascore_page(url)
    return html.split("var PRELOADED_STATE = ")[1].split(";</script>")[0]


def scrape(website, endpoint):
    file = open("resources/" + endpoint + ".json", "w")
    file.write(get_json(websites[website][endpoint]))
