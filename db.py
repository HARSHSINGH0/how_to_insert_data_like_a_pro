import random
dict={0:'Harsh',1:'brendon',2:'alfaiz',3:'siddhant',4:'pawan'}
dictmarks={0:10,1:50,2:60,3:70,4:35}
dictsubject={0:'biology',1:'economics',2:'computer science',3:'history',4:'physics'}
dictcity={0:'mumbai',1:'delhi',2:'trivandrum',3:'bengaluru',4:'kolkata'}
for i in range(200):#number of time you want to insert
    a=random.randrange(0,4)
    b=random.randrange(0,4)
    c=random.randrange(0,4)
    d=random.randrange(0,4)
    name=dict[a]
    marks=dictmarks[b]
    subject=dictsubject[c]
    city=dictcity[d]
    print("insert into emp values(",i,",'{}',{},'{}','{}')"
        .format(name,marks,subject,city))
