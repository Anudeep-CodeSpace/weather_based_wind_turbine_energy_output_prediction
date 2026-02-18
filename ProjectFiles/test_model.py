# Test the saved Wind Mill Power Prediction model
# This script loads the saved model and runs test predictions

import joblib
import pandas as pd

# Load the saved model
model = joblib.load('power_prediction.sav')
print("Model loaded successfully!")
print(f"Model type: {type(model).__name__}")
print(f"Number of estimators: {model.n_estimators}")
print(f"Max depth: {model.max_depth}")

# Test predictions with sample inputs
# Features: ['WindSpeed(m/s)', 'Theoretical_Power_Curve (KWh)']
# Target: 'ActivePower(kW)'
test_cases = [
    {'WindSpeed(m/s)': 8.18, 'Theoretical_Power_Curve (KWh)': 1638.50},
    {'WindSpeed(m/s)': 12.92, 'Theoretical_Power_Curve (KWh)': 3597.33},
    {'WindSpeed(m/s)': 6.38, 'Theoretical_Power_Curve (KWh)': 759.43},
    {'WindSpeed(m/s)': 7.85, 'Theoretical_Power_Curve (KWh)': 1445.55},
    {'WindSpeed(m/s)': 6.87, 'Theoretical_Power_Curve (KWh)': 960.60},
    {'WindSpeed(m/s)': 4.14, 'Theoretical_Power_Curve (KWh)': 148.88}
]

print("\n" + "=" * 98)
print(f"{'WindSpeed(m/s)':>20} {'Theoretical_Power_Curve (KWh)':>40} {'Predicted ActivePower(kW)':>30}")
print("=" * 98)

for case in test_cases:
    val_X = pd.DataFrame(
        [[case['Theoretical_Power_Curve (KWh)'], case['WindSpeed(m/s)']]],
        columns=['Theoretical_Power_Curve (KWh)', 'WindSpeed(m/s)']
    )
    prediction = model.predict(val_X)[0]
    print(f"{case['WindSpeed(m/s)']:>20.2f} {case['Theoretical_Power_Curve (KWh)']:>40.2f} {prediction:>30.2f}")

print("=" * 98)
print("\nAll Tests completed Successfully")
