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

## Statistical Study

### [Study Design](./study_design.ipynb)

---

### [Confidence Intervals](./confidence_intervals.ipynb)

---

### [Hypothesis Testing](./hypothesis_testing.ipynb)

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

In the table below, the symbols used are defined at the bottom of the table. Many other tests can be found in [other articles](https://en.wikipedia.org/wiki/Category:Statistical_tests "Category:Statistical tests"). Proofs exist that the test statistics are appropriate.

<table class="wikitable">
<tbody><tr>
<th>Name
</th>
<th>Formula
</th>
<th>Assumptions or notes
</th></tr>
<tr>
<td>One-sample <a href="/wiki/Z-test" title="Z-test">z-test</a>
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle z={\frac {{\overline {x}}-\mu _{0}}{({\sigma }/{\sqrt {n}})}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>z</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mover>
                  <mi>x</mi>
                  <mo accent="false">¯<!-- ¯ --></mo>
                </mover>
              </mrow>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>μ<!-- μ --></mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <mrow>
              <mo stretchy="false">(</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mi>σ<!-- σ --></mi>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mo>/</mo>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <msqrt>
                  <mi>n</mi>
                </msqrt>
              </mrow>
              <mo stretchy="false">)</mo>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle z={\frac {{\overline {x}}-\mu _{0}}{({\sigma }/{\sqrt {n}})}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c6aa1a2e4b4b6082ea6682bef8f102c8a1fc893d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.838ex; width:12.655ex; height:6.676ex;" alt="{\displaystyle z={\frac {{\overline {x}}-\mu _{0}}{({\sigma }/{\sqrt {n}})}}}"></span>
</td>
<td>(Normal population <b>or</b> <i>n</i> large) <b>and</b> σ known. <br>
<p>(<i>z</i> is the distance from the mean in relation to the <a href="/wiki/Standard_error" title="Standard error">standard deviation of the mean</a>). For non-normal distributions it is possible to calculate a minimum proportion of a population that falls within <i>k</i> standard deviations for any <i>k</i> (see: <i><a href="/wiki/Chebyshev%27s_inequality" title="Chebyshev's inequality">Chebyshev's inequality</a></i>).
</p>
</td></tr>
<tr>
<td>Two-sample z-test
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle z={\frac {({\overline {x}}_{1}-{\overline {x}}_{2})-d_{0}}{\sqrt {{\frac {\sigma _{1}^{2}}{n_{1}}}+{\frac {\sigma _{2}^{2}}{n_{2}}}}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>z</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mo stretchy="false">(</mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>x</mi>
                    <mo accent="false">¯<!-- ¯ --></mo>
                  </mover>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>x</mi>
                    <mo accent="false">¯<!-- ¯ --></mo>
                  </mover>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
              <mo stretchy="false">)</mo>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>d</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <msqrt>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <msubsup>
                    <mi>σ<!-- σ --></mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>1</mn>
                    </mrow>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msubsup>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>1</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
              <mo>+</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <msubsup>
                    <mi>σ<!-- σ --></mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msubsup>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
            </msqrt>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle z={\frac {({\overline {x}}_{1}-{\overline {x}}_{2})-d_{0}}{\sqrt {{\frac {\sigma _{1}^{2}}{n_{1}}}+{\frac {\sigma _{2}^{2}}{n_{2}}}}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/fd9e493bfa47350881aa8accd4c3ae476f169969" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -6.005ex; width:19.774ex; height:9.843ex;" alt="z=\frac{(\overline{x}_1 - \overline{x}_2) - d_0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}"></span>
</td>
<td>Normal population <b>and</b> independent observations <b>and</b> σ<sub>1</sub> and σ<sub>2</sub> are known where <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle d_{0}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>d</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle d_{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4740381c16ea98c4132510daa642e93c1e42c049" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.263ex; height:2.509ex;" alt="d_0"></span> is the value of <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \mu _{1}-\mu _{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>μ<!-- μ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
        <mo>−<!-- − --></mo>
        <msub>
          <mi>μ<!-- μ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu _{1}-\mu _{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/5f923f77cc9f1769b60b5736084fbf4fc6ca565e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:7.752ex; height:2.509ex;" alt="{\displaystyle \mu _{1}-\mu _{2}}"></span> under the null hypothesis
</td></tr>
<tr>
<td>One-sample <a href="/wiki/Student%27s_t-test" title="Student's t-test"><i>t</i>-test</a>
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle t={\frac {{\overline {x}}-\mu _{0}}{(s/{\sqrt {n}})}},}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>t</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mover>
                  <mi>x</mi>
                  <mo accent="false">¯<!-- ¯ --></mo>
                </mover>
              </mrow>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>μ<!-- μ --></mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <mrow>
              <mo stretchy="false">(</mo>
              <mi>s</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mo>/</mo>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <msqrt>
                  <mi>n</mi>
                </msqrt>
              </mrow>
              <mo stretchy="false">)</mo>
            </mrow>
          </mfrac>
        </mrow>
        <mo>,</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t={\frac {{\overline {x}}-\mu _{0}}{(s/{\sqrt {n}})}},}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/925bdf4f11c6938c078955ff9558de9995ea3660" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.838ex; width:12.814ex; height:6.676ex;" alt="t=\frac{\overline{x}-\mu_0} {( s / \sqrt{n} )} ,"></span><br>
<p><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle df=n-1\ }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>d</mi>
        <mi>f</mi>
        <mo>=</mo>
        <mi>n</mi>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mtext>&nbsp;</mtext>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle df=n-1\ }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/012c754360d275408aedb850435181af14960072" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:11.571ex; height:2.509ex;" alt="df=n-1 \ "></span>
</p>
</td>
<td>(Normal population <b>or</b> <i>n</i> large) <b>and</b> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \sigma }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>σ<!-- σ --></mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \sigma }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/59f59b7c3e6fdb1d0365a494b81fb9a696138c36" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.33ex; height:1.676ex;" alt="\sigma "></span> unknown
</td></tr>
<tr>
<td>Paired <i>t</i>-test
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle t={\frac {{\overline {d}}-d_{0}}{(s_{d}/{\sqrt {n}})}},}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>t</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mover>
                  <mi>d</mi>
                  <mo accent="false">¯<!-- ¯ --></mo>
                </mover>
              </mrow>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>d</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <mrow>
              <mo stretchy="false">(</mo>
              <msub>
                <mi>s</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi>d</mi>
                </mrow>
              </msub>
              <mrow class="MJX-TeXAtom-ORD">
                <mo>/</mo>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <msqrt>
                  <mi>n</mi>
                </msqrt>
              </mrow>
              <mo stretchy="false">)</mo>
            </mrow>
          </mfrac>
        </mrow>
        <mo>,</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t={\frac {{\overline {d}}-d_{0}}{(s_{d}/{\sqrt {n}})}},}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9a5ad85e32e047ee05cbaaceaa308b50cf869309" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.838ex; width:13.906ex; height:7.009ex;" alt="t=\frac{\overline{d}-d_0} { ( s_d / \sqrt{n} ) } ,"></span><br>
<p><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle df=n-1\ }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>d</mi>
        <mi>f</mi>
        <mo>=</mo>
        <mi>n</mi>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mtext>&nbsp;</mtext>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle df=n-1\ }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/012c754360d275408aedb850435181af14960072" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:11.571ex; height:2.509ex;" alt="df=n-1 \ "></span>
</p>
</td>
<td>(Normal population of differences <b>or</b> <i>n</i> large) <b>and</b> <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \sigma }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>σ<!-- σ --></mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \sigma }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/59f59b7c3e6fdb1d0365a494b81fb9a696138c36" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.33ex; height:1.676ex;" alt="\sigma "></span> unknown
</td></tr>
<tr>
<td>Two-sample pooled <a href="/wiki/Student%27s_t-test" title="Student's t-test"><i>t</i>-test</a>, equal variances
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle t={\frac {({\overline {x}}_{1}-{\overline {x}}_{2})-d_{0}}{s_{p}{\sqrt {{\frac {1}{n_{1}}}+{\frac {1}{n_{2}}}}}}},}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>t</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mo stretchy="false">(</mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>x</mi>
                    <mo accent="false">¯<!-- ¯ --></mo>
                  </mover>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>x</mi>
                    <mo accent="false">¯<!-- ¯ --></mo>
                  </mover>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
              <mo stretchy="false">)</mo>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>d</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <mrow>
              <msub>
                <mi>s</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mi>p</mi>
                </mrow>
              </msub>
              <mrow class="MJX-TeXAtom-ORD">
                <msqrt>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mn>1</mn>
                      <msub>
                        <mi>n</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>1</mn>
                        </mrow>
                      </msub>
                    </mfrac>
                  </mrow>
                  <mo>+</mo>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <mn>1</mn>
                      <msub>
                        <mi>n</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msub>
                    </mfrac>
                  </mrow>
                </msqrt>
              </mrow>
            </mrow>
          </mfrac>
        </mrow>
        <mo>,</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t={\frac {({\overline {x}}_{1}-{\overline {x}}_{2})-d_{0}}{s_{p}{\sqrt {{\frac {1}{n_{1}}}+{\frac {1}{n_{2}}}}}}},}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/400b0c5f9c085aa10ef47300da9609afd1ce8f73" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -4.671ex; width:20.172ex; height:8.509ex;" alt="t=\frac{(\overline{x}_1 - \overline{x}_2) - d_0}{s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}},"></span><br>
