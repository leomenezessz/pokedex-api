from fastapi import FastAPI
from client.pokeapi import PokeApi

app = FastAPI()
poke_api = PokeApi()


@app.get("/pokemon/{name}")
async def find_pokemon_by_name(name: str):
    return await poke_api.find_pokemon(name)
