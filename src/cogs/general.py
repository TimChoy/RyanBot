import discord
from discord.ext import commands

class GeneralCog(commands.Cog, name="General Commands"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='ping', brief='pong')
    async def ping(self, ctx):
        print(f'[Log] ping from {ctx.author}')
        ctx.send('pong')

    @commands.command(name='hello', brief='RyanBot says hi!')
    async def hello(self, ctx):
        print(f'[Log] hello from {ctx.author}')
        await ctx.send(f'Hello {ctx.author.mention}!')
    
    @commands.command(name='say', brief='Make RyanBot say something!')
    @commands.guild_only()
    async def say(self, ctx, *, msg=None):
        print(f'[Log] say "{msg}" from {ctx.author}')
        await ctx.message.delete()
        await ctx.send(msg)
    
def setup(bot):
    bot.add_cog(GeneralCog(bot))