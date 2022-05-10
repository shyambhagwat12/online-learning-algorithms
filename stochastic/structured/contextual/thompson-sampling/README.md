# Thompson Sampling
Features:
1) Setup - Baysian algorithm , which uses prior probability information , chooses arm from distribution,  updates the posterior.  and posterior evolves with large number of samples.

Intuiton about randomness- 
The gaps in the distributions allows for the algorithm to explore once in a while and update the posterior hence
doesnt get stuck using arm with highest mean at a given step.

Baysian parameters
<!-- $$
(\epsilon,G,Q,P)
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/LTcqj9Psji.svg"></div>



# Regret analysis
<!-- $$
BR_n(\pi,Q) \leq C\sqrt(knln(n))
$$ --> 

<div align="center"><img style="background: white;" src="../../../../svg/G53FsxwpBC.svg"></div>

TODO
