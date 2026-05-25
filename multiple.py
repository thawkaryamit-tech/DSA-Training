def multiple(x,y):
    if y==1:
        return x
    elif x==1:
        return y
    elif x==0 or y==0:
        return 0
    else:
        return x+multiple(x,y-1)
    
print(multiple(5,3))
    