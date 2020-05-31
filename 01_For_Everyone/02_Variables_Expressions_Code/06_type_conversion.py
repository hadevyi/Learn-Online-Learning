i = 42
type( i ) # int 타입
f = float( i ) # float 타입으로 변환
print( f ) # 42.0으로 출력
type( f ) # float 타입

sval = '123'
type(sval) # str 타입
#print(sval + 1) # 문자열과 int를 더한 것이므로 오류

ival = int(sval)
type(ival) # int 타입
print(ival + 1) # int 타입 간 연산이기 때문에 오류 발생하지 않는다. 124로 출력됨
