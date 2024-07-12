import tkinter as tk  # GUI 생성

# tkinter 모듈에서 필요한 GUI 요소
from tkinter import Text, Scrollbar, Button, BooleanVar, Menu, messagebox, DISABLED, NORMAL  

import subprocess  # 외부 프로세스 실행
import threading  # 스레드 생성 및 관리
from queue import Queue  # 큐(Queue) 자료구조를 사용
import re  # 정규표현식 사용
import time  # 시간 관련 기능 사용



# Queue 객체 생성
url_queue = Queue()
total_tasks = 0
successful_tasks = 0
current_task = 0

# 시작 시간 초기화
start_time = 0



def check_rsack_version():
    result_text.focus_set()  # result_text에 포커스 설정
    result_text.see(tk.END)  # result_text의 커서 위치를 맨 아래로 이동
    
    command = 'rsack --version'

    result_text.insert(tk.INSERT, "===== rsack 버전 확인 =====\n\n")
    
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
        result_text.insert(tk.END, result)
        result_text.insert(tk.INSERT, "\n")
    except subprocess.CalledProcessError as e:
        error_message = f"오류 발생: {e.returncode}\n{e.output}"
        result_text.insert(tk.END, error_message)
    
    result_text.insert(tk.END, "\n\n")
    result_text.see(tk.END)  # 자동 스크롤



def run_rsack():
    global start_time, total_tasks, successful_tasks, current_task
    total_tasks = 0
    successful_tasks = 0
    current_task = 0
    start_time = time.time()  # rsack 실행 버튼을 누른 시간 기록

    # Update root window title to include start time
    update_title_with_time()

    urls = entry.get("1.0", tk.END).strip().splitlines()  # 입력 필드에서 여러 개의 URL 가져오기
    valid_urls = [url.strip() for url in urls if re.match(r'^https://www\.genie\.co\.kr/detail/albumInfo\?axnm=\d+$', url.strip())]
    
    if multi_album_download.get():
        url_queue.put("\n".join(valid_urls))  # 유효한 링크들을 한 번에 큐에 추가
        total_tasks = len(valid_urls)
    else:
        for url in valid_urls:
            url_queue.put(url)  # 큐에 유효한 URL 추가
            total_tasks += 1

    if not url_queue.empty():
        execute_next_rsack()



def execute_next_rsack():
    global current_task
    if not url_queue.empty():
        urls = url_queue.get().splitlines()
        for url in urls:
            command = f'rsack -u "{url}"'
            current_task += 1

            # "작업 시작" 문구를 맨 앞에 추가
            result_text.insert(tk.INSERT, f"===== 작업 시작: {url} ({current_task} / {total_tasks}) =====\n\n")
            result_text.see(tk.END)  # 자동 스크롤

            # 버튼, 입력 필드, 체크 박스 비활성화
            disable_buttons()

            # 결과 텍스트 위젯의 커서를 맨 아래로 이동
            result_text.see(tk.END)

            # 스레드를 사용하여 비동기적으로 명령어 실행
            thread = threading.Thread(target=execute_command, args=(command, url))
            thread.start()



def execute_command(command, url):
    global successful_tasks, current_task

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='euc-kr')

    def read_stream(stream, display_tag):
        while True:
            try:
                line = stream.readline()
                if not line and process.poll() is not None:
                    break
                if line:
                    result_text.insert(tk.END, line, display_tag)
                    result_text.see(tk.END)  # 자동 스크롤
            except UnicodeDecodeError:
                result_text.insert(tk.END, "UnicodeDecodeError: Cannot decode this line\n", 'stderr')

    stdout_thread = threading.Thread(target=read_stream, args=(process.stdout, 'stdout'))
    stderr_thread = threading.Thread(target=read_stream, args=(process.stderr, 'stderr'))

    stdout_thread.start()
    stderr_thread.start()

    stdout_thread.join()
    stderr_thread.join()

    process.stdout.close()
    process.stderr.close()
    process.wait()

    if process.returncode == 0:
        successful_tasks += 1

    # 작업 완료 메시지 추가
    if multi_album_download.get():
        result_text.see(tk.END)  # 자동 스크롤
    else:
        result_text.insert(tk.END, f"\n===== 작업 완료: {url} ({successful_tasks} / {total_tasks}) =====\n\n\n\n")
        result_text.see(tk.END)  # 자동 스크롤

    # 모든 작업이 완료된 후에 버튼 다시 활성화
    if successful_tasks == total_tasks:
        root.after(100, enable_buttons)  # 0.1초 후에 enable_buttons 함수 호출

    # 스레드 시작 전 1초 대기
    time.sleep(1)
    
    # 모든 작업이 완료된 후에 다음 URL 작업 실행
    execute_next_rsack()



