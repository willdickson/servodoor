import time
from servodoor import ServoDoor

port = '/dev/ttyACM0'
ctrl = ServoDoor(port)

rsp = ctrl.get_config()
print(rsp['config'])

rsp = ctrl.get_positions()
print(rsp['positions'])

ctrl.set_doors({'front': 'open'})
time.sleep(5.0)

ctrl.set_doors({'front': 'close'})
time.sleep(5.0)





