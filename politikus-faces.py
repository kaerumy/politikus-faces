import requests
import urllib
import pathlib

HEADERS = {'Accept': 'application/json'}
BASE_URL = "https://politikus.sinarproject.org/@search?portal_type=Person" + \
           "&fullobjects=1"

for i in range(0, 1472, 25):
    b_start = i+1
    URL = BASE_URL + "&b_start=" + str(b_start)
    r = requests.get(URL, headers=HEADERS)

    for person in r.json()['items']:
        if person['image']:
            filename_suffix = pathlib.Path(person['image']['download']).suffix
            filename = person['id'] + filename_suffix
            print(filename)

            photo = requests.get(person['image']['download'])

            with open(filename, "wb") as f:
                f.write(photo.content)
                f.close
