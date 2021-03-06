import subprocess
import discord
import perms
import STATICS


description = "Start zekro bot if it went offline"


async def ex(message, client):
    if not perms.check(message.author):
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("Sorry, but you need to have role `%s` to use this command!" % STATICS.PERMS_ROLE_1)))
    elif message.server.get_member("272336949841362944").status.__str__() != "offline":
        text = "zekroBot is currently online. Please dont start the bot if its still online.\nIf zekroBot is not reaction to commands, please use `!restart` command."
        await client.send_message(message.channel,
                                  embed=discord.Embed(description=text, colour=discord.Color.red()))
    else:
        subprocess.Popen(["bash", "start.sh"])
        await client.send_message(message.channel, embed=discord.Embed(description="Starting zekroBot...", colour=discord.Color.green()))
