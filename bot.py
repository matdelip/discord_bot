
import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

client = discord.Bot()
token = os.getenv('TOKEN')

.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    print(f'Message {user_message} by {username} on {channel}')
    if message.author == client.user:
        return
    if channel == "random":
           if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
           elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
            elif user_message.lower() == "tell me a joke":
            jokes = ["your life.", "Did you hear the rumor about butter? Well, I'm not going to spread it."]
            await message.channel.send(random.choice(jokes))
client.run(token)


         