<p><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle s_{p}^{2}={\frac {(n_{1}-1)s_{1}^{2}+(n_{2}-1)s_{2}^{2}}{n_{1}+n_{2}-2}},}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msubsup>
          <mi>s</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>p</mi>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msubsup>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mo stretchy="false">(</mo>
              <msub>
                <mi>n</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <mn>1</mn>
              <mo stretchy="false">)</mo>
              <msubsup>
                <mi>s</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msubsup>
              <mo>+</mo>
              <mo stretchy="false">(</mo>
              <msub>
                <mi>n</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <mn>1</mn>
              <mo stretchy="false">)</mo>
              <msubsup>
                <mi>s</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msubsup>
            </mrow>
            <mrow>
              <msub>
                <mi>n</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>+</mo>
              <msub>
                <mi>n</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <mn>2</mn>
            </mrow>
          </mfrac>
        </mrow>
        <mo>,</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle s_{p}^{2}={\frac {(n_{1}-1)s_{1}^{2}+(n_{2}-1)s_{2}^{2}}{n_{1}+n_{2}-2}},}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d9501fde4e2ff040650db386051a49e2124e5322" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.171ex; width:30.383ex; height:6.176ex;" alt="s_p^2=\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2},"></span><br>
<span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle df=n_{1}+n_{2}-2\ }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>d</mi>
        <mi>f</mi>
        <mo>=</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
        <mo>+</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
        <mo>−<!-- − --></mo>
        <mn>2</mn>
        <mtext>&nbsp;</mtext>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle df=n_{1}+n_{2}-2\ }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4ce5946e0f8015a39940ddf1d750fc0ce83de698" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:17.915ex; height:2.509ex;" alt="df=n_1 + n_2 - 2 \ "></span><sup id="cite_ref-NIST2mean_3-0" class="reference"><a href="#cite_note-NIST2mean-3">[3]</a></sup>
