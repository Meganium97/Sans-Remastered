# Sans-Remastered
Basically Sans but remastered.
It serves a whole new purpose now that the [original snas](https://github.com/Lazr1026/Sans) has been archived.

Open to PR's. I'm still figuring out how to do python.
### Instructions - selfhosting
1. Install [Python3.8](https://www.python.org/downloads/) or newer.
2. Install everything in requirements.txt with `pip install -r path/to/requirements.txt` (if this fails try `pip3 install -r path/to/requirements.txt`)
3. Place the token in a file called `token.json` in the same directory as `sans.py`, then run `sans.py`.
Enjoy hosting Sans(-Remastered)!
### Instructions - Userphone
1. Follow steps 1 and 2 from Instructions - selfhosting
2. Put your input channel in place of the numbers in the line `bot.channel = bot.get_channel(770100020736688128)`
3. Put your output channel(s) in place of the numbers in the line `if message.channel.id in (794603732947042337, ):`. Remember to keep the comma at the end.
4. Put your output channel (just one)(from step 3) in place of the numbers in the line `bot.channel = bot.get_channel(770100020736688128)` in the file userphone-1.py.
5. Put your input channel (from step 2) in place of the numbers in the line `if message.channel.id in (794603732947042337, ):` in userphone-1.py. Once again, remember to keep the comma at the end.
6. Run both userphone.py files. You are now done!

Kudos to [Gnome!](https://github.com/Gnome-py) for making the userphone code and helping me make it work.

### Invite link
if you want to invite this shit of a bot to your server invite link is [here](https://discord.com/api/oauth2/authorize?client_id=754750158125924483&permissions=805431350&scope=bot)
