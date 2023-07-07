import time
from servodoor import ServoDoor

port = '/dev/ttyACM0'
num_test = 1

print(f'port: {port}')
print()

ctrl = ServoDoor(port)


for i in range(num_test):

    print(f'test: {i+1}/{num_test}')
    print(f'----------------------')
    print()

    rsp = ctrl.get_config_errors()
    print(f'config errors: {rsp}')
    print()
    
    rsp = ctrl.get_config()
    print('config')
    for k, v in rsp['config'].items():
        print(f'{k}: {v}')
    print()
    
    rsp = ctrl.is_enabled()
    print(f'is_enabled: {rsp["is_enabled"]}')
    print()
    
    rsp = ctrl.disable()
    print(f'disable: {rsp}')
    print()
    
    rsp = ctrl.is_enabled()
    print(f'is_enabled: {rsp["is_enabled"]}')
    print()
    
    rsp = ctrl.enable()
    print(f'enable:  {rsp}')
    print()
    
    rsp = ctrl.is_enabled()
    print(f'is_enabled: {rsp["is_enabled"]}')
    print()
    
    rsp = ctrl.get_doors()
    print(f'get_doors: {rsp["doors"]}')
    door_list = [name for name in rsp['doors']]
    
    print() 
    
    for door in door_list:
    
        print(f'test door: {door}')
        cmd = {door: 'open'}
        rsp = ctrl.set_doors(cmd)
        print(f'set_doors: {rsp["doors"]}')
        time.sleep(1.0)
    
        cmd = {door: 'close'}
        rsp = ctrl.set_doors(cmd)
        print(f'set_doors: {rsp["doors"]}')
        time.sleep(1.0)
        print()
    
    print(f'testing all doors: {door_list}')
    cmd = {door: 'open' for door in door_list}
    rsp = ctrl.set_doors(cmd)
    print(f'set_doors: {rsp["doors"]}')
    time.sleep(1.0)
    print()
    
    cmd = {door: 'close' for door in door_list}
    rsp = ctrl.set_doors(cmd)
    print(f'set_doors: {rsp["doors"]}')
    time.sleep(1.0)
    print()

    