</p>
</td>
<td>(Normal populations <b>or</b> <i>n</i><sub>1</sub>&nbsp;+&nbsp;<i>n</i><sub>2</sub>&nbsp;&gt;&nbsp;40) <b>and</b> independent observations <b>and</b> σ<sub>1</sub> = σ<sub>2</sub> unknown
</td></tr>
<tr>
<td>Two-sample unpooled <i>t</i>-test, unequal variances (<a href="/wiki/Welch%27s_t_test" class="mw-redirect" title="Welch's t test">Welch's <i>t</i>-test</a>)
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle t={\frac {({\overline {x}}_{1}-{\overline {x}}_{2})-d_{0}}{\sqrt {{\frac {s_{1}^{2}}{n_{1}}}+{\frac {s_{2}^{2}}{n_{2}}}}}},}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>t</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mo stretchy="false">(</mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>x</mi>
                    <mo accent="false">¯<!-- ¯ --></mo>
                  </mover>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>x</mi>
                    <mo accent="false">¯<!-- ¯ --></mo>
                  </mover>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
              <mo stretchy="false">)</mo>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>d</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <msqrt>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <msubsup>
                    <mi>s</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>1</mn>
                    </mrow>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msubsup>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>1</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
              <mo>+</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <msubsup>
                    <mi>s</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msubsup>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
            </msqrt>
          </mfrac>
        </mrow>
        <mo>,</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t={\frac {({\overline {x}}_{1}-{\overline {x}}_{2})-d_{0}}{\sqrt {{\frac {s_{1}^{2}}{n_{1}}}+{\frac {s_{2}^{2}}{n_{2}}}}}},}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/f1c0ca18b71147510095cb89368272ea5f627f2d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -6.005ex; width:20.172ex; height:9.843ex;" alt="t=\frac{(\overline{x}_1 - \overline{x}_2) - d_0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}},"></span><br>
