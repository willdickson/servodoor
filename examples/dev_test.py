import time
from servodoor import ServoDoor

port = '/dev/ttyACM0'

print(f'port: {port}')
print()

ctrl = ServoDoor(port)
rsp = ctrl.get_config()
print('config')
for k, v in rsp['config'].items():
    print(f'{k}: {v}')
print()
print(ctrl.get_positions())
time.sleep(0.1)

for i in range(2):
    print('opening')
    ctrl.set_doors({'front': 'open'})
    time.sleep(5.0)
    print(ctrl.get_positions())
    print('closing')
    ctrl.set_doors({'front': 'close'})
    time.sleep(5.0)
    print(ctrl.get_positions())



