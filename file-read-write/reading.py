# read() : 파일 전체 내용을 문자열로 반환
file = open('test.txt')

print(file.read())

file2 = open('../root_test.txt')

print(file2.read())

# readlines() : 파일의 모든 줄을 읽고 각 줄을 리스트로 바꿈

newFile = open('test_lines.txt')

print(newFile.read())

print(newFile.readlines())

# readline() : 파일의 첫 줄을 읽고 문자열을 반환. 재호출시 그 다음 줄 반환

newFile2 = open('test_lines.txt')
print(newFile2.readline())
print(newFile2.readline())
print(newFile2.readline())

# for : for 제어문으로 읽으면 줄 별로 문자열
forFile = open('test_lines.txt')

for i in forFile:
    print('for', i)
