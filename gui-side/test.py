#test-file
import json
 
# Opening JSON file
f = open('./settings.json')
data = json.load(f)
print (data["username"])
# Closing file
f.close()
