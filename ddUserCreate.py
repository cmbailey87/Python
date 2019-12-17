options = {
  'api_key':'25af742dc74b5c5d1efd29459b5c7c08',
  'app_key':'bcc64e922e922b0e92282821fd15e044d85aa46f',
  'api_host': 'https://api.datadoghq.com'
}


initialize(**options)

count = {
'default':1000
}

start = {
'default':200
}

filter = {
'default':'dc' in
}

filter = {
'default': 'Prod01-dc-01'
}
#getall users

ddusers = api.User.get_all()

for d in ddusers:
    print

ddusers.keys()
ddusers.values()

ddusers['users'][0]['handle']
#print all items in the dict
ddusers = api.User.get_all()
for e in ddusers['users']:
    print(e['handle'],e['name'])


disabled
handle
name
is_admin
role
access_role
verified
email
icon


(['last_reported_time', 'name', 'up', 'is_muted', 'mute_timeout', 'apps', 'tags_by_source', 'aws_name', 'metrics', 'sources', 'meta', 'host_name', 'aws_id', 'id', 'aliases'])

for e in ddhost['host_list']:
...     if 'dc' in e['name']:

for e in ddhost['host_list']:
    if '-dc-' in e['host_name']:
        data.append(e)
