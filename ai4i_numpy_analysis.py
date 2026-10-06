import numpy as np


# ============================================
# 1. Load Dataset
# ============================================

data = np.genfromtxt(
    "ai4i2020.csv",
    delimiter=",",
    dtype=str,
    skip_header=1
)

print("Dataset shape:", data.shape)


# ============================================
# 2. Extract Machine Condition Data
# ============================================

# Columns:
# 0 - Air temperature
# 1 - Process temperature
# 2 - Rotational speed
# 3 - Torque
# 4 - Tool wear

machine_data = data[:, 3:8].astype(float)

print("Machine data shape:", machine_data.shape)


# ============================================
# 3. Basic Machine Statistics
# ============================================

rotational_speed = machine_data[:, 2]
torque = machine_data[:, 3]
tool_wear = machine_data[:, 4]

print("\n--- Rotational Speed ---")
print("Minimum:", rotational_speed.min())
print("Maximum:", rotational_speed.max())
print("Average:", rotational_speed.mean().round(2))

print("\n--- Torque ---")
print("Minimum:", torque.min())
print("Maximum:", torque.max())
print("Average:", torque.mean().round(2))
print("Range:", (torque.max() - torque.min()).round(2))

print("\n--- Tool Wear ---")
print("Minimum:", tool_wear.min())
print("Maximum:", tool_wear.max())
print("Average:", tool_wear.mean().round(2))
print("Range:", (tool_wear.max() - tool_wear.min()).round(2))


# ============================================
# 4. Temperature Analysis
# ============================================

air_temperature = machine_data[:, 0]
process_temperature = machine_data[:, 1]

average_air_temperature = air_temperature.mean()
average_process_temperature = process_temperature.mean()

temperature_difference = process_temperature - air_temperature

print("\n--- Temperature Analysis ---")
print("Average air temperature:",
      average_air_temperature.round(2), "K")
print("Average process temperature:",
      average_process_temperature.round(2), "K")
print("Average temperature difference:",
      temperature_difference.mean().round(2), "K")
print("Minimum temperature difference:",
      temperature_difference.min().round(2), "K")
print("Maximum temperature difference:",
      temperature_difference.max().round(2), "K")


# ============================================
# 5. Machine Failure Analysis
# ============================================

# Machine failure:
# 0 = No failure
# 1 = Failure

machine_failure = data[:, 8].astype(int)

total_records = machine_failure.shape[0]
failure_count = machine_failure.sum()
failure_rate = failure_count / total_records * 100

print("\n--- Machine Failure ---")
print("Total records:", total_records)
print("Machine failures:", failure_count)
print("Failure rate:", round(failure_rate, 2), "%")


# ============================================
# 6. Failed vs Non-Failed Machines
# ============================================

# Torque
failed_torque = torque[machine_failure == 1]
non_failed_torque = torque[machine_failure == 0]

# Tool wear
failed_tool_wear = tool_wear[machine_failure == 1]
non_failed_tool_wear = tool_wear[machine_failure == 0]

# Rotational speed
failed_speed = rotational_speed[machine_failure == 1]
non_failed_speed = rotational_speed[machine_failure == 0]

# Air temperature
failed_air_temperature = air_temperature[machine_failure == 1]
non_failed_air_temperature = air_temperature[machine_failure == 0]

# Process temperature
failed_process_temperature = process_temperature[machine_failure == 1]
non_failed_process_temperature = process_temperature[machine_failure == 0]


print("\n--- Failed vs Non-Failed: Average Values ---")

print("\nTorque")
print("Failed:", failed_torque.mean().round(2), "Nm")
print("Non-failed:", non_failed_torque.mean().round(2), "Nm")

print("\nTool Wear")
print("Failed:", failed_tool_wear.mean().round(2), "min")
print("Non-failed:", non_failed_tool_wear.mean().round(2), "min")

print("\nRotational Speed")
print("Failed:", failed_speed.mean().round(2), "rpm")
print("Non-failed:", non_failed_speed.mean().round(2), "rpm")

print("\nAir Temperature")
print("Failed:", failed_air_temperature.mean().round(2), "K")
print("Non-failed:", non_failed_air_temperature.mean().round(2), "K")

print("\nProcess Temperature")
print("Failed:", failed_process_temperature.mean().round(2), "K")
print("Non-failed:", non_failed_process_temperature.mean().round(2), "K")


# ============================================
# 7. Percentile Analysis
# ============================================

print("\n--- Torque Percentiles ---")

print("Median torque - Failed:",
      np.median(failed_torque), "Nm")

print("Median torque - Non-failed:",
      np.median(non_failed_torque), "Nm")

print("75th percentile torque - Failed:",
      np.percentile(failed_torque, 75), "Nm")

print("75th percentile torque - Non-failed:",
      np.percentile(non_failed_torque, 75), "Nm")


print("\n--- Tool Wear Percentiles ---")

print("Median tool wear - Failed:",
      np.median(failed_tool_wear), "min")

print("Median tool wear - Non-failed:",
      np.median(non_failed_tool_wear), "min")

print("75th percentile tool wear - Failed:",
      np.percentile(failed_tool_wear, 75), "min")

print("75th percentile tool wear - Non-failed:",
      np.percentile(non_failed_tool_wear, 75), "min")