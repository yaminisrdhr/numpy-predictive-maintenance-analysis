# NumPy Predictive Maintenance Analysis

## Project Overview

This project applies NumPy to a real-world-style industrial predictive maintenance dataset.

The goal was to use NumPy to explore machine operating conditions and compare failed and non-failed machines.

This project is part of my learning journey in Python, NumPy, and Industrial Engineering.

## Dataset

The project uses the **AI4I 2020 Predictive Maintenance Dataset** from the UCI Machine Learning Repository.

The dataset contains **10,000 machine records** with variables including:

- Air temperature
- Process temperature
- Rotational speed
- Torque
- Tool wear
- Machine failure
- Failure-mode indicators

**Dataset source:** UCI Machine Learning Repository — AI4I 2020 Predictive Maintenance Dataset

The dataset is not included in this repository. It can be obtained from the official UCI source.

## Analysis Performed

### Basic Machine Statistics

Calculated:

- Average rotational speed
- Minimum and maximum rotational speed
- Average torque
- Minimum and maximum torque
- Torque range
- Average tool wear
- Tool wear range

### Temperature Analysis

Calculated:

- Average air temperature
- Average process temperature
- Process-to-air temperature difference
- Minimum and maximum temperature difference

### Machine Failure Analysis

Calculated:

- Total number of records
- Number of machine failures
- Overall failure rate

The dataset contains:

- **10,000 total records**
- **339 machine failures**
- **3.39% failure rate**

### Failed vs Non-Failed Machine Comparison

Compared average operating conditions between failed and non-failed machines:

| Variable | Failed | Non-Failed |
|---|---:|---:|
| Air temperature (K) | 300.89 | 299.97 |
| Process temperature (K) | 310.29 | 310.00 |
| Rotational speed (rpm) | 1496.49 | 1540.26 |
| Torque (Nm) | 50.17 | 39.63 |
| Tool wear (min) | 143.78 | 106.69 |

### Percentile Analysis

Calculated the median and 75th percentile for torque and tool wear.

#### Torque

| Statistic | Failed | Non-Failed |
|---|---:|---:|
| Median | 53.7 Nm | 39.9 Nm |
| 75th percentile | 61.2 Nm | 46.3 Nm |

#### Tool Wear

| Statistic | Failed | Non-Failed |
|---|---:|---:|
| Median | 165 min | 107 min |
| 75th percentile | 207.5 min | 160 min |

## Key Findings

In this dataset, machine failures are associated with noticeable differences in several operating conditions.

The largest differences were observed in:

- **Torque**
- **Tool wear**
- **Rotational speed**

Failed machine records showed higher average torque and tool wear, while average rotational speed was somewhat lower.

Temperature differences between failed and non-failed records were comparatively smaller.

These observations describe associations in the dataset and should **not** be interpreted as proof that a particular variable directly causes machine failure.

## NumPy Concepts Demonstrated

- NumPy arrays
- `np.genfromtxt()`
- 2D indexing and slicing
- Column extraction
- `.astype()`
- `.shape`
- `.min()`
- `.max()`
- `.sum()`
- `.mean()`
- Vectorized array operations
- Boolean indexing
- `np.median()`
- `np.percentile()`

## Manufacturing Context

This project demonstrates how machine operating data can be explored to identify differences between failed and non-failed equipment.

The analysis is intended as a learning project connecting Python/NumPy skills with predictive maintenance and manufacturing data analysis.

## Limitations

The AI4I 2020 dataset does not contain production quantity, cycle time, operating time, or downtime duration.

Therefore, this project does **not** attempt to calculate:

- Process capacity
- Flow rate
- Utilisation
- OEE

These metrics require appropriate production and time-based data and will be explored separately.

## Learning Outcome

This project helped me move from basic Python calculations to working with multidimensional NumPy arrays and applying Boolean filtering and statistical analysis to an industrial dataset.

The main learning approach was:

**Learn → Understand → Implement → Create evidence**

## Next Steps

Future projects will apply additional Python, data analysis, and Industrial Engineering concepts to manufacturing problems.
