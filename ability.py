import requests, json

def ability(name):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(name))
    text = json.dumps(response.json(), indent=4)

    json_object = json.loads(text)


    A = []
    for i in range(len(json_object['abilities'])):
        a= json_object['abilities']
        b = a[i]
        c = b['ability']
        final = c['name']
        A.append(final)

    return A