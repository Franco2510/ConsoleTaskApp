import os
#==VARIABLES====================================================================
#--de archivo-------------------------------------------------------------------

#--de programa------------------------------------------------------------------
linea=""
opc=0
meses={"01":"ENE",
       "02":"FEB",
       "03":"MAR",
       "04":"ABR",
       "05":"MAY",
       "06":"JUN",
       "07":"JUL",
       "08":"AGO",
       "09":"SEP",
       "10":"OCT",
       "11":"NOV",
       "12":"DIC"}

tipos={"1":"FACU",
       "2":"PROY",
       "3":"QUEA",
       "4":"FAVO"}
#==FUNCIONES===================================================================
def titulo(texto) :
    os.system("cls")
    print "="*80
    linea=texto
    print linea.center(80)
    print "="*80


def alta_tareas() :
    while True :
        registro=""
        titulo("ALTA DE TAREAS")
        
        registro+=raw_input("-Descripcion: ")
        if len(registro)>50 :
            registro=registro[:-(len(registro)-50)]
        registro+="|"

        print "Fecha Limite"
        n=raw_input("-mes(0=sin limite): ")
        if int(n)>=1 and  int(n)<=12:
            registro+=n.zfill(2)
            registro+=raw_input("-dia: ").zfill(2)+"|"
        else :
            registro+="9999|"
            print "sin fecha limite"
        
        while True :
            n=raw_input("-Categoria: (1-Facu 2-Proyectos 3-Quehaceres 4-Favores) ")
            if n=="1" or n=="2" or n=="3" or n=="4" : break
            else : print "*valor no valido*"
        registro+=n+"|"
                
        a=open("tareas.txt","a")
        a.write(registro+"\n")
        a.close()
        print
        n=raw_input("Ingresar otra tarea? (1=Si 0=No): ")
        if n=="1" : continue
        else : break

def listar(orden=0) :
    a=open("tareas.txt", "r")
    tareas=a.readlines()

    for i in range(len(tareas)) :
        tareas[i]=tareas[i].split("|")
        tareas[i].remove(tareas[i][3])

    if orden==1 :
        aux=0
        for i in range(len(tareas)) :
            for j in range(len(tareas)) :
                if tareas[i][1]<tareas[j][1] :
                    aux=tareas[i]
                    tareas[i]=tareas[j]
                    tareas[j]=aux
                    
    print "ID| TAREA                                              | FECHA  | TIPO |"
    print "-"*80

    ID="00"
    for x in range(len(tareas)) :
        ID=str(x+1).zfill(2)
        print ID+"|",
        
        tareas[x][0]=tareas[x][0].ljust(50)

        if tareas[x][1]!="9999" :
            mes=tareas[x][1][:-2]
            mes=meses[mes]
            tareas[x][1]=tareas[x][1][-2:]+" "+mes
        else : tareas[x][1]="  -   "
        
        tareas[x][2]=tipos[tareas[x][2]]
        
        for campo in tareas[x] :
            print campo, "|",
        print
    print "-"*80
    a.close()
        

def listado_fecha() :
    titulo("LISTADO POR FECHA")
    listar(1)
    raw_input("\nEnter para volver...")

def baja_tareas() :
    titulo("TERMINAR TAREA")
    listar()
    x=raw_input("Ingrese el id de la tarea terminada: ")
    try :
        if int(x)>0 :
            x=int(x)-1
            a=open("tareas.txt","r+")
            tareas=a.readlines()
            tareas.remove(tareas[x])
            a.close()

            a=open("tareas.txt","w")
            for tarea in tareas :
                a.write(tarea)
            a.close()
            
            print
            print "Tarea dada de baja con exito."
        else : print "\n*valor ingresado no valido*"
    except : print "\n*valor ingresado no valido*"
    raw_input("\nEnter para volver...")
    
#==PROGRAMA=====================================================================
while True :
    titulo("AGENDA DE TAREAS PERSONALES")
    print "1-Agregar tareas"
    print "2-Listado de tareas"
    print "3-Terminar tarea"
    print "0-Salir"
    print "_"*80

    opc=raw_input("ingrese opcion: ")
    if opc=="1" : alta_tareas()
    elif opc=="2" : listado_fecha()
    elif opc=="3" : baja_tareas()
    else :
        if opc=="0" : break
