from random import SystemRandom
from time import clock_settime
from thehive4py.api import TheHiveApi
from thehive4py.models import *

def print_parameters(a,b,c,d,e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

def prepare_custom_field(template):
    customField = CustomFieldHelper()
    for k,v in template.items(): 
        customField.add_string(k, v)
    return customField.build()          


template_x =  {
    "atividade-de-rede":"dominio.teste.com",
    "businessimpact":"LOW",
    "businessunit":"HR"
}

# Server variables
hiveServer = 'http://192.168.2.23/thehive/'
hiveKey = 'yZR4AuSwQp1wjVD6PwOYheS/b4MV0lby'

# Establish API
api = TheHiveApi(hiveServer, hiveKey)

case = Case(title='Teste 2 - TheHive4Py',
        tlp=3,
        flag=True,
        tags=['TheHive4Py', 'sample'],
        description='Testando o método POST da API',
        customFields=prepare_custom_field(template_x))

# response = api.create_case(case)

# if response.status_code == 201:
#     print(json.dumps(response.json(), indent=4, sort_keys=True))
#     print('')
#     id = response.json()['id']
# else:
#     print('ko: {}/{}'.format(response.status_code, response.text))
#     SystemRandom.exit(0)
