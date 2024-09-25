from ast import If, Pass
from http.client import CONTINUE
from math import e
from pickle import TRUE
from re import Match


print(

"""""

__________              _________     _________        ___________     __________           ______
|_________/      __   | _________/   |    ____/       |  ________/    |_________/          / ___ \\
|  |            |__|  |  |           |   |            |   |           |  |                / /     \\
|  |______      |  |  |  |_____      |   |            |   |______     |  |_______        / ________\\
|_______  \\     |  |  |_____   \\    | __________     |________/      |________  \\     / /        \\\\
       |   |    |  |        |   |    |   _____   /    |   |                   |   |    / /           \\
|______    /    |  |  |_______  /    |   |____| /     |   |______     |_______    /   / /             \\
|_________/     |__|  |________/     |__________/     |__________/    |_________ /   / /               \\ v.1.5.5
http://sisgesa.org/

"""""
                          )


print("===============================================================================================================")
        


# CENTRAR USUARIO Y CONTRASEÑA
# REPARAR LOGO Y REPLANTEAR ESTRATEGIA DE INICIO( LOGO )
# SI LA CONTRASEÑA ES INCORRECTA QUE NO SE INTERRUMPA, DE LA OPORTUNIDAD DE VOLVER A COLOCARLA, IDEA " NUMERO DE INTENTOS V.1", O TAMBIEN OPCIONES INFINITAS V.1

Usu = (input(" Ingrese su Usuario \n")).capitalize()
cont =(input(" Ingrese su contraseña "))

# ORGANIZAR MEJOR EL MENU NO TANTO EN LO ESTETICO SINO MAS EN LO PRACTICO 



if cont == "SISGESA":
 
 print("00")
 print("")
 print(">>>>>>>>>>>>>>>>>>>>>MENU<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
 print("")
#exepciones
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


#MAYUSCULAS EN LAS OPCIONES REVISAR

resp= int(input("ingrese una opcion \n"))
# revisar las especificaciones del trainer
match resp:
 
    case 1:
        print("")
        print(" HAS INGRESADO LA OPCION REGISTRAR GRUPOS")
        print("")
        num1= int(input(" ingrese cuantos grupos quiere registrar\n"))
        i= 0
# UTILIZAR EL TRY
        while TRUE:
             
             if num1 <= 0:
              print(" NUMERO INCORRECTO")

             else:
                
              grup= input(" Ingrese el grupo a registrar ")


    case 2:
          pass
    case 3:
         pass
