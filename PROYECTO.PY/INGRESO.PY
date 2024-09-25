from ast import Pass, While
from errno import EADDRNOTAVAIL
import getpass
from http.client import CONTINUE
import math
from msilib.schema import ODBCSourceAttribute
from operator import truediv
from optparse import Values
from pickle import FALSE, TRUE
from re import T, Match
import json
from shutil import which
from string import whitespace


# Funciones pra subir, decargar y mirar .Json
# utilizacon de las funciones para mejor lectura del codigo

def cargar_archivo(estudiantes):
    with open("PROYECTO.PY\\estudiantes.json", "r") as archivo:
        return json.load(archivo)
    return[]



ingres= True


while ingres is True:
    print("sisgesa")
    usu = input( "\t USUARIO : \n")
    cont= getpass.getpass(" \tCONTRASEÑA : \n")

    if cont == "SISGESA":
        print("================")
        print(" INGRESO CONCEDIDO")
        print(F" BIENVENID@ {usu}")
        print("================")
        ingres = False
        continue

        print(" menu")

    elif cont != "SISGESA":
        print("")
        print("===============")
        print(" CONTRASEÑA INVALIDA.....")
        print(" iNGRESA UNA CONTRASEÑA VALIDA")
        print("===============")


print("""""

       
1. Registro de grupos. 
2. Registro de módulos. 
3. Registro de estudiantes. 
4. Registro de docentes. 
5. Registro de asistencia. 
6. Consultas de información. 
7. Generación de informes. 
8. Cambio de contraseña. 
9. Salida del sistema.

"""""                          )
# IMPLEMENTAR FUNCIONES
# ingresar excepciones, para evitar el colapso del programa.
# ARREGLAR EXCEPCION
swith = True
while swith is True:
           
    elecc= int(input(" ingrese una opcion valida.......\n "))

    if elecc >= 1 and elecc <= 9:
      print(" Has elegido una opcion valida")
      swith = False
      continue

    

    else:
       print(" ERROR.(404) has elegido una opcion invalida")
       print("")
       print("=========================")
       swith = True
      
    

#C4_campus_DOT( DESARROLLO DE OPORTUNIDADES TECNOLOGICAS)
         # GUARDAR LA INFORMACION PARA UTILIZARLA
         



         # prueba del sistema #1
# funciones
swith = True
grup = []
grupsum =[]
#print("CARGANDO ARCHIVOS......")
match elecc:

    case 1:

        while swith is True:
                  numgrup= int(input(" Ingrese el numero de grupos que desea añadir"))


                  for i in range(numgrup):
                     numgrup= input(" ingrese el codigo del grupo:  ")
                     nombregrup= input( " ingrese el nombre del grupo:  ")
                     sigla= input(" ingrese la sigla del grupo ")
                     grupsum.append({"codigo":numgrup, "nombre": nombregrup, "sigla":sigla})
    
                     swith = False

   
        with open ("PROYECTO.PY\\ grupos.json", "a") as archivo:
            json.dump(grupsum,archivo)

            print (grupsum)
            print("REGISTRADO")
    

# uniones de los diccionarios 

    case 2: 
        swith = True
        modulo = []

        while swith is True:
                  elecc = int(input(" \tCuantos modulos desea registrar\n"))
                  for i in range (elecc):
                   nombre = input("\t digite el nombre del modulo\n")
                   codigo= int(input("\t digite el codigo del modulo\n"))
                   duracion= int(input("\t Ingrese la duracion del modulo en semanas\n"))
                  modulo.append({"nombre":nombre, "codigo": codigo, "duracion": duracion})
                  switch = False
       
       
       
                  
                  
                  
                  
                  with open ("PROYECTO.PY\\ modulos.json", "a") as fd:
                         json.dump(modulo,fd)

                         
                         print(" ingresado con exito ")






    case 3: 
          switch = True
          estudiantes =[]
          

          while switch is True:
              es_elecc=int(input(" cuantos estudiantes desea añadir"))
              for i in range (es_elecc):
                  nom_es= input(" Ingrese el nombre del estudiante\n")
                  sex_es=input(" ingrese el genero del estudiante (h) o (m) \n")
                  codig= int(input("Ingrese el codigo del Estudiante \n"))
                  edad= input("Ingrese la edad del estudiante ")

                  estudiantes.append({ "nombre":nom_es,"sexo":sex_es, "edad": edad})
                  
                  switch = False

                  with open ("PROYECTO.PY\\ estudiantes.json", "a") as est:
                      json.dump(estudiantes,est)
                      print(estudiantes)



                  est.close()




    case 4:
          switch = True
          docentes = []
          
          while switch is True:
              
              elec3= int(input(" Cuantos Docentes desea registrar\n"))
              for i in range(elec3):
                  cc= int(input("ingrese la Cedula del docente\n"))
                  nombr= input(" ingrese el nombre del docente\n")
                  
                  docentes.append({"cedula":cc,"nombre": nombr})
                  
                  switch = False


                  with open ("PROYECTO.PY\\docentes.json", "w") as re:
                      json.dump(docentes,re)

                      print(" REGISTRO EXITOSO")
                      print(docentes)


            
                  
              

    case 5:
        print(" has accedido a la opcion de registrar asistencia")
        switch = True
        while switch is True:
            cod_es= int(input(" ingrese el codigo del estudiante \n"))
            cod_mod = int(input( " ingrese el codigo del modulo \n"))
            hora_actual = datetime.datetime.now()
            pass


# UNIR TODOS LOS DATOS REGISTRADOS 


    case 6:
        print("\t CONSULTAS DE INFORMACION \n")
        print(">>>>>>>>>>>>>>>>>>>>>MENU<<<<<<<<<<<<<<<<<<<")


        print("""
              
              1. Consultar los estudiantes matriculados en un grupo. 
              2. Consultar los estudiantes inscritos en un módulo. 
              3. Consultar los docentes que imparten un módulo. 
              4. Consultar los estudiantes a cargo de un docente en un módulO
                            """)
        elecc4= int(input(" Ingrese una opcion valida de consilta\n"))

        match elecc4:


            case 1: 
                 with open("estudiantes.json", "r") as archivo:
                     
                     estudiantes =json.load(archivo)



                 grupo= input(" ingrese el codigo del grupo: ")
                 todos_estu= [ est for est in estudiantes if est.get("grupo")== grupo]
                 if todos_estu:
                    print(f" estudiantes en el grupo {grupo}:")
                    for est in todos_estu:
                        print(f"{est['nombre']}  cogigo: {est['codigo']} ")
                 else:
                    print("no hay estudinates en este grupo ")







