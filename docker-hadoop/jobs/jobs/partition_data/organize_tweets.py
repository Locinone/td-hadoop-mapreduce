import json
from datetime import datetime
import os
import shutil

# dossier local temporaire
# local_base = '/app/twitter_data_partitioned' # on docker
local_base = '../twitter_data_partitioned_local' # on my macbook

os.makedirs(local_base, exist_ok=True)

# lecture des tweets
with open('tweets_with_locations.json', 'r') as f:
    tweets = json.load(f)

# organiser par année/mois
for tweet in tweets:
    ts = datetime.strptime(tweet['timestamp'], '%Y-%m-%d %H:%M:%S')
    year = ts.year
    month = f"{ts.month:02d}"
    local_dir = os.path.join(local_base, f'year={year}', f'month={month}')
    os.makedirs(local_dir, exist_ok=True)
    
    local_file = os.path.join(local_dir, 'tweets.json')
    with open(local_file, 'a', encoding='utf-8') as writer:
        writer.write(json.dumps(tweet) + '\n')

print("Local organization done. Ready to push to HDFS.")