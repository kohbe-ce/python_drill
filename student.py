from person import Person


class Student(Person):	   # Person 클래스를 상속 받음

	def study(self):
		print('열공열공...')


lee = Person()	# 일반 사람 이순신을 만든다.
print(lee.mouth)	# 이순신의 입 개수는?
lee.talk()		# 이순신 말걸기 시도

kim = Student()	# 학생 김유신을 만든다.
print(kim.mouth)	# 김유신의 입 개수는?
kim.talk()		# 김유신 말걸기 시도
kim.study()		# 김유신 공부 시키기