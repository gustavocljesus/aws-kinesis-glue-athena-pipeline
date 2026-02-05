# codicao ideal = 1
# variacao entre 0.8 e 1

from random import uniform
from datetime import datetime, timezone

def gerador(id):
    dado = round(uniform(0.8, 1), 4)
    return {'id': id, 
                'data': dado, 
                'type': 'Power Factor', 
                'timestamp': datetime.now(timezone.utc).isoformat()
                }
    

