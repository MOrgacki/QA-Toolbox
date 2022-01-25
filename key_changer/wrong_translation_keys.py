import json

# Opening JSON file
pl = open('pl-PL.json')
de = open('de-DE.json')
good_keys = []

# returns JSON object as
# a dictionary
data_pl = json.load(pl)
data_de = json.load(de)

temp_de = data_de.copy()
temp_pl = data_pl.copy()


# data manipulation
for k, v in temp_pl.items():
    good_keys.append(k)

for (k, v), keys in zip(list(data_de.items()), list(good_keys)):

    temp_de[keys] = temp_de.pop(k)


# store final JSON
open('de-DE-fixed.json', "w",
     encoding="utf8").write(json.dumps(temp_de, indent=4, ensure_ascii=False))
