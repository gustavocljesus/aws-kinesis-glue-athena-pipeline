# pressao media = 76 BAR
# variacao entre 75 e 78

from random import uniform
from datetime import datetime, timezone

def gerador(id):
    dados = uniform(75, 78)
    return {'id': str(id), 
                'data': str(dados), 
                'type': 'Hydraulic Prepressure', 
                'timestamp': datetime.now(timezone.utc).isoformat()
                }