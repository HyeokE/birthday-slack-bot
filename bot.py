from datetime import *
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime as dt
import pytz as pytz
#member list
array = [
    ['month', 'date', "name"],
]
Month = datetime.now(pytz.timezone('Asia/Seoul')).strftime('%m')
Date = datetime.now(pytz.timezone('Asia/Seoul')).strftime('%d')
# print(datetime.now(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S'))
# print (Month, Date)
#
# for i in range (len(array)):
#        if (Month == array[i][0] and Date == array[i][1]):
#             print(array[i][0], array[i][1])
#             print (array[i][2])


try:
    client = WebClient(token="xoxb-2388082878180-2442111717364-WNUYSV6fnpU3OU8zgsXSNCxq")
    for i in range (len(array)):
        if (Month == array[i][0] and Date == array[i][1]):
            # print(array[i][0], array[i][1])
            # print (i)
            client.chat_postMessage(
                channel = "#일반",
                text =
                '------------------------------------------------\n'+
                '['+Month+' 월 '+Date+ ' 일은 '+array[i][2]+' 님의 생일입니다~!!!!]\n'+
                ':tada::tada::tada: 생일 축하합니다~!!! :tada::tada::tada:\n'+
                ':party_blob::party_blob::meow_code:행복한 코딩생활하세요:meow_code::party_blob::party_blob:\n'+
                '------------------------------------------------')
    if (Month == 8 and Date == 31):
        # print(array[i][0], array[i][1])
        client.chat_postMessage(
            channel = "#일반",
            text =
            '------------------------------------------------\n'+
            '['+Month+' 월 '+Date+ ' 일은 BOT의 생일입니다~!!!!]\n'+
            ':tada::tada: 생일 축하합니다~~!!~~!!:tada::tada:\n'+
            ':party_blob::party_blob::meow_code:행복한 코딩생활하세요:meow_code::party_blob::party_blob:\n'+
            '------------------------------------------------')

except SlackApiError as e:
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")



