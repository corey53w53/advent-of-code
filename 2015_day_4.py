import hashlib
input = "ckczppom"
counter=0
p1=True
while True:
    c=str(counter)
    hash=input+c
    result = hashlib.md5(hash.encode()).hexdigest()
    if result[0:5]=="00000" and p1:
        print(f'part 1: {counter}')
        p1=False
    if result[0:6]=="000000":
        print(f'part 2: {counter}')
        exit()
    counter+=1