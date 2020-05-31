astr = "123"

try:
    print("Hello")
    isInt = int(astr)
    print("World")
except:
    isInt = "Integer로 변환할 수 없습니다."

print('Done', isInt)
# Hello
# World
# Done 123이 순서대로 출력됩니다.
