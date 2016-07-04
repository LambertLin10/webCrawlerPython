#coding=utf-8
'''
Created on 2016年6月30日

@author: Lambert
'''


import sys
import psycopg2

con = None

try:
     
    con = psycopg2.connect("dbname='db名稱' user='帳號'") 
    
    cur = con.cursor()    
    cur.execute("SELECT url FROM foodcomment group by url")
    
    rows = cur.fetchall()
    list3 = []
    list4 = []
    for row in rows:
           
        list1 = str(row).replace("('", "").replace("',)","").rsplit('/')
        del list1[5]
        list2 = list1[0] + "//" + list1[2] + "/" + list1[3] + "/" + list1[4]
        print list2
        list3.append(list2)
        list4 = list(set(list3))
        
     
except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
        
        



con = None

try:
     
    con = psycopg2.connect("dbname='db名稱' user='帳號'")   
    
    cur = con.cursor()
  
    cur.execute("CREATE TABLE keys(Url TEXT PRIMARY KEY)")
    for item in list4:
        cur.execute("INSERT INTO keys VALUES('" + str(item) + "')")
    
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()