#Requirements.txt<br />
Requirements.txt can be created using <br />
code pip -m > requirements.txt<br /><br />

#config<br />
For config.py you need to input your own api key and your own cse id into that file. <br />
After putting your cse and api key into the config file just use python3 cse.py to get the google search data. <br /><br />

#download_youtube_data<br />
For the download youtube data run the download_youtube_data_batch.sh script and redirect the data to youtube_data.txt <br />
Use bash download_youtube_data_batch.sh > youtube_data.txt for this <br /><br />

#create_data_for_indexing<br />
For the create_data_for_indexing.py just run the script and you will get the json file.<br />
Use python3 create_data_for_indexing.py <br /><br />

#create_whoosh_index<br />
For the create_whoosh_index.py run the script then run the query_on_whoosh.py script<br />
Use python3 create_whoosh_index.py then use query_on_whoosh.py<br /> <br />
