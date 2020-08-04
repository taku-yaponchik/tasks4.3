with open('assessment.txt') as file:
    line = 0
    for i in file:
        line += 1
        flag = 0
        word = 0
        for x in i:
            if x != ' ' and flag == 0:
                word += 1
                flag = 1
            elif x == ' ':
                flag = 0
        print(line,'str',len(i),'characters',word,'words')