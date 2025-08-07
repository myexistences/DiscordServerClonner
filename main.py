import asyncio
from utils.innit import *
from func.cloner import *
from func.clone_stickers import *
from func.clone_emojis import *
from func.guild_info import *
from func.token_checker import *

# Main Menu
async def menu():
    while True:
        clear()
        logo()
        o = f"""
                {b}[{w}01{b}]{w} Clone Server    {b}[{w}04{b}]{w} Server Info
                {b}[{w}02{b}]{w} Clone Sticker's {b}[{w}05{b}]{w} Token Checker
                {b}[{w}03{b}]{w} Clone Emoji's"""
        print(o)
        cs = input(f"                {b}[{w}@myexistences{b}]{w} >> ")

        if cs == "1":
            await cloner()
        elif cs == "2":
            await sticker_cloner()
        elif cs == "3":
            await emoji_cloner()
        elif cs == "4":
            await guild_info()
        elif cs == "5":
            await token_checker()

# Start Menu
if __name__ == "__main__":
    asyncio.run(menu())