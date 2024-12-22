#===============================START==============================
import pandas as pd
import mysql.connector as con
import pymongo
import sqlite3

def project():

    
        def exceltomysql():
                        def DataTransfer():
                                mydb = con.connect(host="localhost",user="root",password="ronit@2722",database=f"{database}")
                                mycursor = mydb.cursor()
                                df = pd.read_csv(f"{inputname}.csv")
                                for index, row in df.iterrows():
                                    sql = f"INSERT INTO {table} (roll_no, name, class, fees, adress) VALUES (%s, %s, %s, %s, %s)"
                                    val = (row['roll_no'], row['name'], row['class'], row['fees'], row['adress'])
                                    mycursor.execute(sql, val)
                                mydb.commit()
                        DataTransfer()
        #exceltomysql()
        def  mysqltoexcel():
            
            
            mydb=con.connect(host='localhost',user='root',password="ronit@2722",database=f"{database}")
            cur=mydb.cursor()
            cur.execute(f"select * from {table}")
            data=cur.fetchall()
            mydb.close()

            
            df = pd.DataFrame(data, columns=[desc[0] for desc in cur.description])
            df.to_csv(f"{outputname}.csv", index=False)
            
        #mysqltoexcel()
            
                       
        
        def mongotoexcel():                #1
                
                client = pymongo.MongoClient("mongodb://localhost:27017")
                db = client[f"{dbdatabase}"]  
                collection = db[f"{dbcollection}"]  

                
                data = list(collection.find({}, {'_id': 0}))

                
                df = pd.DataFrame(data)

                
                df.to_csv(f"{outputname}.csv", index=False)
                client.close()
            #mongotoexcel()
                      
        def spreadsheettoexcel():              #2
            
                df = pd.read_excel(f"{inputname}.ods", engine='odf', index_col=None)
                #print(df)
                df.to_csv(f"{outputname}.csv")
            #spreadsheettoexcel()
        
       
        def sqlitetoexcel():                        #3
                
                connection = sqlite3.connect(f'{sqlitedatabase}.db')
                cursor = connection.cursor()

                
                select_query = f'SELECT * FROM {sqlitetable};'
                cursor.execute(select_query)

                
                records = cursor.fetchall()
                df = pd.DataFrame(records, columns=[desc[0] for desc in cursor.description])
                
                if records:
                    df.to_csv(f"{outputname}.csv", index=False)
                else:
                    print("No records found.")

                connection.close()

        #sqlitetoexcel()

        
        
        def bintoexcel():                      #4
            file=open(f"{inputname}.bin", 'rb')
            df = pd.read_pickle(file)
            df.to_csv(f"{outputname}.csv", index=False)
            file.close()

            
            #bintoexcel()   
                           
        
        def exceltomongo():                                   #1
                    
                    client = pymongo.MongoClient("mongodb://localhost:27017")
                    db = client[f"{dbdatabase}"]  
                    collection = db[f"{dbcollection}"]  

                    
                    df = pd.read_csv(f"{inputname}.csv")  
                    
                    data = df.to_dict(orient='records')
                    
                    collection.insert_many(data)
                    
            #exceltomongo()                   

        
        def exceltoods():                                             #2                                                         
                
                df = pd.read_csv(f"{inputname}.csv")

                
                df.to_excel(f"{outputname}.ods", index=False)

                
            #excel_to_ods()

       
        def exceltosqlite():                                   #3

                connection = sqlite3.connect(f'{sqlitedatabase}.db')
                cursor = connection.cursor()

                df = pd.read_csv(f"{inputname}.csv")
                df = df.drop(columns=["Unnamed: 0"], errors="ignore")

                df.to_sql(f'{sqlitetable}', connection, index=False, if_exists='append')

                connection.commit()
                connection.close()
                 
            #exceltosqlite()


        
        def exceltobin():
                df = pd.read_csv(f"{inputname}.csv")
                df.to_pickle(f"{outputname}.bin")
            #exceltobin()

              


        
        while True:
            print("====================Database Converter====================")
            print("1. To see available mode of Datatransfer")
            print("2. Start")
            print("3. Exit")
            ch=int(input("Enter your choice:"))
            if(ch==1):
                print("1. Mysql")
                print("2. Excel")
                print("3. Mongodb")
                print("4. Spreadsheet")
                print("5. Sqlite3")
                print("6. Binary file")
                pass
            elif(ch==3):
                print("Thanks for using this program")
                break
            elif(ch==2):
                print("1. Mysql")
                print("2. Excel")
                print("3. Mongodb")
                print("4. Spreadsheet")
                print("5. Sqlite3")
                print("6. Binary file")

                
                inp=int(input("Enter the mode of input database:"))
                outp=int(input("Enter the mode of output database :"))
                inputname=input("Enter the name of your input and output file(if not required type extra):")
                outputname= inputname                                                        



                if(inp==1):
                     table=input("Enter the name of mysql table:")                           #school
                     database=input("Enter the name of mysqldatabase:")             #menhibataunga
                     if(outp==1):
                        print("Your input and outmode are same. No need to change it.")
                        pass
                     elif(outp==2):
                        mysqltoexcel()
                        print("Your output file is ready")
                        pass
                     elif(outp==3):                        
                        mysqltoexcel()
                        #mongohost=input("Enter the mongo connection string")                mongodb://localhost:27017
                        dbdatabase=input("Enter the name of database of mongo(that exists):")           #mongo
                        dbcollection=input("Enter the name of collection of mongodb(that exists):")    #project
                        exceltomongo()
                        
                        print(f"An extra excel file is made for mode of transferring named {inputname}")
                        print("Your data has been transfered to mongodb")
                        pass
                     elif(outp==4):
                         mysqltoexcel()
                         exceltoods()
                         print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                         print("Your output file is ready")
                         
                         pass
                     elif(outp==5):
                         mysqltoexcel()
                         sqlitedatabase=input("Enter name of your sqlite databse:")                        #test
                         sqlitetable=input("Enter the name of table in your sqlite database with suitable fields or columns which match with fields of given data:")      #project
                         exceltosqlite()
                         print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                         print("Your data has been transfered to sqlite3")
                         pass
                     elif(outp==6):
                         mysqltoexcel()
                         exceltobin()
                         print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                         print("Your output file is ready")
                         pass
                     else:
                         print("Invalid choice try again")
                         pass

                elif(inp==2):

                    if(outp==1):
                        database=input("Enter name of your mysql database:")                       #menhibataunga
                        table=input("Enter the name of table in your mysql database with suitable fields or columns which match with fields of given data:")         #school
                        exceltomysql()
                        print("Your data has been transfered to mysql")
                        pass
                    elif(outp==2):
                        print("Your input and outmode are same. No need to change it.")
                        pass
                    elif(outp==3):                  
                        dbdatabase=input("Enter the name of database of mongo(that exists)")           #mongo
                        dbcollection=input("Enter the name of collection of mongodb(that exists)")    #project
                        exceltomongo()
                        print("Your data has been transfered to mongodb")
                        pass
                    elif(outp==4):
                        exceltoods()
                        print("Your output file is ready")
                        pass
                    elif(outp==5):
                        sqlitedatabase=input("Enter name of your sqlite databse:")                         #test
                        sqlitetable=input("Enter the name of table in your sqlite database with suitable fields or columns which match with fields of given data:")                         #project
                        exceltosqlite()
                        print("Your data has been transfered to sqlite3")
                        pass
                    elif(outp==6):
                        
                        exceltobin()
                        print("Your output file is ready")
                        pass
                    else:
                        print("Invalid choice")
                        pass
                elif(inp==3):
                    dbdatabase=input("Enter the name of database of mongo(that exists):")           #mongo
                    dbcollection=input("Enter the name of collection of mongodb(that exists):")    #project
                    if(outp==1):
                        mongotoexcel()
                        database=input("Enter name of your mysql database:")                       #menhibataunga
                        table=input("Enter the name of table in your mysql database with suitable fields or columns which match with fields of given data:")         #school
                        exceltomysql()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your data has been transfered to mysql")
                        pass
                    elif(outp==2):
                        mongotoexcel()
                        print("Your output file is ready")
                        pass
                    elif(outp==3):
                        print("Your input and outmode are same. No need to change it.")
                        pass
                    elif(outp==4):
                        mongotoexcel()
                        exceltoods()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your output file is ready")
                        pass
                    elif(outp==5):
                        sqlitedatabase=input("Enter name of your sqlite databse:")                         #test
                        sqlitetable=input("Enter the name of table in your sqlite database with suitable fields or columns which match with fields of given data:")                         #project
                        mongotoexcel()
                        exceltosqlite()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your data has been transfered to sqlite3")
                        pass
                    elif(outp==6):
                        mongotoexcel()
                        exceltobin()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your output file is ready")
                        pass
                    else:
                        print("Invalid choice")
                        pass

                elif(inp==4):

                    if(outp==1):
                        database=input("Enter name of your mysql database:")                       #menhibataunga
                        table=input("Enter the name of table in your mysql database with suitable fields or columns which match with fields of given data:")         #school
                        spreadsheettoexcel()
                        exceltomysql()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your data has been transfered to mysql")
                        pass
                    elif(outp==2):
                        spreadsheettoexcel()
                        print("Your output file is ready")
                        pass
                    elif(outp==3):          
                        spreadsheettoexcel()
                        dbdatabase=input("Enter the name of database of mongo(that exists):")           #mongo
                        dbcollection=input("Enter the name of collection of mongodb(that exists):")    #project
                        exceltomongo()
                        print(f"Yn extra excel file is made for mode of transferring named {inputname}")
                        print("Your data has been transfered to mongodb")
                        pass
                    elif(outp==4):
                        print("Your input and outmode are same. No need to change it.")
                        pass
                    elif(outp==5):
                        sqlitedatabase=input("Enter name of your sqlite databse:")                         #test
                        sqlitetable=input("Enter the name of table in your sqlite database with suitable fields or columns which match with fields of given data:")                         #project                        
                        spreadsheettoexcel()
                        exceltosqlite()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your data has been transfered to sqlite3")
                        pass
                    elif(outp==6):
                        spreadsheettoexcel()
                        exceltobin()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your output file is ready")
                        pass
                    else:
                        print("Invalid choice")
                        pass
                elif(inp==5):
                    sqlitedatabase=input("Enter name of your sqlite databse:")                        #test
                    sqlitetable=input("Enter the name of table in your sqlite database:")      #project
                    if(outp==1):
                        database=input("Enter name of your mysql database:")                       #menhibataunga
                        table=input("Enter the name of table in your mysql database with suitable fields or columns which match with fields of given data:")         #school
                        sqlitetoexcel()
                        exceltomysql()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your data has been transfered to mysql")
                        pass
                    elif(outp==2):
                        sqlitetoexcel()
                        print("Your output file is ready")
                        pass
                    elif(outp==3):         
                        sqlitetoexcel()
                        dbdatabase=input("Enter the name of database of mongo(that exists):")           #mongo
                        dbcollection=input("Enter the name of collection of mongodb(that exists):")    #project
                        exceltomongo()
                        print(f"An extra excel file is made for mode of transferring named {inputname}")
                        print("Your data has been transfered to mongodb")
                        pass
                    elif(outp==4):
                        sqlitetoexcel()
                        exceltoods()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your output file is ready")
                        pass
                    elif(outp==5):
                        print("Your input and outmode are same. No need to change it.")
                        pass
                    elif(outp==6):
                        sqlitetoexcel()
                        exceltobin()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your output file is ready")
                        pass
                    else:
                        print("Invalid choice")
                        pass

                elif(inp==6):

                    if(outp==1):
                        database=input("Enter name of your mysql database:")                       #menhibataunga
                        table=input("Enter the name of table in your mysql database with suitable fields or columns which match with fields of given data:")         #school
                        bintoexcel()
                        exceltomysql()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your data has been transfered to mysql")
                        pass
                    elif(outp==2):
                        bintoexcel()
                        print("Your output file is ready")
                        pass
                    elif(outp==3):
                        bintoexcel()
                        dbdatabase=input("Enter the name of database of mongo(that exists):")           #mongo
                        dbcollection=input("Enter the name of collection of mongodb(that exists):")    #project
                        exceltomongo()
                        print(f"An extra excel file is made for mode of transferring named {inputname}")
                        print("Your data has been transfered to mongodb")
                        pass
                    elif(outp==4):
                        bintoexcel()
                        exceltoods()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your output file is ready")
                        pass
                    elif(outp==5):
                        sqlitedatabase=input("Enter name of your sqlite databse:")                        #test
                        sqlitetable=input("Enter the name of table in your sqlite database with suitable fields or columns which match with fields of given data:")      #project
                        bintoexcel()
                        exceltosqlite()
                        print(f"An extra excel file is made for mode of transferring named {inputname} please ignore or delete that file")
                        print("Your data has been transfered to sqlite3")
                        pass
                    elif(outp==6):
                        print("Your input and outmode are same. No need to change it.")
                        pass
                    else:
                        print("Invalid choice")
                        pass
                else:
                    print("Invalid choice try again")
                    pass



                            
            else:
                print("Invalid choice")
                pass
project()
