date: 2021-03-23 13:17:17
author: Jerry Su
slug: Apache2 Deploy Multi-sites
title: Apache2 Deploy Multi-sites
category: 
tags: Apache2, Server
summary: Reason is the light and the light of life.
toc: show

[I submit the issue](https://github.com/posativ/isso/issues/718)

## 1. Isso as systemd service

Switch back to your privileged(root) user and create new service file.

`vim /etc/systemd/system/isso.service`
Paste the following in it.

```
[Unit]
Description=Isso Commenting Server
After=network.target
[Service]
Type=simple
User=isso
WorkingDirectory=/home/isso
ExecStart=/home/isso/.local/bin/isso -c /home/isso/isso.conf
Restart=on-failure
RestartSec=5
[Install]
WantedBy=multi-user.target
```

Enable and start the service.

`systemctl enable isso`

`systemctl start isso`

Check the status.

`systemctl status isso`



- apache2 Multi-sites

- 阿里云二级域名

- Apach2 as reverse proxy

#### 1.1 新增站点配置文件


```python
!ls /etc/apache2
```

    apache2.conf	core	 mods-available  sites-available
    conf-available	envvars  mods-enabled	 sites-enabled
    conf-enabled	magic	 ports.conf



```python
!cat /etc/apache2/apache2.conf
```

    # This is the main Apache server configuration file.  It contains the
    # configuration directives that give the server its instructions.
    # See http://httpd.apache.org/docs/2.4/ for detailed information about
    # the directives and /usr/share/doc/apache2/README.Debian about Debian specific
    # hints.
    #
    #
    # Summary of how the Apache 2 configuration works in Debian:
    # The Apache 2 web server configuration in Debian is quite different to
    # upstream's suggested way to configure the web server. This is because Debian's
    # default Apache2 installation attempts to make adding and removing modules,
    # virtual hosts, and extra configuration directives as flexible as possible, in
    # order to make automating the changes and administering the server as easy as
    # possible.
    
    # It is split into several files forming the configuration hierarchy outlined
    # below, all located in the /etc/apache2/ directory:
    #
    #	/etc/apache2/
    #	|-- apache2.conf
    #	|	`--  ports.conf
    #	|-- mods-enabled
    #	|	|-- *.load
    #	|	`-- *.conf
    #	|-- conf-enabled
    #	|	`-- *.conf
    # 	`-- sites-enabled
    #	 	`-- *.conf
    #
    #
    # * apache2.conf is the main configuration file (this file). It puts the pieces
    #   together by including all remaining configuration files when starting up the
    #   web server.
    #
    # * ports.conf is always included from the main configuration file. It is
    #   supposed to determine listening ports for incoming connections which can be
    #   customized anytime.
    #
    # * Configuration files in the mods-enabled/, conf-enabled/ and sites-enabled/
    #   directories contain particular configuration snippets which manage modules,
    #   global configuration fragments, or virtual host configurations,
    #   respectively.
    #
    #   They are activated by symlinking available configuration files from their
    #   respective *-available/ counterparts. These should be managed by using our
    #   helpers a2enmod/a2dismod, a2ensite/a2dissite and a2enconf/a2disconf. See
    #   their respective man pages for detailed information.
    #
    # * The binary is called apache2. Due to the use of environment variables, in
    #   the default configuration, apache2 needs to be started/stopped with
    #   /etc/init.d/apache2 or apache2ctl. Calling /usr/bin/apache2 directly will not
    #   work with the default configuration.
    
    
    # Global configuration
    #
    
    #
    # ServerRoot: The top of the directory tree under which the server's
    # configuration, error, and log files are kept.
    #
    # NOTE!  If you intend to place this on an NFS (or otherwise network)
    # mounted filesystem then please read the Mutex documentation (available
    # at <URL:http://httpd.apache.org/docs/2.4/mod/core.html#mutex>);
    # you will save yourself a lot of trouble.
    #
    # Do NOT add a slash at the end of the directory path.
    #
    #ServerRoot "/etc/apache2"
    
    #
    # The accept serialization lock file MUST BE STORED ON A LOCAL DISK.
    #
    #Mutex file:${APACHE_LOCK_DIR} default
    
    #
    # The directory where shm and other runtime files will be stored.
    #
    
    DefaultRuntimeDir ${APACHE_RUN_DIR}
    
    #
    # PidFile: The file in which the server should record its process
    # identification number when it starts.
    # This needs to be set in /etc/apache2/envvars
    #
    PidFile ${APACHE_PID_FILE}
    
    #
    # Timeout: The number of seconds before receives and sends time out.
    #
    Timeout 300
    
    #
    # KeepAlive: Whether or not to allow persistent connections (more than
    # one request per connection). Set to "Off" to deactivate.
    #
    KeepAlive On
    
    #
    # MaxKeepAliveRequests: The maximum number of requests to allow
    # during a persistent connection. Set to 0 to allow an unlimited amount.
    # We recommend you leave this number high, for maximum performance.
    #
    MaxKeepAliveRequests 100
    
    #
    # KeepAliveTimeout: Number of seconds to wait for the next request from the
    # same client on the same connection.
    #
    KeepAliveTimeout 5
    
    
    # These need to be set in /etc/apache2/envvars
    User ${APACHE_RUN_USER}
    Group ${APACHE_RUN_GROUP}
    
    #
    # HostnameLookups: Log the names of clients or just their IP addresses
    # e.g., www.apache.org (on) or 204.62.129.132 (off).
    # The default is off because it'd be overall better for the net if people
    # had to knowingly turn this feature on, since enabling it means that
    # each client request will result in AT LEAST one lookup request to the
    # nameserver.
    #
    HostnameLookups Off
    
    # ErrorLog: The location of the error log file.
    # If you do not specify an ErrorLog directive within a <VirtualHost>
    # container, error messages relating to that virtual host will be
    # logged here.  If you *do* define an error logfile for a <VirtualHost>
    # container, that host's errors will be logged there and not here.
    #
    ErrorLog ${APACHE_LOG_DIR}/error.log
    
    #
    # LogLevel: Control the severity of messages logged to the error_log.
    # Available values: trace8, ..., trace1, debug, info, notice, warn,
    # error, crit, alert, emerg.
    # It is also possible to configure the log level for particular modules, e.g.
    # "LogLevel info ssl:warn"
    #
    LogLevel warn
    
    # Include module configuration:
    IncludeOptional mods-enabled/*.load
    IncludeOptional mods-enabled/*.conf
    
    # Include list of ports to listen on
    Include ports.conf
    
    
    # Sets the default security model of the Apache2 HTTPD server. It does
    # not allow access to the root filesystem outside of /usr/share and /var/www.
    # The former is used by web applications packaged in Debian,
    # the latter may be used for local directories served by the web server. If
    # your system is serving content from a sub-directory in /srv you must allow
    # access here, or in any related virtual host.
    <Directory />
    	Options FollowSymLinks
    	AllowOverride None
    	Require all denied
    </Directory>
    
    <Directory /usr/share>
    	AllowOverride None
    	Require all granted
    </Directory>
    
    <Directory /var/www/>
    	Options Indexes FollowSymLinks
    	AllowOverride None
    	Require all granted
    </Directory>
    
    #<Directory /srv/>
    #	Options Indexes FollowSymLinks
    #	AllowOverride None
    #	Require all granted
    #</Directory>
    
    
    
    
    # AccessFileName: The name of the file to look for in each directory
    # for additional configuration directives.  See also the AllowOverride
    # directive.
    #
    AccessFileName .htaccess
    
    #
    # The following lines prevent .htaccess and .htpasswd files from being
    # viewed by Web clients.
    #
    <FilesMatch "^\.ht">
    	Require all denied
    </FilesMatch>
    
    
    #
    # The following directives define some format nicknames for use with
    # a CustomLog directive.
    #
    # These deviate from the Common Log Format definitions in that they use %O
    # (the actual bytes sent including headers) instead of %b (the size of the
    # requested file), because the latter makes it impossible to detect partial
    # requests.
    #
    # Note that the use of %{X-Forwarded-For}i instead of %h is not recommended.
    # Use mod_remoteip instead.
    #
    LogFormat "%v:%p %h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" vhost_combined
    LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %O" common
    LogFormat "%{Referer}i -> %U" referer
    LogFormat "%{User-agent}i" agent
    
    # Include of directories ignores editors' and dpkg's backup files,
    # see README.Debian for details.
    
    # Include generic snippets of statements
    IncludeOptional conf-enabled/*.conf
    
    # Include the virtual host configurations:
    IncludeOptional sites-enabled/*.conf
    
    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet


```
# Include the virtual host configurations:

IncludeOptional sites-enabled/*.conf
```


```python
#  blog.conf -> ../sites-available/blog.conf配置的软链接，指向真实的配置
!ls /etc/apache2/sites-enabled
```

    blog.conf



```python
# 新建站点的配置文件，comments_blog.conf
!ls /etc/apache2/sites-available
```

    blog.conf  comments_blog.conf  default-ssl.conf



```python
!cat /etc/apache2/sites-available/comments_blog.conf
```

    <VirtualHost *:80>
    	# The ServerName directive sets the request scheme, hostname and port that
    	# the server uses to identify itself. This is used when creating
    	# redirection URLs. In the context of virtual hosts, the ServerName
    	# specifies what hostname must appear in the request's Host: header to
    	# match this virtual host. For the default virtual host (this file) this
    	# value is not decisive as it is used as a last resort host regardless.
    	# However, you must set it for any further virtual host explicitly.
    	#ServerName www.example.com
    
    	ServerAdmin webmaster@localhost
    	ServerName http://www.comments.jerrylsu.net
    	DocumentRoot /var/www/blog/isso
    
      # off表示开启反向代理，on表示开`启正向代理
      ProxyRequests Off
      # 将这个虚拟主机跳转到本机的8180端口
      # Proxy for Isso commenting
      ProxyPass / http://localhost:8180/
      ProxyPassReverse / http://localhost:8180/
      <Proxy *>
              Order Deny,Allow
              Allow from all
      </Proxy>
    	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
    	# error, crit, alert, emerg.
    	# It is also possible to configure the loglevel for particular
    	# modules, e.g.
    	#LogLevel info ssl:warn
    
    	ErrorLog ${APACHE_LOG_DIR}/error.log
    	CustomLog ${APACHE_LOG_DIR}/access.log combined
    
    	# For most configuration files from conf-available/, which are
    	# enabled or disabled at a global level, it is possible to
    	# include a line for only one particular virtual host. For example the
    	# following line enables the CGI configuration for this host only
    	# after it has been globally disabled with "a2disconf".
    	#Include conf-available/serve-cgi-bin.conf
    </VirtualHost>
    
    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet


#### 1.2 建立软链接


```python
# 为comments_blog.conf站点建立软链接

"""
cd /etc/apache2/sites-enabled

#建立对应的软链接
sudo ln -s /etc/apache2/sites-available/comments_blog.conf /etc/apache2/sites-enabled/comments_blog.conf

-> a2ensite comments_blog.conf

"""
!ls /etc/apache2/sites-enabled
```

    blog.conf  comments_blog.conf


#### 1.3 修改/etc/hosts


```python
!cat /etc/hosts
```

    127.0.0.1	localhost
    ::1	localhost ip6-localhost ip6-loopback
    fe00::0	ip6-localnet
    ff00::0	ip6-mcastprefix
    ff02::1	ip6-allnodes
    ff02::2	ip6-allrouters
    172.17.0.2	e7cac75317f0


#### 1.4 重启Apache2

service apache2 restart


```python

```

[https://hackriculture.fr/isso-commentaires-auto-heberges-pour-pelican-et-autres-sites-statiques.html](https://hackriculture.fr/isso-commentaires-auto-heberges-pour-pelican-et-autres-sites-statiques.html)

[https://therandombits.com/2018/12/how-to-add-isso-comments-to-your-site/](https://therandombits.com/2018/12/how-to-add-isso-comments-to-your-site/)

[http://www.linuxidc.com/Linux/2017-05/143590.htm](http://www.linuxidc.com/Linux/2017-05/143590.htm)


```python

```
