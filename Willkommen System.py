import discord
from discord.ext import tasks, commands

WELCOME_CHANNEL_ID = CHAT_ID  	 # Willkommenskanal
PIN_CHANNEL_ID = CHAT_ID     	 # Kanal, in dem der PIN eingegeben werden muss
VERIFIED_ROLE_ID = ROLE_ID 	 # Replace with the actual role ID

# Setze deinen Token hier ein
TOKEN = 'TOKEN_HIER'

# Der PIN, den die Benutzer eingeben müssen
PIN_CODE = "2021"

# Initialize the bot
bot = commands.Bot(command_prefix="!")  # Use any prefix you like

@bot.event
async def on_member_join(member):
    guild = member.guild
    member_count = guild.member_count

    channel_welcome_message = (f'Willkommen auf dem Server, {member.mention}!\n'
                               f'Du bist nun Mitglied Nummer **{member_count}** auf diesem Server!')

    private_message = (f'Hallo **{member.name}**, willkommen auf unserem Discord-Server! '
                       f'Wir freuen uns, dich hier zu haben. Wenn du Fragen hast oder Hilfe benötigst, zögere nicht, uns zu kontaktieren')

    image_path = 'willkommen.jpg'

    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel is not None:
        try:
            with open(image_path, 'rb') as f:
                picture = discord.File(f)
                await channel.send(content=channel_welcome_message, file=picture)
        except FileNotFoundError:
            print(f'Die Bilddatei {image_path} wurde nicht gefunden.')
    else:
        print(f'Kanal mit der ID {WELCOME_CHANNEL_ID} nicht gefunden.')

    try:
        await member.send(private_message)
    except discord.Forbidden:
        print(f'Konnte {member.name} keine private Nachricht senden.')

@bot.event
async def on_message(message):
    # Ignoriere Nachrichten vom Bot selbst
    if message.author == bot.user:
        return

    # Überprüfe, ob die Nachricht im richtigen Kanal gesendet wurde
    if message.channel.id == PIN_CHANNEL_ID:
        if message.content == PIN_CODE:
            role = message.guild.get_role(VERIFIED_ROLE_ID)
            if role:
                await message.author.add_roles(role)
                await message.delete()  # Lösche die Nachricht mit dem PIN-Code
                try:
                    await message.author.send(f"Du hast den korrekten PIN eingegeben und die Rolle **{role.name}** erhalten!")
                except discord.Forbidden:
                    print(f"Konnte {message.author.name} keine private Nachricht senden.")
            else:
                await message.channel.send("Die Rolle konnte nicht gefunden werden.", delete_after=4)
        else:
            await message.author.send("Falscher PIN, bitte versuche es erneut.")
            await message.delete()  # Lösche die Nachricht bei falschem PIN

    # Verarbeite andere Nachrichten
    await bot.process_commands(message)

# Startet den Bot
bot.run(TOKEN)
