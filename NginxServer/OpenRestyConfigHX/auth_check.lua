function quote_char(c)
    return string.format("%%%02X", string.byte(c))
end

function url_quote(s, quote_plus)
    if type(s) ~= "string" then
        return s
    end

    s = s:gsub("\n", "\r\n")
    s = s:gsub("([^A-Za-z0-9 %-_%./])", quote_char)
    if quote_plus then
        s = s:gsub(" ", "+")
        s = s:gsub("/", quote_char)
    else
        s = s:gsub(" ", "%%20")
    end

    return s
end

function string_split(str, split_char)
    local sub_str_tab = {};
    while (true) do
        local pos = string.find(str, split_char);
        if (not pos) then
            sub_str_tab[#sub_str_tab + 1] = str;
            break;
        end
        local sub_str = string.sub(str, 1, pos - 1);

        if sub_str ~= "" then
            sub_str_tab[#sub_str_tab + 1] = sub_str;
        end

        str = string.sub(str, pos + 1, #str);
    end
 
    return sub_str_tab;
end

function nil2emptystr( v )
    if v == nil then
        return ""
    end
    return v
end

local http = require "resty.http"
local cjson = require("cjson")
local request_method = ngx.var.request_method



--uri_pathes = string_split(ngx.var.uri, "/")
--local mod = uri_pathes[1]
--local method = uri_pathes[2]

body = "remote_addr=" .. nil2emptystr(ngx.var["remote_addr"]) ..
       "&cookie_auth=" .. nil2emptystr(ngx.var["cookie___Secure-HYJH"]) ..
       "&header_auth=" .. nil2emptystr(ngx.var["http_authorization"]) ..
       "&cert_subject_dn=" .. url_quote( nil2emptystr(ngx.var["ssl_client_s_dn"]) ) ..
       "&cert_issuer_dn=" .. url_quote( nil2emptystr(ngx.var["ssl_client_i_dn"]) ) ..
       "&cert_thumbprint=" .. url_quote( nil2emptystr(ngx.var["ssl_client_fingerprint"]) ) ..
       "&role=" .. url_quote( nil2emptystr( ngx.req.get_uri_args()["_role"] ) ) ..
       "&api=" .. url_quote( ngx.var.uri )
--       "&mod=" .. url_quote( nil2emptystr( mod ) ) ..
--       "&method=" .. url_quote( nil2emptystr( method ) )
-- request http
local httpc = http.new()
ok, err = httpc:connect("127.0.0.1", 12018)

if not ok then
    ngx.say("lua auth ... connect to local server failed.", err)
    return
end

local res, err = httpc:request_uri("http://127.0.0.1:12018/inner/sasl/acl_gateway", {
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
local ret = cjson.decode(res.body)
--ngx.say(ret.auth)

if ret.auth then
    ngx.var.mod = ret.mod
    ngx.var.session = ret.session
    ngx.var.srv_addr = ret.srv_addr

    local pptbl = {}
    pptbl["jws"]="http://10.110.20.15:18095"
    pptbl["j-bpms"]="http://10.110.20.15:18092"
    ngx.var.ppaddr = pptbl[ngx.var.mod]

    --if ret.srv_mode == 2 then
    if ngx.var.ppaddr then
        ngx.exec("@remote")
    else
        ngx.exec("@process")
    end
else
    --ngx.status = 403
    if ret.status then
        ngx.status = ret.status
    else
        ngx.status = 403
    end

    if ngx.status == 401 then
        ngx.header['WWW-Authenticate'] = 'HYJH passport'
    end
    
    ngx.header['Access-Control-Allow-Methods'] = 'POST, OPTIONS, HEAD, GET'
    ngx.header['Access-Control-Allow-Credentials'] = 'true'
    ngx.header['Access-Control-Allow-Headers'] = 'Origin, Accept-Language, Accept-Encoding, X-Forwarded-For, Connection, Accept, User-Agent, Host, Referer, Cookie, Content-Type, Cache-Control, *'
    if ngx.var['http_origin'] then
        ngx.header['Access-Control-Allow-Origin'] = ngx.var['http_origin']
    else
        ngx.header['Access-Control-Allow-Origin'] = '*'
    end
    ngx.say('{"error":"'  .. ret.reason .. '", "status":' .. ngx.status .. ', "id":null}')
    ngx.exit(ngx.status)

end

return
