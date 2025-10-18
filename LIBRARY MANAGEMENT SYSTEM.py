import mysql.connector as mycon
con=mycon.cursor(host="localhost",user="root",password="_") #enter your MySql password
cur=con.cursor()
cur.execute("Create database LMS")
cur.execute("Use LMS")
cur.execute("""Create table Books(Bkno int, Bname varchar(45), Author varchar(40), Genre varchar(20), Qty int,
            No_of_Issues int, Date_of_Entry date)""")
cur.execute("""Create table Members(Idno int, Name varchar(45), Book_Issued varchar(40), Date_of_Issue date,
            Date_of_Return date, Overdue_Days int, Fine int,
            Contact int)""")

def addrec():
    n=int(input("Total number of records to be added:"))
    for i in range(n):
        c=int(input("Press 1 for adding record to Books. Press 2 for adding record to Members. Enter choice:"))
        if c==1:
            bn=int(input("Book number:"))
            bnm=input("Book name:")
            a=input("Author name:")
            g=input("Genre:")
            q=int(input("Number of books:"))
            isu=int(input("Number of issues:"))
            dt=input("Date of entry:")
            cur.execute("insert into Books values({},'{}','{}','{}',{},{},'{}')").format(bn,bnm,a,g,q,isu,dt)
            con.commit()
        elif c==2:
            idn=int(input("Member id number:"))
            nm=input("Member name:")
            bi=input("Book issued:")
            di=input("Date of issue:")
            dr=input("Date of return:")
            od=int(input("Number of overdue days:"))
            f=int(input("Enter fine:"))
            cn=int(input("Enter contact number:"))
            cur.execute("insert into Members values({},'{}','{}','{}','{}',{},{},{})").format(idn,nm,bi,di,dr,od,f,cn)
            con.commit()
        else:
            print("Choices don't match")
    cur.execute("select * from Books")
    re=cur.fetchall()
    for r in re:
        print(*r)
    cur.execute("select * from Members")
    res=cur.fetchall()
    for row in res:
        print(*row)

def updaterec():
    n=int(input("How many turns do you need to complete all your updates?:"))
    for i in range (n):
        c=int(input("Press 1 for updating Books. Press 2 for updating Members. Enter choice:"))
        if c==1:
            co=input("Enter name of column in which record needs to be updated")
            qn=input("""Do you want to update all records of the column? If yes then press Y, else
                     press N:""")
            if qn=="Y":
                ask=input("""Does this to be updated column data only consist of digits? If yes then
                          press T, else press F:""")
                if ask=="T":
                    nw=int(input("New value:"))
                    cur.execute("update Books set `{}`={}").format(co.nw)
                    con.commit()
                else:
                    nw=input("New value:")
                    cur.execute("update Books set `{}`='{}'").format(co,nw)
                    con.commit()
            else:
                cc=input("Condition column:")
                ak=input("""Does this condition column data consists only of digits? If yes then press T,
                         else press F:""")
                if ak=="T":
                    cv=int(input("Condition value:"))
                    ask=input("""Does this to be updated column data consists only of digits? If yes then
                              press T, else press F:""")
                    if ask=="T":
                        nw=int(input("New value:"))
                        cur.execute("update Books set `{}`={} where `{}`={}").format(co,nw,cc,cv)
                        con.commit()
                    else:
                        nw=input("New value:")
                        cur.execute("update Books set `{}`='{}' where `{}`={}").format(co,nw,cc,cv)
                        con.commit()
                else:
                    cv=input("Condition value:")
                    ask=input("""Does this to be updated column data consists only of digits? If yes then
                              press T, else press F:""")
                    if ask=="T":
                        nw=int(input("New value:"))
                        cur.execute("update Books set `{}`={} where `{}`=`{}`").format(co,nw,cc,cv)
                        con.commit()
                    else:
                        nw=input("New value:")
                        cur.execute("update Books set `{}`='{}' where `{}`=`{}`").format(co,nw,cc,cv)
                        con.commit()                                                                
        elif c==2:
            co=input("Enter name of column in which record needs to be updated")
            qn=input("""Do you want to update all records of the column? If yes then press Y, else
                     press N:""")
            if qn=="Y":
                ask=input("""Does this to be updated column data only consist of digits? If yes then press
                          T, else press F:""")
                if ask=="T":
                    nw=int(input("New value:"))
                    cur.execute("update Members set `{}`={}").format(co.nw)
                    con.commit()
                else:
                    nw=input("New value:")
                    cur.execute("update Members set `{}`='{}'").format(co,nw)
                    con.commit()
            else:
                cc=input("Condition column:")
                ak=input("""Does this condition column data consists only of digits? If yes then press T,
                         else press F:""")
                if ak=="T":
                    cv=int(input("Condition value:"))
                    ask=input("""Does this to be updated column data consists only of digits? If yes then
                              press T, else press F:""")
                    if ask=="T":
                        nw=int(input("New value:"))
                        cur.execute("update Members set `{}`={} where `{}`={}").format(co,nw,cc,cv)
                        con.commit()
                    else:
                        nw=input("New value:")
                        cur.execute("update Members set `{}`='{}' where `{}`={}").format(co,nw,cc,cv)
                        con.commit()
                else:
                    cv=input("Condition value:")
                    ask=input("""Does this to be updated column data consists only of digits? If yes then press T,
                              else press F:""")
                    if ask=="T":
                        nw=int(input("New value:"))
                        cur.execute("update Members set `{}`={} where `{}`='{}'").format(co,nw,cc,cv)
                        con.commit()
                    else:
                        nw=input("New value:")
                        cur.execute("update Members set `{}`='{}' where `{}`='{}'").format(co,nw,cc,cv)
                        con.commit()
        else:
            print("Choices don't match")                                                                        
    cur.execute("select * from Books")
    re=cur.fetchall()
    for r in re:
        print(*r)
    cur.execute("select * from Members")
    res=cur.fetchall()
    for row in res:
        print(*row)                                       

