from netmiko import ConnectHandler
from jinja2 import Template
import os
os.chdir('C:\GNS3\Python\python_out\new')
template_1 = (int_config.j2)
cisco_rw={
    'device_type':'cisco_ios',
    'host':'172.16.138.161',
    'username':'cisco',
    'password':'cisco',
    'secret':'cisco'
}


temp_render={
    'iface_number':'f1/0',
    'ip_address':'10.10.10.1 255.255.255.252'
 }

ssh=ConnectHandler(**cisco_rw)
ssh.enable*()
with open(template_1) as temp:
    switch_temp=Template(temp.read(),keep_trailing_newline=True)
    temp_in = switch_temp.render(temp_render)
    final_out= temp_in.split('\n')
    print(temp)

