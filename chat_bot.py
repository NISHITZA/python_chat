import time
import json


continue_flag = 1
tickets = ['123','124']
ticket_status = {
    '123':'1',
    '1234':'0'
}

while (continue_flag==1):
    current_time = time.strftime("%H", time.localtime())
    if(int(current_time)<12 and int(current_time)>6):
        print('Good Morning!')
    elif(int(current_time)>12 and int(current_time)<19):
        print('Good Evening')
    else:
        print('Good Night')

    print('Please enter your name')
    user_name = input()
    print(user_name+', I hope you\'re doing well')

    print('Do you have a ticket number Y/N')
    ticket_choice = input()
    if(ticket_choice=='Y' or ticket_choice=='y'):
        ticket_flag = 1
        while(ticket_flag==1):
            print('Please enter your ticket number')
            ticket_number = input()
            try:
                ticket_flag=0
                print('Ticket number found')
                if(ticket_status[ticket_number]==1):
                    print('The ticket has been resolved')
                else:
                    print('The ticket has not yet been resolved, we are going our best to solve it')
            except Exception:
                print('Ticket number not found, please enter again')
                
    else:
        print('Create new ticket')
        
        json_file = open('products.json',)
        product_list = json.load(json_file)

        print('Product List:')

        for i in product_list['products']:
            print(i)

        print('For which product do you want to raise a ticket ')
        product_choice = input()
        issue_product = ''
        temp_count = 0
        for i in product_list['products']:
            temp_count = temp_count+1
            if(temp_count==int(product_choice)):
                issue_product=i

        print('Product '+issue_product)




    print('Do you want to continue? Y/N ')
    end_choice = input()
    if(end_choice=='y' or end_choice=='Y'):
        continue_flag = 1
        print('\n\n\n')
    else:
        continue_flag = 0
        print('Thank you!\n\n\n')
    
