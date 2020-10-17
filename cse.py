import pprint, json
from googleapiclient.discovery import build
import config
my_api_key = config.my_api_key #The API_KEY you aquired
my_cse_id = config.my_cse_id # The search-engine-ID you created
# cse: custom search engine
my_search_topic = 'Playstation 5' # The phrase im searching in Twitter

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch","v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
if __name__ == '__main__':
    myList = []
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=0)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=11)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=21)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=31)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=41)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=51)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=61)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=71)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=81)
    myList.extend(results)
    results = google_search(my_search_topic, my_api_key, my_cse_id, start=91)
    myList.extend(results)
    with open('google_search.json', 'w') as f:
        json.dump(myList, f)
