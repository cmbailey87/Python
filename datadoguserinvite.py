from datadog import api, initialize

options = {
  'api_key':'25af742dc74b5c5d1efd29459b5c7c08',
  'app_key':'bcc64e922e922b0e92282821fd15e044d85aa46f',
  'api_host': 'https://api.datadoghq.com'
}

initialize(**options)

email = input("PLease enter the emailaddress of the user: ")
api.User.create(handle=email, access_role='st')
