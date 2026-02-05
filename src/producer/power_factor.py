# codicao ideal = 1
# variacao entre 0.8 e 1

from random import uniform
from datetime import datetime, timezone

def gerador(id):
    dados = uniform(0.8, 1)
    return {'id': str(id), 
                'data': str(dados), 
                'type': 'Power Factor', 
                'timestamp': datetime.now(timezone.utc).isoformat()
                }
    

