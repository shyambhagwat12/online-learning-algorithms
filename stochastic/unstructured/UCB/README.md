
# UCB Algorithm
Features:
1. Smooth explore/exploit algorithm without separation b/w explore and exploit
2. No dependency on suboptimality gap/time horizon. horizon is dynamic. 
3. Optimistic model - Uses UCB Confidence Index to bump up estimate so that algorithm is not stuck
   with bad arm.





UCB index function (Finite horizon)
<!-- $$
U_j(t-1,\delta) = \mu_j(t-1) + \sqrt(2ln(1/\delta)/T_j(t-1))
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/RA4n7eA8X8.svg"></div>

UCB index function (InFinite horizon)
<!-- $$
U_j(t-1,\delta) = \mu_j(t-1) + \sqrt(2ln(f(t))/T_j(t-1))
$$
$$
f(t) = 1+ tln^2(t)
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/ZkbSi3qfBd.svg"></div>

# Parameters

Intuition - Challenge of dynamic horizon is to find an unbiased estimator without introducing bias of finding the best arm based on things in the past.



# Regret analysis

## Finite horizon:

Instance dependent.
<!-- $$
R_n \leq 3\sum_{j=1}^k\delta_j + \sum 16*ln(n)/\delta_j^2
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/WJ4oEqhVFb.svg"></div>

Intuition

Proof - consider 2 arms , need to show below:
1) the index of the best arm is larger than its true mean with high
probability
2) The index of second best arm falls below the mean of the optimal arm after only a few plays

Instance indepdent. 
​
 δ - 1/n^2

<!-- $$
R_n \leq 3\sum_{j=1}^k\delta_j + 8\sqrt( nk*ln(n))
$$ --> 

<div align="center"><img style="background: white;" src="../../../svg/vstScHBY6X.svg"></div>


## InFinite horizon:

$$
f(t) = 1+ tln^2(t)
$$ 

$$
R_n \leq C \sum_{\delta_j >0} (\delta_j + (ln(n)/\delta_j))
$$