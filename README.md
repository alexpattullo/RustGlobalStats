# Examples of it setup!
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834595574685707/Screenshot_2022-03-22_at_14.16.37.png)
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834595138502666/Screenshot_2022-03-22_at_14.21.28.png)
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834594622595072/Screenshot_2022-03-22_at_14.14.29.png)
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834594169585764/Screenshot_2022-03-22_at_14.14.07.png)


# Rust Global Stats to Discord Bot in Python
Simple bot utilising the battlemetrics api to display your org pop & stats to a discord bot!

NB : If your not using a bot container :
You will need to install python and git (must be 3.7+)
(https://www.youtube.com/watch?v=XF_rklW9XkU&ab_channel=CBTNuggets)

Also might need to install git if you get an error like this (https://i.imgur.com/1Cl6whB.png)
https://www.linode.com/docs/guides/how-to-install-git-on-linux-mac-and-windows/



1. Go to https://discord.com/developers/applications, create a new bot application

2. Create a bot & enable all intents -> https://imgur.com/sZtM5N3

3. Go to O2Auth - > URL Generator -> Select bot & invite the bot to your discord

4. Go to https://www.battlemetrics.com/developers, create a token with perms to view your ban list

# Example Config
```
{
    "BotToken": "",
    "BmOrgID": "",
    "BanListID": "",
    "BmApiKey": ""

}
```

5. Your org id is the numbers at the end of the org management page eg here it is : 41737 -> https://imgur.com/mey9Wun

6. Your Ban list id is the strung at the end of your ban list eg here it is : d8461f90-fbfe-11e9-a94e-7d2750722003 -> https://imgur.com/idqYZvq

* Fill in config.json 
* Then run **pip install -r requirements.txt** in your console and run the main.py file

For any issues message me at Skizzy#0037(307862931213778946) or reach out to me via lone design / codefling tickets etc.

Suggested hosts -> https://serverstarter.host/ or anything offering a simple bot container - Python is key!


