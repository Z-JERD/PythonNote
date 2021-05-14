# OpenResty：

    参考文档安装：
    
        https://www.cnblogs.com/zlslch/p/10318884.html
        
    nginx与lua的执行顺序和步骤说明：
    
        https://blog.csdn.net/chupu1940/article/details/100616256?utm_source=app&app_version=4.6.1
    
    OpenResty高并发测试：
    
        https://blog.csdn.net/lupengfei1009/article/details/86062644
        
## OpenResty启动：
    
    openresty默认安装位置:
        /usr/local/openresty
    
    启动 openresty：
        
        systemctl start openresty.service
        
    重新启动 openresty：
    
        systemctl restart openresty.service
        
    关闭 openresty:
        
        systemctl stop openresty.service
    
    
    set_by_lua_file
        
        lua中使用http请求需要在lualib/resty/添加以下文件：
            http.lua和http_headers.lua
        
    http请求的文件中不能用：set_by_lua_file
    
    请求接口返回值：
        
            '{"status": 200, "result": {"file_path": "/stm/20200804162922.jpg"}}'
