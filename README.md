# 🎙️ TempVoice Discord Bot
A bot developed for generating temporary voice channels on Discord. Inspired by [VoiceMaster](https://www.voicemaster.xyz/).

This bot was dedicated for the official Discord Events Server for Google Developer Student Club McMaster, to help manage and reduce the amount of unused voice channels.

## 📑 Contents

1. **[How it Works](#-how-it-works)**  
1.1 [Dependencies](#dependencies)  
1.2 [Discord API](#discord-api)  
2. **[How to Install](#-how-to-install)**  

## ⚙️ How it Works

### Dependencies 

1. Create your own Discord server
    <details>
      <summary>More Info</summary>

      [Documentation on how to create a Discord Server](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-)

    </details>
    

2. A virtual private server to host the bot 24/7
    <details>
      <summary>More Info</summary>

      [How I hosted the Discord bot](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/#:~:text=How%20to%20Set%20Up%20the%20Bot%20to%20Run%20Continuously)

    </details>

3. Generate a new Discord Bot token that the program will connect to
    <details>
      <summary>More Info</summary>

      [How to get a Discord Bot token](https://www.writebots.com/discord-bot-token/)

    </details>

### Discord API
#### What is it?

[Discord API](https://discord.com/developers/docs/intro) (Application Programming Interface) allows for communication between your program and your Discord bot by making different kinds of calls and requests.

#### How does it work?

The Discord bot listens for the `on_voice_state_update()` event, which is triggered every time a user enters or leaves an existing voice channel. Three arguments are given: `member` (the user who triggered the event), `before` (the channel that the user came from), and `after` (the channel that the user went to).

Using the arguments, the `checkChannels()` function checks the `after` channel to test if the user has entered a specific channel in which a new voice channel should be generated, and checks the `before` channel to test if the user was the last user to leave a specific channel, leaving it empty, triggering the voice channel to be deleted.

The server has a dedicated `❔︱Click here for help!` voice channel, where new voice channel will be generated using `category.create_voice_channel()` upon request when a user joins the `❔︱Click here for help!` channel. Then the user will be moved to the newly generated voice channel using `member.move_to()`. This support voice channel allows for anyone to start a new call that notifies support staff when a participant is in need of help, and can join the temporary voice channel to aid them.

The server also has a dedicated voice channels for generating group calls (`⛺︱2 People`, `🏠︱5 People`, `🏨︱10 People`, `🎉︱No Limit`), where a new voice channel will be generated using `category.create_voice_channel()` upon request when a user joins any of the listed dedicated voice channels. Each temporary voice channel will also be set with a user limit to how many people can join the voice channel at once, depending on the specific limit that a user requests upon generating the new voice channel.

## 🛠 How to Install
Due to the code being designed specific to the Discord server that it was intended for, there is no reason to use the exact same Discord bot in your own server.

However, feel free to use my code in the repository as a guide to help you develop your own TempVoice Discord bot for your own purposes.
