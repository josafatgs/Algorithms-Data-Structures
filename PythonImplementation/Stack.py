array = [1,2,3]

def Stack(array):
    if len(array) > 0:
        #print(array.append(4))
        print(array.pop())
        Stack(array)
    

print(Stack(array))

