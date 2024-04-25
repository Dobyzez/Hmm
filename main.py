import discord

# Define your Discord token
TOKEN = 'your_discord_token'

# Define the channel ID you want to decode messages from
CHANNEL_ID = 'your_channel_id'

# Create a Discord client
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == int(CHANNEL_ID):
        print(f'Message from {message.author}: {message.content}')

# Run the client
client.run(TOKEN)
