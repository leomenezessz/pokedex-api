import httpx

from model.pokemon import Pokemon


class PokeApi:
    _BASE_URL = 'https://pokeapi.co/api/v2/pokemon'

    async def find_pokemon(self, pokemon) -> Pokemon:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self._BASE_URL}/{pokemon}")

        return Pokemon.parse_obj(response.json())
