# print("Hello World")


#function 
# def my_function():
#     print("Hello Python Dev's")
# my_function()


# return function 
# def add_numbers(num1 , num2):
#     ans = num1 + num2
#     return ans

# ans = add_numbers(20,50)
# print(ans)


# type() function 
# a = 45
# b = 3.333
# c = "Hello World"
# print(type(c))


#Loops
# for i in range(1,10):
#     print(i)

# i = 1
# while i<100:
#     print(i)
#     i +=3

# numbers =  [1,2,3,4,5]
# for i in numbers:
#     print(i)

# cities = ['Palestine', 'Pakistan','Iran']
# for city in cities:
#     print(city , len(city))


#if else elif
# buy = int (input("Please Enter the Buy Price:"))
# sell = int(input("Please Enter the Sell Price:"))

# if(sell<buy):
#     print("Loss")
# elif (sell>buy):
#     print("Profit")
# elif (buy == sell):
#     print("No Profit No Loss")
# else:
#     print("End")

#fibonacci Series
# def fib(num):
#     a = 0;
#     b = 1;
#     while a<num:
#         c = a + b;
#         print(a + " "+ b +" " + c)
#         a = a+1

#Class
# class CreditCared:
#     def __init__(self , customer, bank, acc,limit,balance):
#         self.customer=customer
#         self.bank=bank
#         self.acc=acc
#         self.limit=limit
#         self.balance=balance
    
#     def get_coustomer(self):
#         return self.customer

#     def get_bank(self):
#         return self.bank

#     def get_acc(self):
#         return self.acc

#     def get_limit(self):
#         return self.limit

#     def get_balance(self):
#         return self.balance
    
#     def Print(obj):
#         print("Customer Name: "+obj.customer)
#         print("Customer Bank: "+obj.bank)
#         print("Customer Account: "+ obj.acc)
#         print("Customer Limi: "+str(obj.limit))
#         print("Customer Balance: "+str(obj.balance))

#     def calculation(obj):
#         widtrawl = int (input("Plese Enter The Withdrawl Amount:"))
#         if(widtrawl==0):
#             print("Enter the Valid Value")
#             return 

#         elif(obj.balance<widtrawl):
#             print("Withdrawl Amount is out of balance")
#             return

#         elif(widtrawl<obj.balance):
#             if(widtrawl<obj.limit):
#                  obj.balance = obj.balance - widtrawl;
#                  print(str(widtrawl)+ " Amount is withdrawl your remaning balance is: cle" + str(obj.balance))
#                  return

#         elif(widtrawl<obj.balance):
#             if(widtrawl>obj.limit):
#                  print("Withdrawl amount greater than limit")
#                  return

#         else:
#             print("Enter interger value only")
#             return

#     def deposit(obj):
#         deposit = int (input("Please Enter the Deposit Amount:"))
#         if deposit>0:
#             obj.balance = obj.balance + deposit
#             print("Amount is deposit New Balance is: "+str(obj.balance))
#             return 
#         elif deposit<=0:
#             print("pLease Enter the Valid Value")
#             return 
        

# c1 = CreditCared("Ali", "HBL", "Saving",50000,100000000)        
# c1.Print()
# c1.deposit();
# # c1.calculation()


#File 
# "a" Append Mode
# f = open("myfile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# # "r" Read FIle
# f = open("myfile.txt","r")
# print(f.read())


# "w" Overwrite
# f = open("file2.txt","w")
# f.write("Now the file2 has more content!")
# f.close()

# f = open("file2.txt", "r")
# print(f.read())


# Delete file 
# import os
# if os.path.exists("file2.txt"):
#     os.remove("file2.txt")
# else:
#     print("File is does not exixt")


# Remove Directory
# import os
# os.rmdir("myfolder")