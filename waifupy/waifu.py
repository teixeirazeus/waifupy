import webbrowser
import requests

class Waifu:
    def __init__(self, url):
        """
        Waifu class constructor.
        Contains the url of the image.
        """
        self.url = url

    def display_in_webbrowser(self):
        """
        Display the image.
        """
        webbrowser.open(self.url)
    
    def __str__(self):
        return self.url
    
    def download(self, image_name: str):
        """
        Download the image.
        """
        extension = self.__get_image_extension()
        with open(image_name+'.'+extension, 'wb') as f:
            f.write(requests.get(self.url).content)
    
    def __get_image_extension(self) -> str:
        """
        Get the extension of the image from the url.
        """
        image_name = self.url.split('/')[-1]
        return image_name.split('.')[-1]
        
    @staticmethod
    def from_json(json):
        """
        Create a waifu from a json.
        """
        return Waifu(json['url'])