#학교 클래스 만들기
#이름 설립연도, 주소 포함
#클래스 퐐성화 시, 위의 3 데이터 반드시 입력하도록

#School variables
class School:
    def __init__(self, name, year, address):
        self.name=name
        self.year=year
        self.address=address

school1=School("봉덕", "2000", "대구")
school2=School("효명", "2010", "부산")
school3=School("강남", "2000", "서울")

print(school1.name)