def searchrec():
    n=int(input("How many turns do you need to complete all your searches?:"))
    for i in range (n):
        c=int(input("""Press 1 for searching from Books. Press 2 for searching from Members.
                    Enter choice:"""))
        if c==1:
            co=input("Enter name of column which needs to be searched:")
            qn=input("""Do you want to search all records of the column? If yes then press Y,
                     else press N:""")
            if qn=="Y":
                cur.execute("select `{}` from Books").format(co)
                res=cur.fetchall()
                for row in res:
                    print(*row)
                con.commit()
            else:
                cc=input("Condition column:")
                ak=input("""Does this condition column data consists only of digits? If yes
                         then press T, else press F:""")
                if ak=="T":
                    cv=int(input("Condition value:"))
                    cur.execute("select `{}` from Books where `{}`={}").format(co,cc,cv)
                    res=cur.fetchall()
                    for row in res:
                        print(*row)
                    con.commit()
                else:
                    cv=input("Condition value:")
                    cur.execute("select `{}` from Books where `{}`='{}'").format(co,cc,cv)
                    res=cur.fetchall()
                    for row in res:
                        print(*row)
                    con.commit()
                
        elif c==2:
            co=input("Enter name of column which needs to be searched:")
            qn=input("""Do you want to search all records of the column? If yes then press Y,
                     else press N:""")
            if qn=="Y":
                cur.execute("select `{}` from Members").format(co)
                res=cur.fetchall()
                for row in res:
                    print(*row)
                con.commit()
            else:
                cc=input("Condition column:")
                ak=input("""Does this condition column data consists only of digits? If yes
                         then press T, else press F:""")
                if ak=="T":
                    cv=int(input("Condition value:"))
                    cur.execute("select `{}` from Members where `{}`={}").format(co,cc,cv)
                    res=cur.fetchall()
                    for row in res:
                        print(*row)
                    con.commit()
                else:
                    cv=input("Condition value:")
                    cur.execute("select `{}` from Members where `{}`='{}'").format(co,cc,cv)
                    res=cur.fetchall()
                    for row in res:
                        print(*row)
                    con.commit()
        else:
            print("Choices don't match")

def deleterec():
    n=int(input("How many turns do you need to delete all your desired records?:"))
    for i in range (n):
        c=int(input("""Press 1 for deleting from Books. Press 2 for deleting from
                    Members. Enter choice:"""))
        if c==1:
            cc=input("Condition column:")
            ak=input("""Does this condition column data consists only of digits? If yes
                     then press T, else press F:""")
            if ak=="T":
                cv=int(input("Condition value:"))
                cur.execute("delete from Books where `{}`={}").format(cc,cv)
                con.commit()
            else:
                cv=input("Condition value:")
                cur.execute("delete from Books where `{}`='{}'").format(cc,cv)
                con.commit()
        elif c==2:
            cc=input("Condition column:")
            ak=input("""Does this condition column data consists only of digits? If yes
                     then press T, else press F:""")
            if ak=="T":
                cv=int(input("Condition value:"))
                cur.execute("delete from Members where `{}`={}").format(cc,cv)
                con.commit()
            else:
                cv=input("Condition value:")
                cur.execute("delete from Members where `{}`='{}'").format(co,cc,cv)
                con.commit()
        else:
            print("Choices don't match")
    cur.execute("select * from Books")
    re=cur.fetchall()
    for r in re:
        print(*r)
    cur.execute("select * from Members")
    res=cur.fetchall()
    for row in res:
        print(*row)

def searchallinfo():
    n=int(input("How many turns do you need to complete all your searches?:"))
    for i in range (n):
        c=int(input("""Press 1 for searching from Books. Press 2 for searching from
                    Members. Enter choice:"""))
        if c==1:
            cc=input("""Condition column:")
            ak=input("Does this condition column data consists only of digits? If yes
                     then press T, else press F:""")
            if ak=="T":
                cv=int(input("Condition value:"))
                cur.execute("select * from Books where `{}`={}").format(cc,cv)
                con.commit()
            else:
                cv=input("Condition value:")
                cur.execute("select * from Books where `{}`='{}'").format(cc,cv)
                con.commit()
        elif c==2:
            cc=input("Condition column:")
            ak=input("""Does this condition column data consists only of digits? If yes
                     then press T, else press F:""")
            if ak=="T":
                cv=int(input("Condition value:")
                cur.execute("select * from Members where `{}`={}").format(cc,cv)
                con.commit()
                res=cur.fetchall()
                for row in res:
                    print(*row)
            else:
                cv=input("Condition value:")
                cur.execute("select * from Members where `{}`='{}'").format(cc,cv)
                con.commit()
                res=cur.fetchall()
                for row in res:
                    print(*row)
        else:
            print("Choices don't match")

choice=input("""Press 'a' for adding records. Press 'b' for updating records. Press 'c'
for searching selected columns of a record. Press 'd' for deleting records.
Press 'e' for selecting all the colums of desired records. Enter choice:""")
if choice=="a":
    addrec()
elif choice=="b":
    updaterec()
elif choice=="c":
    searchrec()
elif choice=="d":
    deleterec()
elif choice=="e":
    searchallinfo()
else:
    print("Choices don't match")
            
            
    
    
            
                    
    
    



            
            
