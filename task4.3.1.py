with open('assessment.txt') as file1:
    summa=0
    x=0    
    for i in file1:
        file1=int(i[len(i)-2])
        summa+=file1
        x+=1
        if file1<3:
            print(i)
    print("Average mark:",round(summa/x,2))