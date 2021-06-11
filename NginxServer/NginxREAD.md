# Nginx参考文档：https://zhuanlan.zhihu.com/p/362701011

# Nginx安装

## Nginx命令:

    1. 安装Nginx：默认安装在/etc/nginx目录下

        yum -y install nginx


    2. 开机配置
        
        systemctl enable nginx                  # 开机自动启动
        
        systemctl disable nginx                 # 关闭开机自动启动

    3. 启动Nginx

        systemctl start nginx 

    4. 停止Nginx
        
        systemctl stop nginx

    5. 重启Nginx
        
        systemctl restart nginx

    6. 重新加载Nginx
        
        systemctl reload nginx

    7. 查看 Nginx 运行状态
        
        systemctl status nginx

    8. 检查配置文件有没有问题
        
        /usr/sbin/nginx -t

## 启动Nginx报错：

    connect() to 127.0.0.1:8001 failed (13: Permission denied)

    解决方法：
        
        1.查看SELinux状态：
            
            /usr/sbin/sestatus -v ##如果SELinux status参数为enabled即为开启状态
            
            getenforce ##也可以检查
            
            SELinux status: enabled

        
        2.关闭SELinux：
            
            1、临时关闭（不用重启机器）：
            
                setenforce 0 ##设置SELinux 成为permissive模式
                
                ##setenforce 1 设置SELinux 成为enforcing模式
            
            2、修改配置文件需要重启机器：
            
                修改/etc/selinux/config 文件
                
                将SELINUX=enforcing改为SELINUX=disabled

# Nginx 核心配置

## 配置文件结构:
    # main段配置信息
    user  nginx;                        # 运行用户，默认即是nginx，可以不进行设置
    worker_processes  auto;             # Nginx 进程数，一般设置为和 CPU 核数一样
    error_log  /var/log/nginx/error.log warn;   # Nginx 的错误日志存放目录
    pid        /var/run/nginx.pid;      # Nginx 服务启动时的 pid 存放位置

    # events段配置信息
    events {
        use epoll;     # 使用epoll的I/O模型(如果你不知道Nginx该使用哪种轮询方法，会自动选择一个最适合你操作系统的)
        worker_connections 1024;   # 每个进程允许最大并发数
    }

    # http段配置信息
    # 配置使用最频繁的部分，代理、缓存、日志定义等绝大多数功能和第三方模块的配置都在这里设置
    http { 
        # 设置日志模式
        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

        access_log  /var/log/nginx/access.log  main;   # Nginx访问日志存放位置

        sendfile            on;   # 开启高效传输模式
        tcp_nopush          on;   # 减少网络报文段的数量
        tcp_nodelay         on;
        keepalive_timeout   65;   # 保持连接的时间，也叫超时时间，单位秒
        types_hash_max_size 2048;

        include             /etc/nginx/mime.types;      # 文件扩展名与类型映射表
        default_type        application/octet-stream;   # 默认文件类型

        include /etc/nginx/conf.d/*.conf;   # 加载子配置项
        
        # server段配置信息
        server {
        listen       80;       # 配置监听的端口
        server_name  localhost;    # 配置的域名
        
        # location段配置信息
        location / {
        root   /usr/share/nginx/html;  # 网站根目录
        index  index.html index.htm;   # 默认首页文件
        deny 172.168.22.11;   # 禁止访问的ip地址，可以为all
        allow 172.168.33.44；# 允许访问的ip地址，可以为all
        }
        
        error_page 500 502 503 504 /50x.html;  # 默认50x对应的访问页面
        error_page 400 404 error.html;   # 同上
        }
    }

## 各部分功能:

    main 全局配置，对全局生效；
    
    events 配置影响 Nginx 服务器与用户的网络连接；
    
    http 配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置；
    
    server 配置虚拟主机的相关参数，一个 http 块中可以有多个 server 块；

    location 用于配置匹配的 uri ；

    upstream 配置后端服务器具体地址，负载均衡配置不可或缺的部分；


# 指定静态资源目录位置

## root：会将定义路径与 URI 叠加
    
    可以写在 http 、 server 、 location 等配置中

    EX:

        location /seatmap/ {
            root /root/static/;
        }

        当用户访问 www.test.com/seatmap/980416d26e.png 时，实际在服务器找的路径是：/root/static/seatmap/980416d26e.png

## alias：只取定义路径

    它只能写在 location 中

     EX:

        location /seatmap/ {
            
            alias /root/static/;
        }

        当用户访问 www.test.com/seatmap/980416d26e.png 时，实际在服务器找的路径是：/root/static/980416d26e.png

        使用 alias 末尾一定要添加 / ，并且它只能位于 location 中

##  autoindex: 列出目录结构

    列出指定目录下的文件, 同时也可是使用alias

    EX: /root/static/stm 文件下所有的内容。默认以bytes显示出⽂件的确切⼤⼩

        location /stm/ {

                root  /root/static;
                autoindex on;
        }

    EX: 修改配置

        location /stm/ {

                root  /root/static;
                autoindex on; # 打开 autoindex，，可选参数有 on | off
                autoindex_exact_size off; # 修改为off，以KB、MB、GB显示文件大小，默认为on，以bytes显示出⽂件的确切⼤⼩
                autoindex_format html; # 以html的方式进行格式化，可选参数有 html | json | xml
                autoindex_localtime on; # 显示的⽂件时间为⽂件的服务器时间。默认为off，显示的⽂件时间为GMT时间
                }



# location 中的反斜线
    
    location /test {
    ...
    }

    
    location /test/ {
    ...
    }

    
    如果不带 / 的话,nginx默认还是认为test是一个文件目录,它会去找test这个文件夹(一定是文件夹);如果找不到test这个文件夹的话,nginx会去找test这个文件,如果这个文件存在,nginx会直接返回test这个文件中的内容;

    如果URL末尾中带 / nginx在处理的时候会直接将test作为一个目录, test这个文件夹不存在,直接返回404


# Nginx IP 访问限制配置:
    
    参考文档：https://www.zhangbj.com/p/26.html

    allow 同意ip访问
    deny  限制ip访问

## 屏蔽IP

    屏蔽所有 IP 访问:
    
        deny all
        
    允许所有 IP 访问:
    
        allow all
    
    限制单个IP：
        
        192.168.1.100 不能访问Nginx代理的9000端口
        
        server {
                    listen       9000;
                    server_name  localhost;
                    deny 192.168.1.100；
                }
                
    除了几个 IP 外，其他全部拒绝:
    
        server {
                    listen       9000;
                    server_name  localhost;
                    allow 1.1.1.1;
                    allow 1.1.1.2;
                    deny all;
                }
    
    屏蔽整个段:
        
        deny 123.0.0.0/8                # 123.0.0.1 -- 123.255.255.254
        
    屏蔽 IP 段:
    
        deny 124.45.0.0/16             #  123.45.0.1 -- 123.45.255.254
        
        deny 123.45.6.0/24             #  123.45.6.1 -- 123.45.6.254

## 配置：
    
    http 语句块：   所有网站屏蔽 IP
        
        http {
            deny 1.1.1.1;
            allow all;
        }
    
    server 语句块：  单独网站屏蔽 IP
        
        server {
            allow 127.0.0.1;
            deny all;
        }
    
    location 语句块： URL屏蔽 IP
        
        location / {
            deny 123.0.0.0/8
        }
