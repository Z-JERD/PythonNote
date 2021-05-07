gmp = require 'resty.gmp' ('libgmp')
local yaml = require "resty.tinyyaml"
local open = io.open

local function read_file(path)
    local file = open(path, "rb") -- r read mode and b binary mode
    if not file then return nil end
    local content = file:read "*a" -- *a or *all reads the whole file
    file:close()
    return content
end

local fileContent = read_file("/etc/hyjh/hxsto.yaml");

local doc = yaml.parse(fileContent)

apkpath = doc['apkpath']
stopath = doc['stopath']
rsa_e = tostring(doc['rsakey']['e'])
rsa_n = tostring(doc['rsakey']['n'])

--ngx.log(ngx.ERR, rsa_e, rsa_n)
