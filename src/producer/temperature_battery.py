# temperatura media = 23 C
# variacao entre 22 e 25

from random import uniform
from datetime import datetime, timezone

def gerador(id):
    dado = round(uniform(22, 25), 4)
    return {'id': id, 
                'data': dado, 
                'type': 'Temperature Battery', 
                'event_timestamp': datetime.now(timezone.utc).isoformat()
                }