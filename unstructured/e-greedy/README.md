
# E-Greedy Algorithm
Features:
1. Explore Exploit unstructured algorithm , which does not need the knowledge of time horizon T as observed in ETC alg.
2. Initially one round of round robin -  at time t, choice at random with probability ϵ_t. If success, explore , if not exploit based on estimates available. 


Limitations:
1. Dependence of suboptimality gap is still present.
2. Regret for A > 2 is not optimal

# Parameters

Intuition - log n dependence observed in paramter m of ETC algorithm is eliminated by choice of ϵ_t. As in Harmonic series - the explore phase diminishes with time eventually requring log n samples.


$$
\epsilon = min(1, ck/t\delta_{min}^2)
$$



# Regret analysis

$$
R_n = C \sum_{i=1}^k (\delta_i + (\delta_i/\delta_{min}^2) ln .max(e,n\delta_{min}^2/k))
$$

For 2 arms, nice logarithmic regret
$$
Rn \leq C + ln(n)
$$

However for more than 2 arms , R_n as seen in the equation would give much higher regret (Intuition - alg spend more time on unlikely arms , increasing the regret)

