# Rust Global Stats to Discord Bot in Python
Simple bot utilising the battlemetrics api to display your server stats to a discord bot!

* Fill in config.json as below
* Then run **pip install -r requirements.txt** in your console and run the main.py file


![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834595574685707/Screenshot_2022-03-22_at_14.16.37.png)
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834595138502666/Screenshot_2022-03-22_at_14.21.28.png)
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834594622595072/Screenshot_2022-03-22_at_14.14.29.png)
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955834594169585764/Screenshot_2022-03-22_at_14.14.07.png)


# Config
config.json

```
{
    "BotToken": "",
    "BmOrgID": "",
    "BanListID": "",
    "BmApiKey": ""

}
```
* Bot Token can be found at https://discord.com/developers/applications
* Bm Org ID is the id at the end on the org management page eg 46894 is the id here 
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955835388876967978/Screenshot_2022-03-22_at_14.28.19.png)
* Ban list ID can be found under the ban list section by editing a ban list eg dc27cd80-5ecf-11ec-a3b5-5504f08c6982 is the ban list id
![Example](https://cdn.discordapp.com/attachments/860941782887039007/955836171118850129/Screenshot_2022-03-22_at_14.31.19.png)
* A Bm developer key can be obtained at https://www.battlemetrics.com/developers
