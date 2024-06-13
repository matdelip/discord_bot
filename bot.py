
import discord
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

load_dotenv()

token = str(os.getenv('TOKEN'))

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

print('This is my Ec2_metadata.region:', ec2_metadata.region)
print('This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
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


         