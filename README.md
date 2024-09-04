# Post instalación de contenedores LXC con inventarios dinámicos

Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

Clona el repositorio en tu máquina local:

    git clone https://github.com/rafAlon84/ansible_post_install.git
    cd ansible_post_install

Estructura del Proyecto

Aquí tienes un desglose de la estructura del proyecto:

    # ansible_post_install
    # ├── dynamic_inventory.py  # Script en Python para inventario
    # ├── main.yml              # Archivo principal del playbook de Ansible
    # ├── roles/                # Carpeta con roles de Ansible
    # │   ├── aws/              # Instala la CLI de AWS
    # │   ├── Common-repo/      # Instalación de repositorios básicos
    # │   ├── NewDirectories/   # Creación de ficheros
    # │   ├── Python/           # Instalación de python y pip
    # │   ├── Terraform/        # Instalación de Terraform
    # │   └── zsh/              # instalación y configuración de zsh como shell
    # └── README.md             # Este archivo

Uso
Ejecución del Playbook

Para ejecutar el playbook principal con el inventario dinámico, usa el siguiente comando:

    # Ejecutando de la siguiente manera el comando, el playbook se aplicará sobre
    # todos los contenedores LXC que se encuentren levantados
        
        ansible-playbook -i dynamic_inventory.py main.yml

    # Para ejecutar el playbook sobre contenedores específicos, hay que añadir
    # el flag --limit <nombre_del_container>

        ansible-playbook -i dynamic_inventory.py main.yml --limit <nombre_del_container>

Asegúrate de tener los permisos adecuados y de que el inventario dinámico esté configurado correctamente.

Ejecución de Roles

Si tienes roles propios que quieras añadir para tu caso de uso específico, añádelo en directorio
/roles y posteriormente añade el nombre del rol en el fichero "main.yml" del directorio raíz del proyecto.

En el caso de uso del repositorio, he aprovechado para probar con las aplicaciones que utilizo
habitualmente, de esta forma en caso de cambiar de equipo, puedo ejecutar este playbook cambiando el script
para inventariar los contenedores LXC por "localhost".
