
# Elimination Algorithm
Features:
1. Explore exploit alg with no knowledge of sub optimality gap.
2. Time horizon can be eliminated by using doubling trick


Limitations:
1. Explore and Exploit phase tradeoff is unnecessary in certain cases.

Elimination step
<!-- $$
(\mu_{ir}^* + \sqrt(log(n\delta_r^2)/2m_r))  < (\mu_{jr}^* + \sqrt(log(n\delta_r^2)/2m_r))>
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/LaOdjBDxUn.svg"></div>

Intuition - Intially set suboptimality gap to some default (1) . Bump up the confidence of not so likely arm , bump down the confidence of likely arm. If bump up of not so likely arm is still less than bump down of likely arm, then not so likely arm can be eliminated. Update delta and decrese by a step.


If bump down 
# Parameters

<!-- $$
m_r = 2* ln(n\delta_r^2) / \delta_r^2
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/UbnXBOfns0.svg"></div>

dependence on n can be eliminated by doubling trick.


# Regret analysis

<!-- $$
Rn \leq C_1 + C_2/\delta * ln(n)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/1uFx9SPATK.svg"></div>

*scales by logn/delta