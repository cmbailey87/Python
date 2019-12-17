from datadog import api, initialize

options = {
  'api_key':'25af742dc74b5c5d1efd29459b5c7c08',
  'app_key':'bcc64e922e922b0e92282821fd15e044d85aa46f',
  'api_host': 'https://api.datadoghq.com'
}

role_str = ['st','adm','ro']

data = {}

initialize(**options)

def role_switch(arg):
    switcher = {
    "st": "st",
    "adm": "adm",
    "ro": "ro"
    }
    role_conf = switcher.get(arg, "invalid choice")
    return role_conf

def eval_Data(arg):
    if 'errors' in arg.keys():
        for i,j in arg.items():
            crack = i,j
            crackstr = crack[0]+ ' ' + crack[1][0]
        print(crackstr)
        print("User account was not sent invite")
        if input("Do you wish to try again? y or n (Default is 'n' ) ").lower() == 'y':
            invite_User()
    else:
        for i,j in arg.items():
            crack = i,j
            crackstr = crack[0]+ ' ' + crack[1][0]
        print(crackstr)


def invite_User():

    email = input("Please enter the emailaddress of the user: ")
    role = input("Please specify user role. Exmp: Standard = \'st\' ;  Admin = \'adm\' ; Read Only=\'ro\'").lower()

    role_appr = role_switch(role)

    if role_appr == "invalid choice":
        print(role_appr + " " + ", please enter a valid role")
        invite_User()
    else:
        print("invite will be sent to been sent to" +" "+ email)
        data = api.User.create(handle=email, access_role=role_appr)
        ###evaluate the response
    eval_Data(data)

invite_User()