<p><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle df={\frac {\left({\frac {s_{1}^{2}}{n_{1}}}+{\frac {s_{2}^{2}}{n_{2}}}\right)^{2}}{{\frac {\left({\frac {s_{1}^{2}}{n_{1}}}\right)^{2}}{n_{1}-1}}+{\frac {\left({\frac {s_{2}^{2}}{n_{2}}}\right)^{2}}{n_{2}-1}}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>d</mi>
        <mi>f</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <msup>
              <mrow>
                <mo>(</mo>
                <mrow>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <msubsup>
                        <mi>s</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>1</mn>
                        </mrow>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msubsup>
                      <msub>
                        <mi>n</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>1</mn>
                        </mrow>
                      </msub>
                    </mfrac>
                  </mrow>
                  <mo>+</mo>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mfrac>
                      <msubsup>
                        <mi>s</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msubsup>
                      <msub>
                        <mi>n</mi>
                        <mrow class="MJX-TeXAtom-ORD">
                          <mn>2</mn>
                        </mrow>
                      </msub>
                    </mfrac>
                  </mrow>
                </mrow>
                <mo>)</mo>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msup>
            <mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <msup>
                    <mrow>
                      <mo>(</mo>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mfrac>
                          <msubsup>
                            <mi>s</mi>
                            <mrow class="MJX-TeXAtom-ORD">
                              <mn>1</mn>
                            </mrow>
                            <mrow class="MJX-TeXAtom-ORD">
                              <mn>2</mn>
                            </mrow>
                          </msubsup>
                          <msub>
                            <mi>n</mi>
                            <mrow class="MJX-TeXAtom-ORD">
                              <mn>1</mn>
                            </mrow>
                          </msub>
                        </mfrac>
                      </mrow>
                      <mo>)</mo>
                    </mrow>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msup>
                  <mrow>
                    <msub>
                      <mi>n</mi>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mn>1</mn>
                      </mrow>
                    </msub>
                    <mo>−<!-- − --></mo>
                    <mn>1</mn>
                  </mrow>
                </mfrac>
              </mrow>
              <mo>+</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <msup>
                    <mrow>
                      <mo>(</mo>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mfrac>
                          <msubsup>
                            <mi>s</mi>
                            <mrow class="MJX-TeXAtom-ORD">
                              <mn>2</mn>
                            </mrow>
                            <mrow class="MJX-TeXAtom-ORD">
                              <mn>2</mn>
                            </mrow>
                          </msubsup>
                          <msub>
                            <mi>n</mi>
                            <mrow class="MJX-TeXAtom-ORD">
                              <mn>2</mn>
                            </mrow>
                          </msub>
                        </mfrac>
                      </mrow>
                      <mo>)</mo>
                    </mrow>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msup>
                  <mrow>
                    <msub>
                      <mi>n</mi>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mn>2</mn>
                      </mrow>
                    </msub>
                    <mo>−<!-- − --></mo>
                    <mn>1</mn>
                  </mrow>
                </mfrac>
              </mrow>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle df={\frac {\left({\frac {s_{1}^{2}}{n_{1}}}+{\frac {s_{2}^{2}}{n_{2}}}\right)^{2}}{{\frac {\left({\frac {s_{1}^{2}}{n_{1}}}\right)^{2}}{n_{1}-1}}+{\frac {\left({\frac {s_{2}^{2}}{n_{2}}}\right)^{2}}{n_{2}-1}}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c72b7481d7e45a6f70c2c6858e86388948eed52c" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -8.005ex; width:22.686ex; height:15.509ex;" alt="df = \frac{\left(\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}\right)^2} {\frac{\left(\frac{s_1^2}{n_1}\right)^2}{n_1-1} + \frac{\left(\frac{s_2^2}{n_2}\right)^2}{n_2-1}}"></span><sup id="cite_ref-NIST2mean_3-1" class="reference"><a href="#cite_note-NIST2mean-3">[3]</a></sup>
</p>
</td>
<td>(Normal populations <b>or</b> <i>n</i><sub>1</sub>&nbsp;+&nbsp;<i>n</i><sub>2</sub>&nbsp;&gt;&nbsp;40) <b>and</b> independent observations <b>and</b> σ<sub>1</sub> ≠ σ<sub>2</sub> both unknown
</td></tr>
<tr>
<td>One-proportion z-test
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle z={\frac {{\hat {p}}-p_{0}}{\sqrt {p_{0}(1-p_{0})}}}{\sqrt {n}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>z</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>p</mi>
                    <mo stretchy="false">^<!-- ^ --></mo>
                  </mover>
                </mrow>
              </mrow>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>p</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <msqrt>
              <msub>
                <mi>p</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
              <mo stretchy="false">(</mo>
              <mn>1</mn>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>p</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
              <mo stretchy="false">)</mo>
            </msqrt>
          </mfrac>
        </mrow>
        <mrow class="MJX-TeXAtom-ORD">
          <msqrt>
            <mi>n</mi>
          </msqrt>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle z={\frac {{\hat {p}}-p_{0}}{\sqrt {p_{0}(1-p_{0})}}}{\sqrt {n}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/2904f8eeb6187f4bf40cbbd1ddfccc95a9e2ff42" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.171ex; width:20.937ex; height:6.676ex;" alt="z=\frac{\hat{p} - p_0}{\sqrt{p_0 (1-p_0)}}\sqrt n"></span>
</td>
<td><i>n<sup> .</sup>p<sub>0</sub></i> &gt; 10 <b>and</b> <i>n</i> (1&nbsp;−&nbsp;<i>p<sub>0</sub></i>) &gt; 10 <b>and</b> it is a SRS (Simple Random Sample), see <a href="/wiki/Binomial_distribution#Normal_approximation" title="Binomial distribution">notes</a>.
</td></tr>
<tr>
<td>Two-proportion z-test, pooled for <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle H_{0}\colon p_{1}=p_{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>H</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msub>
        <mo>:<!-- : --></mo>
        <msub>
          <mi>p</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
        <mo>=</mo>
        <msub>
          <mi>p</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle H_{0}\colon p_{1}=p_{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cbad260a403201e34162ddc1d6b51cf11b4cd6d4" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:11.565ex; height:2.509ex;" alt="H_0\colon p_1=p_2"></span>
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle z={\frac {({\hat {p}}_{1}-{\hat {p}}_{2})}{\sqrt {{\hat {p}}(1-{\hat {p}})({\frac {1}{n_{1}}}+{\frac {1}{n_{2}}})}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>z</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mo stretchy="false">(</mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mrow class="MJX-TeXAtom-ORD">
                    <mover>
                      <mi>p</mi>
                      <mo stretchy="false">^<!-- ^ --></mo>
                    </mover>
                  </mrow>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mrow class="MJX-TeXAtom-ORD">
                    <mover>
                      <mi>p</mi>
                      <mo stretchy="false">^<!-- ^ --></mo>
                    </mover>
                  </mrow>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
              <mo stretchy="false">)</mo>
            </mrow>
            <msqrt>
              <mrow class="MJX-TeXAtom-ORD">
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>p</mi>
                    <mo stretchy="false">^<!-- ^ --></mo>
                  </mover>
                </mrow>
              </mrow>
              <mo stretchy="false">(</mo>
              <mn>1</mn>
              <mo>−<!-- − --></mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mrow class="MJX-TeXAtom-ORD">
                  <mover>
                    <mi>p</mi>
                    <mo stretchy="false">^<!-- ^ --></mo>
                  </mover>
                </mrow>
              </mrow>
              <mo stretchy="false">)</mo>
              <mo stretchy="false">(</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <mn>1</mn>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>1</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
              <mo>+</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <mn>1</mn>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
              <mo stretchy="false">)</mo>
            </msqrt>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle z={\frac {({\hat {p}}_{1}-{\hat {p}}_{2})}{\sqrt {{\hat {p}}(1-{\hat {p}})({\frac {1}{n_{1}}}+{\frac {1}{n_{2}}})}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d6d25b4eb7124341bed97eab36f8b6a14af29d87" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -4.671ex; width:25.835ex; height:8.509ex;" alt="z=\frac{(\hat{p}_1 - \hat{p}_2)}{\sqrt{\hat{p}(1 - \hat{p})(\frac{1}{n_1} + \frac{1}{n_2})}}"></span>
<p><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle {\hat {p}}={\frac {x_{1}+x_{2}}{n_{1}+n_{2}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mrow class="MJX-TeXAtom-ORD">
            <mover>
              <mi>p</mi>
              <mo stretchy="false">^<!-- ^ --></mo>
            </mover>
          </mrow>
        </mrow>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <msub>
                <mi>x</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>+</mo>
              <msub>
                <mi>x</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
            </mrow>
            <mrow>
              <msub>
                <mi>n</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>+</mo>
              <msub>
                <mi>n</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
            </mrow>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle {\hat {p}}={\frac {x_{1}+x_{2}}{n_{1}+n_{2}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c37500a52c45fdbad597bd64e0d8c9341044c53e" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.171ex; margin-left: -0.089ex; width:13.122ex; height:5.343ex;" alt="\hat{p}=\frac{x_1 + x_2}{n_1 + n_2}"></span>
</p>
</td>
<td><i>n</i><sub>1</sub> <i>p</i><sub>1</sub> &gt; 5 <b>and</b> <i>n</i><sub>1</sub>(1&nbsp;−&nbsp;<i>p</i><sub>1</sub>) &gt; 5 <b>and</b> <i>n</i><sub>2</sub> <i>p</i><sub>2</sub>&nbsp;&gt;&nbsp;5 <b>and</b> <i>n</i><sub>2</sub>(1&nbsp;−&nbsp;<i>p</i><sub>2</sub>) &gt; 5 <b>and</b> independent observations, see <a href="/wiki/Binomial_distribution#Normal_approximation" title="Binomial distribution">notes</a>.
</td></tr>
<tr>
<td>Two-proportion z-test, unpooled for <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle |d_{0}|>0}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mo stretchy="false">|</mo>
        </mrow>
        <msub>
          <mi>d</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msub>
        <mrow class="MJX-TeXAtom-ORD">
          <mo stretchy="false">|</mo>
        </mrow>
        <mo>&gt;</mo>
        <mn>0</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle |d_{0}|&gt;0}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c908ff645dc0d59500ebd64f7b1b020ab458b0c7" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:7.818ex; height:2.843ex;" alt="|d_0|>0"></span>
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle z={\frac {({\hat {p}}_{1}-{\hat {p}}_{2})-d_{0}}{\sqrt {{\frac {{\hat {p}}_{1}(1-{\hat {p}}_{1})}{n_{1}}}+{\frac {{\hat {p}}_{2}(1-{\hat {p}}_{2})}{n_{2}}}}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>z</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mo stretchy="false">(</mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mrow class="MJX-TeXAtom-ORD">
                    <mover>
                      <mi>p</mi>
                      <mo stretchy="false">^<!-- ^ --></mo>
                    </mover>
                  </mrow>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>1</mn>
                </mrow>
              </msub>
              <mo>−<!-- − --></mo>
              <msub>
                <mrow class="MJX-TeXAtom-ORD">
                  <mrow class="MJX-TeXAtom-ORD">
                    <mover>
                      <mi>p</mi>
                      <mo stretchy="false">^<!-- ^ --></mo>
                    </mover>
                  </mrow>
                </mrow>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msub>
              <mo stretchy="false">)</mo>
              <mo>−<!-- − --></mo>
              <msub>
                <mi>d</mi>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>0</mn>
                </mrow>
              </msub>
            </mrow>
            <msqrt>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <mrow>
                    <msub>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mrow class="MJX-TeXAtom-ORD">
                          <mover>
                            <mi>p</mi>
                            <mo stretchy="false">^<!-- ^ --></mo>
                          </mover>
                        </mrow>
                      </mrow>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mn>1</mn>
                      </mrow>
                    </msub>
                    <mo stretchy="false">(</mo>
                    <mn>1</mn>
                    <mo>−<!-- − --></mo>
                    <msub>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mrow class="MJX-TeXAtom-ORD">
                          <mover>
                            <mi>p</mi>
                            <mo stretchy="false">^<!-- ^ --></mo>
                          </mover>
                        </mrow>
                      </mrow>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mn>1</mn>
                      </mrow>
                    </msub>
                    <mo stretchy="false">)</mo>
                  </mrow>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>1</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
              <mo>+</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mfrac>
                  <mrow>
                    <msub>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mrow class="MJX-TeXAtom-ORD">
                          <mover>
                            <mi>p</mi>
                            <mo stretchy="false">^<!-- ^ --></mo>
                          </mover>
                        </mrow>
                      </mrow>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mn>2</mn>
                      </mrow>
                    </msub>
                    <mo stretchy="false">(</mo>
                    <mn>1</mn>
                    <mo>−<!-- − --></mo>
                    <msub>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mrow class="MJX-TeXAtom-ORD">
                          <mover>
                            <mi>p</mi>
                            <mo stretchy="false">^<!-- ^ --></mo>
                          </mover>
                        </mrow>
                      </mrow>
                      <mrow class="MJX-TeXAtom-ORD">
                        <mn>2</mn>
                      </mrow>
                    </msub>
                    <mo stretchy="false">)</mo>
                  </mrow>
                  <msub>
                    <mi>n</mi>
                    <mrow class="MJX-TeXAtom-ORD">
                      <mn>2</mn>
                    </mrow>
                  </msub>
                </mfrac>
              </mrow>
            </msqrt>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle z={\frac {({\hat {p}}_{1}-{\hat {p}}_{2})-d_{0}}{\sqrt {{\frac {{\hat {p}}_{1}(1-{\hat {p}}_{1})}{n_{1}}}+{\frac {{\hat {p}}_{2}(1-{\hat {p}}_{2})}{n_{2}}}}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cb2f8747618eb4c47ea2068fb55385cabc337873" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -6.005ex; width:26.017ex; height:9.843ex;" alt="z=\frac{(\hat{p}_1 - \hat{p}_2) - d_0}{\sqrt{\frac{\hat{p}_1(1 - \hat{p}_1)}{n_1} + \frac{\hat{p}_2(1 - \hat{p}_2)}{n_2}}}"></span>
</td>
<td><i>n</i><sub>1</sub> <i>p</i><sub>1</sub> &gt; 5 <b>and</b> <i>n</i><sub>1</sub>(1&nbsp;−&nbsp;<i>p</i><sub>1</sub>) &gt; 5 <b>and</b> <i>n</i><sub>2</sub> <i>p</i><sub>2</sub>&nbsp;&gt;&nbsp;5 <b>and</b> <i>n</i><sub>2</sub>(1&nbsp;−&nbsp;<i>p</i><sub>2</sub>) &gt; 5 <b>and</b> independent observations, see <a href="/wiki/Binomial_distribution#Normal_approximation" title="Binomial distribution">notes</a>.
</td></tr>
<tr>
<td>Chi-squared test for variance
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \chi ^{2}=(n-1){\frac {s^{2}}{\sigma _{0}^{2}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>χ<!-- χ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
        <mo>=</mo>
        <mo stretchy="false">(</mo>
        <mi>n</mi>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mo stretchy="false">)</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <msup>
              <mi>s</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msup>
            <msubsup>
              <mi>σ<!-- σ --></mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>0</mn>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msubsup>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \chi ^{2}=(n-1){\frac {s^{2}}{\sigma _{0}^{2}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e040afe9eda875a4d65a1d007813658e4cc1cf9a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.005ex; width:16.036ex; height:6.843ex;" alt="\chi^2=(n-1)\frac{s^2}{\sigma^2_0}"></span>
</td>
<td><i>df = n-1</i>
<p>• Normal population
</p>
</td></tr>
<tr>
<td>Chi-squared test for goodness of fit
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \chi ^{2}=\sum ^{k}{\frac {({\text{observed}}-{\text{expected}})^{2}}{\text{expected}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>χ<!-- χ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
        <mo>=</mo>
        <mover>
          <mo>∑<!-- ∑ --></mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>k</mi>
          </mrow>
        </mover>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <mrow>
              <mo stretchy="false">(</mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mtext>observed</mtext>
              </mrow>
              <mo>−<!-- − --></mo>
              <mrow class="MJX-TeXAtom-ORD">
                <mtext>expected</mtext>
              </mrow>
              <msup>
                <mo stretchy="false">)</mo>
                <mrow class="MJX-TeXAtom-ORD">
                  <mn>2</mn>
                </mrow>
              </msup>
            </mrow>
            <mtext>expected</mtext>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \chi ^{2}=\sum ^{k}{\frac {({\text{observed}}-{\text{expected}})^{2}}{\text{expected}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/09e6396747ba7b2d5e987f127e5ef8804084db41" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.338ex; width:33.604ex; height:6.676ex;" alt="\chi^2=\sum^k\frac{(\text{observed}-\text{expected})^2}{\text{expected}}"></span>
</td>
<td><i>df = k</i>&nbsp;−&nbsp;1&nbsp;−&nbsp;<i># parameters estimated</i>, and one of these must hold.
<p>• All expected counts are at least 5.<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup>
</p><p>• All expected counts are &gt;&nbsp;1 and no more than 20% of expected counts are less than&nbsp;5<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup>
</p>
</td></tr>
<tr>
<td>Two-sample F test for equality of variances
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle F={\frac {s_{1}^{2}}{s_{2}^{2}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>F</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <mfrac>
            <msubsup>
              <mi>s</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>1</mn>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msubsup>
            <msubsup>
              <mi>s</mi>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
              <mrow class="MJX-TeXAtom-ORD">
                <mn>2</mn>
              </mrow>
            </msubsup>
          </mfrac>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle F={\frac {s_{1}^{2}}{s_{2}^{2}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0a02686bbefdad27c57e5f8226547764928b4d88" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.838ex; width:7.82ex; height:6.843ex;" alt="F=\frac{s_1^2}{s_2^2}"></span>
</td>
<td>Normal populations<br>Arrange so <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle s_{1}^{2}\geq s_{2}^{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msubsup>
          <mi>s</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msubsup>
        <mo>≥<!-- ≥ --></mo>
        <msubsup>
          <mi>s</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msubsup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle s_{1}^{2}\geq s_{2}^{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/fb6bd2312ee4a6409b3a9285483da9ba691c5c62" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -1.005ex; width:7.388ex; height:3.176ex;" alt="s_1^2 \ge s_2^2"></span> and reject H<sub>0</sub> for <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle F>F(\alpha /2,n_{1}-1,n_{2}-1)}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>F</mi>
        <mo>&gt;</mo>
        <mi>F</mi>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mrow class="MJX-TeXAtom-ORD">
          <mo>/</mo>
        </mrow>
        <mn>2</mn>
        <mo>,</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mo>,</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
        <mo>−<!-- − --></mo>
        <mn>1</mn>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle F&gt;F(\alpha /2,n_{1}-1,n_{2}-1)}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cfc2e9785db49ddace6d6b3e62a08cb663b49a65" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:27.173ex; height:2.843ex;" alt="F > F(\alpha/2,n_1-1,n_2-1)"></span><sup id="cite_ref-6" class="reference"><a href="#cite_note-6">[6]</a></sup>
</td></tr>
<tr>
<td><a href="/wiki/Regression_analysis#Diagnostics" title="Regression analysis">Regression</a> <i>t</i>-test of <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle H_{0}\colon R^{2}=0.}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>H</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msub>
        <mo>:<!-- : --></mo>
        <msup>
          <mi>R</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
        <mo>=</mo>
        <mn>0.</mn>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle H_{0}\colon R^{2}=0.}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9f9cee2e291886cf38af7e76fcac3913dc4806a0" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:11.745ex; height:3.009ex;" alt="H_0\colon R^2=0."></span>
</td>
<td align="center"><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle t={\sqrt {\frac {R^{2}(n-k-1^{*})}{1-R^{2}}}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>t</mi>
        <mo>=</mo>
        <mrow class="MJX-TeXAtom-ORD">
          <msqrt>
            <mfrac>
              <mrow>
                <msup>
                  <mi>R</mi>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mn>2</mn>
                  </mrow>
                </msup>
                <mo stretchy="false">(</mo>
                <mi>n</mi>
                <mo>−<!-- − --></mo>
                <mi>k</mi>
                <mo>−<!-- − --></mo>
                <msup>
                  <mn>1</mn>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mo>∗<!-- ∗ --></mo>
                  </mrow>
                </msup>
                <mo stretchy="false">)</mo>
              </mrow>
              <mrow>
                <mn>1</mn>
                <mo>−<!-- − --></mo>
                <msup>
                  <mi>R</mi>
                  <mrow class="MJX-TeXAtom-ORD">
                    <mn>2</mn>
                  </mrow>
                </msup>
              </mrow>
            </mfrac>
          </msqrt>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t={\sqrt {\frac {R^{2}(n-k-1^{*})}{1-R^{2}}}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/e36f2591428ae162794a84ec88a096037f0bfec6" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.005ex; width:22.229ex; height:7.676ex;" alt="t=\sqrt{\frac{R^2(n-k-1^*)}{1-R^2}}"></span>
</td>
<td>Reject <i>H</i><sub>0</sub> for <span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle t>t(\alpha /2,n-k-1^{*})}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>t</mi>
        <mo>&gt;</mo>
        <mi>t</mi>
        <mo stretchy="false">(</mo>
        <mi>α<!-- α --></mi>
        <mrow class="MJX-TeXAtom-ORD">
          <mo>/</mo>
        </mrow>
        <mn>2</mn>
        <mo>,</mo>
        <mi>n</mi>
        <mo>−<!-- − --></mo>
        <mi>k</mi>
        <mo>−<!-- − --></mo>
        <msup>
          <mn>1</mn>
          <mrow class="MJX-TeXAtom-ORD">
            <mo>∗<!-- ∗ --></mo>
          </mrow>
        </msup>
        <mo stretchy="false">)</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t&gt;t(\alpha /2,n-k-1^{*})}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/56c72889d9cf9f7ea18cea530d01c22dcfd64208" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:21.937ex; height:2.843ex;" alt="t > t(\alpha/2,n-k-1^*)"></span><sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup><br>*Subtract 1 for intercept; <i>k</i> terms contain independent variables.
</td></tr>
<tr>
<td colspan="3">In general, the subscript 0 indicates a value taken from the <a href="/wiki/Null_hypothesis" title="Null hypothesis">null hypothesis</a>, H<sub>0</sub>, which should be used as much as possible in constructing its test statistic. <i>... Definitions of other symbols:</i>
<table border="0">
<tbody><tr>
<td style="vertical-align:top;">
<ul><li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \alpha }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>α<!-- α --></mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \alpha }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b79333175c8b3f0840bfb4ec41b8072c83ea88d3" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.488ex; height:1.676ex;" alt="\alpha "></span>, the <a href="/wiki/Probability" title="Probability">probability</a> of <a href="/wiki/Type_I_and_type_II_errors" title="Type I and type II errors">Type I error</a> (rejecting a <a href="/wiki/Null_hypothesis" title="Null hypothesis">null hypothesis</a> when it is in fact true)</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle n}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>n</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle n}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.395ex; height:1.676ex;" alt="n"></span> = <a href="/wiki/Sample_size" class="mw-redirect" title="Sample size">sample size</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle n_{1}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle n_{1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ee784b70e772f55ede5e6e0bdc929994bff63413" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.449ex; height:2.009ex;" alt="n_{1}"></span> = sample 1 size</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle n_{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle n_{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/840e456e3058bc0be28e5cf653b170cdbfcc3be4" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.449ex; height:2.009ex;" alt="n_{2}"></span> = sample 2 size</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle {\overline {x}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mover>
            <mi>x</mi>
            <mo accent="false">¯<!-- ¯ --></mo>
          </mover>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle {\overline {x}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9fa4039bbc2a0048c3a3c02e5fd24390cab0dc97" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.445ex; height:2.343ex;" alt="{\overline {x}}"></span> = <a href="/wiki/Sample_mean" class="mw-redirect" title="Sample mean">sample mean</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \mu _{0}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>μ<!-- μ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu _{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/fe2fd9b8decb38a3cd158e7b6c0c6e2d987fefcc" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:2.456ex; height:2.176ex;" alt="\mu _{0}"></span> = hypothesized <a href="/wiki/Population_mean" class="mw-redirect" title="Population mean">population mean</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \mu _{1}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>μ<!-- μ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu _{1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d6899621035d3359b9c1c064739b54c7004e220d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:2.456ex; height:2.176ex;" alt="\mu _{1}"></span> = population 1 mean</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \mu _{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>μ<!-- μ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \mu _{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/2f841461ae8f2eafec3fe879f7c061a73c2f7170" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:2.456ex; height:2.176ex;" alt="\mu _{2}"></span> = population 2 mean</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \sigma }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>σ<!-- σ --></mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \sigma }</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/59f59b7c3e6fdb1d0365a494b81fb9a696138c36" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.33ex; height:1.676ex;" alt="\sigma "></span> = <a href="/wiki/Population_standard_deviation" class="mw-redirect" title="Population standard deviation">population standard deviation</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \sigma ^{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>σ<!-- σ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \sigma ^{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/53a5c55e536acf250c1d3e0f754be5692b843ef5" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.385ex; height:2.676ex;" alt="\sigma ^{2}"></span> = <a href="/wiki/Population_variance" class="mw-redirect" title="Population variance">population variance</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle s}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>s</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle s}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/01d131dfd7673938b947072a13a9744fe997e632" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.09ex; height:1.676ex;" alt="s"></span> = <a href="/wiki/Sample_standard_deviation" class="mw-redirect" title="Sample standard deviation">sample standard deviation</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \sum ^{k}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mover>
          <mo>∑<!-- ∑ --></mo>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>k</mi>
          </mrow>
        </mover>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \sum ^{k}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/df79e9ed22803a0e0a023f7ffbb40a6cb2b15df7" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -1.338ex; width:3.355ex; height:5.676ex;" alt="\sum^k"></span> = sum (of <i>k</i> numbers)</li></ul>
</td>
<td style="vertical-align:top;">
<ul><li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle s^{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>s</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle s^{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/58d7841cee3671436949ee789b84a848fd150bd3" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:2.145ex; height:2.676ex;" alt="s^{2}"></span> = <a href="/wiki/Sample_variance" class="mw-redirect" title="Sample variance">sample variance</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle s_{1}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>s</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle s_{1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/eb8baad278d51283e0ef3c99898d583cf2c8a8fd" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.145ex; height:2.009ex;" alt="s_{1}"></span> = sample 1 standard deviation</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle s_{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>s</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle s_{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d4b9a7acc0ae8f54da4b7f4eef2c777d44faecd4" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.145ex; height:2.009ex;" alt="s_{2}"></span> = sample 2 standard deviation</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle t}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>t</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle t}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/65658b7b223af9e1acc877d848888ecdb4466560" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:0.84ex; height:2.009ex;" alt="t"></span> = <a href="/wiki/T_statistic" class="mw-redirect" title="T statistic">t statistic</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle df}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>d</mi>
        <mi>f</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle df}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/53181e2067a93b6bbf150042723cb059d9d2d26f" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.494ex; height:2.509ex;" alt="df"></span> = <a href="/wiki/Degrees_of_freedom_(statistics)" title="Degrees of freedom (statistics)">degrees of freedom</a></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle {\overline {d}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mover>
            <mi>d</mi>
            <mo accent="false">¯<!-- ¯ --></mo>
          </mover>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle {\overline {d}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/147fdfc5e4452853cb2946348d7e2e9cdb11a6d4" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.335ex; height:3.009ex;" alt="\overline{d}"></span> = sample mean of differences</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle d_{0}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>d</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle d_{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4740381c16ea98c4132510daa642e93c1e42c049" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.263ex; height:2.509ex;" alt="d_0"></span> = hypothesized population mean difference</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle s_{d}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>s</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>d</mi>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle s_{d}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4e6c51f4971ab7c0a784790aa1de2040086ddcbe" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.182ex; height:2.009ex;" alt="s_d"></span> = standard deviation of differences</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \chi ^{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msup>
          <mi>χ<!-- χ --></mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msup>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \chi ^{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8c0cc9237ec72a1da6d18bc8e7fb24cdda43a49a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:2.509ex; height:3.009ex;" alt="\chi ^{2}"></span> = <a href="/wiki/Chi-squared_statistic" class="mw-redirect" title="Chi-squared statistic">Chi-squared statistic</a></li></ul>
</td>
<td style="vertical-align:top;">
<ul><li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle {\hat {p}}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mrow class="MJX-TeXAtom-ORD">
          <mrow class="MJX-TeXAtom-ORD">
            <mover>
              <mi>p</mi>
              <mo stretchy="false">^<!-- ^ --></mo>
            </mover>
          </mrow>
        </mrow>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle {\hat {p}}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/8bd4c026f1b3413adc58b9b65e89e62bce92c85a" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; margin-left: -0.089ex; width:1.449ex; height:2.509ex;" alt="{\hat {p}}"></span> = <i>x/n</i> = sample <a href="/wiki/Ratio" title="Ratio">proportion</a>, unless specified otherwise</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle p_{0}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>p</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>0</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle p_{0}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/2b969ada68a88e2aeba9a2d2096abaf1fd53c21d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; margin-left: -0.089ex; width:2.313ex; height:2.009ex;" alt="p_{0}"></span> = hypothesized population proportion</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle p_{1}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>p</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle p_{1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b9b58f22283ca46dd5da309cc34303b06a797783" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; margin-left: -0.089ex; width:2.313ex; height:2.009ex;" alt="p_{1}"></span> = proportion 1</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle p_{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>p</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle p_{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/43f1b08d7d69712872e051c2b33fdfa9f5d42319" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; margin-left: -0.089ex; width:2.313ex; height:2.009ex;" alt="p_{2}"></span> = proportion 2</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle d_{p}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>d</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mi>p</mi>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle d_{p}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/58a3efb685b5e6d0fa5be00ba01cf4e30a5641ce" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -1.005ex; width:2.268ex; height:2.843ex;" alt="d_{p}"></span> = hypothesized difference in proportion</li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \min\{n_{1},n_{2}\}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mo movablelimits="true" form="prefix">min</mo>
        <mo fence="false" stretchy="false">{</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
        <mo>,</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
        <mo fence="false" stretchy="false">}</mo>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle \min\{n_{1},n_{2}\}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/21bcfb1d500a794306ad3da6e63a97c268f2a2fc" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:12.132ex; height:2.843ex;" alt="\min\{n_1,n_2\} "></span> = minimum of <i>n</i><sub>1</sub> and <i>n</i><sub>2</sub></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle x_{1}=n_{1}p_{1}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>x</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
        <mo>=</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
        <msub>
          <mi>p</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>1</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle x_{1}=n_{1}p_{1}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/25762ac068cb7dcf5623fbbf2d4cde0bcfbf88e4" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:10.155ex; height:2.009ex;" alt="x_1 = n_1 p_1"></span></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle x_{2}=n_{2}p_{2}}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <msub>
          <mi>x</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
        <mo>=</mo>
        <msub>
          <mi>n</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
        <msub>
          <mi>p</mi>
          <mrow class="MJX-TeXAtom-ORD">
            <mn>2</mn>
          </mrow>
        </msub>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle x_{2}=n_{2}p_{2}}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/38041e7fc9d3e6c1487a035f8a247bc0365ab611" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.671ex; width:10.155ex; height:2.009ex;" alt="x_2 = n_2 p_2"></span></li>
<li><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle F}">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>F</mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex">{\displaystyle F}</annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/545fd099af8541605f7ee55f08225526be88ce57" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.741ex; height:2.176ex;" alt="F"></span> = <a href="/wiki/F_statistic" class="mw-redirect" title="F statistic">F statistic</a></li></ul>
</td></tr></tbody></table>
</td></tr></tbody></table>

---

### [Chi-squared Test](./chi-squared_test.ipynb)

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

If you don't have jupyter, run `pipenv install jupyter --dev`.

---

List your kernels:

```sh
jupyter-kernelspec list
```

If your Jupyter was installed under a specific virtual environment, you need to run the above list command under this env.