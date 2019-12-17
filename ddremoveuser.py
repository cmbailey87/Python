from datadog import api, initialize

options = {
  'api_key':'25af742dc74b5c5d1efd29459b5c7c08',
  'app_key':'bcc64e922e922b0e92282821fd15e044d85aa46f',
  'api_host': 'https://api.datadoghq.com'
}

initialize(**options)


run = 'y'

def remove_User():
    email = input("Please enter the emailaddress of the user to disable: ")

    data = api.User.delete(email)


    for i,j in data.items():
            crack = i,j
            crackstr = crack[0]+ ' ' + crack[1][0]
    if 'error'  in crackstr:
        print(crackstr)
        if input("Do you wish to try again? y or n (Default is 'n' ) ").lower() == 'y':
            #run program again
            remove_User()
    elif 'disabled' in crackstr:
        print(crackstr)
        input('command has been ran successfull')


remove_User()
