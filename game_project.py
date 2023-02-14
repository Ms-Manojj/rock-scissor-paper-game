import random
print("In this game we have only 3 round !!!")
print()
print("Game start.............")
print()

print("""
          Only select R,S or P
          R = Rock,
          S = Scissor,
          P = Paper
""")

print()
user_count=0
com_count=0
tie=0
worong_key=0
for i in range(1,4):
    user=input("User enter  :")
    user1=user.lower()
    
    if user1 in("r","p","s"):
        computer=["r","p","s"]
        com=random.choice(computer)
        print("computer entered :",com)
        print()
        if user1==com:
            # print("Tie")
            tie=tie+1
            print()
 #condition-           
        elif user1=="r" and com=="p":
            # print("computer win ")
            com_count=com_count+1
        elif user1=="p" and com=="r":
            # print("user win ")
            user_count=user_count+1
            print()
#condition-
        elif user1=="r" and com=="s":
            # print("user win ")
            user_count=user_count+1
        elif user1=="s" and com=="r":
            # print("computer win ")
            com_count=com_count+1
            print()

#condition-
        elif user1=="p" and com=="s":
                # print("computer win ")
                com_count=com_count+1
        elif user1=="s" and com=="p":
                # print("computer win ")
                user_count=user_count+1
                print()
    else:
        worong_key=worong_key+1
        print("You have entered the wrong keywords ")

print()
print()
print(f"""Tie match count :{tie}
User total count :{user_count}:
Computer total count :{com_count}
Wrong key press :{worong_key}""")

print()
print()

if tie>=3 or tie>=2:
     print("The ganme is tie ")
elif user_count>=3 or user_count>=2:
     print("User Win ")
elif com_count>=3 or com_count>=2:
     print("Computer Win")
elif worong_key>=3 or worong_key>=2:
     print("Your have entered multipal wrong keywords So computer win this game ")
elif tie==1 and user_count==1 and com_count==1 and worong_key==0:
     print("Gamre tie")
elif tie==0 and user_count==1 and com_count==1 and worong_key==1:
     print("Game tie")
elif tie==1 and user_count==0 and com_count==1 and worong_key==1:
     print("Game tie")
elif tie==1 and user_count==1 and com_count==0 and worong_key==1:
     print("Game tie")

     
print("Game finish")



