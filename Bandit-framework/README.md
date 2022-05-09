# Bandit Framework Notations,Setting,Types & Regret


# Notations:

A - Action/arm

μ - Joint distribution across arms (unstructured)

π - Policy (Policy which minimizes regret)

ϵ - Environment (Set of possible distributions)

x_t - Reward at time t


<div align="center"><img style="background: white;" src=".\resultsSummary.png"></div>

# Model

1. Stochastic - Successive rewards from random selection is from same distribution , but independent. Also known as IID
2. Adversarial -  Non stochastic/random. Adversary chooses reward.

# Setting:

1. Unstructured - Arms donot share info. μ - joint distribution
2. Structured - Arms leak info. (Contextual bandit)




# Types 
1. Frequentist
2. Bayesian (prior knowledge)


# Regret
<!-- $$
R_t(\pi, \mu) = \mathbb{E}[ \sum_{t=1}^n X_t^* ]- \mathbb{E}[ \sum_{t=1}^n X_t ]$$ --> 

<div align="center"><img style="background: white;" src="../svg/BPt4OqQUx3.svg"></div>



Regret Decomposition:


Suboptimality gap:

 <!-- $$
 \delta_a(\mu) = \mu^*(a) - \mu(a) 
 $$ --> 

<div align="center"><img style="background: white;" src="../svg/5g4z0t3LFW.svg"></div>

Time each arm played
<!-- $$
T_a(t) = \sum_{t=1}^n x_{A_s=a}
$$ --> 

<div align="center"><img style="background: white;" src="../svg/zt7Fht5srE.svg"></div>

decomposition based on gap and time
<!-- $$
R_t(\pi, \mu) =  \sum_{t=1}^n \delta_a(\mu) T_a(t)
$$ --> 

<div align="center"><img style="background: white;" src="../svg/LLZvzwGrfa.svg"></div>




