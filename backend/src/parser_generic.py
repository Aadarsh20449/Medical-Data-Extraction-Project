import abc
class MedicalDocParser(metaclass=abc.ABCMeta):
    def __int__(self,text):
        self.text=text 
    
    @abc.abstractmethod
    def parse(self):
        #return the josn object of the text
        pass