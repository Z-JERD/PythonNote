## Windows清除C盘
  
   【C:\Windows\SoftwareDistribution\Download】，我们只需要进入该目录，将里面的垃圾直接删除，就可以省下很多空间。

	另外，我们还可以清理下软件的缓存数据，具体路径是在【C:\Users\个人用户名\AppData\Local\Temp


## VirtualBox下安装CentOS7系统
    
	https://www.cnblogs.com/hihtml5/p/8217062.html
    
## CentOS 7下Samba服务器的安装与配置
	
	https://www.cnblogs.com/muscleape/p/6385583.html
	
### smb.conf
	[global]
		workgroup = SAMBA
		security = user

		passdb backend = tdbsam

		printing = cups
		printcap name = cups
		load printers = yes
		cups options = raw

	[share]
		comment = shared directories
		path = /share/local/%u
		browseable = yes
		writable = yes
		read only = no
		valid users = @uap
		invalid users = uap
    
# Linux基本操作命令
### 查看当前系统的版本和内核：
        1.版本信息
            [root@99 zhaoguangfei]# cat /etc/centos-release

        2.内核信息：
            [root@99 zhaoguangfei]# uname -r 
            
### centos7没有ifconfig命令：
      [root@99 zhaoguangfei]# yum search ifconfig
        显示： net-tools.x86_64 ：Basic networkin tools
      安装：
         yum install net-tools.x86_64
     或者使用 ip addr 查询ip信息
     
     
     
### 查看端口：
    
	netstat -tunlp | grep 80
            
### rpm查看安装的软件：
   
	rpm -qa     查看全部的软件
    
	rpm -qa     软件名 例：[root@99 zhaoguangfei]# rpm -qa lrzsz 
    
### 安装rzsz：
    
	yum -y install lrzsz
        
		windows ===== >  linux    上传    rz 
        
		linux   ===== >  windows  下载    sz 
        
