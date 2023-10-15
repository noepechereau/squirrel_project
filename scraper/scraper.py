import requests

endpoints = {
    "football": "https://www.winamax.fr/paris-sportifs/sports/1",
}

user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/87.0.4280.141 Safari/537.36")


def get_page(url):
    response = requests.get(url, headers={"User-Agent": user_agent})
    return response.text


def get_json(url):
    html = get_page(url)
    return html.split("var PRELOADED_STATE = ")[1].split(";</script>")[0]


def scrape(endpoint):
    file = open("resources/" + endpoint + ".json", "w")
    file.write(get_json(endpoints[endpoint]))
