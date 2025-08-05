import asyncio
from bot_config import bot, TOKEN

from commands import setup

async def main():
    await setup(bot)
    
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
