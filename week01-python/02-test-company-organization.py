#사람 클래스를 하나 만든다. 사람의 기본 요소는 이름, 나이, 성별
#직장 동룍 클래스를 사람 클래스를 이용해서 만든다. 사람 기본 요소 외 별도의 추가 사항은 직급
#클래스와 상속을 활용
#사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들때, 입력 받을 수 있도록
#직장 동료의 기본 직급은 "대라"로 지정
#사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서, 직급도 처음 만들어질 때 입력하도록 변경

class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Staff(People):
    def __init__(self, name, age, gender, title):
        super().__init__(name, age, gender)
        self.title = title

staff = Staff("marco", 20, "Female", "대리")
print(staff.__dict__)
