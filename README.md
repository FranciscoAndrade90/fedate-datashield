# Federated Average Treatment Effect Estimation for Multi-Site RCTs with DataSHIELD
Francisco Andrade†, Rémi Khellaf†, Julie Josse
2026-10-10

### Citation

Submitted to Computo.

### Badges

[![build and
publish](https://github.com/FranciscoAndrade90/fedate-datashield/actions/workflows/build.yml/badge.svg)](https://github.com/FranciscoAndrade90/fedate-datashield/actions/workflows/build.yml)
[![reviews](https://img.shields.io/badge/review-report-blue)](https://github.com/FranciscoAndrade90/fedate-datashield/issues?q=is%3Aopen+is%3Aissue+label%3Areview)
[![SWH](https://archive.softwareheritage.org/badge/origin/https://github.com/FranciscoAndrade90/fedate-datashield)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/FranciscoAndrade90/fedate-datashield)
[![DOI:10.5072/computo.0000](https://img.shields.io/badge/DOI-10.5072%2Fcomputo.0000-034E79.svg)](https://doi.org/10.5072/computo.0000)
[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/80x15.png)](http://creativecommons.org/licenses/by/4.0/)

### Authors’ affiliations

- Francisco Andrade† (PreMeDICaL, Inria, Inserm, Idesp, UMR 1318, Université de Montpellier, UMR1346, HeKA, Inserm, Inria, Université Paris Cité)
- Rémi Khellaf† (PreMeDICaL, Inria, Inserm, Idesp, UMR 1318, Université de Montpellier)
- Julie Josse (PreMeDICaL, Inria, Inserm, Idesp, UMR 1318, Université de Montpellier)

### Abstract

We introduce `dsFedAte` and `dsFedAteClient`, two companion R packages
for federated estimation of the average treatment effect (ATE) from
multiple randomized controlled trials (RCTs), without sharing
individual-level data. Built on the open-source DataSHIELD
privacy-preserving infrastructure, they implement a covariate-adjusted
G-formula estimator accommodating heterogeneous covariate distributions
and study effects. Unlike iterative federated optimization methods, our
approach fits arm-specific linear outcome models in a single
communication round by aggregating local sufficient statistics, yielding
estimates identical to those obtained from centrally pooled data. The
entire analysis is accessible through a single client-side function,
`ds.EstimateAte()`. Beyond implementation, we also present
methodological contributions. First, we derive the asymptotic variance
of the ATE estimator, accounting for heterogeneous covariate
distributions and study effects, and express its estimator in terms of
locally aggregable quantities, enabling federated confidence intervals
equivalent to those obtained from pooled data. Second, we establish
consistency and asymptotic normality under misspecified linear outcome
models, showing that covariate adjustment is asymptotically at least as
efficient as the unadjusted stratified difference-in-means estimator. We
illustrate the packages through reproducible examples using the DSLite
simulation environment, covering homogeneous and heterogeneous
populations, DataSHIELD disclosure controls, and adjustment for study
effects. A simulation study validates the theoretical results and
demonstrates nominal confidence interval coverage.
