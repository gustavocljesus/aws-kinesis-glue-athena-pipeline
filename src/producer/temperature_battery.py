# temperatura media = 23 C
# variacao entre 22 e 25

from random import uniform
from datetime import datetime, timezone

def gerador(id):
    dados = uniform(22, 25)
    return {'id': str(id), 
                'data': str(dados), 
                'type': 'Temperature Battery', 
                'timestamp': datetime.now(timezone.utc).isoformat()
                }