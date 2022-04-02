# 외장 함수
# > 다른 사람이 미리 정의해 놓은 함수. 파이썬을 설치할 때 자동으로 컴퓨터에 설치돼 있다.
# > Import 키워드를 사용해서 외장함수를 사용 가능하게 만든다.

# 1. time.
# > time.time()
import time

print(time.time())  # UTC 시간

# > time.sleep(x) : x초 동안 대기한다
# > time.localtime() : time.time() 에서 나온 실수 값을 이용해, 우리가 보기 편한 방식의 형태로 바꿔준다

print(time.localtime(time.time()))

# > time.strftime(출력할 형식, time.localtime(time.time())) : time.localtime 로 만든 객체를 출력할 형식 모양에 맞춘다
# >> time.strftime("%Y-%m-%d, ~~) H: 시간, M: 분, S: 초

print(time.strftime("%Y-%m-%d", time.localtime(time.time())))

# 2. OS, Sys
import os
import sys

# > sys.path : 파이썬 모듈들이 저장돼 있는 위치를 반환
print(sys.path)

# > os : 환경 변수, 디렉토리, 파일 등의 os 자원을 제어한다
# > os.environ : 내 시스템 환경 보기
print(os.environ)
# > os.getcwd() : 현재 위치 확인
print(os.getcwd())
# > os.chdir(path) : 현재 디렉토리 위치 변경
