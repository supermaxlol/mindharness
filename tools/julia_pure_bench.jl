using Random, Statistics, Dates
println("Julia ", VERSION, " ", now())
function bench_julia(N,T; seed=42)
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
        mean_a = mean(b)*0.5
        x = 0.70*x + 0.30*mean_a + randn(rng)*0.1
    end
    time()-t0, x
end
println("warmup")
bench_julia(100,10)
for (N,T) in [(1000,100),(10000,100),(1000,1000),(10000,1000)]
    GC.gc()
    dt, x = bench_julia(N,T)
    println("N=$N T=$T -> $(round(dt,digits=4))s")
end
