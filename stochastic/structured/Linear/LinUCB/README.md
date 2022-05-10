# Lin UCB Algorithm
Features:
1) Linear Bandit algorithm which directly works in feature space using Actions - A_t which is vector in R^d which could be finite (k arms for instance) or infinite( information about multiple arms simultaneously )
2) Uses confidence elipsoid to boost the confidence of estimate similar to regular UCB. Calculates the confidence index and plays the one with max index


Linear Bandit Model
$$
X_t =<\theta^*,A_t> +\eta_t  \\  A_t \in R^d , \\ \theta^* \in R^d
$$



Construction of Confidence Ellipsoid , theta derived by regularized least squares
$$
\theta_{k-1}^* = argmin_{\theta \in R^d} ( \sum_{s=1}^{t-1} (x_s-<\theta,A_s>)^2  + \lambda |\theta|_2^2)
$$

$$
C_t = {\theta \in R^d : |\theta -\theta^*|_{V_t-1}^2} \leq \beta_t
$$

Lin-UCB Index where C_t is the confidence ellipsoid
$$
UCB(a) = max_{\theta\in C_t} <\theta,a>
$$

# Regret analysis


