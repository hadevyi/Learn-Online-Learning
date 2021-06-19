fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
# 94646으로 출력됩니다.
print(inp[:20])
# From stephen.marquar으로 출력됩니다.
