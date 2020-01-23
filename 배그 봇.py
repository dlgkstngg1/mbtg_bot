import discord
import datetime



client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print((client.user.id))
    print("------------------")
    game = discord.Game("배틀그라운드")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    #if message.author.bot:
        #return None

    if message.content.startswith("!공지사항"):
        embed = discord.Embed(title="공지사항",
        description="```매 시즌 골드3티어 미만, 30일 미접속시 추방\n"
        "등급 및 추방은 매 시즌 초기화 1일전 정산후 다음시즌때 반영됩니다.```", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("!승급조건"):
        embed = discord.Embed(title="승급조건",
        description="```ini\n[정예]```  다이아4티어 달성 시 다음 시즌 승급\n"
        "\n```diff\n-부마스터``` 다이아3티어 달성 후 솔로티어\n"
        "골드이상 KR서버 에란겔에서 3판 진행 후\n"
        "등수, 킬, 생존시간 종합 점수를 계산 후 결정", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("!명령어"):
        embed = discord.Embed(title="명령어",
        description= "```diff\n-명령어 입력후 타이핑 한 명령어는 꼭     삭제해주세요!!!```"
                     "```diff\n+기본 명령어 부르는법 ![명령어이름]```\n"
        "!공지사항\n" "!승급조건\n" "!본인프로필\n" "!배그1,2,3\n"
        "!채널메시지", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("!도움말"):
        embed = discord.Embed(title="도움말",
        description="채널메시지 사용방법\n"
        "[!채널메시지(메시지를 보내려는 채널 ID를 복붙) (메시지입력)"
        "```추가사항이나 개선해줬으면 하는것은           '소리함'채널에 적어주시길 바랍니다.```", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("!본인프로필"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="Name", value=message.author.name, inline=False)
        embed.add_field(name="Join Date", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일", inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("!배그1"):
        embed = discord.Embed(title="배그하실분", description="@everyon 1명구합니다.", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)
    if message.content.startswith("!배그2"):
        embed = discord.Embed(title="배그하실분", description="@everyon 2명구합니다.", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)
    if message.content.startswith("!배그3"):
        embed = discord.Embed(title="배그하실분", description="@everyon 3명구합니다.", color=0x00ff00)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)




client.run("NjY5ODg0NDM4OTA1MDk0MTU0.XimUhw.9CeVX8i2Zm-lRjxJZEZpodJQL7Y")