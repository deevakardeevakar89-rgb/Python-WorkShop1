class Aadhar:

    def __init__(self,name,aadhar_number,dob,finger_print,retina):
        self.name=name
        self.aadhar_number=aadhar_number
        self.dob=dob
        self._finger_print=finger_print   #protected
        self.__retina=retina  #private


    def display_userdata(self):
        print(f"Retena:{self.__retina},Aadhar Number:{self.aadhar_number}")


    def getRetena(self):
        return self.__retina

var=Aadhar("Prasad",123456778 ,"1-jan-2000","gffgff","aeaeae")
var.display_userdata()
