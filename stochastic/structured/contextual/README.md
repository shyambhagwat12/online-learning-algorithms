# Contextual Bandit Algorithm
Features:
1) Player knows the contextual information about the arms being played ,which along with the arm introduces
the feature map. Algorithm tries to optimize over the best parameter theta against the feature map.( which would be k arms or groups of arms -finite, infinite)


Reward 
<!-- $$
X_t = reward(C_t,A_t) \eta_t
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/vvtaF9tjVJ.svg"></div>

Reward function
<!-- $$
reward(c,a) = <\theta^*,\phi(c,a)>  , \theta^* \in R^d
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/9PYAkSYIX3.svg"></div>

Feature map (One hot encoded)
<!-- $$
\phi(c,a)  , \phi(c,a) \in R^d
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/gysATs0Sz4.svg"></div>


# Regret analysis

<!-- $$
R_n(\pi,\mu) = E[ \sum_{t=1}^k max(reward(C_t,a)) - \sum_{t=1}^n x_t ]
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/5uWCJWnDla.svg"></div>

