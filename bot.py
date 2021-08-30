from datetime import *
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
array = ['month', 'day', 'username']
nowDate = datetime.now()
# print(nowDate.month , nowDate.day)

try:
    client = WebClient(token="Token")
    for i in range (len(array)):
        if (nowDate.month == array[i][0] and nowDate.day == array[i][1]):
            # print(array[i][0], array[i][1])
            # print (i)
            client.chat_postMessage(
                channel = "#일반",
                text =
                '------------------------------------------------\n'+
                '['+nowDate.month.__str__()+' 월 '+nowDate.day.__str__()+ ' 일은 '+array[i][2]+' 님의 생일입니다~!!!!]\n'+
                ':tada::tada::tada: 생일 축하합니다~!!! :tada::tada::tada:\n'+
                ':party_blob::party_blob::meow_code:행복한 코딩생활하세요:meow_code::party_blob::party_blob:\n'+
                '------------------------------------------------')
    if (nowDate.month == 8 and nowDate.day == 31):
        # print(array[i][0], array[i][1])
        client.chat_postMessage(
            channel = "#일반",
            text =
            '------------------------------------------------\n'+
            '['+nowDate.month.__str__()+' 월 '+nowDate.day.__str__()+ ' 일은 BOT의 생일입니다~!!!!]\n'+
            ':tada::tada: 생일 축하합니다~~!!~~!!:tada::tada:\n'+
            ':party_blob::party_blob::meow_code:행복한 코딩생활하세요:meow_code::party_blob::party_blob:\n'+
            '------------------------------------------------')

except SlackApiError as e:
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")



