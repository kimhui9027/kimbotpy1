import discord

client = discord.client

@client.event
async def on_ready():
    print("ready")
    game = discord.Game("".투표 투표주제.투표1.투표2.투표3.~"을 쳐서 투표를 하실 수 있습니다!")

@client.event
async def on_message(message):
    if message.content.startswith(".투표"):
        vote = message.content[4:].split(".")
        await message.channel.send('투표 주제' + ' = ' + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send('```' + vote[i] + '```')
        await message.channel.send("(원하는 이모지를 추가하시오.)")


client.run("NzI4NjAxNzYxMTIzNjYzODgy.Xv8xTQ.GChXzcuPVqE-vYDO6Ar17EW5RUU")
