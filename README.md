![banner](https://raw.githubusercontent.com/teixeirazeus/waifupy/master/images/waifupy_header.png)  
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ecb1a0c929044119bfc32a5e987a095a)](https://www.codacy.com/gh/teixeirazeus/waifupy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=teixeirazeus/waifupy&amp;utm_campaign=Badge_Grade)

Unofficial minimal python wrapper for waifu.pics API.

## Installation

```bash
pip install git+https://github.com/teixeirazeus/waifupy
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
