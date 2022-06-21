import csv
"""
 Cantidad de habitantes censados.
 Nombre del jefe/a de familia con la mayor cantidad de caracteres (o sea, el nombre más largo)
 Cantidad de personas de viven solas..
 Porcentaje de viviendas donde viven personas solas.
 Cantidad de menores de 18 años registrados en el censo.
 Informar el salario familiar registrado más bajo.
 Informar cuantas familias no tienen vehículos.
 Informar cuantas familias viven en departamentos y el promedio de metros cuadrados.
"""
#Cantidad de habitantes censados.
def cantidadHc(censo):
    cantidadHc=0
    for item in censo:
        cantidadHc=cantidadHc+item["cantidad de integrantes del grupo familiar"]
    return cantidadHc    

#Nombre del jefe/a de familia con la mayor cantidad de caracteres (o sea, el nombre más largo)
def nombreL(censo):
    nombreAnterior=0
    for item in censo:
        if len(item["nombre del jefe familiar"]) >nombreAnterior:
            nombreAnterior=len(item["nombre del jefe familiar"])
            for item in censo:
                if nombreAnterior==len(item["nombre del jefe familiar"]):
                    print("el nombre mas largo es",item["nombre del jefe familiar"])
                    break
    return

#Cantidad de personas de viven solas.
def solitarios(censo):
    solitarios=0
    for item in censo:
        if item["cantidad de integrantes del grupo familiar"] == 1:
            solitarios=solitarios+1
    return solitarios

#Porcentaje de viviendas donde viven personas solas.
def porSol(censo):
    totales=0
    for item in censo:
        totales=totales + 1
    return (solitarios(censo)*100)/totales 

#Informar el salario familiar registrado más bajo.
def salarioBajo(censo):
    salarioBajo=99999999
    for item in censo:
        if item["ingreso salarial familiar"]< salarioBajo:
            salarioBajo=item["ingreso salarial familiar"]
    return salarioBajo

#Informar cuantas familias no tienen vehículos.
def nVehiculos(censo):
    familiasSinVehiculos=0
    for item in censo:
        if item["cantidad de vehiculos"] ==0:
            familiasSinVehiculos=familiasSinVehiculos+1
    return familiasSinVehiculos        

#Informar cuantas familias viven en departamentos y el promedio de metros cuadrados.
def familiasD(censo):
    familiasD=0
    for item in censo:
        if item["viven en departamento"] =="s":
            familiasD=familiasD+1
    return familiasD            
            
def promMetros2(censo):
    metros2t=0
    for item in censo:
        metros2t=metros2t+item["metros cuadrados del departamento"]
    try:
        return metros2t/familiasD(censo)   
    except:
          print("hay un error de division por cero")

#registro adicional,cantidad de familias con cochera propia
def cocheraP(censo):
    cocheraP=0
    for item in censo:
        if item["cochera propia"] == "s":
            cocheraP=cocheraP+1
        else:
            cocheraP=cocheraP
    return cocheraP            

def guardarCSV(censo):
    
    fieldnames = [
        "numerofamilia","cantidad de integrantes del grupo familiar","nombre del jefe familiar","menores18",
                "mayores18","mayores18","persona mas vieja","persona mas joven","ingreso salarial familiar",
                "cantidad de vehiculos","viven en departamento","metros cuadrados del departamento","cochera propia"
                ]
    with open("censo.csv","w")as file:
         writer=csv.DictWriter(file, fieldnames = fieldnames)
         writer.writeheader()
         writer.writerows(censo)
    return    










    