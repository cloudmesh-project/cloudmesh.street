#!/bin/sh
echo [all_nodes]|cat > hosts
cm cluster nodes cluster-001|awk '{print $2 }'> ip_list
sed -i 's/$/ ansible_ssh_user=cc/' ip_list
sed -i '/\[all_nodes\]/ r ip_list' hosts
rm ip_list
