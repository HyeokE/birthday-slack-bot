# Slack-bot-gdsc
## 멤버 분들의 생일을 축하해주는 봇입니다

### 출력 예시
<img width="289" alt="Screen Shot 2021-08-31 at 3 21 24 AM" src="https://user-images.githubusercontent.com/61281239/131386141-c76bd6ee-8f89-4ca7-ab26-d7b079a406e4.png">

import
```
from datetime import *
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
```

array로 값을 받습니다.
```
array = [[Month, Day, "username1"],[3, 4, "username2"]]
```
Output
```
'------------------------------------------------\n'+
'['+nowDate.month.__str__()+' 월 '+nowDate.day.__str__()+ ' 일은 '+array[i][2]+' 님의 생일입니다~!!!!]\n'+
':tada::tada::tada: 생일 축하합니다~!!! :tada::tada::tada:\n'+
':party_blob::party_blob::meow_code:행복한 코딩생활하세요:meow_code::party_blob::party_blob:\n'+
'------------------------------------------------')
```
