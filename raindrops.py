def my_function(n):
    f3 = n%3 == 0
    f5 = n%5 == 0
    f7 = n%7 == 0
    if(f3 and f5 and f7):
        s = "PlingPlangPlong"
    elif(not(f3) and f5 and f7):
        s = "PlangPlong"
    elif(f3 and not(f5) and f7):
        s = "PlingPlong"
    elif(f3 and f5 and not(f7)):
        s = "PlingPlang"
    elif(not(f3) and not(f5) and f7):
        s = "Plong"
    elif(f3 and not(f5) and not(f7)):
        s = "Pling"
    elif(not(f3) and f5 and not(f7)):
        s = "Plang"
    else:
        s = str(n)
    print(s)