# rsack GUI Manager
rsack를 GUI로 사용할 수 있게 만든 추가 파이썬 코드 입니다. <BR>
(* rsack GUI Manager를 사용하려면 rsack가 설치되어 있어야 합니다.)

<BR> <BR> <BR>



## 🔍 주요 기능
■ 단일 또는 다중 앨범 링크를 입력란에 작성하면 직접 명령어를 입력 할 필요 없이 모든 작업이 순차적 또는 일괄 처리 됩니다. <BR>
( ※ rsack의 자세한 기능은 https://github.com/Slyyxp/rsack 참고) <BR>

<BR> <BR> <BR>



## 💾 다운로드
### ※ 본 Repositories에 업로드 된 rsack GUI Manager.py 파일을 직접 다운 또는 복사하거나, Releases로 이동하여 다운로드 하십시오. <br><br>
### ※ 본 도구를 사용할 때 필요한 모든 파일들은 zip 파일 내 `📁\01_Install` 폴더에 포함되어 있습니다. <BR>
***본 Repositories Releases에 제공 된 .zip 파일을 사용하려는 경우 개별 다운로드 과정을 생략해도 되며, 제공 된 설치 파일들을 신뢰하지 않을 경우 아래 링크를 통해 개별 다운로드 하시기 바랍니다.** <BR>

| Program                                | URL                                                | 필수여부 | 비고                                                                                           |
|----------------------------------------|----------------------------------------------------|----------|------------------------------------------------------------------------------------------------|
| `Python 3.9.0`            | [Download](https://www.python.org/downloads/release/python-390/)   | 필수     | ◼ Python Script 동작, 파이썬 3.9.0 버전 또는 그 이상 사용 가능 |

<BR> <BR> <BR>



## ❗ 주의 사항 ❗
### ※ 모든 내용은 2024-07-12 기준입니다.
### ※ 반드시 저장 장치의 여유 공간을 확인 후 작업하시기 바랍니다.
### ※ 미처 발견하지 못한 오류가 있을 수 있습니다.

<BR> <BR> <BR>



## ⏩ 설치 방법 (초급자용 설명서)
01. Python 공식 홈페이지에서 설치 파일을 다운로드 받거나 Repositories에서 다운로드 받은 zip 파일을 적절한 위치에 압축 해제 한 후 Python 설치 파일을 실행 합니다. <BR> <BR>
![2024-07-12 04 26 46](https://github.com/user-attachments/assets/7c88f4e1-3414-4268-8a14-cee13ac12233) <BR> <BR>
or <BR> <BR>
![2024-07-12 04 26 55](https://github.com/user-attachments/assets/56d9006d-b28d-46f3-bd2d-9ffe383ead12) <BR> <BR>
![2024-07-12 04 47 21](https://github.com/user-attachments/assets/b9242a42-c989-449f-974e-22a2ece46fd3)

<BR> <BR> <BR>



2. Python을 설치합니다. <BR> <BR>
![2024-07-12 04 27 14](https://github.com/user-attachments/assets/6cb0b356-e12f-4714-adde-30cd9850ec81) <BR>
**[ ※ 주의 ] Python 설치 시 Add python.exe to PATH 에 반드시 체크 후 Install Now 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 또는 제거 후 재 설치) <BR> <BR>
![2024-07-12 04 27 26](https://github.com/user-attachments/assets/050db49e-0478-4f0f-9ce8-44fdef0cadc9) <BR>
**[ ※ 주의 ] 설치 후 Disable path length limit 기능을 사용할 수 있도록 반드시 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 후 작업 또는 제거 후 재 설치) <BR> <BR> <BR> <BR>


3. 모두 설치가 끝났다면 키보드 `Win + R` 또는 `시작 -> 검색`란에 `cmd`를 입력하여 cmd를 실행합니다. <BR> <BR>
![2024-07-12 04 37 07](https://github.com/user-attachments/assets/c403930d-a1b3-469f-b0ee-3811e7d68b8e) <BR> <BR> <BR> <BR>



4. cmd가 실행되었다면 아래 내용을 참고하여 필요한 패키지를 업데이트(선택) 또는 설치 합니다. <BR> <BR>
4-1. **(선택사항, 생략가능) Python Package Update** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip` <BR>
or <BR>
`python -m pip install --upgrade pip` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip --user` <BR>
or <BR>
`python -m pip install --upgrade pip --user` <BR>
<BR> <BR> <BR>
4-2. **(필수) rsack Package 설치** <BR> <BR>
`pip install rsack` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 사용) <BR>
`pip install rsack --user` <BR>
<BR> <BR> <BR>
4-3. **(필수) BeautifulSoup4 설치** <BR> <BR>
`pip install beautifulsoup4` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 사용) <BR>
`pip install beautifulsoup4 --user` <BR>
<BR> <BR> <BR>



5. (필수) rsack_settings.ini 파일 생성 <BR> <BR>
5-1. 확장자 숨김 처리 해제 <BR> <BR>
![확장자 표시 설명](https://github.com/user-attachments/assets/ec81c43a-2c51-48c3-bcfe-d681cedd0832) <BR>
(📌 **[ ※ 필수 ]** 확장자가 숨김 처리 된 상태인 경우 반드시 위 스크린 샷 참고하여 확장자 표시 상태로 작업 ) <BR> <BR> <BR> <BR>
5-2. PC 계정 폴더로 이동 후 rsack_settings.ini 생성 <BR> <BR>
![2024-07-12 04 52 57](https://github.com/user-attachments/assets/e2db3ffd-b622-42f9-bb9a-c483d1d4a6bc) <BR> <BR>
![2024-07-12 04 51 28](https://github.com/user-attachments/assets/751b9658-0b1d-4848-8c59-e7a4604b6ce0) <BR>
(📌 PC 계정 명이 User 인 경우 `C:\Users\User` 로 이동 후 rsack_settings.ini 생성 ) <BR> <BR> <BR> <BR>
5-3. rsack_settings.ini 내용 작성 <BR> <BR>
**[ ※ 주의 ] 반드시 https://github.com/Slyyxp/rsack/blob/master/rsack_settings.ini.example 전체 코드 기반으로 작업** <BR> <BR> <BR> <BR>
![2024-07-12 05 06 58](https://github.com/user-attachments/assets/8d28ca3c-4583-4014-97b5-ab7b6e4f9d53) <BR>
(📌 위 링크 이동 후 전체 본문 복사 후 붙여넣고 proxy 설정은 반드시 `proxy = false`로 수정) <BR> <BR>
![2024-07-12 04 28 25](https://github.com/user-attachments/assets/19c098fe-7a65-4723-a076-68e242de3400) <BR>
(📌 위 예시는 아래와 같음 (* 아래 내용은 단순히 참고용으로만 사용) ) <BR> <BR>
![2024-07-12 05 19 06](https://github.com/user-attachments/assets/8091ade2-cf9b-44ae-aa41-8a7e8b71e280) <BR>
(📌 만약, 한글이 포함 된 경로를 사용하거나, 주석을 포함하여 저장하고 싶은 경우 `UTF-8` 인코딩이 아닌 `ANSI` 인코딩으로 설정 변경 후 저장) ) <BR>
```
# 지니뮤직 정보만 할당
[Genie]
# 사용자 계정 명 (* 만약, 지니뮤직 아이디가 abc1234 일 경우)
username = abc1234

# 사용자 계정 비밀번호 (* 만약, 지니뮤직 비밀번호가 def5678!@ 일 경우)
password = def5678!@

# 한 번에 처리 될 곡의 수 (* PC 사양과 인터넷 속도에 따라 적절히 설정, 잘 모르겠다면 1~10 사이로 설정 (기본값: 2))
threads = 2

# 파일이 저장 될 경로 (* 사용자 계정명이 User 이고 바탕화면 test 폴더에 음악 다운로드 (* 기본 값: C:\Music\Korean))
path = C:\Users\User\Desktop\test

timed_lyrics = true
contributions = false

# 음악이 저장 되는 폴더 규칙 (* 반드시 접두사 template = \ 는 입력되어 있어야 함)
template = \{artist}\{artist} - {title}

# proxy 설정(* 반드시 false로 설정해야 하며, 다른 값 입력시 오류 발생)
proxy = false
```
<BR> <BR> <BR>



## ⏩ 사용 방법
01. `rsack GUI Manager.py`를 실행합니다. <BR> <BR>
![2024-07-12 05 33 07](https://github.com/user-attachments/assets/d83eabf5-525c-4a04-be21-80dda4d39278) <BR> <BR> <BR> <BR>



2. `rsack GUI Manager GUI` 상단 Album URL 입력: 란에 URL을 입력합니다. (* 한 줄당 하나의 URL 입력) <BR> <BR>
![2024-07-12 05 34 53](https://github.com/user-attachments/assets/763fb190-38df-42c3-8e9a-58c204866855) <BR>
(📌 `https://www.genie.co.kr/detail/albumInfo?axnm=`로 시작하는 문자열만 Que에 올라서 처리 됩니다.) <BR> <BR> <BR> <BR>



3. Album URL을 입력했다면 `rsack 실행`버튼을 누르거나, 체크 박스 기능을 활성화 하고 `rsack 실행`버튼을 누릅니다. <BR> <BR>
![_2024_07_12_05_28_42_749-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/4ecfe8d3-7b4c-4cae-8544-3299c886e56e) <BR>
(📌 `rsack 버전 확인`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_12_05_28_49_89-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/822b7f8a-fd2c-40bb-9a44-7728223f919a) <BR>
(📌 `log Clear`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_12_05_29_04_620-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/e78a3c4f-f3af-4092-a949-39cf992b3845) <BR>
(📌 `작업 후 입력 값 초기화`, `작업 완료시 알림` 체크 박스 활성화 후 `rsack 실행`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_12_05_29_33_396-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/838d7691-496b-48a6-bf56-dcadf455970a) <BR>
(📌 `다중 다운로드` 체크 박스 활성화 후 `rsack 실행`버튼 클릭) <BR> <BR> <BR> <BR>



## ⚙ 코드 수정 (선택)
### ※ 이 작업은 Python 언어로 작성 된 Script의 내용을 이해하고 응용할 수 있는 분들께 추천드리는 작업입니다. <BR><BR>

### ❗ 필수 작업 ❗ <BR>
![PRICONNE_EXTRACTION_TOOLS(Portable)_AIO 읽기전용 해제 지시](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/33179bbf-4e0d-4624-9b1d-4e313879d2bb) <BR>
제공 된 Python Script를 수정하고자 하는 파일 선택 후 `마우스 우클릭 -> 속성 -> 일반 -> 특성`항목 중 `읽기 전용(R)`상태 해제 후 확인 <BR> <BR> <BR> <BR>

01. `https://www.genie.co.kr/detail/albumInfo?axnm=`로 시작하는 URL만 Que에 할당하는 기능 삭제 <BR> <BR>
57번째 줄 `valid_urls = [url.strip() for url in urls if re.match(r'^https://www\.genie\.co\.kr/detail/albumInfo\?axnm=\d+$', url.strip())]` 코드를 `valid_urls = [url.strip() for url in urls]` 로 수정 <BR> <BR> <BR> <BR>



02. 순차 다운로드(`다중 다운로드` 체크 박스 비 활성화)시 하나의 URL 처리 후 대기 시간 조절 <BR> <BR>
141번째 줄 `time.sleep(1)` 코드 괄호 내 숫자 조절 (* 1 = 1초) <BR> <BR> <BR> <BR>



## 해야 할 일
- (없음)

<BR> <BR> <BR>



## Special Thanks to
✨ Slyyxp ( https://github.com/Slyyxp ) <BR> <BR> <BR> <BR>
