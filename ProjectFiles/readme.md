# <img width="312" height="63" alt="Screenshot 2026-02-18 191843" src="https://github.com/user-attachments/assets/a11aea4c-fc09-450c-b9d3-cefd26db3975" />


## A Weather-Based Prediction of Wind Turbine Energy Output: A Next-Generation Approach to Renewable Energy Management

This project uses real-time meteorological data to accurately forecast wind turbine energy generation. Our ML model uses theoretical power capacity &amp; wind speed to deliver precise KWh predictions — enabling smarter grid decisions.

---

## Project Demo Video


https://github.com/user-attachments/assets/55d3c3eb-3d7a-46a3-a8c4-0239cfcd2a13


---

## Team Details
<table>
  <tr>
    <td><strong>Team ID</strong></td>
    <td>LTVIP2026TMIDS80501</td>
  </tr>
  <tr>
    <td><strong>Team Leader</strong></td>
    <td>Anudeep Reddy Bandi</td>
  </tr>
  <tr>
    <td rowspan="2"><strong>Team Members</strong></td>
    <td>Giri Kumar Pandaram</td>
  </tr>
  <tr>
    <td>Nagaraju Pasupula</td>
  </tr>
</table>

---

## Project Structure
```
weather_based_wind_turbine_energy_output_prediction/
├── Documents/
├── Video Demo/
├── ProjectFiles/
|    ├── data/
|    │   └── ###T1.csv                            # Downloaded Dataset (from Kaggle)
|    ├── flask_server/
|    │   ├── static/
|    │   │   └── style.css                        # Stylesheet for the web app
|    │   ├── templates/
|    │   │   ├── home.html                        # Landing page
|    │   │   └── predict.html                     # Weather API & prediction page
|    |   ├── __init__.py                          # Python Package Declaration
|    │   ├── app.py                               # Flask app entry point
|    │   └── windApp.py                           # Flask routes & prediction logic
|    ├── download_data.py                         # Download Dataset from Kaggle using kaggleApi
|    ├── Wind_mill_model.ipynb                    # Jupyter Notebook (full ML pipeline)
|    ├── wind turbine energy prediction.py        # Standalone ML pipeline script
|    ├── test_model.py                            # Script to test saved model
|    ├── main.py                                  # Entry point for the project
|    ├── pyproject.toml                           # UV-Project Configuration
|    ├── uv.lock                                  # UV-Dependencies' Version lock
|    ├── .python-version                          # Python Version recommended for the project
|    └── readme.md
└── README.md
```

---

## Technologies Used
<table>
    <tr>
        <th>Category</th>
        <th>Technology Used</th>
    </tr>
    <tr>
        <td><strong>Language</strong></td>
        <td>Python</td>
    </tr>
    <tr>
        <td><strong>Package Manager</strong></td>
        <td><a href="https://docs.astral.sh/uv/">UV</a></td>
    </tr>
    <tr>
        <td><strong>ML Libraries</strong></td>
        <td>Scikit-Learn, NumPy, Pandas</td>
    </tr>
    <tr>
        <td><strong>Visualization</strong></td>
        <td>Matplotlib, Seaborn</td>
    </tr>
    <tr>
        <td><strong>Model</strong></td>
        <td>Random Forest Regressor</td>
    </tr>
    <tr>
        <td><strong>Frontend Framework</strong></td>
        <td>HTML, CSS</td>
    </tr>
    <tr>
        <td><strong>Backend Framework</strong></td>
        <td>Flask</td>
    </tr>
    <tr>
        <td><strong>Weather Provider</strong></td>
        <td>OpenWeatherMap API</td>
    </tr>
    <tr>
        <td><strong>Model Serialization</strong></td>
        <td>Joblib</td>
    </tr>
    <tr>
        <td rowspan="2"><b>Environment</strong></td>
        <td>Jupyter Notebook</td>
    </tr>
    <tr>
        <td>Visual Studio Code</td>
    </tr>
</table>

---

## Project Setup

### 1. Clone the git repository
```
git clone https://github.com/Anudeep-CodeSpace/weather_based_wind_turbine_energy_output_prediction.git
cd weather_based_wind_turbine_energy_output_prediction/ProjectFiles
```
### 2. Install Package Manager
[Click Here](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) to install UV (Official Documentation). <br> Follow these instructions to install UV (A super-fast Python package manager & project manager).
### 3. Install Python Version - 3.10
```
uv python install
```
UV does the installation without disturbing the native version.
### 4. Install Dependencies
```
uv sync
```
### 5. Create a .env file
Sample .env file
```.env (example)
OPENWEATHER_API_KEY=<Your openweather api key>
KAGGLE_USERNAME=<Your Kaggle username>
KAGGLE_KEY=<Your kaggle api token>
```
#### To create a Open Weather API key:
- [Click here](https://home.openweathermap.org/users/sign_in) to open the Open Weather Map official website.
- Create an account / Sign-in to your account.
- Select **API Keys** from the menu after login.
- You can copy the default api key or create a new one.
#### To create a Kaggle API token:
- Go to [Kaggle](https://kaggle.com).
- Click on "Register" (for new users) or "Sign in".
- After Logging in, go to settings.
- You can find your username at the top (Landscape mode).
- Scroll down to API section.
- Click on "Generate New Token" and enter any key name.
- A pop-up displays showing the API key.

### 5. Download dataset and train
```
uv run python main.py train
```
Be sure to close the heatmap - to ensure training execution continues
### 6. Test the model
```
uv run python main.py test
```
### 7. Start the Flask Server
```
uv run python main.py serve
```
Open http://127.0.0.1:5000 in chrome/mozilla browser
