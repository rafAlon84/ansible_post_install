#!/bin/zsh

# We get the directory where the script is located
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Path to dynamic inventory
DYNAMIC_INVENTORY="$DIR/dynamic_LXC_inventory.py"

# Path to playbook-test
PLAYBOOK_TEST="$DIR/roles/Terraform/tests/test.yml"

# if you pass an argument, use it as a limit, otherwise, it runs over all nodes
if [ -n "$1" ]; then
    ansible-playbook -i "$DYNAMIC_INVENTORY" "$PLAYBOOK_TEST" --limit "$1"
else
    ansible-playbook -i "$DYNAMIC_INVENTORY" "$$PLAYBOOK_TEST"
fi