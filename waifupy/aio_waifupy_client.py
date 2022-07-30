import aiohttp
from waifupy.waifu import Waifu

class AioWaifuPyClient:
    BASE_URL = 'https://api.waifu.pics'
    def __init__(self, session=None):
        """
        Asynchronous WaifyPyClient class constructor.
        """
        self.session = session or aiohttp.ClientSession()
    
    async def close(self):
        """
        Close the session.
        """
        await self.session.close()

    async def get_sfw_image(self, category='waifu'):
        """
        Get a random SFW image from a specified category.
        Category is optional.
        """
        response = await self.session.get(self.BASE_URL + f'/sfw/{category}')
        return await self.__process_response(response)
    
    async def get_nfsw_image(self, category='waifu'):
        """
        Get a random NSFW image from a specified category.
        Category is optional.
        """
        response = await self.session.get(self.BASE_URL + f'/nfsw/{category}')
        return await self.__process_response(response)
    
    async def __process_response(self, response: aiohttp.ClientResponse):
        """
        Get a waifu from a reponse.
        """
        if response.status != 200:
            raise Exception(f'Error: {response.status}')
        return Waifu.from_json(await response.json())