using Agents, BenchmarkTools
@agent struct ReflexiveAgent(NoSpaceAgent)
    b::Float64
end

function init_model(N)
    model = StandardABM(ReflexiveAgent; agent_step! = (agent, model) -> begin
        # reflexive update: b = 0.5*randn + 0.3*mean(all b) + 0.2*b_prev
        # simplified mean field
        mean_b = mean([a.b for a in allagents(model)])
        agent.b = 0.5*randn() + 0.3*mean_b + 0.2*agent.b
    end, properties=Dict(:x=>0.0))
    for i in 1:N
        add_agent!(model, 0.0)
    end
    model
end

# Fallback pure Julia if Agents not available
function bench_pure(N,T)
    b = zeros(Float64,N)
    x=0.0
    rng = MersenneTwister(42)
    t0=time()
    for t in 1:T
        s = x .+ randn(rng,N)*0.5
        b_prev=copy(b)
        mean_b=mean(b)
        for i in 1:N
            b[i]=0.5*s[i]+0.3*mean_b+0.2*b_prev[i]
        end
        mean_a=mean(b)*0.5
        x=0.70*x+0.30*mean_a+randn(rng)*0.1
    end
    time()-t0
end

# Benchmark
for N in [1000,10000]
    for T in [100]
        try
            model = init_model(N)
            t = @belapsed step!($model, 100)
            println("Agents.jl N=$N T=$T -> $(round(t,digits=4))s (BenchmarkTools step!)")
        catch e
            dt = bench_pure(N,T)
            println("Pure Julia fallback N=$N T=$T -> $(round(dt,digits=4))s  fallback: $e")
        end
    end
end
