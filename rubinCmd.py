import os
import multiprocessing

def Main():
    
    counter = 0
    listofpaths = []
    os.system("cls")
    print("welcome to my shell dear golan :) ")
    totalstop = False
    stop1 = False
    stop2 = False
    while not totalstop:
        
        while not stop1:
            
            try:

                cmd = input("the path is ->>")
                if(cmd == "exit"):
                    totalstop = True
                    stop2 = True
                    break 
                os.chdir(cmd)
                stop1 = True


            except:
                if(os.path.isdir(cmd) == False):
                    print("unknown cmd")
        
        
        listofpaths.append(cmd) 
        while not stop2:
                
                
                

                print(" ")
                print(" ")
                print(" ")
                

                print("the current path is -> ",os.getcwd())
                print(" ")
                print(" ")
            
                print("all functions that available : printdir  ,  snp(setnewpath) ,  gbtp(gobacktoprevious)  ,  find , redirection ")

                fun = input("opened ears, tell me what i need to do :")

                if(fun == "exit"):
                    print(" ")
                    stop2 = True

                if(fun == "printdir"):
                    print(" ")
                    printdir()
                
                if(fun == "snp"):
                    print(" ")
                    setnewpath(listofpaths) 
                    counter+=1

                if(fun == "gbtp"):
                    print(" ")
                    gotoprevious(listofpaths,counter)
                    counter-=1
                
                if(fun == "find"):
                    print(" ")
                    s = input("what do u want to find? -  > ")
                    find(s)
                
                if(fun == "redirection"):
                      
                    name = input("enter a file name") 
                    s = input("enter what do u want to add ->> ")    
                    redirection(s,name)

                if(fun == "pipes"):
                    file1 = input("enter file name")
                    des = input("enter a path destintion")
                    pipe(file1,des)

                    
                




                



                






                    
                


                
            

                

    






        
try:
        
        #להדפיס את כל הדיר בפנים
        def printdir():
            print("the list dir is :")
            print(os.listdir())

        #להיכנס עמוק יותר בתקיות
        #אפשר להכניס כתובת מלאה 
        #או אפשר להכניס את המילה וזה ימצא את התקייה


        def setnewpath(list):

            newpath = input("enter the new path or word ") 
            for i in newpath:
                if(i == ':'):
                    list.append(newpath)
                    os.chdir(newpath)
            st = os.getcwd()+ '\\' + newpath
            list.append(st)
            os.chdir(st)
            

        #הולך לקודם 
        def gotoprevious(list,place):

            list.remove(list[place])
            os.chdir(list[place-1])

        #פותח קובץ

        def open(name):

            flags = os.O_RDWR 
            return os.open(name,flags)



        def find(st):
            directory_listing = os.listdir()
            for row in directory_listing:
                if(st in row):
                    print(row)
            
            
        #יוצר קובץ חדש עם סטרינג 
        def redirection (s,nameoffile):

            f = os.open(nameoffile,os.O_CREAT | os.O_RDWR)
            line = str.encode(s)
            os.write(f,line)

        def pipe(filename,dest):
            path = os.getcwd()+ '\\' + filename
            file = os.open(path,os.O_RDONLY)
            n = 20000
            read = os.read(file,n)
            os.chdir(dest)
            f = os.open(filename,os.O_CREAT | os.O_RDWR)
            os.write(f,read)

            

        


except:

    print("typed wrong")

    


Main()