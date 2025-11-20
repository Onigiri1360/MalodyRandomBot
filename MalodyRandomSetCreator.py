# -*- coding: utf-8 -*-


#py実行に必要不可欠な要素をまとめたセル

!pip install nest_asyncio
!pip install discord.py
from dotenv import load_dotenv
import os
import discord
import nest_asyncio
import random
import requests
import csv

# nest_asyncioを適用して、既存のイベントループ内で新しいイベントループを許可する
nest_asyncio.apply()

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からトークンを取得する
TOKEN = SECRET

# すべてのイベントに対して反応するIntentsオブジェクトを作成
intents = discord.Intents.default()
intents.message_content = True # メッセージの内容を受け取るための権限を付与

# Discordのクライアントを作成
client = discord.Client(intents=intents)



import requests
import pandas as pd
from io import StringIO
splitRecord1 = []
splitRecord2 =[]

# 1. GitHubのRaw URLを指定
# 修正: GitHubのblobページではなく、生のコンテンツのURLを指定
url1 = "https://raw.githubusercontent.com/Onigiri1360/MalodyRandomBot/refs/heads/main/MalodySongs.csv"
url2 = "https://raw.githubusercontent.com/Onigiri1360/MalodyRandomBot/refs/heads/main/MalodySongs_WE.csv"

# 2. requestsでコンテンツを取得
response1 = requests.get(url1)
response2 = requests.get(url2)
response1.encoding = response1.apparent_encoding # エンコーディングを自動判別（または 'utf-8' などを指定)
response2.encoding = response2.apparent_encoding

# 3. 取得したテキストデータをStringIOに渡し、pandasで読み込む
csv_data1 = response1.text
df = pd.read_csv(StringIO(csv_data1), engine='python', on_bad_lines='skip')
recordNormalLine = csv_data1.splitlines()
recordNormal = csv_data1

csv_data2 = response2.text
df = pd.read_csv(StringIO(csv_data2), engine='python', on_bad_lines='skip')
recordWELine = csv_data2.splitlines()
recordWE = csv_data2

@client.event
async def on_ready():
  print(f'{client.user}としてログインしました')
  print(client.user.id)

@client.event
async def on_message(message):
  # Bot自身のメッセージには反応しないようにする
  if message.author.bot:
    return
  # 'Botさん、こんにちは！'というメッセージに反応する
  id = (f"<@{client.user.id}>")
  if message.content.find(id) != -1:
    anotherResponse = message.content.replace(id,'')
    anotherResponse1 = anotherResponse.split(",")
    #MalodyRandom.py
    # -*- coding: utf-8 -*-
    try:
      float(anotherResponse1[0])
    except Exception as e:
      await message.channel.send("形式が不正です")
      return

    splitRecord1 = []
    splitRecord2 = []
    noTemp = []
    sortedSongs = []
    randomRecord = []
    count = 0

    """
    @param splitRecord1 通常譜面の個々の要素を","で区切って参照できるようにしたもの
    @param splitRecord2 splitRecord1のWE版
    @param sortedSongs 条件に合致する楽曲のリスト
    @param randomRecord (ここからランダムで選択される)
    @param count 条件の数値(COOL以下{count}個とか平均{count}%以上)
    """

    for i in range(len(recordNormalLine)):
      lineNum = i + 1
      record1 = recordNormalLine[i] #record1 = Normalの行単位のレコード
      splitRecord1.append(record1.split(","))

    for j in range(len(recordWELine)):
      lineNum = j + 1
      record2 = recordWELine[j] #record2 = WE・隔離枠の行単位のレコード
      splitRecord2.append(record2.split(","))

    lowerLevel = float(anotherResponse1[0].replace(' ',''))
    higherLevel = float(anotherResponse1[1].replace(' ',''))
    try:
      judge = anotherResponse1[2].replace(' ','')
    except Exception as e:
      judge = "%"
    #0を入力するとWORLD'S ENDが選択可能
    #定数ではなくレベルで指定する場合は.0~.9で絞り込み

    #ランダム性を高める為、全曲を1回ランダムに振り分ける
    for q in range(len(recordNormalLine)):
      line = splitRecord1[q]
      randomRecord.insert(random.randint(0,len(randomRecord)),line)

    if lowerLevel == 0.0 and higherLevel == 0.0:
      for k in range(len(splitRecord2)):
        tempWE = splitRecord2[k]
        sortedSongs.append(tempWE)
    elif lowerLevel == -1.0 and higherLevel == -1.0:
      noTemp += splitRecord1
      noTemp += splitRecord2
      sortedSongs = noTemp
    else:
      for l in range(len(splitRecord1)):
        temp = randomRecord[l]
        if lowerLevel == -1.0:
            if higherLevel+0.1 > float(temp[2]):
                sortedSongs.append(temp)

        elif higherLevel == -1.0:
            if lowerLevel-0.1 < float(temp[2]):
                sortedSongs.append(temp)

        elif lowerLevel-0.1 < float(temp[2]) and higherLevel+0.1 > float(temp[2]):
            sortedSongs.append(temp)


    setSong1 = sortedSongs[random.randint(0,len(sortedSongs)-1)]
    title1 = setSong1[0].replace('"', '')
    if setSong1[0] == "Destruction3.2.1": #元のタイトルのままだと正常に動作しないのでゴリ押し
      title1 = "DESTRUCTION3,2,1"
    try:
      difficulty1 = setSong1[1]
    except Exception as e:
      await message.channel.send(setSong1)
    if lowerLevel == 0:
      const1 = setSong1[2]
    else:
      const1 = setSong1[2]


    setSong2 = sortedSongs[random.randint(0,len(sortedSongs)-1)]
    title2 = setSong2[0].replace('"', '')
    if setSong1[0] == "Destruction3.2.1":
      title2 = "DESTRUCTION3,2,1"
    difficulty2 = setSong2[1]
    if lowerLevel == 0:
      const2 = setSong2[2]
    else:
      const2 = setSong2[2]


    setSong3 = sortedSongs[random.randint(0,len(sortedSongs)-1)]
    title3 = setSong3[0].replace('"', '')
    if setSong1[0] == "Destruction3.2.1":
      title3 = "DESTRUCTION3,2,1"
    difficulty3 = setSong3[1]
    if lowerLevel == 0:
      const3 = setSong3[2]
    else:
      const3 = setSong3[2]

    if judge == "COOL":
      count = random.randrange(50,150,5)
    elif judge == "GOOD":
      count = random.randint(10,50)
    elif judge == "MISS":
      count = random.randint(5,30)
    elif judge == "%":
      count = random.randint(5,15)
    else:
      count = random.randrange(50,150,10)
      judge = "COOL"

    await message.channel.send(f"1曲目：{title1} [{difficulty1} {const1}]")
    await message.channel.send(f"2曲目：{title2} [{difficulty2} {const2}]")
    await message.channel.send(f"3曲目：{title3} [{difficulty3} {const3}]")
    if judge == "%":
      await message.channel.send(f"条件 ：平均{float(98 + count/10):.2f}%以上")
    else:
      await message.channel.send(f"条件 ：{judge}以下 {count}")

    # メッセージ送信者の表示名を取得
    user_name = message.author.display_name



client.run(TOKEN)
