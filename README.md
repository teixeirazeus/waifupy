![banner](https://raw.githubusercontent.com/teixeirazeus/waifupy/master/images/waifupy_header.png)  
Unofficial minimal python wrapper for waifu.pics API.

## Installation

```bash
pip install waifupy
```

## Usage
### Example 1

```python
from waifupy import WaifuPyClient
from waifupy import WaifuCategory

# Create a WaifuPyClient object
client = WaifuPyClient()

# Get your waifu
waifu = client.get_sfw_image()

# Open the image in the web browser
waifu.display_in_webbrowser()

# Print all waifus categories
print(WaifuCategory.sfw)
print(WaifuCategory.nsfw)

# Get your waifu in a specific category
waifu = client.get_sfw_image("smile")

# Download the image to a file
waifu.download(image_name="my_waifu")

# Close the client
client.close()
```

### Example 2
#### Asynchronous usage

```python
import asyncio
from waifupy import AioWaifuPyClient

async def main():
    client = AioWaifuPyClient()
    waifu = await client.get_nsfw_image()
    waifu.download(image_name="my_waifu")
    await client.close()

asyncio.run(main())
```