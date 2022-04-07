
#Needed libs
import discord
from discord.ext import commands
import requests
import urllib
import os
import json
import time
import asyncio #this isn't really needed so you can take it off
import inspect
import shutil
import sys
import datetime
from keep_alive import keep_alive

#Needed variables throughout the code
prefix = '' #may customise the prefix to your own likings
intents = discord.Intents.all() #may customise the intents to your likings
client = commands.Bot(command_prefix=prefix, intents=intents)
my_secret = os.environ['token'] #since this was based on replit, i had stored my token in a secrets variable, feel free to modify this to your own likings.


@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Watching Temp-Mails! Stay safe!')) #Add a status in the variable 'name'
	print('I am online discord!') #Just to show that the bot is online, feel free to modify the text for this either, will only be printed on the console.
	

@client.event
async def on_message(message):
        if client.user.mentioned_in(message) and message.mention_everyone is False:
        	await message.channel.send(f"My prefix is `{client.command_prefix}`")
        await client.process_commands(message) #This would return the bots prefix if ping/replied to, feel free to delete this if not necessary




@client.command()
async def generate(ctx):
    URL = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    r = requests.get(url = URL)
    response = r.json()
    embed1=discord.Embed(title='Mail Generated!', description='Below are your 10 mails for the week! Keep it noted. We will give you another 10 next week!', color = discord.Color.blue())
    embed1.add_field(name=f"Your Temp Mail:", value= response[0])
    embed1.timestamp = datetime.datetime.utcnow()
    embed1.set_footer(text='Generated Mail!', icon_url=ctx.author.avatar_url) #feel free to change the messages on each command/event! 
    await ctx.send(embed=embed1)


@client.command()
async def domains(ctx):
	embed = discord.Embed(title='Domains:', description='Below are the following domain types we host!', color=discord.Color.blue())
	embed.set_author(name='ExoMail', icon_url=ctx.guild.icon_url)
	embed.add_field(name='Domain Hosts', value="`1secmail.com` \n `1secmail.org` \n `1secmail.net` \n `xojxe.com` \n `yoggm.com` \n `wwjmp.com` \n `esiix.com` \n `oosln.com` \n `vddaz.com`")
	embed.set_footer(text='Domain Hosts')
	await ctx.send(embed=embed)

@client.command()
async def mails(ctx,email = None):
    if email == None:
        await ctx.send("Please provide the email we gave you!\nExample format: `$mails exocodedthis@wwjmp.com`")
    else:
        id, domain = email.split("@")
        URL1 = f"https://www.1secmail.com/api/v1/?action=getMessages&login={id}&domain={domain}"
        re = requests.get(url = URL1)
        response1 = re.json()
        mailemb = discord.Embed(title='Checking Your Newly Generated Mail!', description= f"Here is your mail! You might have to retry for changes to take effect! If there is nothing after a set period of time of trying, then we did not give you the email your provided or you have not received a mail yet! **Your Mail: {email}** ", color=discord.Color.blue())
        x = 0
        for i in response1:
            mailemb.add_field(name='---------------- New Mail\nFrom:', value= response1[x]["from"], inline = False)
            mailemb.add_field(name='ID:', value = response1[x]["id"], inline = False)
            mailemb.add_field(name='Date:', value = response1[x]["date"], inline = False)
            mailemb.add_field(name='Subject:', value = response1[x]["subject"], inline = False)
            mailemb.set_footer(text = '`NOTE:` This does not show the message content of the mail, to do that, do **$check <email> <id>**. ID is posted in this command and email is your generated email.')
            x += 1
            #what this does is posts all the mails instead of just 1 through a loop, note that the message content is not here and it's just the subject. The check command features the message content preview.

        await ctx.send(embed = mailemb)
		#No message input => output message no checks availabe or tempmail finished!



@client.command() #message content is available to be previewed here!
async def check(ctx, email = None, id = None):
    if email == None:
        await ctx.send('Enter an email and id to check!')
    elif id == None:
        await ctx.send('Enter an email and id to check!')
    else:
        mailid, domain = email.split("@")
        URL2 = f"https://www.1secmail.com/api/v1/?action=readMessage&login={mailid}&domain={domain}&id={id}" #gets the email you provides and tries reading the requests
        re1 = requests.get(url = URL2)
        re1.raise_for_status()
        if (re1.status_code != 204 and re1.headers["content-type"].strip().startswith("application/json")):
            try:
                 response2 = re1.json()
            except ValueError:
                await ctx.send('Error!')
            checkEmb = discord.Embed(title='Check a separate email!', description = 'Let\'s check your mail for that one separate incoming email!', color = discord.Color.blue())
            checkEmb.add_field(name='Your Mail:', value = email, inline = False)
            checkEmb.add_field(name='From: ', value = response2["from"], inline = False)
            checkEmb.add_field(name='Subject: ', value = response2["subject"], inline = False)
            checkEmb.add_field(name='Date And Time: ', value = response2["date"], inline = False)
            checkEmb.add_field(name='Message For You From Mailer: ', value = response2["textBody"], inline = False) # here is the message content
            checkEmb.add_field(name='Body: ', value = response2['body'], inline = False)
            checkEmb.add_field(name='Attachments: ', value = response2["attachments"], inline = False)

            await ctx.send(embed=checkEmb)


#finally, run the bot :D!
client.run(my_secret)

#Coded By Exo#4313 - You may take this credit off in your code.
