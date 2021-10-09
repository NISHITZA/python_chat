import time

continue_flag = 1

while (continue_flag==1):
    current_time = time.strftime("%H", time.localtime())
    if(int(current_time)<12 and int(current_time)>6):
        print('Good Morning!')
    elif(int(current_time)>12 and int(current_time)<19):
        print('Good Evening')
    else:
        print('Good Night')

    print('Do you want to continue? Y/N')
    end_choice = input()
    if(end_choice=='y' or end_choice=='Y'):
        continue_flag = 1
    else:
        continue_flag = 0
        print('Thank you!')
    

