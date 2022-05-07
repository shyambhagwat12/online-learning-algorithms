
# ETC Algorithm
Features:
1. Simple unstructured alg.
2. For a known suboptimatility gap & time horizon, we can get logarthmic regret.

Limitations:
1. Dependence of suboptimality gap and time horizon in tuning the param -m.

# Parameters
<!-- $$
m(\delta,t) = \max{ 1, [4/\delta^2 * ln(n\delta^2/4)]}
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/qSmB4eOZr7.svg"></div> 

Inversely proportional to \delta - if delta is too small - we need large m

# Regret analysis

<!-- $$
Rn \leq m \sum_{i=1}^k \delta_i + (n-mk) \sum_{i=1}^k \delta_i e^(-m\delta^2/4)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/bGa5zF6fcN.svg"></div>

For given m defined as per above :
<!-- $$
m(\delta,t) = \min( n\delta, \delta + 4/\delta ( 1 + \max(0,ln(n\delta^2/4)))
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/VVGkUAr6P6.svg"></div> 

For large n and given m,
<!-- $$
Rn \leq 4/\delta *ln(n) +C
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/QJpxlkaVCU.svg"></div>