
# EXP3 Algorithm
Features:
1) Adversarial setting algorithm which runs in two phases to get regret in terms of best arm in hindsight.
2) Phase 1 - Exponentially boost arms using the idea that counterfactual information of all arms will help in choosing best arm
3) Phase 2 - Use Importance weighted estimator(Inverse proportionality trick) to come up with unbiased estimator for all the arms


Update step:

<!-- $$
P_{tj} = e^{-\eta *R_tj} / \sum_{i=1}^k e^{-\eta*R_tj,k}
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/inEhvw2D7B.svg"></div>

<!-- $$
R_{tj} = R_{t-1,j} + X_{tj}
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/huTQVb1eiO.svg"></div>
# Parameters
<!-- $$
\eta = \sqrt(ln(k)/nk)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/JKd7YjaAEd.svg"></div>


# Regret analysis
<!-- $$
R_n(\pi,r) = 2*\sqrt(nk*ln(k))
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/Sh0vQnClIG.svg"></div>

