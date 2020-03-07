from discord.ext import commands

class AdminCog(commands.Cog, name="Admin Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            print(f'[Log] Failed to load {cog}')
            await ctx.send(f'> Error: failed to load **{cog}**')
            return
        print(f'[Log] Successfully loaded {cog}')
        await ctx.send(f'> **{cog}** loaded')
    
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            print(f'[Log] Failed to unload {cog}')
            await ctx.send(f'> Error: failed to unload **{cog}**')
            return
        print(f'[Log] Successfully unloaded {cog}')
        await ctx.send(f'> **{cog}** unloaded')
    
    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            print(f'[Log] Failed to reload {cog}')
            await ctx.send(f'> Error: failed to reload **{cog}**')
            return
        print(f'[Log] Successfully reloaded {cog}')
        await ctx.send(f'> **{cog}** reloaded')

    @commands.command(name='purge', hidden=True)
    @commands.is_owner()
    async def purge(self, ctx, *, number: int):
        deleted = await ctx.channel.purge(limit=number)
        print(f'[Log] {ctx.author} purged {len(deleted)} messages.')
        await ctx.send(f'> Deleted **{len(deleted)}** messages')

def setup(bot):
    bot.add_cog(AdminCog(bot))