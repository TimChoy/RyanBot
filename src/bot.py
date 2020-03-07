from discord.ext import commands
import settings

startup_extensions = ["cogs.general"]
token = settings.TOKEN
bot = commands.Bot(command_prefix="!", description="RyanBot")

@bot.event
async def on_ready():
    print("Logged in as")
    print(f'name: {bot.user.name}')
    print(f'id: {bot.user.id}')
    print("------")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Failed to load extension {extension}\n{exc}')
    
    bot.run(token, bot=True, reconnect=True)
