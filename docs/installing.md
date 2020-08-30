
Server setup
https://www.linode.com/docs/security/securing-your-server/

firewall:
    apt install ufw
   sudo ufw default allow outgoing
   sudo ufw default deny incoming
   sudo ufw allow 71 #ssh
   sudo ufw allow http/tcp
   sudo ufw allow https/tcp
   ufw enable
   ufw status


```
mkdir -p /var/www/edu.macaca.life/
cd /var/www/edu.macaca.life/
git clone <repo>
chown root:www-data -R macacaedu/
python3 -m venv venv
source venv/bin/activate
pip install -r  requirements.txt
```

apt install apache2 libapache2-mod-wsgi-py3


```
<VirtualHost *:80>
     ServerAdmin gustavo@padovan.org
     ServerName edu.macaca.life

     Alias /static /var/www/edu.macaca.life/macacaedu/static
     Alias /media  /var/www/edu.macaca.life/macacaedu/macacaedu/media                                                        

     <Directory /var/www/edu.macaca.life/macacaedu/macacaedu>
      <Files wsgi.py>
        Require all granted
        </Files>
     </Directory>

     WSGIDaemonProcess macacaedu python-home=/var/www/edu.macaca.life/venv python-path=/var/www/edu.macaca.life/macacaedu:/var/www/edu.macaca.life/venv/lib/python3.7/site-packages
     WSGIProcessGroup macacaedu
     WSGIScriptAlias / /var/www/edu.macaca.life/macacaedu/macacaedu/wsgi.py                                                  

     LogLevel warn
     ErrorLog /var/www/edu.macaca.life/logs/error.log
     CustomLog /var/www/edu.macaca.life/logs/access.log combined
</VirtualHost>
```

./manage.py collectstatic
./manage.py migrate
chown root:www-data -R db.sqlite3
./manage.py createsuperuser
