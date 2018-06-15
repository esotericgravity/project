# to setup:

add this bot to your discord server 
you probably want to just set up your own bot first
get your client id and token, then go to https://discordapp.com/oauth2/authorize?client_id=xxxxxx&scope=bot
set token in line 6 equal to your bot's token
clone this repo
change directory to the location it was saved to
edit line 71 in the file 'bot_init.py' to the username of the person you want to troll
edit the strings in line 72 to whatever you want, the variable in that line (ctx.message.author.name) is their username
run the command 'python bot_init.py'in the directory of the repo
enter "!tictactoe" in your server and play tictactoe, if the person you enteres in line 71 runs the command you message will appear
