# -*- coding: utf-8 -*-


import MySQLdb
import logging
from ryanModule import classes

#========================================================================= 

            
#========================================================================= 
def getAllDbUsers():
    _users = []
    
    conn = MySQLdb.connect(host='localhost',port=3306,user="me",passwd="secret",db="testdb",charset="utf8")
    
    cur = conn.cursor()
    
    sql = """
            select userName, userType, email, height from users where userType <> 'test'
          """
    
    cur.execute(sql)
    rows = cur.fetchall()
    
    if rows is not None:    
        for row in rows: 
            user = classes.cUser()
            user.userName = row[0]
            user.userType = row[1]
            user.email = row[2]
            user.height = float(row[3])

    conn.close()
    
    return _users
    
    
#=========================================================================     