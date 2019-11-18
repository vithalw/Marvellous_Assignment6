class Demo:
    value=0;
    def __init__(self,val1,val2):
        self.no1=val1;
        self.no2=val2;
    def Fun(self):
        print("In Fun: ",self.no1);
        print("In Fun: ",self.no2);    
    
    def Gun(self):
        print("In Gun: ",self.no1);
        print("In Gun: ",self.no2);    
    



def main():
    o1=Demo(11,21);
    o2=Demo(51,101);

    o1.Fun();
    o2.Fun();

    o1.Gun();
    o2.Gun();

if __name__=="__main__":
    main();