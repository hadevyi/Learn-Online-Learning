class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()

'''
'나'는 자식의 Object 이므로, '나'의 '호출' 함수를 부르게 된다. 
'''