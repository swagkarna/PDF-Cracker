print("""

╔═══╦═══╦═══╗╔═══╦═══╦═══╦═══╦╗╔═╦═══╦═══╗
║╔═╗╠╗╔╗║╔══╝║╔═╗║╔═╗║╔═╗║╔═╗║║║╔╣╔══╣╔═╗║
║╚═╝║║║║║╚══╗║║─╚╣╚═╝║║─║║║─╚╣╚╝╝║╚══╣╚═╝║
║╔══╝║║║║╔══╝║║─╔╣╔╗╔╣╚═╝║║─╔╣╔╗║║╔══╣╔╗╔╝
║║──╔╝╚╝║║───║╚═╝║║║╚╣╔═╗║╚═╝║║║╚╣╚══╣║║╚╗
╚╝──╚═══╩╝───╚═══╩╝╚═╩╝─╚╩═══╩╝╚═╩═══╩╝╚═╝
                       Author:Swagkarna

""")              


import PyPDF2 as pd



     

filename = input('Enter the Path of Pdf File: ')
passlist = input('Enter the Path of Passlist file:') 
file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('Your PDF file does not Contain a Password you can Easily open')

     
else:
    wordListFile = open(passlist, 'r')
    body = wordListFile.read().lower()
    words = body.split()

    for i in range(len(words)):
        print("Attempts tried :",i)
        word = words[i]
        print('Cracking {}'.format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print('\n[-]Password Cracked Successfuly \n[-]The password is: ' + word)
            break

        elif result == 0:
            tried += 1
            print("Passwords cannot be cracked:  + str(tried)")
            continue
            
print("Happy Cracking")
