import requests
from settings import local_settings

app_id = local_settings.APP_ID
app_key = local_settings.APP_KEY
language = "en-gb"


def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output={}
    definitions=[]
    for i in range(len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])):
        definitions.append(f"👉🏻{res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['definitions']}")
    output['definitions']='\n'.join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio']=res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output

if __name__ == '__main__':
    from pprint import pprint as print
    # print(getDefinitions('america'))
    print(getDefinitions('sun'))