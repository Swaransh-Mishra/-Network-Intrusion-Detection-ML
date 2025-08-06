# Exploratory Data Analysis Report

## Dataset Composition
- **Total Observations**: 148,517 (125,973 training / 22,544 testing)
- **Features**: 41 network metrics + 1 target variable
- **Data Quality**: Complete (no missing values)

## Attack Distribution
| Class    | Frequency | Security Impact Level |
|----------|-----------|-----------------------|
| normal   | 53.5%     | Baseline              |
| DoS      | 36.5%     | Critical              |
| probe    | 9.3%      | High                  |
| r2l      | 0.8%      | Severe                |
| u2r      | 0.04%     | Critical              |

## Critical Insights

### 1. Traffic Anomalies
- **DoS Attacks**: Characterized by:
  - High `dst_bytes` (>100KB)
  - Short `duration` (<2s)
  - TCP `protocol_type`

### 2. Scanning Activity
- **Probes** exhibit:
  - Elevated `serror_rate` (>0.7)
  - High `count` (>50 connections)
  - `flag=S0` (unanswered SYNs)

### 3. Rare Attack Patterns
- **u2r Attacks** (0.04%):
  - `root_shell=1`
  - `num_file_creations` >3
  - `su_attempted=1`

## Recommended Actions

### Feature Engineering
1. Create composite features:
   - `bytes_ratio = src_bytes/dst_bytes`
   - `error_density = serror_rate × count`

### Modeling Strategy
- **Class Weighting**: Prioritize recall for u2r/r2l
- **Validation**: Stratified k-fold cross-validation

*Figure 2: Class imbalance visualization*