def disable_buttons():
    # Disable buttons during task execution
    button_version.config(state=DISABLED)
    button_rsack.config(state=DISABLED)
    button_clear.config(state=DISABLED)
    entry.config(state=DISABLED)
    multi_album_checkbox.config(state=DISABLED)



def update_title_with_time():
    global start_time, current_task

    # 시작 시간부터 현재까지의 경과 시간 계산
    elapsed_time = time.time() - start_time
    elapsed_minutes = int(elapsed_time // 60)
    elapsed_seconds = elapsed_time % 60

    if start_time > 0 and current_task > 0:  # 작업이 시작된 후에만 제목 업데이트
        if multi_album_download.get():
            root.title(f"rsack GUI Manager (다중 다운로드 활성화) (진행 중 ({current_task}/{total_tasks}) - 소요 시간: {elapsed_minutes:02d}분 {elapsed_seconds:05.2f}초)")
        else:
            root.title(f"rsack GUI Manager (진행 중 ({current_task}/{total_tasks}) - 소요 시간: {elapsed_minutes:02d}분 {elapsed_seconds:05.2f}초)")
    else:  # 작업이 시작되지 않았거나 초기 상태일 때
        if multi_album_download.get():
            root.title("rsack GUI Manager (다중 다운로드 활성화)")
        else:
            root.title("rsack GUI Manager")

    if start_time > 0 or current_task > 0:  # 작업이 시작되었거나 진행 중일 때
        root.after(50, update_title_with_time)  # 0.05초마다 업데이트



def enable_buttons():
    global start_time
    
    button_version.config(state=NORMAL)
    button_rsack.config(state=NORMAL)
    button_clear.config(state=NORMAL)
    entry.config(state=NORMAL)
    multi_album_checkbox.config(state=NORMAL)

    # 체크 박스 상태 확인
    if delete_url_after_download.get():
        entry.delete("1.0", tk.END)  # 체크 박스가 체크되어 있으면 URL 입력 필드 지우기

    # 작업 시간 계산 및 작업 완료 메시지 추가
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_minutes = int(elapsed_time // 60)
    elapsed_seconds = elapsed_time % 60

    # 전체 작업 완료 메시지 추가
    if multi_album_download.get():
        result_text.insert(tk.INSERT, f"\n\n===== 전체 {total_tasks}개 작업 중 {successful_tasks}개의 다중 작업이 완료되었습니다. (소요 시간: {elapsed_minutes:02d}분 {elapsed_seconds:05.2f}초) =====\n\n\n\n")
    else:
        result_text.insert(tk.INSERT, f"===== 전체 {total_tasks}개 작업 중 {successful_tasks}개의 작업이 완료되었습니다. (소요 시간: {elapsed_minutes:02d}분 {elapsed_seconds:05.2f}초) =====\n\n\n\n")
    result_text.see(tk.END)  # 자동 스크롤

    # start_time 강제 초기화
    start_time = 0

    # 작업 완료 알림 표시
    if notify_after_completion.get():
        show_completion_notification()



def show_completion_notification():
    messagebox.showinfo("알림", f"작업이 완료되었습니다.")



def clear_result_text():
    result_text.delete('1.0', tk.END)  # 결과 텍스트 위젯의 모든 내용 삭제



"""
Context Menu

"""

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def cut():
    entry.event_generate("<<Cut>>")

def copy():
    entry.event_generate("<<Copy>>")

def paste():
    entry.event_generate("<<Paste>>")

def delete():
    entry.delete("sel.first", "sel.last")

def select_all():
    entry.tag_add("sel", "1.0", "end")

def exit_program():
    root.quit()



"""
도움말 메시지 박스 내용
"""
def show_help():
    help_text = """[안내]
rsack를 사용하여 음원 스트리밍 사이트에 업로드 된 앨범 URL을 입력하여 앨범을 다운로드 합니다.

rsack를 사용하려면 rsack에서 지원하는 음원 스트리밍 사이트 계정에 스트리밍 이용권(종류 무관)이 등록되어 있어야 합니다.



[체크 박스]
작업 후 입력 값 초기화:
ㄴ 비 활성화(기본값): 입력 값 유지
ㄴ 활성화: 모든 작업이 끝나면 입력 값 모두 삭제

다중 다운로드:
ㄴ 비 활성화(기본값): 입력한 URL을 하나씩 순차적으로 처리
ㄴ 활성화: 입력한 URL 전체를 한 번에 처리

작업 완료시 알림:
ㄴ 비 활성화(기본값): 화면 하단 Log 값 안내
ㄴ 활성화: 화면 하단 Log 값 + 메시지 박스 알림 안내



[버튼]
rsack 버전 확인: 사용 중인 PC에 설치된 rsack 버전 확인
rsack 실행: GENIE MUSIC Album URL 입력: 란에 입력한 앨범 URL 다운로드 처리
log Clear: 화면 하단 Log 값 모두 삭제
"""
    messagebox.showinfo("도움말(Help)", help_text)



def show_program_about():
    show_program_about_text = """rsack GUI Manager (Version 1.0)

Created by (Github) IZH318 in 2024.
"""
    messagebox.showinfo("정보(About)", show_program_about_text)



"""
GUI SETTINGS
"""
# GUI 창 생성
root = tk.Tk()
root.title("rsack GUI Manager")

# 메뉴 생성
menubar = Menu(root)

# 파일 메뉴
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="강제 종료(Force Exit)", command=exit_program)
menubar.add_cascade(label="파일(File)", menu=file_menu)

# 도움말 메뉴
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="도움말 보기(Help)", command=show_help)
help_menu.add_separator()  # 구분선 추가
help_menu.add_command(label="정보(About)", command=show_program_about)
menubar.add_cascade(label="도움말(Help)", menu=help_menu)