### 显示目录或文件的大小：
     
	 1.du 显示指定的目录或文件所占用的磁盘空间
    
          [root@99 zhaoguangfei]# du            只显示当前目录下面的子目录的目录大小和当前目录的总的大小，最下面的为当前目录的总大小
          [root@99 zhaoguangfei]# du -h test    方便阅读的格式显示test目录各文件所占空间情况
          du -sh [目录/文件名]                  返回该目录/文件的总大小
          du -sh ./* 　　                       统计当前目录各文件夹总大小
          
     2.df
        df -hl              查看磁盘剩余空间
        df -h               查看每个根路径的分区大小
        sudo fdisk -l       查看硬盘的分区 
     
	 3.free -h 　           查看内存大小
  
 
### Linux 系统中查找最大的前 10 个文件
    find / -type f -print0 | xargs -0 du -h | sort -rh | head -n 10

        find：在目录结构中搜索文件的命令
        /：在整个系统（从根目录开始）中查找
        -type：指定文件类型
        f：普通文件
        -print0：在标准输出显示完整的文件名，其后跟一个空字符（null）
        |：控制操作符，将一条命令的输出传递给下一个命令以供进一步处理
        xargs：将标准输入转换成命令行参数的命令
        -0：以空字符（null）而不是空白字符（LCTT 译者注：即空格、制表符和换行）来分割记录
        du -h：以可读格式计算磁盘空间使用情况的命令
        sort：对文本文件进行排序的命令
        -r：反转结果
        -h：用可读格式打印输出
        head：输出文件开头部分的命令
        n -10：打印前 10 个文件
    
    找出当前目录下大于1M的文件
        find . -type f -size +1000k  -print0 | xargs -0 du -h | sort -rh



    
### 文件的查找命令：which/whereis/locate/find

    1.which
        which命令的作用是，在PATH变量指定的路径中，搜索某个系统命令的位置
        [root@virtue ~]# which cd
            /usr/bin/菜刀
    2.whereis	查看可执行文件的位置及相关文件
        whereis命令只能用于程序名的搜索，而且只搜索二进制文件（参数-b）、man说明文件（参数-m）和源代码文件（参数-s）
        1.查找二进制文件
            [root@virtue ~]# whereis -b git
            git: /usr/bin/git
            
        2.查找帮助文件
            [root@virtue ~]# whereis -m git
            git: /usr/握手/man/man1/git.1.gz
            
        3.普通查找
            [root@virtue ~]# whereis svn
            svn:
            [root@virtue ~]# whereis git
            git: /usr/bin/git /usr/握手/man/man1/git.1.gz
            
    3. locate
        locate可以快速的找到文件的位置，因为locate查找的是数据库的文件来确定文件的位置
        1.普通查找
            查找内容: /etc下有以sh开头的文件
            [root@virtue ~]# locate /etc/sh
            /etc/shadow
            /etc/shadow-
            /etc/shells
        2.手动更新数据库
            [root@virtue ~]# updatedb
    4.find
        Linux下find命令在目录结构中搜索文件，并执行指定的操作。
        1.按名称查找
            find / -name filename
            find / -name "demo.py" 
            find . -name "*.txt"       在当前目录及子目录中查找所有的*.txt文件
            find /etc -name "host*"    在/etc目录中查找文件名以host开头的文件
            
        2.按权限查找
            find -perm 755              在当前目录下查找文件权限位为755的文件 
        3.查找子目录
            find / -depth -name "CON.FILE"    首先匹配所有的文件然后再进入子目录中查找
            
        4.按时间查找
            用减号-来限定更改时间在距今n日以内的文件
            用加号+来限定更改时间在距今n日以前的文件
            
            在系统/root目录下查找更改时间在5日以内的文件
                find /root -mtime -5 -print
                
        5.按类型查找
            类型	说明
            -type b	查找块设备
            -type d	查找目录
            -type c	查找字符设备文件
            -type p	查找管道文件
            -type l	查找符号链接文件
            -type f	查找普通文件
            
            在/etc目录下查找所有的目录
                find /etc -type d
                
        6.按文件大小查找
         find . -type f -size +1000k


# 安装MySQL5.7

    1.添加mysql源
        # rpm -Uvh http://repo.mysql.com//mysql57-community-release-el7-7.noarch.rpm
    2.安装mysql
        # yum -y install mysql-community-server
    3.启动mysql并设置为开机自启动服务
        # chkconfig mysqld on
        # service mysqld start
    4.检查mysql服务状态
        # service mysqld status
## 密码设置    
    第一次启动mysql，会在日志文件中生成root用户的一个随机密码，使用下面命令查看该密码
        # grep 'temporary password' /var/log/mysqld.log
    设置新密码：
        mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
        如果出现：
            Your password does not satisfy the current policy requirements
            原因：密码过于简单，更改密码策略
            mysql> set global validate_password_policy=0;
            mysql> set global validate_password_length=4;
    
    MySQL数据库文件在/var/lib/mysql  配置文件在/etc/my.cnf


## Centos7中设置MySQL授权远程登录
    1.mysql> use mysql
    2.mysql> grant all privileges on *.* to 'root'@'%' identified by '12345';
             使用root:12345来外部访问
    3.刷新权限:
        mysql> flush privileges;
    4.开放端口
        [root@localhost /]# vim /etc/sysconfig/iptables-config 
            添加一下内容：
                -A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT
    5.关闭防火墙：
        systemctl stop firewalld.service
        禁止firewall开机启动：systemctl disable firewalld.service 

## MySQL服务相关命令   
    启动、关闭、重启、查看MySQL服务
    # service mysqld start      启动命令
    # service mysqld stop       关闭命令
    # service mysqld status     查看服务状态
    # service mysqld restart    重启命令
    
## Linux中登录MySQL数据库
### 1.简洁登录 只登录本服务器的MySQL
    mysql -uroot -p
    
### 2.登录其他服务器上的MySQL
    mysql -hlocalhost -uroot -p -P3306
    
    -h数据库主库
    -u用户
    -p密码
    -P端口号（大写P）
    
    例如：mysql -h127.0.0.1 -uroot -p123456 -P3306
          PS:-p密码部分，可以直接指定密码，如果不指定，会提示输入密码
    登录其他服务器：
           mysql -h10.110.1.90 -uphp -p -P3307

    

# 安装Redis及设置密码
    
	参考文档：https://www.cnblogs.com/rslai/p/8249812.html
	1. yum install epel-release
		若失败:
			yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
	2.安装 Redis ： yum install redis 
	
	3.启动 redis ：
		 启动redis：service redis start
		 停止redis：service redis stop
		 查看redis运行状态：service redis status
		 查看redis进程：ps -ef | grep redis
	
	4.设置开机自动启动：chkconfig redis on 
	
	5.开放端口： firewall-cmd –zone=public –add-port=6379/tcp –permanent 
	
	6.应用防火墙设置：firewall-cmd –reload 
	
	7.配置远程连接及修改密码： 
	(1).找到redis.conf配置文件的位置： whereis redis.config 
	(2)如在etc/redis.conf，就进入etc目录：vim /etc/redis.conf 
		找到下面这一行bind 127.0.0.1 
		注释成 #bind 127.0.0.1（这样就能监听所有的IP地址）
		protected-mode 要设置成no
	(3)设置密码
		找到下面这一行#requirepass foobared，去掉注释，并修改密码, 
		requirepass dulixing（这样登录Redis的密码就更改为dulixing了） 


    源码安装redis：	
        https://www.cnblogs.com/stulzq/p/9288401.html
    
    Centos7 执行firewall-cmd报错“ModuleNotFoundError: No module named 'gi'”
        https://www.cnblogs.com/vixiaode/p/9939104.html
    
    
    
# CentOS 7 Python3.6和Pip3

    参考文档：http://www.opsroad.com/1352.html
    
    1、安装依赖环境
        yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

    2、下载Python3

        mkdir -p /application/tools/
        
        cd /application/tools/

        wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
    3、安装python3
        创建目录：
        mkdir -p /usr/local/python3
        
        解压下载好的Python-3.x.x.tgz包
        tar -xvf Python-3.6.5.tgz 

    4.进入解压后的目录，编译安装
            cd Python-3.6.5
            ./configure --prefix=/usr/local/python3
            
            make && make install

    5.建立python3 和 pip3的软链
            rm -fr /usr/bin/python
        
            ln -s /usr/local/python3/bin/python3 /usr/bin/python
            
            rm -fr /usr/bin/pip
            
            ln -s /usr/local/python3/bin/pip3 /usr/bin/pip

## 检查Python3及pip3是否正常可用：
    [root@beatz bin]# python -V
        Python 3.6.5
    [root@beatz bin]# pip -V
        pip 9.0.3 from /usr/local/python3/lib/python3.6/site-packages (python 3.6)
        
## 创建虚拟环境：
    1.安装：
        pip install virtualenv 
    
    2.查看virtualenv的位置：
        find / -name 'virtualenv.py'
        
        #/usr/local/python3/lib/python3.6/site-packages/virtualenv.py
    
    3.当前目录下新建虚拟环境：
        [root@localhost ~]# python /usr/local/python3/lib/python3.6/site-packages/virtualenv.py myenv
        
   
   
# linux根分区满了怎么办?
## 通过命令查找根分区内的大文件

    1.du -sh /* 2>/dev/null | sort -hr | head -3
    
    2.如果上述命令执行后发现/var/占空间最大，那么在查找/var分区内的大文件，如：

	    du -sh /var/* 2>/dev/null | sort -hr | head -3

## Linux 下清理系统缓存并释放内存
	sync
	echo 3 > /proc/sys/vm/drop_caches 
	
## linux中删除目录下文件大小为0KB的文件
	find . -name "*" -type f -size 0c | xargs -n 1 rm -f

# CentOS7 yum 安装git

    使用yum命令报错：SyntaxError: invalid syntax
    
    问题出现原因： 
        yum包管理是使用python2.x写的，将python2.x升级到python3.x以后，由于python版本语法兼容性导致问题出现 
    
    解决办法： 
        修改yum配置文件，将python版本指向以前的旧版本
        
        # vi /usr/bin/yum
        #!/usr/bin/python2.7
        修改urlgrabber-ext-down文件，更改python版本
        
        # vi /usr/libexec/urlgrabber-ext-down
        #!/usr/bin/python2.7
        
    安装git：
        yum install -y git
        
    查看是否成功安装git：
        git --version
    
    配置git：
        git config --global user.name "zhaoguangfei"
        git config --global user.email "zhaoguangfei@163.com"
        查看配置是否生效：
            git config --list
       
    配置远程仓库：
        在自己的linux服务器本地生成ssh key：
            ssh-keygen -t rsa -C "zhaoguangfei@163.com"


# pycharm远程上传文件到Linux
    参考文档：https://blog.csdn.net/z_yong_cool/article/details/80716020
    
    1. 在PyCharm中打开SFTP配置面板，路径为Tools => Deployment => Configuration
    
    2. 配置Connection参数设置，填写远程服务器域名或者IP地址及用户名密码后，点击Test按钮进行连接测试，另外可以点击Autodetect按钮自动关联root path：
    
    3.配置Mappings参数设置，进行本地项目路径和远程服务器项目路径的关联：（圈红的是上传到Linux上的哪个文件下）
    
    4. 点击OK后，即可通过右键点击待操作文件进行本地、远程的Upload、Download及Sync


# 进程管理
    1.获取某个服务的进程号：
        [root@99 zhaoguangfei]# ps -ef | grep slide
        root      499783       1  0 4月19 ?       00:00:12 uwsgi -y slp.yaml:slide
        root      499790  499783  0 4月19 ?       00:01:36 uwsgi -y slp.yaml slide
        root      707362  706210  0 11:15 pts/8    00:00:00 grep --color=auto slide
        
        slide服务的PID为499783
        
    2.查看该进程的启动文件所在目录
        [root@99 zhaoguangfei]# ls -ll /proc/499783
        lrwxrwxrwx 1 root root 0 4月  22 11:11 cwd -> /home/zhaoguangfei/wsgi-slp
        cwd所指即工作目录

# Centos下Nginx操作
## nginx命令

    yum -y install nginx                安装Nginx
	systemctl start nginx               开启nginx服务
	systemctl stop nginx                停止nginx服务
	systemctl restart nginx             重启nginx服务
	nginx -t                            查看nignx服务的状态
	cat /var/log/nginx/error.log        查看错误日志

	
## Linux下如何查看定位当前正在运行的Nginx的配置文件
    1. 查看nginx的PID，以常用的80端口为例：
        [root@xiaoyuer scripts]# netstat -lntup|grep 80
        tcp        0      0 0.0.0.0:80                  0.0.0.0:*                   LISTEN      13309/nginx
     
        可以知道nginx进程是13309
    2. 通过相应的进程ID(比如：13309）查询当前运行的nginx路径：
        [root@xiaoyuer scripts]# ll /proc/13309/exe
        lrwxrwxrwx. 1 root root 0 Jun  4 19:37 /proc/10174/exe -> /usr/sbin/nginx
    
    3. 获取到nginx的执行路径后，使用-t参数即可获取该进程对应的配置文件路径，如：
        [root@localhost ~]# /usr/sbin/nginx -t
        nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
        nginx: configuration file /etc/nginx/nginx.conf test is successful
        
## Nginx和Uwsgi联合使用
	
### 1.uwsgi自定义端口号启动
	uwsgi配置文件使用yaml格式
	flask_demo.yaml
		flask_demo:
		  wsgi-file: app.py
		  socket: 127.0.0.1:8001
		  pidfile: /var/wsgi/flask_demo.pid
		  daemonize: /var/wsgi/flask_demo.log
		  
	启动服务：uwsgi -y flask_demo.yaml:flask_demo
	查看服务日志：tail -f /var/wsgi/flask_demo.log
	
	nginx配置：添加以下内容
	server {
			listen      80; 
			server_name   _;
			location / { 
				
				 include         uwsgi_params;
				 uwsgi_pass      127.0.0.1:8001;
			}  

	    } 

### 2.uwsgi定义socket文件启动
	flask_demo:
			  wsgi-file: app.py
			  socket: /var/wsgi/flask_demo.socket
			  pidfile: /var/wsgi/flask_demo.pid
			  daemonize: /var/wsgi/flask_demo.log
			  
	配置Nginx：
	server {
                        listen      9000;
                        server_name   _;
                        location / {
							 include         uwsgi_params;
							 uwsgi_pass      unix:/var/wsgi/flask_demo.socket;
                        }

            }
            
    Nginx报错：connect() to unix:/var/wsgi/flask_demo.socket failed (111: Connection refused)
    解决方案：
    	修改Nginx的配置文件 vim /etc/nginx/nginx.conf：
    	前几行的内容如下：
			user nginx;
			worker_processes auto;
			error_log /var/log/nginx/error.log;
			pid /run/nginx.pid;

    	将user nginx; 改为user root;


### 3.Nginx中一个server配置多个服务
	uwsgi配置文件
		flask_demo:
		  wsgi-file: app.py
		  socket: /var/wsgi/flask_demo.socket
		  #http: 0.0.0.0:8000
		  pidfile: /var/wsgi/flask_demo.pid
		  daemonize: /var/wsgi/flask_demo.log
	
		secondary:
		  wsgi-file: secondary.py
		  socket: /var/wsgi/secondary.socket
		  pidfile: /var/wsgi/secondary.pid
		  daemonize: /var/wsgi/secondary.log
		  
	Nginx服务配置:
		url以index开头请求发到flask_demo这个服务中
			以secondary开头的请求发到secondary这个服务中
	
		server {
					
					listen      9000; 
					server_name   _;
					location /index { 
						
						 include 	 uwsgi_params;
						 uwsgi_pass      unix:/var/wsgi/flask_demo.socket;
					}
		
					location /secondary {
										
										 include         uwsgi_params;
										 uwsgi_pass      unix:/var/wsgi/secondary.socket;
								}  
		
		
				} 



## 启动Nginx报错:
	connect() to 127.0.0.1:8001 failed (13: Permission denied)

### 解决方法：
	1.查看SELinux状态：
		/usr/sbin/sestatus -v ##如果SELinux status参数为enabled即为开启状态
		getenforce ##也可以检查
		SELinux status: enabled
		关闭SELinux：
	
	2.关闭SELinux：
		1、临时关闭（不用重启机器）：
		
		setenforce 0 ##设置SELinux 成为permissive模式
		
		##setenforce 1 设置SELinux 成为enforcing模式
		
		2、修改配置文件需要重启机器：
		
		修改/etc/selinux/config 文件
		
		将SELINUX=enforcing改为SELINUX=disabled

