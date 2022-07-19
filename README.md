# Gurobi-Portfolio
## Basic process

### Math model
    Decision variable(unknown)
    Objective 
    Constraints
    Coefficient
### Modeling process
    1. Create model
    2. Setting variable and update
    3. Setting objective and constraints
    4. Optimize
# MV Model
**Decision variable**: weight
**Coefficient**: variance, covariance, return, expective return
    
**Objective**: 
${Min}\,\sigma_{p}=\sum_{i=1}^{n}w_{i}^{2}\sigma_{i}^{2}+\sum_{i=1}^{n}\sum_{j=1(j\neq i)}^{n}\sigma_{ij}w_{i}w_{j}$

**Constraints**: 
$\begin{split}s.t.&\sum_{i=1}^{n}r_{i}w_{i}\geq \mu\\
&\sum_{i=1}^{n}w_{i}=1\\
&w_{i}\geq1,i=1,2,...,n\end{split}$