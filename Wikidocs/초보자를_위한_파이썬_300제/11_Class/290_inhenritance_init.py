class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

'''
자식생성이 출력되고, 상위 클래스의 생성자를 호출한다.
따라서 자식생성 후 부모 생성이 출력된다.
'''