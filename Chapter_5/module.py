# module.py

import mod1

print(mod1.add(3, 4))
print(mod1.sub(5, 8))

# ----------------------------------------------------------
# 모듈 내 모듈 함수를 일부만 불러오는 방법

from mod1 import add

print(add(3, 4))
# print(sub(5, 8)) # sub은 호출하지 않았으므로 사용 불가

# ----------------------------------------------------------
# 모듈 내 모든 모듈 함수를 불러오는 방법

from mod1 import *

print(add(3, 4))
print(sub(5, 8))
