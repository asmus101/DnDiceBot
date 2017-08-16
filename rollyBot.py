import discord
from discord.ext import commands
import random
import string
import re


description = '''D&D Dice rolling bot.'''
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def r(ctx, roll : str):

    totalResult = 0
    resultString = ''
    try:
        try:
            diceNum = roll.split('d')[0]
        except Exception as e:
            print(e)
            await bot.say("Format has to be in #d# %s." % ctx.message.author.name)
            return

        if int(diceNum) > 50:
            await bot.say("That's way too many dice %s." % ctx.message.author.name)
            return
        
        if roll.find("+") != -1:
            diceMod = roll.split('+')[1]
            diceFix = roll.split('+')[0]
            diceSide = diceFix.split('d')[1]
            bot.type()
            await bot.say("Rolling %sd%s+%s for %s" % (diceNum, diceSide, diceMod, ctx.message.author.name))
            totalRoll = 0

            intNum = int(diceNum)
            intSide = int(diceSide)
            intMod = int(diceMod)

            array = []
            
            for r in range(intNum):
                number = random.randint(1, intSide)
                print(number)
                array = array + [number]
                totalResult = totalResult + number
            finalResult = totalResult + intMod
            await bot.say(ctx.message.author.mention + " rolled: " + str(finalResult) + " (%s (%s) + %s)" % (totalResult, str(array).strip('[]'), diceMod))
        elif roll.find("-") != -1:
            diceMod = roll.split('-')[1]
            diceFix = roll.split('-')[0]
            diceSide = diceFix.split('d')[1]
            bot.type()
            await bot.say("Rolling %sd%s-%s for %s" % (diceNum, diceSide, diceMod, ctx.message.author.name))
            totalRoll = 0

            intNum = int(diceNum)
            intSide = int(diceSide)
            intMod = int(diceMod)

            array = []
            
            for r in range(intNum):
                number = random.randint(1, intSide)
                print(number)
                array = array + [number]
                totalResult = totalResult + number
            finalResult = totalResult - intMod
            await bot.say(ctx.message.author.mention + " rolled: " + str(finalResult) + " (%s (%s) - %s)" % (totalResult, str(array).strip('[]'), diceMod))
        else:
            diceSide = roll.split('d')[1]
            bot.type()
            await bot.say("Rolling %sd%s for %s" % (diceNum, diceSide, ctx.message.author.name))
            totalRoll = 0

            intNum = int(diceNum)
            intSide = int(diceSide)

            array = []
            
            for r in range(intNum):
                number = random.randint(1, intSide)
                print(number)
                array = array + [number]
                totalResult = totalResult + number
            await bot.say(ctx.message.author.mention + " rolled: " + str(totalResult) + " (%s)" % str(array).strip('[]'))

        
    except Exception as e:
        print(e)
        return

    print(diceNum + " and " + diceSide)

bot.run("MzQ1MjI3NTQ3NzMyMDgyNjkw.DG4Nvg.sD6qcilC2UrRGIOxbSMzvCEyL0I")



