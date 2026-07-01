# TDEE Estimator — Numerical Methods Approach

A numerical computing pipeline that estimates Total Daily Energy Expenditure (TDEE)
across distinct dietary phases (bulk/cut) using personal weight and caloric intake data.

## Overview
Rather than relying on static TDEE formulas, this project treats TDEE estimation as
a data-driven numerical problem:

- **Interpolation** — fills missing weight/calorie entries using linear and cubic
  spline methods, with error comparison (MAE/RMSE) to justify method selection
- **Phase Detection** — identifies bulk/cut phases via polynomial curve fitting and
  numerical differentiation (5-point stencil) to find slope sign changes
- **Piecewise Polynomial Regression** — fits an independent polynomial curve to each
  detected phase (least-squares via normal equations), capturing the deceleration in
  weight change caused by adaptive TDEE — a single global fit or straight line
  cannot represent this without overfitting or Runge's-phenomenon-style artifacts
- **BIC-Guided Degree Selection** — chooses the polynomial degree per segment by
  minimizing Bayesian Information Criterion, capped at a maximum degree justified by
  diminishing improvement and visual inspection, to avoid fitting local noise rather
  than the underlying phase trend
- **TDEE Estimation** — back-calculates average TDEE per phase using the Mean Value
  Theorem (average slope of the fitted curve) combined with average caloric intake

## Methods Used
- Linear & cubic spline interpolation
- Numerical differentiation (finite difference, 5-point stencil)
- BIC-based polynomial degree selection
- Least-squares regression (normal equations)
- Piecewise polynomial regression across phase segments

## Tech Stack
Python · NumPy · Pandas · SciPy · Matplotlib