"""
This scripts shows how to shutdown all the running VMs from a cluster
"""


import sys
import pprint
import json
sys.path.append("../src")
from pyproxmox import prox_auth,pyproxmox



# Blacklist some VM you don't want to shutdown
# vmblacklist = []
vmblacklist = ['134','158','133']

a = prox_auth('proxmoxnode','pveadmin@pve', 'pveadmin')
# If the authentication did not generate a ticket, the process failed.
if not a.ticket: 
    sys.exit(1)
b = pyproxmox(a)

nodes = b.getNodes()
# Browse the JSON output
for node in nodes['data']:
    pprint.pprint("====== "+node['node']+" ======")
    vmindex = b.getNodeVirtualIndex(node['node'])
    for vm in vmindex['data']:
        if vm['status'] == 'running' :
            print("%s :: %s" % (vm['vmid'],node['node']))
            if  vm['vmid'] not in vmblacklist :
                print("Shutting down VM %s" % (vm['vmid']))
#               Uncomment this 2 lines to actually do something
#                rc = b.shutdownVirtualMachine(node['node'],vm['vmid'])
#                pprint.pprint(rc)
            else :
                print("Cuidado ! Not shutting down %s" % (vm['vmid']))
                
