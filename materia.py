from abc import ABC 

class Persona(ABC): 
    def __init__(self,nombre,apellido,domicilio, dni,edad,sexo):
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__domicilio = domicilio
        self.__dni = dni
        self.__edad = edad
        self.__sexo = sexo
    @property 
    def nombre(self) :
        return self.__nombre
    @nombre.setter
    def nombre(self,value): 
        self.__nombre = value
    
    @property 
    def apellido(self) :
        return self.__apellido
    @apellido.setter
    def apellido(self,value): 
        self.__apellido = value
    
    @property
    def domicilio(self):
        return self.__domicilio
    @apellido.setter
    def apellido(self,value):
        self.__domicilio=value
        
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,value):
        self.__dni=value
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,value):
        self.__edad=value
    
    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def edad(self,value):
        self.__sexo=value
    
    
    def __str__(self):
        return  "nombre:" + self.nombre +" "+ ", apellido:" + self.apellido +" "+ "domicilio:" +" "+ self.domicilio +" "+ ", dni:" +" "+ str(self.dni) + "edad:" + str(self.edad) + "sexo:" + self.sexo 
     
class Alumno(Persona): 
    def __init__(self,nombre,apellido,domicilio, dni,edad,sexo,nroMatricula, carrera,materiasAprobadas = [] , materiasCursando = [] ):
        super().__init__(nombre,apellido,domicilio, dni,edad,sexo) 
        self.__nroMatricula = nroMatricula
        self.__carrera = carrera
        self.__materiasAprobadas = materiasAprobadas
        self.__materiasCursando = materiasCursando
        
    @property
    def nroMatricula(self):
        return self.__nroMatricula
    @nroMatricula.setter
    def nroMatricula(self,value):
        self.__nroMatricula=value
    
    @property
    def carrera(self):
        return self.__carrera
    @carrera.setter
    def carrera(self,value):
        self.__carrera=value
    
    
    @property
    def materiasAprobadas(self):
        return self.__materiasAprobadas
    @materiasAprobadas.setter
    def materiasAprobadas(self,value):
        self.__materiasAprobadas = value
        
    @property
    def materiasCursando(self):
        return self.__materiasCursando
    @materiasCursando.setter
    def materiasCursando(self,value):
        self.__materiasCursando = value
    
    def promedioDeNotas()-> float: 
        pass 
    def incripcionAFinal()-> bool: 
        pass
    def rendirFinal() -> float:
        pass
    def __str__(self):
        return  super().__str__() + "nroMatricula:" + str(self.nroMatricula) + "carrera:" + self.carrera 
                
                
        
class Profesor(Persona):
    def __init__(self,nombre,apellido,domicilio, dni,edad,sexo, nroLegajo, antiguedad, carrera, materias):
        super().__init__(nombre,apellido,domicilio, dni,edad,sexo) 
        self.__nroLegajo = nroLegajo
        self.__antiguedad = antiguedad
        self.__carrera = carrera
        self.__materias = materias
    
    @property
    def nroLegajo(self):
        return self.__nroLegajo
    @nroLegajo.setter
    def materiasCursando(self,value):
        self.__nroLegajo = value
        
    @property
    def carrera(self):
        return self.__carrera
    @carrera.setter
    def materiasCursando(self,value):
        self.__carrera = value
    
    @property
    def materias(self):
        return self.__materias
    @materias.setter
    def materiasCursando(self,value):
        self.__materias = value
        
class Carrera():
    def __init__(self, codigo, nombre, tituloOtorgado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__tituloOtorgado = tituloOtorgado
        
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,value):
        self.__codigo = value
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,value):
        self.__nombre = value
        
    @property
    def tituloOtorgado(self):
        return self.__tituloOtorgado
    @tituloOtorgado.setter
    def tituloOtorgado(self,value):
        self.__tituloOtorgado = value
        

class Materia (ABC): 
    def __init__(self, codigo, nombre, carrera, modalidad): 
        self.codigo = codigo
        self.nombre = nombre
        self.carrera = carrera
        self.modalidad = modalidad
    
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,value):
        self.__codigo = value
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,value):
        self.__nombre = value
    
    @property
    def carrera(self):
        return self.__nombre
    @carrera.setter
    def carrera(self,value):
        self.__carrera = value
    
    @property
    def modalidad(self):
        return self.__modalidad
    @modalidad.setter
    def modalidad(self,value):
        self.__modalidad = value
            
            
        
    def __str__(self):
        return ("codigo: " + str(self.codigo) +" "+" nombre:" +" "+" "+ self.nombre +" "+ ",  carrera:" +" "+" " +self.carrera +" "+ "modalidad:" +" "+" "+self.modalidad) +" "
        
        
class MateriaAprobada(Materia):
    def __init__(self,codigo, nombre, carrera, modalidad, notaFinal):
        super().__init__(codigo, nombre, carrera, modalidad)
        self.notaFinal = notaFinal
        
        
    @property
    def notaFinal(self):
        return self.__notaFinal
    @notaFinal.setter
    def notaFinal(self,value):
        self.__notaFinal= value
        
            
    def __str__(self):
        return super().__str__() + "notaFinal:" + str(self.notaFinal) 

class MateriaCursando(Materia):
    def __init__(self, codigo, nombre, carrera, modalidad, notaParcial, asistencia):
        super().__init__(codigo, nombre, carrera, modalidad)
        self.notaParcia = notaParcial
        self.asistencia = asistencia
    
    @property
    def notaParcial(self):
        return self.__notaParcial
    @notaParcial.setter
    def notaParcial(self,value):
        self.__notaParcial= value
    
    @property
    def asistencia(self):
        return self.__asistencia
    @asistencia.setter
    def asistencia(self,value):
        self.__asistencia= value
        
        
      
def main(): 
    alumno = Alumno("Juan", "Perez", "Perú", "38026494", 26, "M", 4856, "TSDS")
    print(alumno)
    materia = MateriaAprobada(3232, "Algebra" , "TSDS" , "virtual" , 9)
    print(materia)
main()
        

        
        
    

    