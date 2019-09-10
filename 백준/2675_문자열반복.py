count = int(input())
for _ in range(count):
    input_list = input().split()
    length = int(input_list[0])
    for i in range(len(input_list[1])):
        print(input_list[1][i]*length,end='')
    print()
