import discord


description = "Enter bot ID witch the bot sends as invite link to zekro (Server Owner)"


async def ex(message, client):
    args = message.content.split(" ")
    if len(args) > 1:
        await client.send_message(message.server.get_member("221905671296253953"), embed=discord.Embed(
            title=message.author.name,
            description="https://discordapp.com/oauth2/authorize?client_id=%s&scope=bot" % args[1]))
        await client.send_message(message.author, embed=discord.Embed(colour=discord.Color.green(),
                                                                      description="Invite link (*https://discordapp.com/oauth2/authorize?client_id=%s&scope=bot*) send to zekro (Server Owner)." % args[1]))
        await client.delete_message(message)
    else:
        await client.send_message(message.channel, "**COMMAND USAGE:**\n`!invite <botID>`\n\n*The bot ID you get from there (Client ID: ...): \nhttps://discordapp.com/developers/applications/me*")
