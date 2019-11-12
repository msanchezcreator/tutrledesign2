import  turtle
bob=turtle.Turtle()
bob.speed(0)



turtle.colormode(255)
turtle.bgcolor("black")



for times in range(1000):
        
        bob.forward(times*2)
        bob.right(90)
        bob.color("white")
        bob.circle(times*5)
        bob.color("red")
        bob.backward(times*5)
        bob.right(90)
        bob.circle(times*2)
       
       
        
        

        
    
      
        
        
    
     

        

        
