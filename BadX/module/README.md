<h1> Add your Own Plugin <h1>

```python
from . import TheBadX
from pyrogram import Client, filters

@Client.on_message(
    filters.command("hi", , prefixes=TheBadX.handler)
)
async def hi(_, message):
    if await TheBadX.sudo.sudoFilter(message, 3): #sudo filter
        return
    await message.reply("Hello")
```
