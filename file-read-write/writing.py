# open( ) 의 두 번째 파라미터로 파일 여는 방식을 지정할 수 있다
# > r : 읽기용
# > w : 쓰기용 단, 이미 같은 경로에 파일이 존재할 경우 내용을 지움
# > a : 쓰기용 단, 이미 같은 경로에 파일이 존재할 경우 내용 덧붙임
# > x : 베타적 생성모드. 파일이 이미 존재하면 예외를 일으킴
# > rb : 바이트 어레이 읽기
# > wb : 바이트 어레이 쓰기

file = open('test.txt', 'w')
# 이미 존재하는 내용이 있다면 'w' 라서 지워버린다
file.write('새로운 줄')
file.close()

newFile = open('test.txt', 'a')
newFile.write('\n또 다른 줄 생성')
newFile.close()
# With ~ as
# > open 과 함께 with ~ as 구문을 사용하면 명시적으로 close() 를 사용하지 않아도 파일이 항상 닫힌다
with open('test.txt', 'r') as file:
    text = file.read()
    print(text)