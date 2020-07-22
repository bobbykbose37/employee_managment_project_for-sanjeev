from datetime import date


str1="2017-04-30"
str2="2017-05-30"
num=""
list=[]


u=str1.split("-")
print(u,u[0],u[1],u[2])

y=str2.split("-")
print(y,y[0],y[1],y[2])



d0 = date(int(u[0]),int(u[1]),int(u[2]))
d1 = date(int(y[0]),int(y[1]),int(y[2]))
delta = d1 - d0
print(delta.days)