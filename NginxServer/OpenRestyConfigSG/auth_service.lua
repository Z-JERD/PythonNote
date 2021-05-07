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

--local mod = string_split(ngx.var.uri, "/")[1]
--ngx.say("hello:"..mod)

ngx.var.mod = string_split(ngx.var.uri, "/")[1]
--ngx.say("hello:"..ngx.var.mod)
--ngx.exec("@process")
