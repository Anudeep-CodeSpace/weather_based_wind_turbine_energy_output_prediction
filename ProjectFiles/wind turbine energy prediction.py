# Wind Turbine Energy Prediction - Complete Pipeline
# This script contains the full ML pipeline from data loading to model saving

######################################
# <--- STEP 1: Import Libraries ---> #
######################################
print("Importing Libraries...")
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score as R2, mean_absolute_error as mae, root_mean_squared_error as rmse

import warnings
warnings.filterwarnings('ignore')
print("Libraries Imported Successfully!")
##############################################
# <--- STEP 2: Load and Analyze Dataset ---> #
##############################################

path = r'data/T1.csv'
df = pd.read_csv(path)

# Rename columns for better understanding
df.rename(columns={
    "Date/Time": "Time",
    "LV ActivePower (kW)": "ActivePower(kW)",
    "Wind Speed (m/s)": "WindSpeed(m/s)",
    "Wind Direction (°)": "Wind_Direction"
}, inplace=True)

# Adjust the time column format
df['Time'] = pd.to_datetime(df['Time'], format="%d %m %Y %H:%M", errors="coerce")

# Dataset Details
print(f"Dataset Shape: {df.shape}")
print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print(df.head())

######################################
# <--- STEP 3: Data Description ---> #
######################################
print("\n" + "=" * 50)
print("DATASET INFO")
print("=" * 50)
df.info()

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

##########################################
# <--- STEP 4: Correlation Analysis ---> #
##########################################
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
print("\n" + "=" * 50)
print("Correlation with \"ActivePower(kW)\" (Target):")
print("=" * 50)
power_corr = corr['ActivePower(kW)'].drop('ActivePower(kW)').sort_values(ascending=False)
for feature, value in power_corr.items():
    print(f"{feature:>25s} : {value:+.4f}")

# Correlation HeatMap
plt.figure(figsize=(10, 8))
ax = sns.heatmap(corr, vmin=-1, vmax=1, annot=True, fmt='.2f', square=True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.title("Correlation Heatmap", fontsize=14, pad=20)
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()

##########################################################################
# <--- STEP 5: Independent and Dependent Variables & Data Splitting ---> #
##########################################################################

# Data Cleaning
df = df[['WindSpeed(m/s)', 'Theoretical_Power_Curve (KWh)', 'ActivePower(kW)']].dropna()

# Apply logic filters to delete entries that are physically impossible
CUT_IN_SPEED = 3.5 # Turbine starts power generation only above this speed
RATED_POWER = 3600
STOP_SPEED = 25.5

# Power is generated only above the CUT-IN Speed and Turbine is stopped at the Maximum STOP Speed
df = df[(df['WindSpeed(m/s)'] >= CUT_IN_SPEED) & 
        (df['WindSpeed(m/s)'] <= STOP_SPEED)]

# Active Power is always positive and less than rated Power Ceiling
df = df[(df['ActivePower(kW)'] > 0) &
        (df['ActivePower(kW)'] <= RATED_POWER + 100)]

# Define Variables
y = df['ActivePower(kW)'] # Target
X = df[['Theoretical_Power_Curve (KWh)', 'WindSpeed(m/s)']] # Input Parameters

# Train-Test splitting
train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.2, random_state=0)
print(f"\nTraining Samples: {len(train_X)}")
print(f"Testing Samples: {len(val_X)}")

##############################################################
# <--- STEP 6: Model Building - Random Forest Regressor ---> #
##############################################################
rf_model = RandomForestRegressor(
    n_estimators=200,
    max_depth=6,
    min_samples_leaf=15,
    random_state=42
)

print("Training the Random Forest Model.....")
rf_model.fit(train_X, train_y)
print("Model Trained Successfully!")

######################################
# <--- STEP 7: Model Evaluation ---> #
######################################

# Predicting for test data
power_preds = rf_model.predict(val_X)

# Calculate Performance Metrics
r2_score = R2(val_y, power_preds)
mean_abs_err = mae(val_y, power_preds)
root_mean_sq_err = rmse(val_y, power_preds)

# Print the metrics
print("\n" + "=" * 50)
print("MODEL EVALUATION RESULTS")
print("=" * 50)
print(f"R² Score                      : {r2_score:.4f}")
print(f"Mean Absolute Error (MAE)     : {mean_abs_err:.4f}")
print(f"Root Mean Squared Error (RMSE): {root_mean_sq_err:.4f}")

# Step 8: Save the Model
joblib.dump(rf_model, "power_prediction.sav")
print("\nModel saved as 'power_prediction.sav'")
