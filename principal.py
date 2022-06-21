"""
a. Cantidad de integrantes en la familia.
b. Nombre del jefe/a de la familia.
c. Cantidad de menores de 18 años.
d. Cantidad de mayores de 65 años.
e. Edad de la persona más vieja y edad de la persona más joven.
f. Ingreso salarial de la familia.
g. Informar cuantos vehículos tiene.
h. Si vive en departamento, informar cuantos metros cuadrados tiene el mismo.
i. El fin de ingreso se indica con cantidad de integrantes = 0
"""
from funciones import cantidadHc,nombreL,solitarios,porSol,salarioBajo,nVehiculos, promMetros2,familiasD,cocheraP
from funciones import guardarCSV
censo=[]

metrosCuadrados=0
familia=0
while True :
    familia=familia+1
    
    #a. Cantidad de integrantes en la familia.
    cantidadIntegrantesF = int(input("ingrese la cantidad de integrantes del grupo familiar = "))
    
    #i. El fin de ingreso se indica con cantidad de integrantes = 0
    if cantidadIntegrantesF == 0:
        break
      
    #b. Nombre del jefe/a de la familia.
    nombreJefeF=str(input("ingrese el nombre del jefe de familia "))
    #c. Cantidad de menores de 18 años.
    menores18 =int(input("ingrese la cantidad de menores de 18 que tiene su grupo familiar = "))

    #d. Cantidad de mayores de 65 años.
    mayores18 =int(input("ingrese la cantidad de mayores de 18 que tiene su grupo familiar = "))
 
    #e. Edad de la persona más vieja y edad de la persona más joven.
    personaMasVieja = int(input("ingrese la edad de la persona mas vieja = "))
   
    personaMasJoven=int(input("ingresar la edad de al persona mas joven= "))
   
    #f. Ingreso salarial de la familia.
    ingresoSalarialFamiliar =float(input("ingreso familiar ="))  
   
    #g. Informar cuantos vehículos tiene su grupo familiar.
    vehiculos=int(input("informar la cantidad de vehiculos que tinen su grupo familiar=  ")) 
   
    # h. Si vive en departamento, informar cuantos metros cuadrados tiene el mismo.
    viveEnD=str(input("si vive en departamento ingrese s ,de no ser asi ingrese cualquier tecla para continuar "))
    if viveEnD == "s":
       
        
        metrosCuadrados=float(input("ingrese la cantidad de metros cuadrados que tiene el departamento donde vive = "))
   
    #registro adicional
    cocheraPropia=str(input("si tine cochera propia ingrese s "))
        
    datos={
        "numerofamilia": " " ,
        "cantidad de integrantes del grupo familiar":" ",
          "nombre del jefe familiar": " ",
          "menores18": " ",
          "mayores18": " ",
          "persona mas vieja":" ",
          "persona mas joven": " ",
          "ingreso salarial familiar": " ",
          "cantidad de vehiculos": " ",
          "viven en departamento":" ",
          "metros cuadrados del departamento":" ",
          "cochera propia":" "
         }
    datos["numerofamilia"] = familia
    datos["cantidad de integrantes del grupo familiar"] = cantidadIntegrantesF
    datos["nombre del jefe familiar"] =nombreJefeF
    datos["menores18"]= menores18
    datos["mayores18"]= mayores18
    datos["persona mas vieja"] =personaMasVieja
    datos["persona mas joven"]=personaMasJoven   
    datos["ingreso salarial familiar"]=ingresoSalarialFamiliar
    datos["cantidad de vehiculos"]= vehiculos
    datos["viven en departamento"]= viveEnD   
    datos["metros cuadrados del departamento"]= metrosCuadrados 
    datos["cochera propia"] = cocheraPropia    
    censo.append(datos)
print(censo)
#Cantidad de habitantes censados
print("la cantidad de habitantes totales censados es de ",cantidadHc(censo))
#Nombre del jefe/a de familia con la mayor cantidad de caracteres (o sea, el nombre más largo)
nombreL(censo)
#Cantidad de personas de viven solas.
print("la cantidad de  personas que viven solas es de {}".format(solitarios(censo)))
#Porcentaje de viviendas donde viven personas solas.
print("la cantidad de viviendas donde viven personas  solas es de {} %".format(porSol(censo)))
#Informar el salario familiar registrado más bajo.
print("el salario familiar mas bajo es de {}$".format(salarioBajo(censo)))
#Informar cuantas familias no tienen vehículos.
print("la cantidad de familias sin vehiculo es de ",nVehiculos(censo))
#Informar cuantas familias viven en departamentos y el promedio de metros cuadrados.
print("la cantidad de familias que viven en departamentos es de ",familiasD(censo))
print(" el promedio de metros cuadrados es de ",promMetros2(censo))
#registro adicional,cantidad de familias con cochera propia
print("la cantidad de familias con cochera propia es de ",cocheraP(censo))
#exportar a csv
guardarCSV(censo)
















