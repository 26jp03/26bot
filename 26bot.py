import discord
import os
import openpyxl
from captcha.image import ImageCaptcha
import random
from discord import Member
import datetime
from discord.ext import commands
import asyncio
import youtube_dl
import re
import bs4
import time
import urllib
from urllib.request import urlopen, Request
from selenium import webdriver

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")
    print("ready")
    game = discord.Game("πμ½λ‘λμλ κ·€μ΄ μ’λ°μ!π")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    if message.content.startswith("μλνμΈμ"):
        msg = 'π²μ, λλμ΄ μ€μ¨κ΅°μ, {0.author.mention}λ!π³'.format(message)
        await message.channel.send(msg)

    if message.content.startswith("!26/λ°°κ·Ένμ"):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="λ€! λ°°κ·Έν©μλ€!", color=discord.Color.blue()))
        else:
            await message.channel.send(embed=discord.Embed(title="μλ¬κ°μλ€....", color=discord.Color.red()))

    if message.content.startswith("!26/νμΉ"):
        file = openpyxl.load_workbook('κΈ°μ΅.xlsx')
        sheet = file.active
        learn = message.content.split(" ")
        for i in range(1, 201):
            if sheet["A"+str(i)].value == "-":
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                await message.channel.send("μ’λ λλ €μ€μ΄μ΄μν­ν­νγγμμ")
                await message.channel.send("β νμ¬ μ¬μ©μ€μΈ λ°μ΄ν° μ μ₯μ©λ : 200/" + str(i)+" β")
                break
        file.save("κΈ°μ΅.xlsx")

    if message.content.startswith("!26/λ§ν΄"):
        file = openpyxl.load_workbook("κΈ°μ΅.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 201):
            if sheet["A" + str(i)].value == memory[1]:
                await message.channel.send(sheet["B" + str(i)].value)
                break

    if message.content.startswith("!26/κΈ°μ΅ μ΄κΈ°ν") or message.content.startswith("!26/κΈ°μ΅μ΄κΈ°ν"):
        file = openpyxl.load_workbook("κΈ°μ΅.xlsx")
        sheet = file.active
        for i in range(1, 251):
            sheet["A"+str(i)].value = "-"
        await message.channel.send("κΈ°μ΅μ΄κΈ°ν μλ£")
        file.save("κΈ°μ΅.xlsx")

    if message.content.startswith("!26/λ°μ΄ν°λͺ©λ‘") or message.content.startswith("!26/λ°μ΄ν° λͺ©λ‘"):
        file = openpyxl.load_workbook("κΈ°μ΅.xlsx")
        sheet = file.active
        for i in range(1, 201):
            if sheet["A" + str(i)].value == "-" and i == 1:
                await message.channel.send("λ°μ΄ν° μμ")
            if sheet["A" + str(i)].value == "-":
                break
            await message.channel.send("A : "+sheet["A" + str(i)].value + " B : "+ sheet["B" + str(i)].value)

    if message.content.startswith("!26/λͺ¨λλͺ¨μ¬"):
        await message.channel.send("@everyone")

    if message.content.startswith("!26/μ¬κΈ°λͺ¨μ¬"):
        await message.channel.send("@here")

    if message.content.startswith("!26/λ μ¨"):
        learn = message.content.split(" ")
        enc_location = urllib.parse.quote('λ μ¨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # μ¨λ
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # λ°μ,μ΄μ λ³΄λ€ ?λ λκ±°λ λ?μμ λνλ΄μ€
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # μ²΄κ°μ¨λ
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # λ―ΈμΈλ¨Όμ§
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # μ€λ μ€μ ,μ€νμ¨λ
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # λ΄μΌ μ€μ  μ¨λ
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # λ΄μΌ μ€μ  λ μ¨μν, λ―ΈμΈλ¨Όμ§ μν
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # λ΄μΌ μ€ν μ¨λ
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # λ΄μΌ μ€ν λ μ¨μν,λ―ΈμΈλ¨Όμ§

        embed = discord.Embed(
            title="μ£ΌμΈλ μ§μ­μ λ μ¨ μ λ³΄".format(message),
            description='λ μ¨ μ λ³΄μλλ€.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='νμ¬μ¨λ', value=todayTemp+'Λ', inline=False)  # νμ¬μ¨λ
        embed.add_field(name='μ²΄κ°μ¨λ', value=todayFeelingTemp, inline=False)  # μ²΄κ°μ¨λ
        embed.add_field(name='νμ¬μν', value=todayValue, inline=False)  # λ°μ,μ΄μ λ³΄λ€ ?λ λκ±°λ λ?μμ λνλ΄μ€
        embed.add_field(name='νμ¬ λ―ΈμΈλ¨Όμ§ μν', value=todayMiseaMongi, inline=False)  # μ€λ λ―ΈμΈλ¨Όμ§
        embed.add_field(name='μ€λ μ€μ /μ€ν λ μ¨', value=tomorrowTemp, inline=False)  # μ€λλ μ¨ # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # κ΅¬λΆμ 
        embed.add_field(name='λ΄μΌ μ€μ μ¨λ', value=tomorrowMoring+'Λ', inline=False)  # λ΄μΌμ€μ λ μ¨
        embed.add_field(name='λ΄μΌ μ€μ λ μ¨μν, λ―ΈμΈλ¨Όμ§ μν', value=tomorrowValue, inline=False)  # λ΄μΌμ€μ  λ μ¨μν
        embed.add_field(name='λ΄μΌ μ€νμ¨λ', value=tomorrowAfterTemp + 'Λ', inline=False)  # λ΄μΌμ€νλ μ¨
        embed.add_field(name='λ΄μΌ μ€νλ μ¨μν, λ―ΈμΈλ¨Όμ§ μν', value=tomorrowAfterValue, inline=False)  # λ΄μΌμ€ν λ μ¨μν
        await message.channel.send(embed=embed)

    if message.content.startswith("!26/λ‘€"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)

        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank3 = rank2.find("span", {"class": "tierRank"})
        rank4 = rank3.text  # ν°μ΄νμ (λΈλ‘ μ¦1,2,3,4,5 λ±λ±)
        print(rank4)
        if rank4 != 'Unranked':
          jumsu1 = rank1.find("div", {"class": "TierInfo"})
          jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
          jumsu3 = jumsu2.text
          jumsu4 = jumsu3.strip()#μ μνμ (11LPλ±λ±)
          print(jumsu4)

          winlose1 = jumsu1.find("span", {"class": "WinLose"})
          winlose2 = winlose1.find("span", {"class": "wins"})
          winlose2_1 = winlose1.find("span", {"class": "losses"})
          winlose2_2 = winlose1.find("span", {"class": "winratio"})

          winlose2txt = winlose2.text
          winlose2_1txt = winlose2_1.text
          winlose2_2txt = winlose2_2.text #μΉ,ν¨,μΉλ₯  λνλ  200W 150L Win Ratio 55% λ±λ±

          print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

        channel = message.channel
        embed = discord.Embed(
            title='λ‘€ μ λ³΄',
            description='λ‘€ μ λ³΄μλλ€.',
            colour=discord.Colour.green()
        )
        if rank4=='Unranked':
            embed.add_field(name='λΉμ μ ν°μ΄', value=rank4, inline=False)
            embed.add_field(name='-λΉμ μ μΈλ­-', value="μΈλ­μ λμ΄μμ μ λ³΄λ μ κ³΅νμ§ μμ΅λλ€.", inline=False)
            await message.channel.send(embed=embed)
        else:
         embed.add_field(name='λΉμ μ ν°μ΄', value=rank4, inline=False)
         embed.add_field(name='λΉμ μ LP(μ μ)', value=jumsu4, inline=False)
         embed.add_field(name='λΉμ μ μΉ,ν¨ μ λ³΄', value=winlose2txt+" "+winlose2_1txt, inline=False)
         embed.add_field(name='λΉμ μ μΉλ₯ ', value=winlose2_2txt, inline=False)
         await message.channel.send(embed=embed)


    if message.content.startswith("!26/μλ°μ΄νΈ"):
        msg = '{0.author.mention} π€³μ΄λ²μ£Ό μλ°μ΄νΈ λ΄μ­μλλ€(v 1.3).π€³ ```1οΈβ£μλνμΈμ λ₯Ό νλ©΄ λ§¨μμΌλ‘ μλ λ°μμ΄ λ©λλ€!``` ```2οΈβ£κ²½κ³ κ° μ λλ€λ μ€λ₯λ₯Ό κ³ μ³€μ΅λλ€.```'.format(message)
        await message.channel.send(msg)

    if message.content.startswith("!λ΄μ¬μ§"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!μ±λλ©μΈμ§"):
        channel = message.content[7:25]
        msg = message.content[26:]
        msg2 = '{0.author.mention} λμ΄ λ³΄λ΄μ¨μ΅λλ€. '.format(message)
        await client.get_channel(int(channel)).send(msg2 + msg)

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("!λ?€νΈ"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="λ?€νΈ")
        await author.add_roles(role)
        await message.channel.send("β οΈμ κ³ λ₯Ό λ°μμ μΆλνμμ΅λλ€. λ€μμλ μ’λ μ’κ² μννλ κ²λ μ’μ κ² κ°μμβ οΈ")

    if message.content.startswith("!μΈλ?€νΈ"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="λ?€νΈ")
        await author.remove_roles(role)
        await message.channel.send("β€οΈλ€μμλ μ€μ νμ§ μκ² μ‘°μ¬νμΈμ!β€οΈ")

    if message.content.startswith("!26/λ³μ "):
        await message.channel.send("μ κ° λ³μ μΈ μ΄μ κ° λ­μ£ ? λλμ²΄ μμ£ ?")
        time.sleep(5)
        await message.channel.send("κ·Έ λ§λν μ΄μ κ° μλ€λ©΄ λ§ν΄μ£ΌμΈμ.")
        time.sleep(3)
        await message.author.send("μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ?")
        await message.author.send("μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ? μμ£ ?")
        await message.author.send("λ΄κ° μΌλ§λ λ μ±κ²¨μ€¬λλ°.")
        await message.author.send("YΜ·ΜΎΝΝΜΝΝΝΝΜΜΝΜ¨Μ€Μ?Μ¦Μ­ΝΜ©OΜ·ΝΝΜΜ³ΜΜΝΜ?Μ«UΜ΅Μ½ΜΝΜΜΜΝΜ’ Μ΅ΜΝΜΜΜΊΝΜ’ΝΜΜΜΝDΜΈΝΝΜΝΜΝΜΝΝΜ°Μ Μ©OΜΈΝΜΜΝΝΜΜΜ?Μ¬Μ’ΝΜ³ΜΜNΜΆΜΝΜΜΜΜΜΎΜΎΜ­'Μ΅Ν ΝΜΝΝΜ?Μ¦Μ­ΝTΜ΅ΜΎΝΜΝΜΝΝ ΜΆΝΝΝΜΝΝHΜ΄ΝΜ§ΝΜ«Μ‘ΜΉΜΜ€AΜ΅ΜΜΜ­VΜΆΝΝΜΉEΜ·ΜΝΜ’ΜͺΝΜ¦Μ¦ΝΜ³Μ’Μ­ Μ΅ΜΜΏΜΜΜΝΝΝTΜ΄ΝΜΌΜΝΜ ΝΝΝOΜ΄ΝΝΜΜΝ ΜΜ½ΝΝΜ»Μ¨ΜΜ¬ΜΜ¦ Μ΄ΝΜΎΝΜΜΜΜ₯Μ€Μ¨Μ©DΜΈΝΝΜΜΜ²ΜΜΜ§Μ’EΜΆΝΝΜΝΜΜΜΜΝΜΜSΜ΄ΜΝΜ€ΝΜ«Μ«ΝΝΝΜΉΜ­Μ«EΜΈΝΝΝΜΜΝΝΜΏΜΝΜ ΝΝΜ£Μ£Μ»Μ?Μ°RΜ΅ΜΜΜΝΜΊΜ±VΜΆΝΝΜΜΜΝΝΜΜΜΝEΜ·ΜΜΎΜΏΜΜΜΝΜΝΜΜ?ΜΜ’Μ­Μ¦Μ‘ Μ·ΝΜΝΜΜ½ΜΏΝΝΝΝΜΜΜAΜ·ΜΜΝΝΝΜ±Μ²Μ¨ΜΝΜ£ΝNΜ΅ΜΝΜΜΝΜΝΜΜΜΜΜΜ¦ΜYΜΆΜΝΝΜΜΝΜ»ΜΜ―Μ©Μ Μ¬ΜTΜΆΝΜ½ΜΜΜΜΝΜ?Μ₯ΝΝΝΜ©ΝΝHΜΈΝΝΜΝΝΜΜΜΝΜ³Μ¦Μ«ΜIΜ΄ΝΝΝΝΜΜΏΜ½ΝΜΜ»Μ€ΜͺNΜ·ΜΏΝΜ€Μ£Μ₯Μ«ΝΜ‘ΜͺGΜΈΜΏΝΜΜΜΝΜ")

    if message.content.startswith("!26/λ°°κ·Έλμ€"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "duo modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----κΈ°λ‘μ΄μμ΅λλ€ λ¬Έκ΅¬----
        print(duoRecord)
        channel = message.channel
        embed = discord.Embed(
            title='λ°°κ·Έλμ€ μ λ³΄',
            description='λ°°κ·Έλμ€ μ λ³΄μλλ€.',
            colour=discord.Colour.green())
        if duoRecord == 'No record':
            print('λμ€ κ²½κΈ°κ° μμ΅λλ€.')
            embed.add_field(name='λ°°κ·Έλ₯Ό ννμ΄λΌλ ν΄μ£ΌμΈμ', value='λμ€ κ²½κΈ° μ μ μ΄ μμ΅λλ€..', inline=False)
            await message.channel.send(embed=embed)

        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()  # ----λ μ΄ν----
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()  # ----λ±κΈ----
            print(duoRank)
            embed.add_field(name='λ μ΄ν', value=duoRat, inline=False)
            embed.add_field(name='λ±κΈ', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()  # ----ν¬λ----
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()  # ----ν¬λ μμ?%----
            print(duoKD)
            print(duoKdSky)
            embed.add_field(name='ν¬λ,ν¬λμμ', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()  # ----μΉλ₯ ----
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()  # ----μΉλ₯  μμ?%----
            print(duoWinRat)
            print(duoWinRatSky)
            embed.add_field(name='μΉλ₯ ,μΉλ₯ μμ', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()  # ----ν€λμ·----
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()  # ----ν€λμ· μμ?%----
            print(duoHead)
            print(duoHeadSky)
            embed.add_field(name='ν€λμ·,ν€λμ·μμ', value=duoHead + " " + duoHeadSky, inline=False)
            await message.channel.send(embed=embed)


    if message.content.startswith('!κ²½κ³ λΆμ¬') :
        author = message.guild.get_member(int(message.content[9:27]))
        file = openpyxl.load_workbook('κ²½κ³ .xlsx')
        sheet = file.active
        why = str(message.content[28:])
        i = 1
        while True :
            if sheet["A" + str(i)].value == str(author) :
                sheet['B' + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("κ²½κ³ .xlsx")
                if sheet["B" + str(i)].value == 4:
                    await message.guild.ban(author)
                    await message.channel.send(str(author) + "λμ κ²½κ³  4νλμ μΌλ‘ μλ²μμ μΆλ°©λμμ΅λλ€.")
                else:
                    await message.channel.send(str(author) + "λμ κ²½κ³ λ₯Ό 1ν λ°μμ΅λλ€")
                    sheet["c" + str(i)].value = why
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author)
                sheet["B" + str(i)].value = 1
                sheet["c" + str(i)].value = why
                file.save("κ²½κ³ .xlsx")
                await message.channel.send(str(author) + "λμ κ²½κ³ λ₯Ό 1ν λ°μμ΅λλ€.")
                break
            i += 1

    if message.content.startswith("!26/λ°°κ·Έμ€μΏΌλ"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "squad modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----κΈ°λ‘μ΄μμ΅λλ€ λ¬Έκ΅¬----
        print(duoRecord)
        channel = message.channel
        embed = discord.Embed(
            title='λ°°κ·Έμ€μΏΌλ μ λ³΄',
            description='λ°°κ·Έμ€μΏΌλ μ λ³΄μλλ€.',
            colour=discord.Colour.green())
        if duoRecord == 'No record':
            print('μ€μΏΌλ κ²½κΈ°κ° μμ΅λλ€.')
            embed.add_field(name='λ°°κ·Έλ₯Ό ννμ΄λΌλ ν΄μ£ΌμΈμ', value='μ€μΏΌλ κ²½κΈ° μ μ μ΄ μμ΅λλ€..', inline=False)
            await message.channel.send(embed=embed)

        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()  # ----λ μ΄ν----
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()  # ----λ±κΈ----
            print(duoRank)
            embed.add_field(name='λ μ΄ν', value=duoRat, inline=False)
            embed.add_field(name='λ±κΈ', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()  # ----ν¬λ----
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()  # ----ν¬λ μμ?%----
            print(duoKD)
            print(duoKdSky)
            embed.add_field(name='ν¬λ,ν¬λμμ', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()  # ----μΉλ₯ ----
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()  # ----μΉλ₯  μμ?%----
            print(duoWinRat)
            print(duoWinRatSky)
            embed.add_field(name='μΉλ₯ ,μΉλ₯ μμ', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()  # ----ν€λμ·----
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()  # ----ν€λμ· μμ?%----
            print(duoHead)
            print(duoHeadSky)
            embed.add_field(name='ν€λμ·,ν€λμ·μμ', value=duoHead + " " + duoHeadSky, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('!26/κ³ μμ΄'):
        embed = discord.Embed(
            title='κ³ μμ΄λ',
            description='λ©λ©',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send(embed=embed)

    if message.content.startswith('!κ°μμ§'):
        embed = discord.Embed(
            title='κ°μμ§λ',
            description='μΌμΉμΌμΉ',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240/dog?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await message.channel.send(embed=embed)

    if message.content.startswith('!λ€μ½'):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed2 = discord.Embed(
            colour=discord.Colour.green()
        )
        embed3 = discord.Embed(
            colour=discord.Colour.green()
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1,3)
        print('?λ²μ§Έμ¬μ§ : '+str(randomnumber))
        print('κΈ°νΈ : '+str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho==1:
            urlbase1 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
            await message.channel.send(embed=embed3)
        else:
            urlbase_1 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
            await message.channel.send(embed=embed3)

    if message.content.startswith('!μ€μκ°κ²μμ΄') or message.content.startswith('!μ€κ²'):
        await message.channel.send("λ€μ΄λ² μ€μκ° κ²μμ΄κ° νμ§λ κ΄κ³λ‘ μ€μκ° κ²μμ΄ λͺλ Ήμ΄λ λΉνμ±ν λμμ΅λλ€.")

        embed = discord.Embed(
            title='λ€μ΄λ² μ€μκ° κ²μμ΄',
            description='μ€μκ°κ²μμ΄',
            colour=discord.Colour.green()
        )
        for i in range(0,20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i+1)+'μ', value='\n'+'[%s](<%s>)' % (realTimeSerach, realURL), inline=False) # [νμ€νΈ](<λ§ν¬>) νμμΌλ‘ μ μΌλ©΄ νμ€νΈ νμ΄νΌλ§ν¬ λ§λ€μ΄μ§λλ€

        await message.channel.send(embed=embed)

    if message.content.startswith("!μΊ‘μ± "):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("β°μκ° μ΄κ³Όνμ¨μ΄μ!β°")
            return

        if msg.content == a:
            await message.channel.send("βοΈλ§μΌμ¨μ΄μ!βοΈ")
        else:
            await message.channel.send("βμ€λ΅μλλ€γ β")

    if message.content.startswith("!26/μ°λ κΈ°"):
        await message.channel.send("π¨λ­, λ­λΌκ³ μ?π¨ μ κΈ° μ£ΌμΈλ..λ,, λ,,γ :warning: 26λ΄ μλ¬ μκ²Όμ΅λλ€. !26/κ³ μΉκΈ°λ₯Ό νμ¬ κ³ μΉμΈμ. :warning:")

    if message.content.startswith("!26/κ³ μΉκΈ°"):
        await message.channel.send(":thumbsup: μλ¬κ° κ³ μ³μ‘μ΅λλ€. :thumbsup:")

    if message.content.startswith("!26/μλ²λ±λ‘"):
        await message.channel.send("πμλνμΈμ. μ¬λ¬λΆλ€μ μλ²μ λ§λ°°λλ₯Ό λ°μ μ€ 26λ΄μ΄λΌκ³  ν©λλ€.π ```λ±λ‘μ ν λ €λ©΄ λ±λ‘ν λ λΌκ³  λ§ν΄μ£ΌμΈμ. μ·¨μνκ³  μΆλ€λ©΄ μ·¨μ λΌκ³  λ§ν΄μ£ΌμΈμ. μ΄ μμμ μ€κ°μ μ·¨μλ₯Ό μΈμ λ μ§ ν  μ μμ΅λλ€.```")

    if message.content.startswith("λ±λ‘ν λ"):
        await message.channel.send("πμκ² μ΅λλ€. μ’μ μκ°μλλ€! μ§κΈ λ°λ‘ λ±λ‘ νκ² μ΅λλ€.π ``λ±λ‘ νμ€ κ±°λ©΄ μ’μ μ΄λΌκ³  λ§ν΄μ£ΌμΈμ. μ«μΌμλ©΄ νμ§λ§ λΌκ³  λ§ν΄μ£ΌμΈμ.``")

    if message.content.startswith("μ·¨μ"):
        await message.channel.send("πμκ² μ΅λλ€. μ£ΌμΈλ λ§μλλ‘μ£ π")

    if message.content.startswith("νμ§λ§"):
        await message.channel.send("πμ€ν μ·¨μνκ² μ΅λλ€!π")\

    if message.content.startswith("μ’μ"):
        await message.channel.send("πκ·Έλ¬λ©΄ ππππ‘ππ. Ξ΄#8277 νν μΉμΆλ₯Ό λ³΄λ΄μκ³  DM λ³΄λ΄μ£ΌμΈμ!π")

    if message.content.startswith("!26MJ/λ§μ£Όμ λ³΄"):
        await message.channel.send("π€λ§μ£Ό#5903 μ μ λ³΄ ```μ΄λ¦: λ§μ£Ό``` ```νΈμμΉ: blueblackslime( https://www.twitch.tv/blueblackslime )``` ```μ νλΈ: λ§μ£Ό ( https://www.youtube.com/channel/UCXeXeCn960Hm-y289HCAxkQ )``` ")

    if message.content.startswith("!μκ°"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        await message.channel.send(str(a) + "λ " + str(b) + "μ " + str(c) + "μΌ " + str(d) + "μ " + str(e) + "λΆ μλλ€!")

    if message.content.startswith("!μ’λΉν"):
        await message.channel.send("λλνκ³  μλ¦¬ν λκ΅¬λ¦¬ μλκ°μ©~")

    if message.content.startswith("!μ€λ² "):
        await message.channel.send("λ©μ²­μ΄ μλκ°μ...?")

    if message.content.startswith("!λ§μ£Ό"):
        await message.channel.send("μ... λ§ν κ² μμ΄ λͺΈλ§€ μΉμνκ³  κ°μΉμ‘΄μ μΈμ± μ²μ¬ νΉκ°μ§±λ§μ£Ό μλκ² μ΅λκΉ!")

    if message.content.startswith("!νλΈμ΄"):
        await message.channel.send("λ­, λ­λΌκ³ ? λ°λμ΄λ€! μμγμμγ!!!! https://im6.ezgif.com/tmp/ezgif-6-4b4007d8f851.gif")

    if message.content.startswith("!26/μλ²λ¦¬μ€νΈ"):
        await message.channel.send("πλ±λ‘λ μλ²λ€π ```πλνλ―Όκ΅­ λ‘λΈλ‘μ€ κ²μμ€μμ κ°μ₯ μ€λλ νλλΆλ κ²μ, π‘νλλΆλλ‘ μ€μΈμ!π‘ μλ²λ§ν¬: https://discord.gg/nWxY5bV```")

    if message.content.startswith("!26/νλ‘νλ±λ‘"):
        await message.channel.send("β οΈμ λ§μ΄μ£ ? νλ‘νμ λ±λ‘νλ©΄ μ κ³ κ° λ  μ μμ΅λλ€.β οΈ ``!κ³μ`` μλλ©΄ ``!κ·Έλ₯μ·¨μ``")

    if message.content.startswith("!κ³μ"):
        await message.channel.send("β€οΈλ΅, μ μλ§ κΈ°λ€λ €μ£ΌμΈμ. ππλ₯#8277 νκ·Έ ν΄μ£ΌμΈμ!β€οΈ")

    if message.content.startswith("!κ·Έλ₯μ·¨μ"):
        await message.channel.send("β€οΈλ΅, μ·¨μλμμ΅λλ€.β€οΈ")

    if message.content.startswith("!26/λ‘κ·ΈμΈ"):
        await message.channel.send("πμ½λλ₯Ό μλ ₯ λΆνλλ¦½λλ€. ``λ€λ₯Έ λΆμ΄ μ¬μ©μ μ²λ²μ΄ λ©λλ€.``π")

    if message.content.startswith("!26/4263"):
        await message.channel.send("πμ΄μμ€μΈμ, μλ¦¬λ!π")

    if message.content.startswith("!26/8277"):
        await message.channel.send("πμ΄μμ€μΈμ, 26λ! μ! λ§λ€ νλΈμ΄λμ΄μ£ !π")

    if message.content.startswith("μ! μμ¦!"):
        embed = discord.Embed(title="κ²λ μ΄.λ ΅.μ΅.λ.λ€", description="μΈλνμΌ μμλκ΅¬λ! νΉμ λͺ¨λ₯΄μλλΆλ€μ λν΄ μ€λͺν΄λλ¦½λλ€. μμ¦λ μΈλνμΌμ μΈκ°μ§ μλ©λ£¨νΈμ€ λͺ°μ΄μλ©μ μ΅μ’λ³΄μ€λ‘ μ§.μ§.κ².λ.μ΄.λ ΅.μ΅.λ.λ€. κ³΅κ²©μ μ λΆλ€ ννΌνκ³  λ§νΌκ° 92μΈλ° μμ¦μ κ³΅κ²©μ 1μ΄λΉ 60μ΄ λ€λλ°λ€κ° λλκΉμ§ μΆκ°λ‘ λΆμ΄μμ΅λλ€.. νμ§λ§ μ΄λ¬λ©΄ μ λλ‘ κ²μμ κΉ° μ κ° μμΌλ μ μμ§μ΄ μΉλͺμ μΈ μ½μ μ λ§λ€μμ£ . μμ¦μ μΉλͺμ μΈ μ½μ μ΄ λ°λ‘ μ§μΉλ€λκ²μλλ€. ν¨ν΄λ€μ λ€ κ²¬λκ³ λλ©΄ μ§μ³μ μμ μ ν΄μ μ μ§νμ±λ‘ μ μλ­λλ€. νμ§λ§ μ μ΄λ€μμλ μ°½μ μ?κ²¨μ κ³΅κ²©μ μλνκ³  μμ¦λ 1μ°¨κ³΅κ²©μ νΌνμ§λ§ κ·Έ νμ λ°λ‘λ μμ€λ 2μ°¨ κ³΅κ²©μ λ§κ³  μ£½μ΅λλ€.", color=0x00B992)
        embed.set_image(url="https://image.librewiki.net/f/f0/Sans.gif")
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/693527349254422528/51LpoPnZ_400x400.png ")
        await message.channel.send("μ! μμ¦ μμλκ΅¬λ!", embed=embed)

    if message.content.startswith('!λ²μ­'):
        learn = message.content.split(" ")
        Text = ""

        client_id = ""
        client_secret = ""

        url = "https://openapi.naver.com/v1/papago/n2mt"
        print(len(learn))
        vrsize = len(learn)  # λ°°μ΄ν¬κΈ°
        vrsize = int(vrsize)
        for i in range(1, vrsize): #λμ΄μ°κΈ° ν νμ€νΈλ€ μΈμν¨
            Text = Text+" "+learn[i]
        encText = urllib.parse.quote(Text)
        data = "source=ko&target=en&text=" + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            data = json.loads(data)
            tranText = data['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        print('λ²μ­λ λ΄μ© :', tranText)

        embed = discord.Embed(
            title='νκΈ->μμ΄ λ²μ­κ²°κ³Ό',
            description=tranText,
            colour=discord.Colour.green()
        )
        await message.channel.send(embed=embed)

        
    if message.content.startswith('!μμ§€'):
        embed = discord.Embed(
            title='λλ€μμ§€',
            description='μ¨μ¨μ¨μ¨γλ΄γλ΄γλ΄γλ΄γλ΄γλ΄γλΌ',
            colour=discord.Colour.green()
        )
        url = "http://www.gifbin.com/random"
        urlBase = "http://www.gifbin.com"
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        gif1 = bsObj.find('form', {'id': 'share-form'})
        gif2 = gif1.find('a')
        gif3 = gif2["href"]
        gifURL = urlBase + gif3
        print(gifURL)
        embed.set_image(url=gifURL)
        await message.channel.send(embed=embed)
        #"http://www.gifbin.com/random"


    if message.content.startswith("!26/λͺλ Ήμ΄"):
        embed = discord.Embed(title="λͺλ Ήμ΄λͺ©λ‘", description="λ λ§μ λͺλ Ήμ΄κ° μΆκ°λ©λλ€!", color=0x00B992)
        embed.add_field(name="!λ΄μ¬μ§", value="λ΄ νμΌμ λ±λ‘λ μ¬μ§μ κ°μ Έμ΅λλ€.", inline=False)
        embed.add_field(name="!μ±λλ©μΈμ§", value="μ±λμ λ΄μ΄ λ©μΈμ§λ₯Ό λ³΄λλλ€.", inline=False)
        embed.add_field(name="!DM", value="νΉμ ν λΆνν DMμ λ³΄λλλ€.", inline=False)
        embed.add_field(name="!μΊ‘μ± ", value="λ‘λ΄ μΈμ¦μ νμ€νΈ νλ μΊ‘μ±  μμ€νμ κΊΌλλλ€.", inline=False)
        embed.add_field(name="!26/μ°λ κΈ°", value="26μ΄νν μ½ν μμ ν΄μ κ³ μ₯λ€ νΈλ¦½λλ€.(λΉμΆμ²)", inline=False)
        embed.add_field(name="!26/μκΈ°μκ°", value="26μ΄κ° μκΈ°μκ°λ‘€ νκ² νλ λͺλ Ήμ΄μλλ€.", inline=False)
        embed.add_field(name="!26/νλ‘νλ±λ‘", value="26μ΄κ° νλ‘νμ λ±λ‘ν΄μ€λλ€.", inline=False)
        embed.add_field(name="!μκ°", value="26μ΄κ° μκ°μ μλ₯΄μΌ μ£Όλ λͺλ Ήμ΄μλλ€.", inline=False)
        embed.add_field(name="!26/μλ²λ±λ‘", value="26μ΄κ° λΉμ μ μλ²λ₯Ό λ±λ‘ ν΄λλ¦¬λ μλΉμ€μμ!(μ¬μ€ μ μμκ° νμ§λ§)", inline=False)
        embed.add_field(name="!26/μλ²λ¦¬μ€νΈ", value="26μ΄κ° λ±λ‘ν μλ²λ€μ λ³΄μ¬μ€μ(λ§ν¬ ν¬ν¨)", inline=False)
        embed.add_field(name="!26/λ‘κ·ΈμΈ", value="μκΈ° νλ‘νλ‘ λ‘κ·ΈμΈ ν©λλ€!", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/689072569076547585/689086114107228186/d201436a554453b7.jpg")
        embed.set_image(url="https://media.giphy.com/media/kDXxjwpazm9b2LzOMc/giphy.gif")
        embed.set_footer(text="λ΄μ λ¬Έμ κ° μμΌλ©΄ !26/κ³ μΉκΈ° λ₯Ό ν΄μ£ΌμΈμ. κ·Έλλ μ λλ©΄ ππππ‘ππ#6242 λ‘ μΉμΆ κ±°μκ³  μ°λ½ μ£ΌμΈμ!", icon_url="https://media.giphy.com/media/kDXxjwpazm9b2LzOMc/giphy.gif")
        await message.channel.send("μ¬κΈ° λͺλ Ήμ΄ λ©λ΄νμλλ€!", embed=embed)

    if message.content.startswith("!26/μκΈ°μκ°"):
        await message.channel.send("```β€οΈμ΄λ¦: π­26μ΄λ΄πͺ``` ```π§‘μ£ΌμΈ: λͺ¨λ λ€(μ΄μν μ¬λ λΉΌκ³ )``` ```πμ·¨λ―Έ: μ£ΌμΈμ΄λ λκΈ°```")

    if message.content.startswith('!μνμμ'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx
        i1 = 0 # λ­νΉ stringκ°
        embed = discord.Embed(
            title = "μνμμ",
            description = "μνμμμλλ€.",
            colour= discord.Color.red()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1+1
            stri1 = str(i1) # i1μ μνλ­νΉμ λνλ΄λλ° μ¬μ©λ©λλ€
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  # ------------------------- 1λ±λ­νΉ μν---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # μνλ°μ€ λνλ΄λ Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # μν μ λͺ©
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # μν νμ 
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # κ°λ΄λ μ§, μλ§€μ¨ λκ°ν¬ν¨ν ddμ
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # κ°λ΄λ μ§
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # μλ§€μ¨ ,λ­νΉλ³λ
            print(moviechartLi1Yerating)  # ------------------------- 1λ±λ­νΉ μν---------------------------
            print()
            embed.add_field(name='---------------λ­νΉ'+stri1+'μ---------------', value='\nμνμ λͺ© : '+moviechartLi1MovieName+'\nμννμ  : '+moviechartLi1Ratting+'μ '+'\nκ°λ΄λ μ§ : '+moviechartLi1openDay+'\nμλ§€μ¨,λ­νΉλ³λ : '+moviechartLi1Yerating, inline=False) # μνλ­νΉ


        await message.channel.send(embed=embed)


    if message.content.startswith("!κΈμ"):
        embed = discord.Embed(
            title='κ΅°ν¬ E λΉμ¦λμ€ κ³ λ±νκ΅ κΈμ',
            description='κΈμμλλ€.',
            colour=discord.Colour.green()
        )
        embed.add_field(name='μ€λ', value=κΈμ.lunchtext(), inline=False)
        embed.add_field(name='λ΄μΌ', value=κΈμ.lunchtextD1(), inline=False)
        embed.add_field(name='λͺ¨λ', value=κΈμ.lunchtextD2(), inline=False)
        await message.channel.send(embed=embed)

    
    if message.content.startswith("!λ³΅κΆ"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # λ§μ½ νμ¬λλ€κ°μ΄ μ΄μ μ«μλ€κ³Ό κ°μ΄ κ°λ€λ©΄
                        numberText = number[i]
                        print("μλ μ΄μ κ° : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("μλ νμ¬κ° : " + str(numberText))
                        if number[i] == number[i2]:  # λ§μ½ λ€μ μμ±ν λλ€κ°μ΄ μ΄μ μ«μλ€κ³Ό λ κ°λ€λ©΄
                            numberText = number[i]
                            print("μλ μ΄μ κ° : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("μλ νμ¬κ° : " + str(numberText))
                            if number[i] == number[i2]:  # λ§μ½ λ€μ μμ±ν λλ€κ°μ΄ μ΄μ μ«μλ€κ³Ό λ κ°λ€λ©΄
                                numberText = number[i]
                                print("μλ μ΄μ κ° : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("μλ νμ¬κ° : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="λ³΅κΆ μ«μ!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(embed=embed)

    if message.content.startswith('!κ²μ'):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # λ°°μ΄ν¬κΈ°
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # λμ΄μ°κΈ° ν νμ€νΈλ€ μΈμν¨
            Text = Text + " " + learn[i]
        encText = Text

        chromedriver_dir = r'C:\selum\chromedriver_win32\chromedriver.exe' #ν¬λ‘¬λλΌμ΄λ² κ²½λ‘
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get('https://www.youtube.com/results?search_query='+encText) #μ νλΈ κ²μλ§ν¬
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'}) # aνκ·Έμμ video title μ΄λΌλ idλ₯Ό μ°Ύμ

        embed = discord.Embed(
            title="μμλ€!",
            description="κ²μν μμ κ²°κ³Ό",
            colour=discord.Color.blue())

        for i in range(0, 5):
            entireNum = entire[i]
            entireText = entireNum.text.strip()  # μμμ λͺ©
            print(entireText)
            test1 = entireNum.get('href')  # νμ΄νΌλ§ν¬
            print(test1)
            rink = 'https://www.youtube.com'+test1
           # embed.add_field(name=str(i+1)+'λ²μ§Έ μμ',value=entireText + '\nλ§ν¬ : '+rink)
            embed.add_field(name=str(i + 1) + 'λ²μ§Έ μμ', value='\n' + '[%s](<%s>)' % (entireText, rink),
                            inline=False)  # [νμ€νΈ](<λ§ν¬>) νμμΌλ‘ μ μΌλ©΄ νμ€νΈ νμ΄νΌλ§ν¬ λ§λ€μ΄μ§λλ€
            searchYoutubeHref[i] = rink
        await message.channel.send(embed=embed)

    if message.content.startswith('1'):

        if not searchYoutubeHref: #μ μ₯λ νμ΄νΌλ§ν¬κ° μλ€λ©΄
            print('searchYoutubeHref μμ κ°μ΄ μ‘΄μ¬νμ§ μμ΅λλ€.')
            await client.send_message(message.channel, embed=discord.Embed(description="κ²μν μμμ΄ μμ΅λλ€."))
        else:
            print(searchYoutubeHref[0])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[0]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await message.channel.send(embed=discord.Embed(description="μ¬μνλ€!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('2'):

        if not searchYoutubeHref:
            print('searchYoutubeHref μμ κ°μ΄ μ‘΄μ¬νμ§ μμ΅λλ€.')
            await message.channel.send(embed=discord.Embed(description="κ²μν μμμ΄ μμ΅λλ€."))
        else:
            print(searchYoutubeHref[1])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[1]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await message.channel.send(embed=discord.Embed(description="μ¬μνλ€!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('3'):

        if not searchYoutubeHref:
            print('searchYoutubeHref μμ κ°μ΄ μ‘΄μ¬νμ§ μμ΅λλ€.')
            await client.send_message(message.channel, embed=discord.Embed(description="κ²μν μμμ΄ μμ΅λλ€."))
        else:
            print(searchYoutubeHref[2])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[2]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await message.channel.send(embed=discord.Embed(description="μ¬μνλ€!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('4'):

        if not searchYoutubeHref:
            print('searchYoutubeHref μμ κ°μ΄ μ‘΄μ¬νμ§ μμ΅λλ€.')
            await message.channel.send(embed=discord.Embed(description="κ²μν μμμ΄ μμ΅λλ€."))
        else:
            print(searchYoutubeHref[3])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[3]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await message.channel.send(embed=discord.Embed(description="μ¬μνλ€!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]

    if message.content.startswith('5'):

        if not searchYoutubeHref:
            print('searchYoutubeHref μμ κ°μ΄ μ‘΄μ¬νμ§ μμ΅λλ€.')
            await client.send_message(message.channel, embed=discord.Embed(description="κ²μν μμμ΄ μμ΅λλ€."))
        else:
            print(searchYoutubeHref[4])
            server = message.server
            voice_client = client.voice_client_in(server)
            url = searchYoutubeHref[4]
            player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
            print(player.is_playing())
            players[server.id] = player
            await message.channel.send(embed=discord.Embed(description="μ¬μνλ€!!!!"))
            print(player.is_playing())
            player.start()

            for i in range(0,5):
                del searchYoutubeHref[i]


    if message.content.startswith('!μ΄λͺ¨ν°μ½'):

        emoji = [" κ°βα΅ΰΌα΅κ± ", " κ°βΛβ‘Λκ± ", " β½β½βκ° Λ κ³ Λ κ±ββΎβΎ ", " ΰΌΌ γ€ β_β ΰΌ½γ€ ", " βΰΌΌ β’Μ β β’Μ ΰΌ½β ",
                 " ( ο½₯ΰΈ΄α΄₯ο½₯ΰΈ΄) ", " β’Σ©β’ ", " ΰΈ^β’ο»β’^ΰΈ ", " γ€βΉγ¦βΉ)γ€ ", " βά«β ", " αΆ Ν‘Β°α΄₯Ν‘Β°αΆ ", " ( ΨΨΚΜ₯Μ₯Μ₯Μ₯ Ω ΨΨΚΜ₯Μ₯Μ₯Μ₯ ) ",
                 " ( β’Μ Μ―β’Μ ) ",
                 " β’Μ.Μ«β’Μβ§ ", " 'Ν‘β’_'Ν‘β’ ", " (ΞβΰΈ΄ΰ±ͺβΰΈ΄β΅) ", " Λ΅Β―Ν ΰ½Β―ΝΛ΅ ", " Ν‘Β° ΝΚ Ν‘Β° ", " Ν‘~ ΝΚ Ν‘Β° ", " (γ₯ο½‘ββΏβΏβο½‘)γ₯ ",
                 " Β΄_γ` ", " Ω©(Ν‘β_Ν‘β ", " β(β ββ’βΟββ’β β)β ", " Ω©(Ν‘Γ―_Ν‘Γ―β ", " ΰ― ", " (Β΄ο½₯ΚΜ«ο½₯`) ", " Ξ΅β―(ΰΈ ΛΟΛ)ΰΈ§ ",
                 " (γ£ΛΪ‘ΛΟ) ", "βββββββββ", "βββ", "οΈ»β¦Μ΅Μ΅ΜΏβ€ββ", "γΌββ»β³οΈ»β", "οΈ»β¦Μ΅Μ΅ΝΜΏΜΏΜΏΜΏβββ€β",
                 " αΏ α αΌ α½ αΏ α αΌ α½ αΏ ", "βββββββββ", " βββ ", " (ΰΉβΉΟβΉΰΉ) ", " (β―Β°β‘Β°οΌβ―οΈ΅ β»ββ» ",
                 " (///β½///) ", " Ο(oΠ΄olll) ", " γoΒ΄οΎβ‘οΎ`oγ ", " οΌΌ(^o^)οΌ ", " (ββΏβΏβο½‘) ", " ο½₯α΄₯ο½₯ ", " κοΉκ "
                                                                                                 " ΛΜ£Μ£Μ£Μ£Μ£Μ£οΈΏΛΜ£Μ£Μ£Μ£Μ£Μ£ ",
                 " ( ββ’γ¦β’β ) ", " (ο½‘Γ¬_Γ­ο½‘) ", " (β­β’Μο?§ β’Μβ?) ", " ΰ¬(ΰ©­*Λα΅Λ)ΰ©­ ", " Β΄_γ` ", " (~ΛβΎΛ)~ "] # μ΄λͺ¨ν°μ½ λ°°μ΄μλλ€.

        randomNum = random.randrange(0, len(emoji)) # 0 ~ μ΄λͺ¨ν°μ½ λ°°μ΄ ν¬κΈ° μ€ λλ€μ«μλ₯Ό μ§μ ν©λλ€.
        print("λλ€μ κ° :" + str(randomNum))
        print(emoji[randomNum])
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum])) # λλ€ μ΄λͺ¨ν°μ½μ λ©μμ§λ‘ μΆλ ₯ν©λλ€.

    if message.content.startswith('!μ£Όμ¬μ'):

        randomNum = random.randrange(1, 7) # 1~6κΉμ§ λλ€μ
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':six: '))

    if message.content.startswith('!νμ΄λ¨Έ'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # λ°°μ΄ν¬κΈ°
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # λμ΄μ°κΈ° ν νμ€νΈλ€ μΈμν¨
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(embed=discord.Embed(description='νμ΄λ¨Έ μλμ€ : '+str(i)+'μ΄'))
            time.sleep(1)

        else:
            print("λ‘")
            await message.channel.send(embed=discord.Embed(description='νμ΄λ¨Έ μ’λ£'))

    if message.content.startswith('!μ λΉλ½κΈ°'):
        channel = message.channel
        embed = discord.Embed(
            title='μ λΉλ½κΈ°',
            description='κ° λ²νΈλ³λ‘ λ²νΈλ₯Ό μ§μ ν©λλ€.',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='λ')


        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # λ°°μ΄ν¬κΈ°
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # λμ΄μ°κΈ° ν νμ€νΈλ€ μΈμν¨
            Text = Text + " " + learn[i]
        print(Text.strip()) #μλ ₯ν λͺλ Ήμ΄

        number = int(Text)

        List = []
        num = random.randrange(0, number)
        for i in range(number):
            while num in List:  # μ€λ³΅μΌλλ§
                num = random.randrange(0, number)  # λ€μ λλ€μ μμ±

            List.append(num)  # μ€λ³΅ μλλλ§ λ¦¬μ€νΈμ μΆκ°
            embed.add_field(name=str(i+1) + 'λ²μ§Έ', value=str(num+1), inline=True)

        print(List)
        await message.channel.send(embed=embed)

    if message.content.startswith('!μ΄λ―Έμ§'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # λ°°μ΄ν¬κΈ°
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # λμ΄μ°κΈ° ν νμ€νΈλ€ μΈμν¨
            Text = Text + " " + learn[i]
        print(Text.strip())  # μλ ₯ν λͺλ Ήμ΄

        randomNum = random.randrange(0, 40) # λλ€ μ΄λ―Έμ§ μ«μ

        location = Text
        enc_location = urllib.parse.quote(location) # νκΈμ urlμ μ¬μ©νκ²λ νμμ λ°κΏμ€λλ€. κ·Έλ₯ νκΈλ‘ μ°λ©΄ μ€νμ΄ μλ©λλ€.
        hdr = {'User-Agent': 'Mozilla/5.0'}
        # ν¬λ‘€λ§ νλλ° μμ΄μ κ°λμ© μλλ μ¬μ΄νΈκ° μμ΅λλ€.
        # κ·Έ μ΄μ λ μ¬μ΄νΈκ° μ μνλ μλλ₯Ό λ΄μΌλ‘ μΈμνμκΈ° λλ¬ΈμΈλ°
        # μ΄ μ½λλ μμ μ΄ λ΄μ΄ μλκ²μ μ¦λͺνμ¬ μ¬μ΄νΈμ μ μμ΄ κ°λ₯ν΄μ§λλ€!
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location # μ΄λ―Έμ§ κ²μλ§ν¬+κ²μν  ν€μλ
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser") # μ μ²΄ html μ½λλ₯Ό κ°μ Έμ΅λλ€.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'}) # bsjObjμμ div class : photo_grid_box μ μ½λλ₯Ό κ°μ Έμ΅λλ€.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'}) # imgfind1 μμ λͺ¨λ  aνκ·Έ μ½λλ₯Ό κ°μ Έμ΅λλ€.
        imgfind3 = imgfind2[randomNum]  # 0μ΄λ©΄ 1λ²μ§Έμ¬μ§ 1μ΄λ©΄ 2λ²μ§Έμ¬μ§ νμμΌλ‘ νλμ μ¬μ§ μ½λλ§ κ°μ Έμ΅λλ€.
        imgfind4 = imgfind3.find('img') # imgfind3 μμ imgμ½λλ§ κ°μ Έμ΅λλ€.
        imgsrc = imgfind4.get('data-source') # imgfind4 μμ data-source(μ¬μ§λ§ν¬) μ κ°λ§ κ°μ Έμ΅λλ€.
        print(imgsrc)
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.add_field(name='κ²μ : '+Text, value='λ§ν¬ : '+imgsrc, inline=False)
        embed.set_image(url=imgsrc) # μ΄λ―Έμ§μ λ§ν¬λ₯Ό μ§μ ν΄ μ΄λ―Έμ§λ₯Ό μ€μ ν©λλ€.
        await message.channel.send(embed=embed) # λ©μμ§λ₯Ό λ³΄λλλ€.


    if message.content.startswith('!members'):
        x = message.server.members
        for member in x:
            print(member.name) 

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
