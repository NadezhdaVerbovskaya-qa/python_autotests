import requests

token='d937b358db69926505189ed595d98185'
host='https://pokemonbattle-stage.me:9101/'

ans_create_pokemon=requests.post(f'{host}/pokemons', json=
                     {
    "name": "Kate",
    "photo": "https://dolnikov.ru/pokemons/albums/585.png"
}, headers={"Content-Type":"application/json", "trainer_token":token})

print(ans_create_pokemon.text)

ans_change_pokemon=requests.put(f'{host}/pokemons', json=
                     {
    "pokemon_id": "1056",
    "name": "Patrik",
    "photo": "https://dolnikov.ru/pokemons/albums/585.png"
}, headers={"Content-Type":"application/json", "trainer_token":token})

print(ans_change_pokemon.text)

ans_pokemon_add_pokeball=requests.post(f'{host}/trainers/add_pokeball', json=
                     {
    "pokemon_id": "1056"
}, headers={"Content-Type":"application/json", "trainer_token":token})

print(ans_pokemon_add_pokeball.text)


