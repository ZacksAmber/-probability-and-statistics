# Statistics and Probability

## Basic

### [Descriptive Analytics](./descriptive_analytics.ipynb)

---

## Probability

### [Probability](./probability.ipynb)

---

### [Counting Permutations and Combinations](/.counting_permutations_and_combinations.ipynb)

---

### [Random Variables](./random_variables.ipynb)

- $E[X+Y] = E[X] + E[Y]$, $E[X-Y] = E[X] - E[Y]$
- $Var[X+Y] = Var[X] + Var[Y]$, $Var[X-Y] = Var[X] + Var[Y]$

#### [Binomial Random Variables](./binomial.ipynb)

Also include:
- [Bernoulli Random Variables](./binomial.ipynb)
- [Geometric Random Variables](./binomial.ipynb)
- [Poisson Random Variables](./binomial.ipynb)

#### [Normal Random Variables](./normal.ipynb)

---

### [Sampling Distributions](./smapling_distributions.ipynb)

---

## Statistical Study

### [Study Design](./study_design.ipynb)

---

### [Confidence Intervals](./confidence_intervals.ipynb)

The **margin of error** is a statistic expressing the amount of random [sampling error](https://en.wikipedia.org/wiki/Sampling_error "Sampling error") in the results of a [survey](https://en.wikipedia.org/wiki/Statistical_survey "Statistical survey").

The **margin of error** is a statistic expressing the amount of random [sampling error](https://en.wikipedia.org/wiki/Sampling_error "Sampling error") in the results of a [survey](https://en.wikipedia.org/wiki/Statistical_survey "Statistical survey").

- One-proportion z interval (One-sample z interval for a proportion)
- One-sample t interval (One-sample t interval for a mean)

---

### [Hypothesis Testing](./hypothesis_testing.ipynb)

#### Common test statistics

**One-sample tests** are appropriate when a sample is being compared to the population from a hypothesis. The population characteristics are known from theory or are calculated from the population.

**Two-sample tests** are appropriate for comparing two samples, typically experimental and control samples from a scientifically controlled experiment.

**Paired tests** are appropriate for comparing two samples where it is impossible to control important variables. Rather than comparing two sets, members are paired between samples so the difference between the members becomes the sample. Typically the mean of the differences is then compared to zero. The common example scenario for when a [paired difference test](https://en.wikipedia.org/wiki/Paired_difference_test "Paired difference test") is appropriate is when a single set of test subjects has something applied to them and the test is intended to check for an effect.

[Z-tests](https://en.wikipedia.org/wiki/Z-test "Z-test") are appropriate for comparing means under stringent conditions regarding normality and a known standard deviation.

A [_t_-test](https://en.wikipedia.org/wiki/Student%27s_t-test "Student's t-test") is appropriate for comparing means under relaxed conditions (less is assumed).

Tests of proportions are analogous to tests of means (the 50% proportion).

Chi-squared tests use the same calculations and the same probability distribution for different applications:

-   [Chi-squared tests](https://en.wikipedia.org/wiki/Chi-squared_test "Chi-squared test") for variance are used to determine whether a normal population has a specified variance. The null hypothesis is that it does.
-   Chi-squared tests of independence are used for deciding whether two variables are associated or are independent. The variables are categorical rather than numeric. It can be used to decide whether [left-handedness](https://en.wikipedia.org/wiki/Left-handedness "Left-handedness") is correlated with height (or not). The null hypothesis is that the variables are independent. The numbers used in the calculation are the observed and expected frequencies of occurrence (from [contingency tables](https://en.wikipedia.org/wiki/Contingency_table "Contingency table")).
-   Chi-squared goodness of fit tests are used to determine the adequacy of curves fit to data. The null hypothesis is that the curve fit is adequate. It is common to determine curve shapes to minimize the mean square error, so it is appropriate that the goodness-of-fit calculation sums the squared errors.

[F-tests](https://en.wikipedia.org/wiki/F-test "F-test") (analysis of variance, ANOVA) are commonly used when deciding whether groupings of data by category are meaningful. If the variance of test scores of the left-handed in a class is much smaller than the variance of the whole class, then it may be useful to study lefties as a group. The null hypothesis is that two variances are the same – so the proposed grouping is not meaningful.

---

#### [one-sample](./one-sample.ipynb)

- One-proportion z-test (One-sample z test for a proportion)
- One-sample t-test (One-sample t test for a mean)

#### [two-sample](./two-sample.ipynb)

- Two-proportion z-test, Two-proportion z interval
- Two-sample t-test, Two sample t interval

---

#### [Inference for categorical data(Chi-square tests)](./chi-square_test.ipynb)

- Chi-square goodness-of-fit tests
- Chi-square tests for relationships

---

## Regression

### [Linear Regression](./linear_regression.ipynb)

---

# Instruction

## Python Virtual Environment

Under the root directory of `statistics-and-probability`:

```sh
pipenv shell
```

---

## Jupyter

> [Jupyter Notebook Kernels: How to Add, Change, Remove](https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove)

After activate pipenv environment, you can add kernel to your Jupyter:

```sh
ipython kernel install --name "statistics-and-probability" --user
```

If you don't have jupyter, run `pipenv install jupyter jupyterlab --dev`.

---

List your kernels:

```sh
jupyter-kernelspec list
```

If your Jupyter was installed under a specific virtual environment, you need to run the above list command under this env.