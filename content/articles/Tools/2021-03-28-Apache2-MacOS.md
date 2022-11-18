date: 2021-03-28 15:17:17
author: Jerry Su
slug: Apache2 MacOS
title: Apache2 MacOS
category: 
tags: Apache2, Blog, Server
summary: Reason is the light and the light of life.
toc: show

Apache2 version: `sudo apachectl -v`

Apache2 diename: `/etc/apache2`

Apache2 config path: `/etc/apache2/httpd.conf`

Defualt Web source dirname **DoucumentRoot**: `/Library/WebServer/Documents`

- **httpd.conf**

```
DocumentRoot "/Library/WebServer/Documents"

Listen 80
```

`sudo apachectl start/restart/stop`

**Enable virtual host**

`sudo vi /etc/apache2/httpd.conf`

`# Include /private/etc/apache2/extra/httpd-vhosts.conf`, remove '#'

**Config virtual host**

`sudo vi /etc/apache2/extra/httpd-vhosts.conf`

```
<VirtualHost *:80>
    ServerAdmin webmaster@jerrylsu.local
    DocumentRoot "/Users/jerry/Documents/blog/output"
    ServerName jerrylsu.local
    ServerAlias www.jerrylsu.local
    ErrorLog "/private/var/log/apache2/jerrylsu.local-error_log"
    CustomLog "/private/var/log/apache2/jerrylsu.local-access_log" common
</VirtualHost>

<VirtualHost *:80>
    ServerAdmin webmaster@isso.jerrylsu.local
    DocumentRoot "/Users/jerry/Documents/blog/isso"
    ServerName isso.jerrylsu.local
    ErrorLog "/private/var/log/apache2/isso.jerrylsu.local-error_log"
    CustomLog "/private/var/log/apache2/isso.jerrylsu.local-access_log" common
</VirtualHost>
```

**Modify /etc/hosts**

```
127.0.0.1	localhost
127.0.0.1	jerrylsu.local
127.0.0.1	isso.jerrylsu.local
255.255.255.255	broadcasthost
::1             localhost
```

**Apache2 reverse proxy**

[设置文件夹权限"/Users/jerry/Documents"](https://support.apple.com/zh-cn/guide/mac-help/mchlp1203/mac)

`sudo vim /etc/apache2/httpd.conf`

```

Include /private/etc/apache2/extra/httpd-vhosts.conf

LoadModule proxy_html_module libexec/apache2/mod_proxy_html.so
LoadModule proxy_module libexec/apache2/mod_proxy.so
LoadModule proxy_connect_module libexec/apache2/mod_proxy_connect.so
LoadModule proxy_ftp_module libexec/apache2/mod_proxy_ftp.so
LoadModule proxy_http_module libexec/apache2/mod_proxy_http.so
LoadModule proxy_fcgi_module libexec/apache2/mod_proxy_fcgi.so
LoadModule proxy_scgi_module libexec/apache2/mod_proxy_scgi.so
LoadModule proxy_uwsgi_module libexec/apache2/mod_proxy_uwsgi.so
LoadModule proxy_fdpass_module libexec/apache2/mod_proxy_fdpass.so
LoadModule proxy_wstunnel_module libexec/apache2/mod_proxy_wstunnel.so
LoadModule proxy_ajp_module libexec/apache2/mod_proxy_ajp.so
LoadModule proxy_balancer_module libexec/apache2/mod_proxy_balancer.so
LoadModule proxy_express_module libexec/apache2/mod_proxy_express.so
LoadModule proxy_hcheck_module libexec/apache2/mod_proxy_hcheck.so

#<Directory />
#    AllowOverride none
#    Require all denied
#</Directory>

#
# Note that from this point forward you must specifically allow
# particular features to be enabled - so if something's not working as
# you might expect, make sure that you have specifically enabled it
# below.
#

#
# DocumentRoot: The directory out of which you will serve your
# documents. By default, all requests are taken from this directory, but
# symbolic links and aliases may be used to point to other locations.
#
#DocumentRoot "/Library/WebServer/Documents"
#<Directory "/Library/WebServer/Documents">
DocumentRoot "/Users/jerry/Documents"
<Directory "/Users/jerry/Documents">
    #
    # Possible values for the Options directive are "None", "All",
    # or any combination of:
    #   Indexes Includes FollowSymLinks SymLinksifOwnerMatch ExecCGI MultiViews
    #
    # Note that "MultiViews" must be named *explicitly* --- "Options All"
    # doesn't give it to you.
    #
    # The Options directive is both complicated and important.  Please see
    # http://httpd.apache.org/docs/2.4/mod/core.html#options
    # for more information.
    #
    Options Indexes FollowSymLinks Multiviews
    MultiviewsMatch Any

    #
    # AllowOverride controls what directives may be placed in .htaccess files.
    # It can be "All", "None", or any combination of the keywords:
    #   AllowOverride FileInfo AuthConfig Limit
    #
    AllowOverride None

    #
    # Controls who can get stuff from this server.
    #
    Require all granted
</Directory>
```

`sudo vim /etc/apache2/extra/httpd-vhosts.conf`

```
<VirtualHost *:80>
    ServerAdmin webmaster@jerrylsu.local
    DocumentRoot "/Users/jerry/Documents/blog/output"
    ServerName jerrylsu.local
    ServerAlias www.jerrylsu.local
    ErrorLog "/private/var/log/apache2/jerrylsu.local-error_log"
    CustomLog "/private/var/log/apache2/jerrylsu.local-access_log" common
</VirtualHost>

<VirtualHost *:80>
    ServerAdmin webmaster@isso.jerrylsu.local
    DocumentRoot "/Users/jerry/Documents/blog/isso"
    ServerName isso.jerrylsu.local

    ProxyRequests off

    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>

    <Location />
        ProxyPass http://localhost:8280/
        ProxyPassReverse http://localhost:8280/
    </Location>

    ErrorLog "/private/var/log/apache2/isso.jerrylsu.local-error_log"
    CustomLog "/private/var/log/apache2/isso.jerrylsu.local-access_log" common
</VirtualHost>
```
