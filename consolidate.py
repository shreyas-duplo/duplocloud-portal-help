import json

import os
# assign directory
directory = 'forms'

finalJson = {
    "lang" : "en",
    "data" : {
        "FORM" : {}
    }
}
forms = finalJson["data"]["FORM"];
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = open(directory + "/" + filename)
    data = json.load(f)
    formName = filename.replace(".json", "")
    forms[formName] = data


with open("en.json", "w") as outfile:
    json.dump(finalJson, outfile, indent=4)
