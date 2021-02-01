user_num=int(input("Enter your number please?"))

number=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]



def rom_num_conversion(user_num):
    user_num_converted = ''
    while user_num > 0:
        for i,j in number:
            while user_num>=i:
                user_num-=i
                user_num_converted+=j
        print(user_num_converted)

rom_num_conversion(user_num)



