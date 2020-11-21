class OMG:
    def print():
        print("Oh my god")


'''
>>> >>> myStock = OMG()
>>> myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given


이유 : 현재있는 클래스를 통해 print()는 자기자신을 호출하는 재귀함수의 꼴이 된다.
하지만 Method는 인자가 없는 형식이므로 내부 print에서 "Oh my god"을 정의하면 정의와 호출이 알맞지 않아 argument 오류가 나게된다.
'''
