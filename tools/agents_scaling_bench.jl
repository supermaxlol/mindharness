using Random, Statistics, Dates
println("=== Agents.jl Scaling Benchmark Reflexive CAS ===")
println("Julia ", VERSION, "  ", now())

function bench_julia(N, T; seed=42)
    rng = MersenneTwister(seed)
    b = zeros(Float64, N)
    x = 0.0
    t0 = time()
    for t in 1:T
        s = x .+ randn(rng, N) * 0.5
        b_prev = copy(b)
        mean_b = mean(b)
        @inbounds for i in 1:N
            b[i] = 0.5*s[i] + 0.3*mean_b + 0.2*b_prev[i]
        end
        mean_a = mean(b) * 0.5
        x = 0.70*x + 0.30*mean_a + randn(rng)*0.1
    end
    dt = time() - t0
    return dt, x
end

agents_available = false
agents_version = "not installed"
try
    using Pkg
    global agents_available, agents_version
    deps = Pkg.dependencies()
    for (uuid, dep) in deps
        if dep.name == "Agents"
            global agents_version = string(dep.version)
            global agents_available = true
            break
        end
    end
catch e
    println("Pkg check failed: $e")
end
println("Agents.jl available: $agents_available version: $agents_version")

println("\nWarming up...")
bench_julia(100, 10)

results = Dict{String,Float64}()
for (N,T) in [(1000,100), (10000,100), (1000,1000), (10000,1000)]
    GC.gc()
    dt, x = bench_julia(N,T)
    println("Julia pure N=$N T=$T -> $(round(dt, digits=4))s  final_x=$(round(x,digits=3))")
    results["$(N)_$(T)"] = dt
end

open("/tmp/agents_bench.json","w") do f
    println(f, "{")
    println(f, "  \"julia_version\": \"$(VERSION)\",")
    println(f, "  \"agents_version\": \"$agents_version\",")
    println(f, "  \"agents_available\": $agents_available,")
    for (k,v) in results
        println(f, "  \"$k\": $v,")
    end
    println(f, "  \"timestamp\": \"$(now())\"")
    println(f, "}")
end
println("Wrote /tmp/agents_bench.json")
