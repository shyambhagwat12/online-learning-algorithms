# online-learning-algorithms
References from UT austin class 2022 Prof Sanjay Shakkottai 

Book - Tor Lattimore and Csaba Szepesvari



# Background on Probability and concentrations.

Tutorial:

https://banditalgs.com/2018/02/09/bandit-tutorial-slides-and-update-on-book/

Beautiful video explaining monte carlo simulation and power of randomness and unbiased estimators.

https://www.youtube.com/watch?v=7ESK5SaP-bc

Bounds - Markhov,Chebyshev,Chernoffs,limit theoarm:

https://www.youtube.com/watch?v=Ij3f__U-iH8


Key background:

Subgaussian random variables are useful in algorithms , keeps computation simple. Bounds are similar to properties of Gaussian random. 

Properties of sub-gaussian

(Intuition - How our estimators is close to true mean and rate of decay of epsilon)

<!-- $$
P(X>=\epsilon) \leq e^(-\epsilon^2/2\delta^2)
$$ --> 

<div align="center"><img style="background: white;" src="svg/YcI8ikq4Fo.svg"></div>
<!-- $$
P(\mu^h >= \mu + \sqrt((2log(1/\delta))/t)) \leq \delta
$$ --> 

<div align="center"><img style="background: white;" src="svg/RYzjvAo5Va.svg"></div>

<!-- $$
P(\mu^h >= \mu - \sqrt((2log(1/\delta))/t)) \leq \delta
$$ --> 

<div align="center"><img style="background: white;" src="svg/gpWkBX86GB.svg"></div>

Subgaussian calculus Key property:

Addition of subgaussian random variables: $$1/\sqrt(m) subgaussian$$

<!-- $$
P(x > \epsilon) <= e^(\epsilon^2/2(1/\sqrt(m)))   
                <= e^(m\epsilon^2/2)
$$ --> 

<div align="center"><img style="background: white;" src="svg/z6GmlgTQeg.svg"></div>