&nbsp;**Document Key Findings**

Create notebooks/findings.md with observations:



**Key Findings**:

✅ Dataset Size:



Train: 125,973 rows × 42 columns



Test: 22,544 rows × 42 columns



✅ **No Missing Values:**



Both datasets are clean (no NaN values)



✅ **Class Distribution (Imbalanced):**



normal: 53.5%



DoS: 36.5%



probe: 9.3%



r2l: 0.8%



u2r: 0.04%



✅ **Feature Types:**



Numerical: duration, src\_bytes, dst\_bytes, etc.



Categorical: protocol\_type, service, flag



✅ **High Correlation:**



Some features (dst\_bytes, src\_bytes) are highly correlated

