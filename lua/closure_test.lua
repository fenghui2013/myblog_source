function f1(n)
    local function f2()
        n = n + 1
        print(n)
    end
    return f2
end

f1(2017)()
