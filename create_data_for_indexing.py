from pathlib import Path
import json

paths = [str(x) for x in Path('./youtube_data').glob('**/*.json')]
results = []
for path in paths:
    with open(path, 'r') as f:
        data = json.load(f)
        # insert your code here
    for p in data['items']:
        print('id: ' + p['id'])
        print('title: ' + p['title'])
        print('description: ' + p['description'])
        print('')
with open('data_for_indexing.json', 'w') as dump_file:
    json.dump(results, dump_file)
