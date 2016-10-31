import requests

url = "http://swapi.co/api/people/1"

json_result = requests.get(url).json()

films = json_result.get("films")

for film in films:
    film_result = requests.get(film).json()
    split_crawl = film_result["opening_crawl"].split("\r\n")
    print (film_result["opening_crawl"])
    for line in split_crawl:
        print(line)
