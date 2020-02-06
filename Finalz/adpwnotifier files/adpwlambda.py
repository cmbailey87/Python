import json
import boto3
from botocore.exceptions import ClientError

#get data from s3

PYDATA = []

S3 = boto3.resource('s3')
BUCKET_NAME = 'ad-pw-notify'
KEY = 'userPW_Notify.json'

OBJ = S3.Object(BUCKET_NAME, KEY)

JSONDATA = OBJ.get()['Body'].read().decode('utf-8')

PYDATA = json.loads(JSONDATA)



##email settings

SENDER = "ARCNotify@arc.travel"
AWS_REGION = "us-east-1"
CHARSET = "UTF-8"


client = boto3.client('ses',region_name=AWS_REGION)

def MAILER(ARG):
    RECIPIENT = ARG["mail"]
    SUBJECT = f"ARC.TRAVEL Password Will Expire in {ARG['days']} days"
    BODY_TEXT = (f'Hello {ARG["name"]}!\r\n'
                 f'Your ARC.Travel Password will expire in {ARG["days"]} days! \r\n'
                 "Please log into your workspace and update your password. \n"
                 "While in your workspace, please do one of the following to update your password....\n"
                 "(A)... If running Windows, click on the Connection Tab at the top of the workspaces window and select send CTRL-ALT-DEL, then select Change a Password and folloe the prompt. \n"
                 "(B)... If running Linux, open Terminal Command line and enter passwd, then follow the prompt. \n"
                 "If there are any questions, please contact ServiceDesk at x1000 or 1-703-341-1000 for futher assistance. \n"
                 "Thanks! \n"
                )

    BODY_HTML = f"""<html>
    <head></head>
    <body>
      <h1>Hello {ARG["name"]}!</h1>
      <h2>Your ARC.Travel Password will expire in {ARG["days"]} days!</h2>
      <p>Please log into your workspace and update your password. \n
      <br> 
      <br>While in your workspace, please do one of the following to update your password....\n
      <br>(A)... If running Windows, click on the Connection Tab at the top of the workspaces window and select send CTRL-ALT-DEL, then select Change a Password and follow the prompt. \n
      <br>(B)... If running Linux, open Terminal Command line and enter passwd, then follow the prompt. \n
      <br> 
      <br>If there are any questions, please contact ServiceDesk at x1000 or 1-703-341-1000 for futher assistance. \n</p>
      <br>  
      <br>Thanks! \n
    </body>
    </html> """
    client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )

info = "The following users have been notified. :  "

notified = []
for i in PYDATA:
    for k,v in i.items():
        if 'name' in k:
            notified.append(v)

def lambda_handler(event, context):
    try:
        #Provide the contents of the email.
        for i in PYDATA:
            #print(f'hello {i["name"]}! Your ARC.TRAVEL credendials will expire in {i["days"]}')
            MAILER(i)

    # Display an error if something goes wrong.
    except ClientError as e:
        return {
        'body': 'Messenges not sent',
        'status': 500,
        }
    else:
        return {
        'body': 'Messenges have been sent ' + info + ' ; '.join(notified),
        'status': 200,
        }
