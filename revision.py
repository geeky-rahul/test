a = 7

# for i in range(a):
#     for j in range(i):
#         print("* ", end=" ")
#     print(" ")

# for i in range(a-1,0,-1):
#     for j in range(i-1):
#         print("* " , end=" ")
#     print()

k = 2*a-2
for i in range(a):
    for j in range(k):
        print(end=" ")
    k = k - 2    
    for j in range(0,i+1):
     print("* ", end="")
     print()
for i in range(a):
    for j in range(i):
        print("* ", end=" ")
    print(" ")
     
    