class Student():
    def __init__(self, Name = None, Calificaion = None, Semestre = None, Carrera = None):
        self.Name = Name
        self.Calificaion = Calificaion
        self.Semestre = Semestre
        self.Carrera = Carrera
        
    def get_Name(self):
    
        self.Name = input("Enter Student's Name: ")
        
    def get_Calificaion(self):
        
        self.Calificaion = input("Enter Student's Calification: ")
        
    def get_Semestre(self):
        
        self.Semestre = input("Enter Student's Semester: ")
        
    def get_Carrera(self):
        
        self.Carrera = input("Enter Student's Carrer: ")
