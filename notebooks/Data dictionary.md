# Network Intrusion Detection Data Dictionary

## Core Features Overview

| Feature Category       | Key Attributes               | Security Relevance                  |
|------------------------|------------------------------|-------------------------------------|
| **Connection Metadata**| duration, protocol_type      | Identifies scanning/slowloris attacks |
| **Traffic Volume**     | src_bytes, dst_bytes         | Detects DDoS/data exfiltration      |
| **Authentication**     | logged_in, failed_logins     | Reveals brute-force attempts        |
| **Privilege**          | root_shell, su_attempted     | Indicates privilege escalation      |

## Detailed Feature Classification

### 1. Network Characteristics
- **duration**: Connection time in seconds (typical: 0-10s, attacks: >30s)
- **protocol_type**: 
  - TCP (82% of traffic) - Common attack vector
  - ICMP (16%) - Ping flood vulnerability
  - UDP (2%) - DNS amplification risk

### 2. Traffic Patterns
| Feature       | Normal Range | Attack Threshold | Associated Threat       |
|---------------|--------------|------------------|-------------------------|
| src_bytes     | 0-1KB        | >10KB            | Data exfiltration       |
| dst_bytes     | 0-1KB        | >100KB           | DDoS payloads           |
| wrong_fragment| 0            | ≥1               | Packet fragmentation    |

### 3. Security Indicators
- **logged_in**: Binary flag for successful authentication
- **root_shell**: Critical indicator of system compromise
- **num_file_creations**: >1 suggests ransomware activity

<<<<<<< HEAD
## Visualization Reference
![Feature Correlation Matrix](images/feature_correlation.png)  
*Figure 1: Relationships between key numerical features*
=======
## Visualization Reference 
*Figure 1: Relationships between key numerical features*
>>>>>>> 73ae0943036290ed6fec8ee3472f7f9a4539b158
