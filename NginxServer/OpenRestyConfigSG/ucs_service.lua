local http = require "resty.http"
local cjson = require("cjson")
local request_method = ngx.var.request_method

body = "&api=" .. ngx.var.uri

local httpc = http.new()
ok, err = httpc:connect("127.0.0.1", 12018)

if not ok then
    ngx.say("lua auth ... connect to local server failed.", err)
    return
end

local res, err = httpc:request_uri("http://127.0.0.1:12018/secondary_income/get_path", {
    method = "POST",
    body = body,
    headers = {
        ["Content-Type"] = "application/x-www-form-urlencoded",
    }
})


if not res then
    ngx.say("failed to request: ", err)
    return
end

--ngx.log(ngx.ERR, res.body)
--ngx.say(res.body)
local ret = cjson.decode(res.body)
--ngx.var.file_path = ret.file_path
--ngx.say(ret.result.file_path)
ngx.exec('/__znc9zkej/' .. ret.result.file_path) 
