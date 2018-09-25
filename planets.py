def weight_on_planets():
   # write your code here
   weight=input("What do you weigh on earth? ")
   
   mars=float(weight)*(.38)
   jupiter=float(weight)*(2.34)
   print("\nOn Mars you would weigh",mars,"pounds.\nOn Jupiter you would weigh" , jupiter,"pounds.") 
   
if __name__ == '__main__':
   weight_on_planets()
   