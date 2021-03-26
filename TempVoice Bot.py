#import libraries
import os

import discord
from dotenv import load_dotenv

# token
load_dotenv()
TOKEN = os.getenv('ODE5OTgwODE5MTY2MjY1MzU0.YEugpQ.acFqYeUUgAQmC_dV1qHNOuKr5IU')

support_channel = 792785756636184587

channel_2_people = 792843227866726470
channel_5_people = 792849033119006780
channel_10_people = 792849062101123073
channel_no_limit = 792849089045856256

group_channels = []
onleave_channels = []

# channel
client = discord.Client()


async def createSupportChannel(member, category):
    global onleave_channels

    # Generate new voice channel
    new_channel = await category.create_voice_channel(f"{member.name} ✋🏼")
    onleave_channels.append(new_channel.id)

    # Move user to newly created voice channel
    await member.move_to(new_channel)
    print("Channel", new_channel.name, "created")


async def createGroupChannel(member, limit, category):
    global group_channels

    # Generates new group channel with group #
    new_channel = await category.create_voice_channel(f"Group #{len(group_channels) + 1}")

    # Adds a user limit to newly generated channel if required
    if limit > 0:
        await new_channel.edit(user_limit=limit)

    # Adds newly generated channel id to lists
    group_channels.append(new_channel.id)
    onleave_channels.append(new_channel.id)

    # Move user to newly created voice channel
    await member.move_to(new_channel)
    print("Channel", new_channel.name, "created")


async def updateGroupChannels(deleted_channel):
    # Updates name numbering of group channels
    for channel in deleted_channel.category.channels:
        if channel.id in group_channels:
            await channel.edit(name=f"Group #{group_channels.index(channel.id) + 1}")


async def checkAfterChannels(member, after_channel):
    # Checks if channel joined is a support channel
    if after_channel.id == support_channel:
        print(f"{member.name} entered support channel")
        await createSupportChannel(member, after_channel.category)

    # Checks if channel joined is 2 person channel
    elif after_channel.id == channel_2_people:
        print(f"{member.name} entered 2 person channel")
        await createGroupChannel(member, 2, after_channel.category)

    # Checks if channel joined is 5 person channel
    elif after_channel.id == channel_5_people:
        print(f"{member.name} entered 5 person channel")
        await createGroupChannel(member, 5, after_channel.category)

    # Checks if channel joined is 10 person channel
    elif after_channel.id == channel_10_people:
        print(f"{member.name} entered 10 person channel")
        await createGroupChannel(member, 10, after_channel.category)

    # Checks if channel joined is no limit channel
    elif after_channel.id == channel_no_limit:
        print(f"{member.name} entered no limit channel")
        await createGroupChannel(member, 0, after_channel.category)


async def checkBeforeChannels(before_channel):
    # Check if channel should be deleted and is empty
    if before_channel.id in onleave_channels and len(client.get_channel(before_channel.id).members) == 0:
        onleave_channels.remove(before_channel.id)

        # Delete empty channel
        await client.get_channel(before_channel.id).delete()

        # Check if channel is a group channel
        if before_channel.id in group_channels:
            group_channels.remove(before_channel.id)
            await updateGroupChannels(before_channel)

        print("Channel", before_channel.name, "deleted")


async def checkChannels(member, before_channel, after_channel):

    # Checks if channel left exists
    if before_channel != None:
        await checkBeforeChannels(before_channel)

    # Checks if channel joined exists
    if after_channel != None:
        await checkAfterChannels(member, after_channel)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" ~help"))

@client.event
async def on_voice_state_update(member, before, after):
    await checkChannels(member, before.channel, after.channel)


client.run(TOKEN)
