using Base.Filesystem
using HTTP

function ping(addr::String)
    try
        resp = HTTP.request("GET", addr)
        return resp.status == 200
    catch e
        return false
    end
end

function mirrors_check_available()
    pm_path = joinpath(homedir(), raw".julia\packages\PkgMirrors")
    pm_path = joinpath(pm_path, readdir(pm_path)[1])
    mirror_list = joinpath(pm_path, raw"data\mirror_list.txt")
    cache_curr = joinpath(pm_path, raw"cache\current.txt")

    open(mirror_list, "r") do io
        mirrors = split(read(io, String), "\n")
        flag = false
        global nameaddr
        for outer nameaddr in mirrors
            nameaddr = rstrip(nameaddr)
            info = split(nameaddr, " ")
            if length(info) == 2 && ping(String(info[2]))
                flag = true
                break
            end
        end
    end

    open(cache_curr, "w") do io
        write(io, nameaddr * "\n")
    end
end

mirrors_check_available()
using PkgMirrors