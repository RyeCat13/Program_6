''' Rye Ledford, Computer Science Lab 101 '''

def encrypt(user_code,s):                    #fucntion for incription 
    result = "" 
    for i in range(len(user_code)): 
        char = user_code[i] 

        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 

        elif(char.islower()): 
            result += chr((ord(char) + s - 97) % 26 + 97)
            upeer = user_code.upper()
        else:
            result+= char
    return result 
    
def decrypt(user_code,s):                   #fucntion for decryption
    result = "" 
 
    for i in range(len(user_code)): 
        char = user_code[i] 
        if (char.isupper()): 
            result += chr((ord(char) - (s-65)) % 26 + 65)      
  
        elif(char.islower()):                                  
            result += chr((ord(char) - (s - 97)) % 26 + 97)
        
        else:
            result+= char
            
    return result 
     
def printMenu():                              #function for main menu
    print('\nMain Menu') 
    print('1). Encode a String')
    print('2). Decode a String')
    print('Q).Quit')
    print('Enter your selection ==> ',end='')
 
choice = 1                                   #choice starts at one

while(choice !=3):                           #for user to choose a choice give. If not a menu selection print 'Wrong Input'
    printMenu()
    choice = input()
    if choice =='1':                          #choice 1, encrypt
        print('\nEnter brief text to encrypt : ')
        user_code = input()
        user_code = user_code.upper()
        print('Enter the number to shift letters by: ')
        user_shift = int(input())
        x = encrypt(user_code,user_shift)
        print('\nEncrypted : ',x)
    elif choice == '2':                        #choice 2, decrypt
        print('\nEnter brief text to encrypt : ')
        user_code = input()
        user_code = user_code.upper()
        print('Enter the number to shift letters by: ')
        user_shift = int(input())
        x = decrypt(user_code,user_shift)
        print('\nDecrypted : ',x)
    elif choice == 'Q':                        #quit the module
        break
    else:
        print('\nWrong Input')


