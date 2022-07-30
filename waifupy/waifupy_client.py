import requests
from waifupy.waifu import Waifu

class WaifuPyClient:
    BASE_URL = 'https://api.waifu.pics'
    def __init__(self, session=None):
        """
        WaifyPyClient class constructor.
        """
        self.session = session or requests.Session()

    def close(self):
        """
        Close the session.
        """
        self.session.close()

    def get_sfw_image(self, category='waifu'):
        """
        Get a random SFW image from a specified category.
        Category is optional.
        """
        response = self.session.get(self.BASE_URL + f'/sfw/{category}')
        return self.__process_response(response)
    
    def get_nfsw_image(self, category='waifu'):
        """
        Get a random NSFW image from a specified category.
        Category is optional.
        """
        response = self.session.get(self.BASE_URL + f'/nfsw/{category}')
        return self.__process_response(response)
    
    def __process_response(self, response: requests.Response):
        """
        Get a waifu from a reponse.
        """
        if response.status_code != 200:
            raise Exception(f'Error: {response.status_code}')
        return Waifu.from_json(response.json())