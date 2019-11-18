class Circle:
    pi=3.14;
    def __init__(self):
        self.radius=0.0;
        self.area=0.0;
        self.circumference=0.0;
    def accept(self,radii):
        self.radius=radii;
    def calculateArea(self):
       # global pi
        self.area=Circle.pi*self.radius**2;
    def calculateCircumference(self):
        #global pi
        self.circumference=2*Circle.pi*self.radius;
    def display(self):
        print("Radius: ",self.radius);
        print("Area: ",self.area);
        print("Circumference: ",self.circumference);

def main():
   o1=Circle();
   o1.accept(5);
   o1.calculateArea();
   o1.calculateCircumference();
   o1.display();


if __name__=="__main__":
    main();