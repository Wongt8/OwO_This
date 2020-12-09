"""
Name : OwO This !
Version : 1.0
Auteur : Wongt8
"""
import discord,random
from discord.ext import tasks
from itertools import cycle

token = ""

client = discord.Client()

liste = [" OwO"," UwU"]

status = cycle(["$rule for help !","I will OwO you 🙃"])


@client.event
async def on_ready():
    print("Connected as : ")
    print(f"{client.user.name}#{client.user.discriminator}")
    print(client.user.id)
    print("-----------------")
    loop_game.start()

@client.event
async def on_message(message):
    def replace_(mess) :
        mess = mess.replace("r","w")
        mess = mess.replace("l","w")
        mess = mess.replace("u","uw")
        mess = mess.replace("R","W")
        mess = mess.replace("L","W")
        mess = mess.replace("U","UW")
        nb_o = mess.count("o") + mess.count("O")
        nb_u = mess.count("u") + mess.count("U")
        if mess[-1] == "?" :
            mess+= " UwU"
        elif nb_o > nb_u :
            mess += " OwO"
        elif nb_o < nb_u :
            mess += " UwU"
        else :
            mess += random.choice(liste)
        return mess
    
    if message.content == "$rule" :
        await message.channel.send("> To use the bot : \n> 1- Put **$** before the message\n> 2- **$tts** make the bot say the message with TTS\n> 3- **$del** delete your message, so only the bot answer appears\n> 4- You can use also **$del tts** or **$tts del** :)\n> 5- **Bot made by Wongt8 and not really Oshida_BCFreedom**")

    elif message.content[0] == "$" :
        mess = message.content
        i = 0
        try :
            while mess[i] == "$" or mess[i] == " " :
                i += 1
            b = mess[i:]
            a = replace_(b)
            
            if a[0:4] == "tts " :
                a = a.replace("tts","")
                print(a[1:4] == "dew")
                if a[1:4] == "dew" :
                    a = a.replace("dew","")
                    await message.channel.purge(limit=1)
                    await message.channel.send(a, tts=True)
                else :
                    await message.channel.send(a, tts=True)
            elif a[0:4] == "dew " :
                a = a.replace("dew","")
                await message.channel.purge(limit=1)
                if a[1:4] == "tts" :
                    a = a.replace("tts","")
                    await message.channel.send(a, tts=True)
                else :
                    await message.channel.send(a)
            else :
                await message.channel.send(a)
        except IndexError :
            await message.channel.send("The syntax of your message is incorrect ! I can't OwO this !")

@tasks.loop(seconds=10)
async def loop_game():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(token)
