# Lin UCB Algorithm
Features:
1) Linear Bandit algorithm which directly works in feature space using Actions - A_t which is vector in R^d which could be finite (k arms for instance) or infinite( information about multiple arms simultaneously )
2) Uses confidence elipsoid to boost the confidence of estimate similar to regular UCB. Calculates the confidence index and plays the one with max index


Linear Bandit Model
<!-- $$
X_t =<\theta^*,A_t> +\eta_t  \\  A_t \in R^d , \\ \theta^* \in R^d
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/bcs4uUjjmM.svg"></div>



Construction of Confidence Ellipsoid , theta derived by regularized least squares
<!-- $$
\theta_{k-1}^* = argmin_{\theta \in R^d} ( \sum_{s=1}^{t-1} (x_s-<\theta,A_s>)^2  + \lambda |\theta|_2^2)
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/tUa5pTmMcN.svg"></div>

<!-- $$
\theta_{t-1}^* = V_{t-1}^{-1} \sum_{s=1}^{t-1} A_sX_s
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/VcLlgCBBz4.svg"></div>

<!-- $$
C_t = {\theta \in R^d : |\theta -\theta_{t-1}^*|_{V_t-1}^2} \leq \beta_t
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/ud2lwsAPsy.svg"></div> 

β - standard deviation
​


Lin-UCB Index where C_t is the confidence ellipsoid
<!-- $$
UCB(a) = max_{\theta\in C_t} <\theta,a>
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/sMk6ao41kj.svg"></div>

# Parameters

Action space can be bounded by constraints
<!-- $$
<\theta^*,a> \leq 1 ,  a \in \cup_{t=1}^n A_t
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/ZNyAyZP5Ed.svg"></div>
<!-- $$
||a||_2  \leq L
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/S6eaFXXERL.svg"></div>


# Regret analysis

$$
R_n \leq C d\sqrt{n} ln(nL)
$$
