# Introduction to Hypothesis Testing in Python

## 1. What is hypothesis testing ?
__Hypothesis testing__ is a statistical method that is used in making statistical decisions using experimental data. Hypothesis Testing is basically an assumption that we make about the population parameter.

## 2. why do we use it ?
__Hypothesis testing__ is an essential procedure in statistics. A hypothesis test evaluates two mutually exclusive statements about a population to determine which statement is best supported by the sample data. When we say that a finding is __statistically significant__, it’s thanks to a hypothesis test.

## Normal Distribution -
A variable is said to be _normally distributed_ or have a normal distribution if its distribution has the shape of a normal curve — a special bell-shaped curve. … The graph of a normal distribution is called the _normal curve_, which has all of the following properties: 
1. The _mean_, _median_, and _mode_ are equal. 
>> X<sub>new</sub> = (X - X<sub>min</sub>) / (X<sub>max</sub> - X<sub>min</sub>)

2. __Standardised Normal Distribution__ 
A standard normal distribution is a normal distribution with _mean 0_ and _standard deviation 1_
>> X<sub>new</sub> = (X - mu) /sigma

## parameters of hypothesis testing ?
__Null hypothesis__:- In inferential statistics, the __null hypothesis__ is a general statement or default position that there is no relationship between two measured phenomena, or no association among groups. i.e, Iit is a basic assumption or made based on domain or problem knowledge. _Example : a company production is = 50 unit/per day etc_.

__Alternative hypothesis__:- is the hypothesis used in hypothesis testing that is contrary to the null hypothesis. It is usually taken to be that the observations are the result of a real effect (with some amount of chance variation superposed). _Example : a company production is !=50 unit/per day_ etc.

## Level of significance: 
Refers to the _degree of significance in which we accept or reject the null-hypothesis_. 100% accuracy is not possible for accepting or rejecting a hypothesis, so we therefore select a level of significance that is usually 5%.

This is normally denoted with _alpha_ and generally it is 0.05 or 5% , which means your output should be _95%_ confident to give similar kind of result in each sample.

## Type I error: 
When we reject the null hypothesis, although that hypothesis was true. __Type I error_ is denoted by alpha. In hypothesis testing, the normal curve that shows the critical region is called the _alpha region_.

## Type II errors: 
When we accept the null hypothesis but it is false. Type II errors are denoted by __beta_. In Hypothesis testing, the normal curve that shows the acceptance region is called the beta region.

## One tailed test :- 
A test of a statistical hypothesis , where the region of rejection is on only one side of the sampling distribution , is called a __one-tailed test__.

_Example :- a college has ≥ 4000 student or data science ≤ 80% org adopted._

## Two-tailed test :- 
A two-tailed test is a statistical test in which the critical area of a distribution is two-sided and tests whether a sample is greater than or less than a certain range of values. If the sample being tested falls into either of the critical areas, the alternative hypothesis is accepted instead of the null hypothesis.

_Example : a college != 4000 student or data science != 80% org adopted_

## P-value :- 
The __P value__, or __calculated probability__, is the _probability of finding the observed, or more extreme, results when the null hypothesis (H<sub>0</sub>) of a study question is true_ — the definition of ‘extreme’ depends on how the hypothesis is being tested.

If your __P value__ is _less than the chosen significance level_ then you reject the null hypothesis i.e. accept that your sample gives reasonable evidence to support the alternative hypothesis. It does NOT imply a “meaningful” or “important” difference; that is for you to decide when considering the real-world relevance of your result.

__Example__ : you have a coin and you don’t know whether that is fair or tricky so let’s decide null and alternate hypothesis.
>> __H<sub>0</sub>__: a coin is a fair coin.
>> __H<sub>1</sub>__ : a coin is a tricky coin. and alpha = 5% or 0.05

Now let’s toss the coin and calculate __p- value__ ( probability value).
>> Toss a coin 1st time and result is tail- P-value = 50% (as head and tail have equal probability)

>> Toss a coin 2nd time and result is tail, now p-value = 50/2 = 25%

and similarly we Toss 6 consecutive time and got result as __P-value = 1.5%__ but we set our significance level as 95% means 5% error rate we allow and here we see we are beyond that level i.e. our null- hypothesis does not hold good so we need to reject and propose that this coin is a tricky coin which is actually.

