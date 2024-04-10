class Student:

    def __init__(self, name, student_id , kr_quiz , ma_quiz , sc_quiz):
        self.__name = name
        self.__student_id = student_id
        self.__kr_quiz = kr_quiz
        self.__ma_quiz = ma_quiz
        self.__sc_quiz = sc_quiz
        self.__total_score = kr_quiz + ma_quiz + sc_quiz

    def set_kr_quiz(self, kr_quiz):
        if kr_quiz >= 100 and kr_quiz <= 0:
            self.__kr_quiz = kr_quiz

    def set_ma_quiz(self, ma_quiz):
        if ma_quiz >= 100 and ma_quiz <= 0:
            self.__ma_quiz = ma_quiz

    def set_sc_quiz(self, sc_quiz):
        if sc_quiz >= 100 and sc_quiz <= 0:
            self.__sc_quiz = sc_quiz

    def get_kr_quiz(self):
        return self.__kr_quiz

    def get_ma_quiz(self):
        return self.__ma_quiz

    def get_sc_quiz(self):
        return self.__sc_quiz

    def get_name(self, name):
        return self.__name 

    def get_student_id(self, student_id):
       return self.__student_id

    def get_total_score(self, kr_quiz, ma_quiz, sc_quiz, total_score):
        total_score=kr_quiz+ma_quiz+sc_quiz
        return self.__total_score

    def get_avg_score(self, total_score):
        return self.__total_score/3

    def __str__(self):
        return 'Student(이름 :'+self.__name+', 학번 :'+str(self.__student_id)+', 국어성적 :'+str(self.__kr_quiz)+', 수학성적 :'+str(self.__ma_quiz)+', 과학성적 :'+str(self.__sc_quiz)+', 합계 :'+str(self.__total_score)+', 평균 :'+str(self.__total_score/3)+')'


name = input('학생의 이름을 입력하세요. : ')
student_id = input('학생의 학번을 입력하세요. : ')



kr_quiz = int(input('학생의 국어 성적을 입력하세요. :  '))
ma_quiz = int(input('학생의 수학 성적을 입력하세요. : '))
sc_quiz = int(input('학생의 과학 성적을 입력하세요. : '))

student = Student(name, student_id, kr_quiz, ma_quiz, sc_quiz)

student.set_kr_quiz(kr_quiz)
student.set_ma_quiz(ma_quiz)
student.set_sc_quiz(sc_quiz)

print(student)
