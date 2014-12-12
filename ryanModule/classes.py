# -*- coding: utf-8 -*-
#========================================================================= 
# classes used by testRyan.py
#========================================================================= 


import MySQLdb


if __name__ == "__main__" and __package__ is None:
    __package__ = "ryanModule.classes"
    

#========================================================================= 
class cBeer(object):
    def __init__(self, 
            _id = None,
            _likeHowFavorite = 0,
            _beerName = "",
            _beerType = ""
        ):
            
        self.id = _id
        self.likeHowFavorite = _likeHowFavorite
        self.beerName =_beerName
        self.beerType = _beerType
    
    
    


#========================================================================= 
class cUser(object):
    def __init__(self, 
            _id = None,
            _userType = "",
            _userName = "",
            _email = "",
            _favoriteBeers = [],
            _heightInCentimeters = 0.00
        ):
            
        self.id = _id
        self.userType = _userType
        self.userName = _userName
        self.email = _email
        self.favoriteBeers = _favoriteBeers
        self.heightInCentimeters = _heightInCentimeters
            
    #-----------------------------------------------
    def mostFavoriteBeer(self):
        # we could get the object in one step,
        # but this shows how to query a particuler property and use an aggregate function on it
        maxFav = max(b.likeHowFavorite for b in self.favoriteBeers)        
        
        # pythonic equivalent to a linq query against a collection of objects
        fb = [x for x in self.favoriteBeers if x.likeHowFavorite == maxFav]                   
        
        return fb
    #-----------------------------------------------
    def postToDatabase(self):
        # no, I didn't handle the berr hierarchy here, just a slim example
        conn = MySQLdb.connect(host='localhost',port=3306,user="me",passwd="secret",db="testdb",charset="utf8")
        
        cur = conn.cursor()
        
        sql = """
                insert into users(userName, email, height, userType) values(%s, %s, %s, %s)
              """, [self.userName, self.email, self.heightInCentimeters, self.userType]
        
        cur.execute(sql)
    
        conn.close()
    
    #-----------------------------------------------    
    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service                
        beers = []
        
        jpl = {
        'userName' : self.userName,
        'userType' : self.userType,
        'email' : self.email,
        'height' : self.height
        }
        
        if self.favoriteBeers != []:
            for o in list(self.favoriteBeers):
                beers.append(o.beerName)
                
        jpl.update({ 'favoriteBeers' : beers })
        
        return jpl        
#========================================================================= 
    



    
#=========================================================================     
    