## Degree of freedom :- 
Suppose You have a data set with 10 values. If you’re not estimating anything, each value can take on any number, right? Each value is completely free to vary.But suppose you want to test the population mean with a sample of 10 values, using a 1-sample t test. You now have a constraint — the estimation of the mean. What is that constraint, exactly? By definition of the mean, the following relationship must hold: The sum of all values in the data must equal __n * mean__, where n is the number of values in the data set.

So if a data set has 10 values, the sum of the 10 values must equal the __mean * 10__. If the mean of the 10 values is 3.5 (you could pick any number), this constraint requires that the sum of the 10 values must equal 10 * 3.5 = 35.

With that constraint, the first value in the data set is free to vary. Whatever value it is, it’s still possible for the sum of all 10 numbers to have a value of 35. The second value is also free to vary, because whatever value you choose, it still allows for the possibility that the sum of all the values is 35.

## widely used hypothesis testing type :-
1. T Test ( Student T test)
2. Z Test
3. ANOVA Test
4. Chi-Square Test

## 1. T- Test :- 
A __t-test__ is a type of inferential statistic which is used to determine if there is a significant difference between the means of two groups which may be related in certain features. It is mostly used when the data sets, like the set of data recorded as outcome from flipping a coin a 100 times, would follow a _
_normal distribution_ and may have _unknown variances_. __T test__ is used as a hypothesis testing tool, which allows testing of an assumption applicable to a population.
T-test has 2 types : 
1. one sampled t-test 
2. two-sampled t-test.

__One sample t-test__ : The One Sample t Test determines whether the sample mean is statistically different from a known or hypothesised population mean. The One Sample t Test is a __parametric test__.

__Two sampled T-test__:-
The __Independent Samples t Test__ or __2-sample t-test__ _compares the means of two independent groups in order to determine whether there is statistical evidence that the associated population means are significantly different_. The Independent Samples t Test is a __parametric test__. This test is also known as: __Independent t Test__.

__Paired sampled t-test__:- 
The __paired sample t-test__ is also called __dependent sample t-test__. It’s an _uni-variate test_ that tests for a significant difference between 2 related variables. An example of this is if you where to collect the blood pressure for an individual before and after some treatment, condition, or time point.

__H0 :- means difference between two sample is 0__

__H1:- mean difference between two sample is not 0__

## When you can run a Z Test.
Several different types of tests are used in statistics (i.e. __f test__, __chi square test__, __t test__). You would use a __Z test if__:
* Your sample size is greater than 30. Otherwise, use a t test.
* Data points should be independent from each other. In other words, one data point isn’t related or doesn’t affect another data point.
* Your data should be normally distributed. However, for large sample sizes (over 30) this doesn’t always matter.
* Your data should be randomly selected from a population, where each item has an equal chance of being selected.
* Sample sizes should be equal if at all possible.

## Two-sample Z test- 
In __two sample z-test__, similar to __t-test__ here we are checking _two independent data groups_ and deciding whether sample mean of two group is equal or not.

__H0 : mean of two group is 0__

__H1 : mean of two group is not 0__

## ANOVA (F-TEST) :- 
The __t-test__ works well when dealing with two groups, but sometimes we want to compare more than two groups at the same time. For example, if we wanted to test whether voter age differs based on some categorical variable like race, we have to compare the means of each level or group the variable. We could carry out a separate t-test for each pair of groups, but when you conduct many tests you increase the chances of false positives. The __analysis of variance__ or __ANOVA__ is a statistical inference test that lets you _compare multiple groups at the same time_.

__F = Between group variability / Within group variability__

Unlike the __z__ and __t-distributions__, the __F-distribution__ does not have any negative values because __between__ and __within-group variability__ are always positive due to squaring each deviation.

### One Way F-test(Anova)
It tell whether two or more groups are similar or not based on their _mean similarity and f-score_.

### Two Way F-test
__Two way F-test__ is extension of __1-way f-test__, it is used when we have __2 independent variable__ and __2+ groups__. 2-way F-test does not tell which variable is dominant. if we need to check individual significance then __Post-hoc__ testing need to be performed.

## Chi-Square Test
The test is applied when you have __two categorical variables__ from a single population. It is used to determine whether there is a significant association between the two variables.
For example, in an election survey, voters might be classified by gender (male or female) and voting preference (Democrat, Republican, or Independent). We could use a chi-square test for independence to determine whether gender is related to voting preference