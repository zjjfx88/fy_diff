#file=open('alltj_result','r')
with open('alltj_result','r') as file:

    try:
        while True:
            line=file.readline().strip()
            if line:
                print(line)
            else:
                print("over")
                break
    except Exceptions as e:
        pass
