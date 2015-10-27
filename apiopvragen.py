import time
import hashlib
import requests
import json
b1fd678511d1c8f24b114a30136d6bcf
timestamp = str(time.time())
private_key = "f488e1be0e07f9091bc71101b6061bcb8fa08445"
public_key = "b1fd678511d1c8f24b114a30136d6bcf"

hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())

url = "http://gateway.marvel.com:80/v1/public/characters?ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest
print(url)

response = requests.get(url)
jsontext = json.loads(response.text)

print(json.dumps(jsontext, sort_keys=True, indent=4)) # om de JSON leesbaar te printen...

print("\nGevonden characters in comics:")
for item in jsontext['data']['results'][0]['comics']['items']: # deze volgorde kun je uit het zojuist geprinte resultaat halen of uit de Marvel documentatie!
    print(item['name'])

print("\nGevonden characters in series:")
for item in jsontext['data']['results'][0]['series']['items']: # deze volgorde kun je uit het zojuist geprinte resultaat halen of uit de Marvel documentatie!
    print(item['name'])
