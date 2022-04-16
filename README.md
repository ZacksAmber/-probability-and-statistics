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

If you don't have jupyter, run `pipenv install jupyter --dev`.

---

List your kernels:

```sh
jupyter-kernelspec list
```

If your Jupyter was installed under a specific virtual environment, you need to run the above list command under this env.

---

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

#### [Binomial Random Variables](./binomial.ipynb)

Also include:
- [Bernoulli Random Variables](./binomial.ipynb)
- [Geometric Random Variables](./binomial.ipynb)
- [Poisson Random Variables](./binomial.ipynb)

#### [Normal Random Variables](./normal.ipynb)

---

### [Sampling Distributions](./smapling_distributions.ipynb)

---

## Hypothesis Testing

### [Study Design](./study_design.ipynb)

---

### [Confidence Intervals](./confidence_intervals.ipynb)

---

### [Hypothesis Testing](./hypothesis_testing.ipynb)

---

### [Chi-squared Test](./chi-squared_test.ipynb)

---

## Regression

### [Linear Regression](./linear_regression.ipynb)
