## Nginx基本配置

    参考文档：https://blog.csdn.net/qq_36564503/article/details/105166112

### 1. 改配置文件nginx.conf 

    写入如下配置：

        upstream s14django {   
                #池子中存放2个服务器，默认轮训方式调度服务器
                server 192.168.12.38:8000; 
                server 192.168.12.67:8000;
            }

       
        server {
               
                listen 80;
               server_name  www.s14huoying.com;
                
                location / {
              
                  #当请求发送到www.s14huoying.com的时候，匹配到 /  ，就执行以下代码
                  proxy_pass http://s14django;
              
                  #这个proxy_params文件创建在/opt/nginx1-12/conf底下
             
                 include proxy_params;
        }

### 2. 手动创建这个参数文件

    touch /opt/nginx1-12/conf/proxy_params      写入信息

        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 
        proxy_connect_timeout 30;
        proxy_send_timeout 60;
        proxy_read_timeout 60;
 
        proxy_buffering on;
        proxy_buffer_size 32k;
        proxy_buffers 4 128k;

    重启Nginx


## Nginx负载均衡策略

    
    参考文档：https://blog.csdn.net/qq_35119422/article/details/81505732

    Nginx的upstream目前支持：
        
        轮询策略
        
        权重轮询策略
        
        ip_hash策略
        
        fair策略
        
        url_hash策略
        
        sticky策略


### 1. 轮询策略（默认）

    每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。

    EX: 当前端有多个请求到后端服务器节点，服务会被轮流分配到下面三个服务器
    
    upstream backserver {
      
        server 172.31.3.82:9170;

        server 172.31.3.82:9171;

        server 172.31.3.82:9173;
    }

### 2. 加权轮询策略

    在基本的轮询策略基础上, 指定各后端服务器节点被轮询到的机率，主要应用于后端服务器节点性能不均的情况

    EX:

    这三个后端服务器被访问的比率是1:3:2，即server172.31.3.82:9171被访问的机率最高，server172.31.3.82:9171次之，server172.31.3.82:9170访问的机率最小

    upstream backserver {
        
        server 172.31.3.82:9170;

        server 172.31.3.82:9171  weight=3;

        server 172.31.3.82:9173  weight=2;

    }

### 3. ip_hash策略

    将前端的访问IP进行hash操作，然后根据hash结果将请求分配到不同的后端服务器节点。这样会使得每个前端访问IP会固定访问一个后端服务器节点

    EX:  在配置upstream中添加ip_hash一行

        upstream  backserver{
                
                ip_hash;

                server 172.31.3.82:9170;

                server 172.31.3.82:9171;

                server 172.31.3.82:9173;

        }

    EX2: ip_hash 可以和加权轮询一起使用

    upstream backserver {
    
        ip_hash;

        server 172.31.3.82:9170;

        server 172.31.3.82:9171  weight=3;

        server 172.31.3.82:9173  weight=2;
   }



### 4. url_hash策略

    按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器  

    upstream  backserver {
       
       hash $request_uri;
       
       hash_method crc32; 

       server 192.168.244.1:8080;

       server192.168.244.2:8080;

       server 192.168.244.3:8080;

       server 192.168.244.4:8080;

    }

### 5. fair

    按后端服务器的响应时间来分配请求，响应时间短的优先分配

    upstream backserver { 
        
        server server1; 
        
        server server2; 
        
        fair; 
    } 


### 6. Sticky策略
    
    该策略在多台服务器的环境下，为了确保一个客户端只和一台服务器通讯，它会保持长连接，并在结束会话后再次选择一个服务器，保证了压力均衡 

    upstream  backserver {
        
        sticky;

        server 172.31.3.82:9170;

        server 172.31.3.82:9171;

        server 172.31.3.82:9173;

    } 
