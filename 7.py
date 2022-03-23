import random
def control(inputs):
    cont=120
    state   = 'straight'
    distance_right = inputs["distance-right"]
    distance_left  = inputs["distance-left"]
   
    if state == 'straight':
       
        if distance_right <300 or distance_left < 300:  
           
            state = 'straight'
            speed = 45          
            
        else:
            state = 'turning'
            speed = 20
            cont = random.randint(5,10)
            
            if state == 'turning' and cont != 0 :
                cont = cont-1
                state = 'turning'
            else:
                
                state = 'straight'
     
    z = distance_right - distance_left
    if z < 0:
        z = z*(-1)
    
    if z >= 200:
     
        if cont != 0 and z>=200:
            state = 'straight'
            cont=cont-1
        
        elif z<100:
            state = 'straight'
        
        else:
            
            state = 'stop'
    
    front_left  = inputs["front-left"]
    front_right = inputs["front-right"]
        
    if front_left > 0.35 or front_right > 0.35:
        aux = random.randint(5,14)
        state = 'turning'
       
        if aux !=0:
            aux=aux-1
            state = 'turning'
   
        else:
            state = 'straight'
            
    
    speed = 30

    
    left_speed  = 0
    right_speed = 0
    
    if state == 'straight':

        left_speed  = speed
        right_speed = -speed
            
    if state == 'turning':
       
        left_speed  =  speed
        right_speed =  speed 
        

  
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [
            { 'name': 'Distance Left',  'value': distance_left,  'min': 0, 'max': 300 },
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 }
        ]
    }
