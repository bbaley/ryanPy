# -*- coding: utf-8 -*-
"""
Created on Tue Sep 09 05:48:05 2014

@author: Brian-Baley

example cherryPy thingy for Ryan B. Gould

create a restful cherryPy service,
which does some CRUD to a database.

use the POSTMAN tets to drive...
"""


import sys, os
import time
import datetime
import json
import cherrypy

from ryanModule import classes as rPyClasses

import logging

#============================================================================



allUsers = []


#logging.basicConfig(filename='testAQ.log', level=logging.DEBUG, filemode='w')   
log = logging.getLogger('testRyPy')
log.setLevel(logging.WARN)
# add a file handler
fh = logging.FileHandler('testRyPy.log', mode='w')
fh.setLevel(logging.WARN)
# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(frmt)
# add the Handler to the logger
log.addHandler(fh)
# You can now start issuing logging statements in your code
#============================================================================

#-------------------------------------------------------      
def debugLog(_msg):
    print(str(_msg))        
    log.debug(str(_msg))
#-------------------------------------------------------   
def warnLog(_msg):
    print(str(_msg))        
    log.warn(str(_msg))
#-------------------------------------------------------        
def errorLog(_msg):
    log.error(str(_msg))
    print(str(_msg))
#-------------------------------------------------------    
     
#============================================================================     
def saveUsers():
    debugLog('saving users to database...')   
    
    for _user in allUsers:
        _user.postToDatabase()
        
#============================================================================

def createSomeUsers():
    user = rPyClasses.cUser()
    
    user.email = 'rgould@spoi.com'
    user.userName = 'RBG'
    user.heightInCentimeters = 72 - 4 * 2.54
    user.userType = 'admin'
    
    beer = rPyClasses.cBeer(None, 1, "HopStoopid", "DIPA")
    user.favoriteBeers.append(beer)
    
    beer = rPyClasses.cBeer(None, 3, "Pliny the Expensive", "DIPA")
    user.favoriteBeers.append(beer)

    beer = rPyClasses.cBeer(None, 99, "MegaChocoStout", "Stout")
    user.favoriteBeers.append(beer)
    
    allUsers.append(user)
    
    
    user = rPyClasses.cUser()
    
    user.email = 'bbaley@gmail.com'
    user.userName = 'BBALEY'
    user.heightInCentimeters = 72 + 4 * 2.54
    user.userType = 'public'
    
    beer = rPyClasses.cBeer(None, 1, "HopStoopid", "DIPA")
    user.favoriteBeers.append(beer)
    
    beer = rPyClasses.cBeer(None, 2, "Pliny the Expensive", "DIPA")
    user.favoriteBeers.append(beer)

    beer = rPyClasses.cBeer(None, 99, "IMPERIAL BISCOTTI BREAK NATALE", "Imperial Porter")
    user.favoriteBeers.append(beer)

    allUsers.append(user)
    
    
#============================================================================

class Users:
    exposed = True

    def GET(self, _uname = None):
    
        user = [x for x in allUsers if x.userName == _uname]        
        
        if _uname == None:
            return('please specify a username')
        elif user is not None:
            return(user.toDict())
        else:
            return('No user with the userName %s :-(' % _uname)
    
    def POST(self, _uname):
        return ('not implemented')
    
    



#============================================================================

        
def main():
    #logging.basicConfig(filename='testAQ.log', level=logging.DEBUG, filemode='w')    

    log.info('starting AQ test') # Neither will this.

    # if you already have them in the database
    # allUsers = rpyFunctions.getAllUsers()

    # otherwise, let's fake it
    allUsers = createSomeUsers()
    saveUsers()
    
    
    cherrypy.tree.mount(
        Users(), '/api/users',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
    
#============================================================================    

if __name__ == '__main__':
    main()

