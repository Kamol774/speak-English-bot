import requests

app_id = "62b446b5"
app_key = "c2fe6960887f53b88999a767283d7e34"
language = "en-gb"


def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return print("Bunday so'z mavjud emas")

    output={}
    definitions=[]
    for i in range(len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])):
        definitions.append(f"👉🏻{res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['definitions']}")
    output['definitions']=definitions

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio']=res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output

if __name__ == '__main__':
    from pprint import pprint as print
    # print(getDefinitions('america'))
    print(getDefinitions('sun'))