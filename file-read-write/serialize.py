# 객체를 컴퓨터에 저장하기 위해서는 직렬화라는 과정이 필요하다
# 직렬화란 객체를 연속적인 데이터로 변환하는 것

# 파이썬에서 객체를 직렬화하는 모듈이 pickle
# pickle.dump(출력할 객체, 파일 객체) : 파일 객체에 출력할 객체를 저장한다.
# with open('test.txt', 'wb') as f :  => 바이트로  써야 한다

# pickle.dumps(출력할 객체) : 출력할 객체를 바이트의 형태로 반환한다.

import pickle

makeBite = pickle.dumps([1, 2, 3, 4])
print(makeBite)

# pickle.load(파일 객체) : pickle 을 통해 바이트화 되어 저장된 파일 객체를 원본의 모습으로 반환
print(pickle.loads(makeBite))
# pickle.loads(바이트 객체) : pickle 을 통해 바이트화 된 객체를 다시 원본의 모습으로 반환

# JSON 모듈
# > 파이썬에서만 쓸지 않고 모든 언어에서 사용할 수 있는 공통된 형식.
# > JSON 으로 직렬화 할 수 있는 객체는 한정적.

# import json
# json.dumps => String 형식으로 반환
# json.loads => String 형식의 데이터를 list 와 directory 등으로 복원

import json
jsonData = json.dumps({'a': 'b', 'c': 'd'})
print(jsonData)
print(json.loads(jsonData))

# with open('test.txt', 'w') as f:
    # json.dump([1, 2, 3, {'4': 5, '6': 7}], f) => 파일에 json 화된 객체를 저장

# with open('test.txt', 'r') as f:
    # json.load(f) => JSON 화된 data 를 list, dictionary 등으로 복원
