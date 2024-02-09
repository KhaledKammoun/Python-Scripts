import json

with open('articles.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


additional_data = {
    "U": "",
    "M": "",
    "Q_manuelle": None,
    "Q_auto": None,
    "prix_u": None,
    "APS": None,
    "APD": None,
    "Dossier_C": None,
    "Marche": None
}
def update(item) :
    data_var = item
    item = {}
    item["ID"] = data_var["ID"]
    item["Name"] = data_var["Name"]
    for key, value in additional_data.items():
        item[key] = value
    if (not data_var["Description"]) :
        item["Description"] = None
    else :
        item["Description"] = [data_var["Description"]]
        
    item["Children"] = data_var["Children"]
    return item

for i in range(len(data["Items"]["Item"])) :

    data["Items"]["Item"][i] = update(data["Items"]["Item"][i])

    if data["Items"]["Item"][i]["Children"] != "" :
        for j in range(len(data["Items"]["Item"][i]["Children"]["Item"])) :
            data["Items"]["Item"][i]["Children"]["Item"][j] = update(data["Items"]["Item"][i]["Children"]["Item"][j])
            if data["Items"]["Item"][i]["Children"]["Item"][j]["Children"] != "" :
                for k in range(len(data["Items"]["Item"][i]["Children"]["Item"][j]["Children"]["Item"])) :
                    data["Items"]["Item"][i]["Children"]["Item"][j]["Children"]["Item"][k] = update(data["Items"]["Item"][i]["Children"]["Item"][j]["Children"]["Item"][k])


with open('your_file.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