# 메뉴 설정
root.config(menu=menubar)

# 화면의 가로 및 세로 크기 구하기
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 창의 크기 설정
window_width = 854
window_height = 480

# 창을 화면 가운데에 위치시키기
position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)

# 위치 설정
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")



# 첫 번째 줄: 주소 입력
# 레이블 생성
label = tk.Label(root, text="Album URL 입력:")
label.grid(row=0, column=0, padx=10, pady=10)

# 입력 필드 스크롤 바 생성
entry_scrollbar = Scrollbar(root, orient=tk.VERTICAL)
entry_scrollbar.grid(row=0, column=4, sticky="ns")

# 입력 필드 생성
entry = Text(root, wrap=tk.WORD, width=70, height=4, yscrollcommand=entry_scrollbar.set)
entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")
entry_scrollbar.config(command=entry.yview)

# 입력 필드 마우스 오른쪽 클릭 컨텍스트 메뉴
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="모두 선택(Select All)", command=select_all)
context_menu.add_separator()  # 구분선 추가
context_menu.add_command(label="잘라내기(Cut)", command=cut)
context_menu.add_command(label="복사(Copy)", command=copy)
context_menu.add_command(label="붙여넣기(Paste)", command=paste)
context_menu.add_separator()
context_menu.add_command(label="삭제(Delete)", command=delete)

# 마우스 오른쪽 클릭 이벤트 바인딩
entry.bind("<Button-3>", show_context_menu)



# 두 번째 줄: 체크 박스
delete_url_after_download = BooleanVar()
checkbox = tk.Checkbutton(root, text="작업 후 입력 값 초기화", variable=delete_url_after_download)
checkbox.grid(row=1, column=0, padx=10, pady=0, sticky="n")

multi_album_download = BooleanVar()
multi_album_checkbox = tk.Checkbutton(root, text="다중 다운로드", variable=multi_album_download, command=update_title_with_time)
multi_album_checkbox.grid(row=1, column=1, padx=10, pady=0, sticky="n")

notify_after_completion = BooleanVar()
notify_checkbox = tk.Checkbutton(root, text="작업 완료시 알림", variable=notify_after_completion)
notify_checkbox.grid(row=1, column=2, padx=10, pady=0, sticky="n")



# 세 번째 줄: 버튼
button_version = Button(root, text="rsack 버전 확인", command=check_rsack_version)
button_version.grid(row=2, column=0, padx=10, pady=5, sticky="n")

button_rsack = Button(root, text="rsack 실행", command=run_rsack)
button_rsack.grid(row=2, column=1, padx=10, pady=5, sticky="n")

button_clear = Button(root, text="log Clear", command=clear_result_text)
button_clear.grid(row=2, column=2, padx=10, pady=5, sticky="n")



# 네 번째 줄: 결과 텍스트
# 결과 텍스트 위젯 생성
result_text = Text(root, wrap=tk.WORD, height=20)
result_text.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# 결과 텍스트 위젯과 스크롤바 연결
scrollbar = Scrollbar(root, command=result_text.yview)
scrollbar.grid(row=3, column=4, sticky="nsew")
result_text.config(yscrollcommand=scrollbar.set)

# stdout과 stderr의 스타일 설정
result_text.tag_config('stdout', foreground='black')
result_text.tag_config('stderr', foreground='red')



# 창 크기 조정 설정
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(1, weight=1)

# GUI 실행
root.mainloop()
