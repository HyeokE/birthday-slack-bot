from datetime import *
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
array = [
    [9, 14, "박현기"],
    [3, 15, "강지명"],
    [9, 9, "정준혁"],
    [5, 9, "안주원"],
    [7, 9, "유형찬"],
    [5, 3, "임종수"],
    [11, 17, "황지영"],
    [1, 23, "김수진"],
    [4, 24, "정소연"],
    [2, 21, "라허운"],
    [7, 13, "신현민"],
    [1, 24, "서정우"],
    [9, 28, "박진혜"],
    [11, 15, "신동석"],
    [5, 23, "김지훈"],
    [9, 29,"깃헙 액션 테스트"],
    [10, 11, " 한글"],
]
nowDate = datetime.now()
# print(nowDate.month , nowDate.day)

try:
    client = WebClient(token="xoxb-2388082878180-2442111717364-dJ2GK2Rk2ASTgGd47Zb5Neq5")
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



