import requests
from bs4 import BeautifulSoup

headers = {

"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

}

########## search for band
search_url = "http://search.azlyrics.com/search.php?q="
artist = "the+mountain+goats"
body = requests.get(search_url + artist)
souper = BeautifulSoup(body.text, "html.parser")
all_a_tags = (souper.findAll("a"))
next_page = all_a_tags[28].get("href")


############## find all songs
body = requests.get(next_page, headers=headers)
souper = BeautifulSoup(body.text, "html.parser")
all_a_tags = souper.findAll("a")[32:496]
song_link_list = []
for counter, tag in enumerate(all_a_tags):
    if not tag.get('rel') and tag.get("href"):
        song_link_list.append(tag.get("href"))

for song_link in song_link_list:
    new_song_link = song_link.replace("..", "http://www.azlyrics.com")
    song_page = requests.get(new_song_link,headers=headers)
    souper = BeautifulSoup(song_page.text, "html.parser")
    song_div = souper.findAll('div')[22]
    print(song_div.text)
    input()
