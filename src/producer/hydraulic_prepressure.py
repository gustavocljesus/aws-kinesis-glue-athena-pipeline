# pressao media = 76 BAR
# variacao entre 75 e 78

from random import uniform
from datetime import datetime, timezone

def gerador(id):
    dado = round(uniform(75, 78), 4)
    return {'id': id, 
                'data': dado, 
                'type': 'Hydraulic Prepressure', 
                'timestamp': datetime.now(timezone.utc).isoformat()
                }