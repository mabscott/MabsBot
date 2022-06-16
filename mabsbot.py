from twitchio.ext import commands
from twitchio.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    token=os.getenv("CLIENT_TOKEN"),
    client_secret=os.getenv("CLIENT_SECRET"),
)

bot = commands.Bot(
    token=os.getenv("TOKEN"),
    client_id=os.getenv("CLIENT_ID"),
    nick=os.getenv("NICK"),
    prefix="!",
    initial_channels=[os.getenv("INITIAL_CHANNELS")],
)


@bot.event
async def event_message(ctx):
    print(ctx.author)
    print(ctx.content)
    print("heree")
    await bot.handle_commands(ctx)


@bot.command(name="test")
async def test_command(ctx):
    await ctx.send("this is a test response")


@bot.command(name="who")
async def get_chatters(ctx):
    chatters = ctx.chatters
    display_names = ", ".join([chatter.display_name for chatter in chatters])
    await ctx.send(f"In chat: {display_names}")


if __name__ == "__main__":
    bot.run()
