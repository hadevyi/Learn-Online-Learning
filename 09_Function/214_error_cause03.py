def 함수(a, b):
    print(a + b)


함수("안녕", 3)
# TypeError: must be str, not int
# 함수 내에서 각 인자가 덧셈(연산) 되고 있다. 따라서 str + int는 불가능해서 오류가 난다.
