from ast import Pass, While
import datetime
import getpass
from http.client import CONTINUE
import math
from operator import truediv
from pickle import FALSE, TRUE
from re import T, Match
import json

from click import pass_context

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
                     grup = (input(" Ingrese el grupo que desea agregar\n"))
                     grupsum+=grup.split("\n")
                     swith = False

   
        with open ("lista.json", "a") as archivo:
            json.dump(grupsum,archivo)

            print (grupsum)
    

# uniones de los diccionarios 

    case 2: 
        swith = True
        modulo = {}

        while swith is True:
                  elecc = int(input(" \tCuantos modulos desea registrar\n"))
                  for i in range (elecc):
                   nombre = input("\t digite el nombre del modulo\n")
                   codigo= int(input("\t digite el codigo del modulo\n"))
                   duracion= int(input("\t Ingrese la duracion del modulo en semanas\n"))
                   lista_mod= modulo.setdefault("nombre",nombre)
                   lista_mod= modulo.setdefault("codigo",codigo)
                   lista_mod= modulo.setdefault("duracion",duracion)
                   swith = False
       
       
       
                  with open ("modulos.json", "a") as fd:
                     json.dump(modulo,fd)

                     print(modulo)
                     print(" ingresado con exito ")






    case 3: 
          switch = True
          estudiantes ={}

          while switch is True:
              es_elecc=int(input(" cuantos estudiantes desea añadir"))
              for i in range (es_elecc):
                  nom_es= input(" Ingrese el nombre del estudiante\n")
                  sex_es=input(" ingrese el genero del estudiante (h) o (m) \n")
                  codig= int(input("Ingrese el codigo del Estudiante \n"))
                  lista_es= estudiantes.setdefault("nombre",nom_es)
                  lista_es= estudiantes.setdefault("sexo",sex_es)
                  lista_es= estudiantes.setdefault("codigo",codig)
                  switch = False

                  with open ("PROYECTO.PY\\ estudiantes.json", "a") as est:
                      json.dump(estudiantes,est)
                      print(estudiantes)

# poner excepciones
# corregir acentos
# agregar excepciones 
# ingresar json

    case 4:
          switch = True
          docentes ={}
          listmod=[]
          while switch is True:
              
              elec3= int(input(" \t Cuantos Docentes desea registrar\n "))
              for i in range(elec3):
                  nom_e= input(" \t ingrese el nombre del Docente\n")
                  docum= int(input(" Ingrese su documetno de identificscion CC. "))
                  mod= int(input(" Ingrese la cantidad de modulos que inpartira\n donde 1 es el minimo y 3 el maximo \n"))
                  for i in range (elec3):
                      moddef= input(" ingrese el modulo que imparte ")
                      listmod.append(moddef)
                  lista_e = docentes.setdefault("nombre",nom_e)
                  lista_e= docentes.setdefault("CC",docum)
                  lista_e = docentes.setdefault("modulos",[listmod])
                  switch= False

                  print(docentes)

                
    
    case 5:
        print(" has accedido a la opcion de registrar asistencia")
        switch = True
        while switch is True:
            cod_es= int(input(" ingrese el codigo del estudiante \n"))
            cod_mod = int(input( " ingrese el codigo del modulo \n"))
            hora_actual = datetime.datetime.now()
            pass





    case 6:
        print("\t CONSULTAS DE INFORMACION \n")
        print(">>>>>>>>>>>>>>>>>>>>>MENU<<<<<<<<<<<<<<<<<<<")


        print("""
              
              1. Consultar los estudiantes matriculados en un grupo. 
              2. Consultar los estudiantes inscritos en un módulo. 
              3. Consultar los docentes que imparten un módulo. 
              4. Consultar los estudiantes a cargo de un docente en un módulo. 

              
              
              
              
              
              
              
              
              """)










                
                  




                  
              



