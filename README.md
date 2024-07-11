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
(📌 미처 누르지 못했다면 설치파일을 다시 실행 또는 소프트웨어 제거 후 재 설치) <BR> <BR>
![2024-07-12 04 27 26](https://github.com/user-attachments/assets/050db49e-0478-4f0f-9ce8-44fdef0cadc9) <BR>
**[ ※ 주의 ] 설치 후 Disable path length limit 기능을 사용할 수 있도록 반드시 클릭** <BR>
(📌 미처 누르지 못했다면 설치파일을 다시 실행 또는 소프트웨어 제거 후 재 설치) <BR> <BR> <BR> <BR>


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
01. `rsack GUI Manager.py`를 실행합니다. <BR>
![2024-07-12 04 28 40](https://github.com/user-attachments/assets/a000a4df-e152-4d8a-8fd7-36acbd814d03) <BR><BR><BR>



2. `01_Install` 폴더로 이동 후 본문 상단 `💾 다운로드`을 참고하여 파일을 설치합니다. <BR>
![2024-05-31 20 53 59](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/0941493c-3d3d-4964-862d-4a21dc6cb768) <BR>
![2024-05-31 20 48 52](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/eb56167a-9aa0-40b8-8dd0-80357f9aae92) <BR>
**[ ※ 주의 ] Python 설치 시 Add python.exe to PATH 에 반드시 체크 후 Install Now 클릭** <BR>
(📌 미처 누르지 못했다면 설치파일을 다시 실행 또는 소프트웨어 제거 후 재 설치) <BR><BR><BR>



3. 모두 설치가 끝났다면 `02_Tools` 폴더로 이동합니다. <BR>
![2024-05-31 20 55 06](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/cc8225d5-65a8-4990-8529-b56a17468d83) <BR><BR><BR>



4. `00. Install required Python packages.bat` 파일을 실행하여 Python Package를 설치합니다. <BR>
![2024-05-31 20 50 43](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/5fe76b28-4bb5-4a86-9953-8e0dc91f55b9) <BR>
![녹화_2024_05_31_17_38_16_882 mp4_snapshot_00 00 000](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/decb8bb1-f0c8-4835-8420-e9e39c09b2b7) <BR>
![녹화_2024_05_31_17_38_16_882 mp4_snapshot_00 11 697](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/6bb9696e-52a6-42bb-9389-9872c38c257b) <BR>
(📌 필수 Python Package 설치가 끝나면 위와 같은 화면이 표시됩니다.) <BR><BR><BR>



5. 게임 클라이언트 원본 구조를 그대로 유지한 상태로 스크립트가 있는 경로로 불러옵니다. <BR>
![2024-05-31 21 00 58](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/05fe810b-1273-447a-b31e-5d2250b758b3) <BR><BR><BR>



6. `01. Manifest File Renamer.py` 파일을 실행하여 SHA1 Hash로 저장 된 파일 이름을 변경합니다. <BR>
![2024-05-31 21 02 05](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/677400d6-2c57-46e5-b235-3c9dc25e6817) <BR>

![녹화_2024_05_31_21_06_50_102 mp4_snapshot_00 00 000](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/f232bf41-85ff-4352-ba32-af4c0907c695) <BR>

![ezgif-6-3dc6ee929c](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/a053907f-6979-4806-a488-d7706425407f) <BR>

![녹화_2024_05_31_21_06_50_102 mp4_snapshot_00 01 282](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/ca0a94af-f572-45a8-8934-8c8c4eeb1514) <BR>
(📌 파일 이름이 모두 변경되면 위와 같은 화면이 표시됩니다.) <BR><BR><BR>



7. `02. unity3d File Converter.py` 파일을 실행하여 *.unity3d 파일에서 Asset을 추출(변환)합니다. <BR>
![2024-05-31 21 12 57](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/4c9d07e1-1742-4b7b-98a9-fa4b42c8e73f) <BR>

![녹화_2024_05_31_20_20_40_361 mp4_snapshot_00 00 000](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/db40c687-b9ce-47f6-b76f-1e2981b2c7e1) <BR>

**[ 🛑 경고 🛑 ] 반드시 저장 공간이 여유로운 곳에서 작업하십시오.** <BR><BR>

![ezgif-4-d611beffd8](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/e2c76417-ebdf-426b-b469-a5dee82cb669) <BR>

![녹화_2024_05_31_20_20_40_361 mp4_snapshot_00 01 294](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/0f3ec38f-028a-4116-b1f9-2f09849eb054) <BR>
(📌 작업이 성공적으로 끝나면 위와 같은 화면이 표시됩니다.) <BR><BR>

![2024-05-31 21 15 56](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/d1c9438c-9041-4cda-ac9b-100d83e0a487) <BR>
(📌 `\a\_Converted` 폴더) <BR><BR>

작업이 성공적으로 끝나면 원본 Resource 폴더 내 `_Converted` 폴더가 생성되며, 해당 폴더 내부에 원본 *.unity3d 파일 이름으로 추출(변환) 된 Asset이 저장되어 있는 것을 확인할 수 있습니다. <BR><BR><BR>



8. `03. Audio File Converter.py` 파일을 실행하여 *.acb, *.awb 파일에서 Resource를 추출(변환)합니다. <BR>
![2024-05-31 21 22 58](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/4cb398ea-d2d0-4984-ac83-8a51a6b51cd6) <BR>

![녹화_2024_05_31_20_26_39_551 mp4_snapshot_00 00 000](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/e81762eb-3af8-4b86-974d-1e5ff84b0e86) <BR>

**[ 🛑 경고 🛑 ] 반드시 저장 공간이 여유로운 곳에서 작업하십시오.** <BR><BR>

![ezgif-4-575f84a008](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/3820ad83-fd3d-4230-b038-79fa6c81c287) <BR>

![녹화_2024_05_31_20_26_39_551 mp4_snapshot_00 07 285](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/41f5457a-7144-4e52-bd80-44fd3976c1cf) <BR>
(📌 작업이 성공적으로 끝나면 위와 같은 화면이 표시됩니다.) <BR><BR>

![2024-05-31 21 23 46](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/eb12e53a-4bec-4e65-a6cc-d7703a67c479) <BR>
(📌 `\b\_Converted` 폴더) <BR><BR>

작업이 성공적으로 끝나면 원본 Resource 폴더 내 `_Converted` 폴더가 생성되며, 해당 폴더 내부에 원본 *.acb 파일 이름 또는 *.awb 파일 이름으로 추출(변환) 된 Resource가 저장되어 있는 것을 확인할 수 있습니다. <BR><BR><BR>



9. `04. Video File Converter.py` 파일을 실행하여 *.usm 파일에서 Resource를 추출(변환)합니다. <BR>
![2024-05-31 21 25 04](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/841748fe-f346-44eb-8857-b2c2641056ff) <BR>

![녹화_2024_05_31_20_26_57_870 mp4_snapshot_00 00 000](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/8c64043f-af90-45dd-a0df-c93698c72d4e) <BR>

**[ 🛑 경고 🛑 ] 반드시 저장 공간이 여유로운 곳에서 작업하십시오.** <BR><BR>

![ezgif-4-37e0380221](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/98854e82-e073-4c55-8936-130a02186318) <BR>

![녹화_2024_05_31_20_26_57_870 mp4_snapshot_00 02 951](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/cd142076-b903-4a24-a33d-f322197d39fa) <BR>
(📌 작업이 성공적으로 끝나면 위와 같은 화면이 표시됩니다.) <BR><BR>

![2024-05-31 21 28 45](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/18675838-dd2b-4a0f-a5dc-30d3cc385eea) <BR>
(📌 `\m\_Converted` 폴더) <BR><BR>

작업이 성공적으로 끝나면 원본 Resource 폴더 내 `_Converted` 폴더가 생성되며, 해당 폴더 내부에 원본 *.usm 파일 이름으로 추출(변환) 된 Resource가 저장되어 있는 것을 확인할 수 있습니다.



<BR><BR><BR>

## 선택 작업
**아래 작업은 필수 작업은 아니며, 필요에 따라 사용하시면 됩니다.** <BR><BR>

**[선택 작업]** <BR>
캐릭터 명을 모두 추출하고 싶다면 `05. Character List Export.py` 파일을 실행합니다. <BR><BR>
![녹화_2024_05_31_20_34_50_160 mp4_snapshot_00 00 000](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/066c93b1-5395-470a-9478-e65e0b6f7f07) <BR>

![ezgif-5-fbc7712a65](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/70735b26-c6c5-47c4-a7d7-6f5d0ca0f25a)

<BR><BR><BR>



**[선택 작업]** <BR>
입력 한 캐릭터명 전체 또는 일부를 기준으로 대사 정보 및 Audio 파일 정보를 찾고싶다면 `06. Vocal Resource Info Export.py` 파일을 실행합니다. <BR><BR>
![캡처_2024_05_31_21_53_33_344](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/0c190cf7-6d68-4967-9a0f-1e928fe35538) <BR>

![ezgif-6-c9bead1666](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/dd55be38-851c-4400-a665-bcc946c43db4) <BR>

예를 들어, 'コッコロ(=콧코로)'를 입력하지 않고, 'コ'만 입력 후 검색을 하면 모든 캐릭터 이름 중 'コ'가 포함 된 캐릭터 모두 결과값을 반환합니다. <BR>
(📌 위 GIF에 녹화 된 내용 기준으로 'コッコロ(콧코로)', 'ペコリーヌ(=페코린느)', 'マコト(=마코토)', 'ミヤコ(=미야코)' 등 'コ'가 포함 된 결과가 출력 된 것을 확인할 수 있습니다.)

<BR><BR><BR>



**[선택 작업]** <BR>
원본 Resource 파일을 모두 제거하려는 경우 `07. Original Resource Remover.bat` 파일을 실행하여 원본 Resource 파일을 제거합니다. <BR><BR>
![녹화_2024_05_31_20_43_14_736 mp4_snapshot_00 00 263](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/81051272-7a83-4669-b01b-0b46f23747ac) <BR>
![ezgif-6-5b02b54d9b](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/4fc88979-1fdd-4385-bf3e-876d0a022821)

<BR><BR><BR>
























## ⚙ 코드 수정 (선택)
### ※ 이 작업은 Python 언어로 작성 된 Script의 내용을 이해하고 응용할 수 있는 분들께 추천드리는 작업입니다. <BR><BR>

### ❗ 필수 작업 ❗ <BR>
![PRICONNE_EXTRACTION_TOOLS(Portable)_AIO 읽기전용 해제 지시](https://github.com/IZH318/PRICONNE_EXTRACTION_TOOLS_Portable/assets/99892351/33179bbf-4e0d-4624-9b1d-4e313879d2bb) <BR>
제공 된 Python Script를 수정하고자 하는 파일 선택 후 `마우스 우클릭 -> 속성 -> 일반 -> 특성`항목 중 `읽기 전용(R)`상태 해제 후 확인 <BR><BR>

<BR><BR><BR>



## 해야 할 일
- (없음)

<BR><BR><BR>



## Special Thanks to
✨ Slyyxp ( https://github.com/Slyyxp ) <BR>
