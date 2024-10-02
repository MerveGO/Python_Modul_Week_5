class School:
    def __init__(self,name,foundation_year):
        self.name=name
        self.foundation_year=foundation_year
        self.students=[]
        self.teachers={}

    def add_new_student(self,student_name,student_class):
        self.students.append((student_name,student_class))
        print(f"Yeni ogrenci basariyla eklendi.\n{student_name},Sinif:{student_class}")

    def add_new_teacher(self,teacher_name,branch):
        self.teachers[teacher_name]=branch
        print(f"Yeni ogretmen basariyla eklendi.\n{teacher_name}\nBrans:{branch}")

    def view_student_list(self):
        print("Ogrenciler:")
        for student_name,student_class in self.students:
            print(f"Ad:{student_name},Sinif:{student_class}") 
    def view_teacher_list(self):       
        print("Ogretmenler:")
        for teacher_name,branch in self.teachers.items():
            print(f"Ad:{teacher_name},Brans:{branch}") 

school=School("Fen Lisesi",1989)     
school.add_new_student("Rana Oz","9A") 
school.add_new_student("Safiye Guven","12A")
school.add_new_teacher("Mehmet Hoca","Matematik")
school.add_new_teacher("Ayse Hoca","Fen Bilgisi")
school.view_student_list()
school.view_teacher_list()