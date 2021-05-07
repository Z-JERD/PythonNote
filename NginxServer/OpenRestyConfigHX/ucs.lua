local ori_img_id = ngx.var.fcode
-- for random suffix
ori_img_id = string.sub(ori_img_id, 1, string.len(ori_img_id) - 4)

--ngx.say('ori_img_id: ', ori_img_id)

local mpz=gmp.types.z
local img_id, e, n = mpz(), mpz(), mpz()
gmp.z_init_set_str(img_id, ori_img_id, 36)
gmp.z_init_set_str(e, ngx.var.rsa_e, 10)
gmp.z_init_set_str(n, ngx.var.rsa_n, 10)
gmp.z_powm(img_id, img_id, e, n)
-- print(gmp.luasprintf('%Zd', img_id))

local path = ''
local str_img_id = gmp.luasprintf('%Zd', img_id)
local idx = 0

--ngx.say('str_img_id: ', str_img_id)

-- last 3 not need
str_img_id = string.sub(str_img_id, 1, string.len(str_img_id) - 3)
while( string.len(str_img_id) > 3 ) do
    path = string.sub(str_img_id, string.len(str_img_id) - 2, string.len(str_img_id)) .. '/' .. path
    idx = idx + 1
    str_img_id = string.sub(str_img_id, 1, string.len(str_img_id) - 3)
end

if string.len(str_img_id) > 0 then
    path = str_img_id .. '/' .. path
    idx = idx + 1
end

local rqs = ''
if ngx.var.arg_filename then
    rqs = '?filename=' .. ngx.var.arg_filename
end

path = tostring(idx) .. '/' .. path
ngx.exec('/__znc9zkej/' .. ngx.var.catalog .. '/' .. ngx.var.form .. '/' .. path .. ngx.var.fcode .. '.' .. ngx.var.fext .. rqs)

return
