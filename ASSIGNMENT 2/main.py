import random
class ATM:
 user_name = "SAYA15"
 passcode = 15112
 Balance = 100000
 user = input("Enter your user name: ")
 password = int(input("Enter your 5 digit code: "))

 def service(self):
  Flag = True
  while Flag == True:
   print("Choose an Option: ")
   choice = int(input(" 1. Credit \n 2. Debit \n 3. Check Balance \n 4. Exit \n"))
   OTP = random.randint(111111,999999)
   print(" your OTP is: ",OTP)
   user_otp = int(input("Enter the 6-digit OTP : "))
   if OTP == user_otp:
    print("OTP Verified !!!")
    if choice == 1:
     deposit = int(input("Enter the amount to deposit: "))
     self.credit(deposit)
    elif choice == 2:
     debit = int(input("Enter the amount to debit: "))
     self.withdraw(debit , self.Balance)
    elif choice == 3:
     self.enquiry()
    elif choice == 4:
     exit()
     Flag = False
    else:
     print("Invalid option")
   else:
    print("Incorrect OTP !!!")
  return self.Balance


 def credit(self, deposit):
  self.Balance += deposit
  print("Amount Credited successfully !!!")
  return self.Balance

 def withdraw(self, debit, Balance):
  if debit > Balance:
   print("Insufficient Balance !!!")
  else:
   self.Balance -= debit
   print("Amount debited successfully !!!")
  return self.Balance

 def enquiry(self):
  print("Your available balance is Rs.%d" % self.Balance)

obj = ATM()

if obj.user_name == obj.user and obj.passcode == obj.password:
 obj.service()
else:
 print("Wrong Credentials")
