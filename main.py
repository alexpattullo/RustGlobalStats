import json
import discord
import random
from discord.ext import commands, tasks
import aiohttp
import asyncio

with open("./config.json", "r") as file:
    secret_file = json.load(file)

client = commands.Bot(command_prefix="",help_command=None,intents=discord.Intents.default())

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@tasks.loop(seconds=20.0)
async def global_status():
    statuss = []

    #Bans
    url = "https://api.battlemetrics.com/bans?filter[banList]=" + secret_file["BanListID"] + "&include=user,server"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers= {"Authorization" : "Bearer " + secret_file["BmApiKey"]}) as resp:
            if resp.status != 200:
                print(f"Error with status code: {resp.status}")
            if resp.status == 200:
                banlist = json.loads(await resp.text())
                activebans = banlist["meta"]["active"]
                abans = f"Active Bans : {activebans}"
                statuss.append(abans)

    #AllServers
    connected = 0
    que = 0
    entity = 0 
    max = 0
    url = f"https://api.battlemetrics.com/servers?filter[organizations]=" + secret_file["BmOrgID"]
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers= {"Authorization" : "Bearer " +secret_file["BmApiKey"]}) as resp:
            if resp.status != 200:
                print(f"Error with status code: {resp.status}")
            if resp.status == 200:
                resp_dict = json.loads(await resp.text())

                for serverid in resp_dict["data"]:
                    connected = connected + serverid["attributes"]["players"]
                    max =  max + serverid["attributes"]["maxPlayers"]
                    que = que + serverid["attributes"]["details"]["rust_queued_players"]
                    entity = entity + serverid["attributes"]["details"]["rust_ent_cnt_i"]

    if que >= 1:
        statuss.append(f"Global Pop : {connected} Ingame (+{que})")
    else:
        statuss.append(f"Come join {connected} others!")

    if que > 0:
        que = f"{que} Queued Users"
        statuss.append(que)

    entity = f"{entity} Total Entities"
    statuss.append(entity)
    
    await client.change_presence(status=discord.Status.online,activity=discord.Game(name=random.choice(statuss)))

@global_status.before_loop
async def before_global_status():
    await client.wait_until_ready()

async def main():
    if __name__ == "__main__":
        async with client:
            global_status.start()
            await client.start(secret_file["BotToken"],reconnect=True)
asyncio.run(main())
