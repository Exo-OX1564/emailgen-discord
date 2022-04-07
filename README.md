# emailgen-discord
A temporary email generator using the 1secAPI to generate unlimited temporary mails. You may use the bot to check the temp-mails' messages. It was created for the purpose of staying safe and for fun and education purposes only!


 - [Installation Guide](docs/installation-guide.md)
 - [Configuration](https://github.com/Exo-OX1564/emailgen-discord/edit/main/README.md#configuration)
 - [Start](https://github.com/Exo-OX1564/emailgen-discord/edit/main/README.md#start)
 - [Error Handling](https://github.com/Exo-OX1564/emailgen-discord/edit/main/README.md#error-handling)
 - [Host Your Bot Online 24/7 On Replit](https://github.com/Exo-OX1564/emailgen-discord/edit/main/README.md#host-your-bot-online-247-on-replit)
 - [Support](https://github.com/Exo-OX1564/emailgen-discord/edit/main/README.md#support)

# Installation Guide
I personally used replit for this project, as it's easy to handle but I suggest to have around python **3.8.12** or older (3.9).
You must have the following libs installed:
- discord
  - import commands from discord.ext 
- requests
- urllib
- os (default)
- json
- time
- inspect
- shutil
- sys
- datetime


![image](https://user-images.githubusercontent.com/95084482/162283558-cf8c9506-6b61-45de-a524-3e91f6044a40.png)


# Configuration
To set up, we only need to setup the token.
I'm pretty sure you guys know how to do that, store your variable named as **'TOKEN'** in a .env file or if you're on replit, in the secrets variable. This would make sure no-one else can access your token. One stored, call it in your code!
For replit users: it would be looking to be as similar as this:

![image](https://user-images.githubusercontent.com/95084482/162284407-52cbfed9-3ad8-499d-8aa7-527327298a22.png)

![image](https://user-images.githubusercontent.com/95084482/162284547-0163e291-09f2-4f69-a75d-6a2fec0c9454.png) #This would be at the end of your code


# Start
To start your code, simply run the following in the shell!
```py
python emailgen.py
```
And that's all! Your bot should be up and running, feel free to open any **pull requests** or DM Exo#4313 on discord if you encounter any errors!

# Error Handling
If you want any error handlings in your code, simpy state the command and discord error you experience.
For example, if I changed my code to add a time limit on my code:
```py
@client.command()
@commands.cooldown(10, 604800, commands.BucketType.user)
async def generate(ctx):
    URL = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    r = requests.get(url = URL)
    response = r.json()
    embed1=discord.Embed(title='Mail Generated!', description='Below are your 10 mails for the week! Keep it noted. We will give you another 10 next week!', color = discord.Color.blue())
    embed1.add_field(name=f"Your Temp Mail:", value= response[0])
    embed1.timestamp = datetime.datetime.utcnow()
    embed1.set_footer(text='Generated Mail! | Exo v0.1', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed1)
```
Then I wanted to add a cooldown message/error, I'd add this:
```py
@generate.error #command name of error
async def generate_error(ctx, error): #letting the generate_error know that it is an error
    if isinstance(error, commands.CommandOnCooldown): #discord error to follow is the cooldown error
        await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))
    else:
        raise error
```

# Host Your Bot Online 24/7 On Replit

If you're using replit, and you want to host your bot online **24/7**, you're in luck! UptimeRobot recently stopped allowing some of replit's hosts to be run on their  service (even though some might still work), but I have en easy solution. First of all, let's setup your keep_alive!
Make a **new file** named **keep_alive.py** and in that file, add the following code:
```py
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
```
Then go back to your main, and in the the top of your code, add:
```py
from keep_alive import keep_alive
```
Then in the 2nd to last line of your code: above the `client.run()` section, add this:
```py
keep_alive()
```
If done correctly, you should be seeing a webserver on your screen and something similarto this on your console:

![image](https://user-images.githubusercontent.com/95084482/162286750-abef9653-15da-4684-bd74-cccafd957654.png)

Then head to [FreshPing](https://www.freshworks.com/website-monitoring/) and add the webservers site on your replit (should be something like https://replitname.yourreplitusernameinlowercase.repl.co) and add it in the monitoring url, then simply add your email, sign up and you've just added your monitor to stay on 24/7!

# Support
If you need any support, feel free to open a **pull request** or DM **Exo#4313** on Discord! I'll try regularly updating this, however I'm a student who always works so might be pretty hard :D. Expect updates around every 1-2 months.
