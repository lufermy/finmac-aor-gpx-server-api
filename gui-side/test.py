#test-file
import json
f = open('settings.json')
data = json.load(f)
print (data["username"])
f.close()
