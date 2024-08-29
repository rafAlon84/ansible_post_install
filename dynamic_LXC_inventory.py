#!/usr/bin/env python3

import json
import subprocess

# Obtenemos la lista de contenedores LXC activos
def get_lxc_containers():
    try:
        result = subprocess.run(['sudo', 'lxc', 'list', '--format=json'], capture_output=True, text=True, check=True)
        containers = json.loads(result.stdout)
    except subprocess.CalledProcessError as error:
        print(f"Error ejecutando el comando lxc list: {error}")
        containers = []
    except json.JSONDecodeError as error:
        print(f"Error decodificando JSON: {error}")
        containers = []
    
    return containers

# Generamos el inventario para Ansible
def generate_inventory():
    inventory = {"lxc_containers": {"hosts": []}, "_meta": {"hostvars": {}}}
    containers = get_lxc_containers()

    for container in containers:
        if container['state']['status'] == 'Running':
            name = container['name']
            ip = None
            
            # Buscamos la dirección IP
            addresses = container.get('state', {}).get('network', {}).get('eth0', {}).get('addresses', [])
            
            for address in addresses:
                if address['family'] == 'inet':
                    ip = address['address']
                    break
            
            if ip:
                inventory["lxc_containers"]["hosts"].append(name)
                inventory["_meta"]["hostvars"][name] = {
                    "ansible_host": ip,
                    "ansible_connection": "ssh",
                    "ansible_user": "ubuntu"  # Ajusta esto según tu configuración SSH
                }

    return inventory

if __name__ == "__main__":
    print(json.dumps(generate_inventory(), indent=2))


