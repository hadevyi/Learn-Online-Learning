'''
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)
와 동일한 기능을 하는 코드를 작성하기
'''
data = ["A", "B", "C"]

for i in range(len(data)):
    b = data[i].lower()
    print("변환:", b)
