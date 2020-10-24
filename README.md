# YouTube Description Search Engine
## Set up
Python version : 3.7.9
1. run `python3 -m pip install -r requirements.txt`
## Retrieves Google Search results
1. modify config.py to add your api key and cse key
2. run: `python3 cse.py`
## Retrieves Video Ids from search results
1. run `python3 download_youtube_data.py google_search.json video_ids.txt`
## Retrieves Youtube Data
1. run `python3 download_youtube_data.py video_ids.txt`
## Prepares for Whoosh Index
1. run `python3 create_data_for_indexing.py`
## Create Whoosh Indexing
1. run `python3 create_whoosh_index.py`
## Query on Whoosh
1. run `python3 query_on_whoosh.py home 2 1`
