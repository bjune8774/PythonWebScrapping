# -*- coding: cp949 -*-

maker = 'bjune.jeong'

class RestaurantInfo :    
    category = ''
    title = ''
    imgUrl = ''
    grade = ''
    addr = ''
    phone = ''
    homepage = ''
    
##    def __init__(self) :

    def printInfo(self) :
        print 'category : ', self.category
        print 'title : ', self.title
        print 'imgUrl : ', self.imgUrl
        print 'grade : ', self.grade
        print 'addr : ', self.addr
        print 'phone : ', self.phone
        print 'homepage : ', self.homepage
        
 
# Test Code
if __name__ == '__main__':
    print 'Test code from here'
    print maker
    
