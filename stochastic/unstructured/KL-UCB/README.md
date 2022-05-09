
# KL-UCB Algorithm
Features:
1. Uses relative entropy/KL Divergence to bump up the confidence boost.
   More fine grained optimistic algorithm.
2. In the case of Bernouli distrubution, the regret scales better compared to UCB.





KL-UCB index function (InFinite horizon)
$$
U_j(t-1) = max ( \mu_j\in[0,1] d(\mu_j(t-1),\mu^{-})) \leq ln f(t)/T_j(t-1)
$$

Intuition - Finds the optimistic best sample with higher probability whose KL divergence is bounded inversly proportional to number of samples(As samples are large, confidence increse, samples less, confidence small)




# Regret analysis
TODO