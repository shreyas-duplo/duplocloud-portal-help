import json
import yaml

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
    data = yaml.load(f,Loader=yaml.FullLoader)
    formName = filename.replace(".yml", "")
    forms[formName] = data


with open("en.json", "w") as outfile:
    json.dump(finalJson, outfile, indent=4)
