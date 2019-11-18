class Arithmetic:
    def __init__(self):
        value1=0;
        value2=0;
    def accept(self,val1,val2):
        self.value1=val1;
        self.value2=val2;    
    def addition(self):
        return self.value1+self.value2;
    def subtraction(self):
        return self.value1-self.value2;        
    def multiplication(self):
        return self.value1*self.value2;
    def division(self):
        return self.value1/self.value2;


def main():
   o1=Arithmetic();
   o1.accept(10,20);
   print("Addition : ",o1.addition());
   
   print("Subtraction : ",o1.subtraction());
   
   print("Multiplication : ",o1.multiplication());
   
   print("Division : ",o1.division());


if __name__=="__main__":
    main();