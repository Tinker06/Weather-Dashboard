# Weather Dashboard

A simple desktop weather application built with Python and Tkinter. The application allows users to enter a city name and retrieve its current weather information using the OpenWeather API. This is a very basic model created to learn about Python and basic GUI.

## Features

* Search for the current weather of any city
* Displays the city name and current temperature
* Displays the "feels like" temperature
* Shows humidity and wind speed
* Displays the current weather condition
* Handles invalid city names
* Handles empty search input
* Simple graphical user interface
* API key stored securely using environment variables

## Technologies Used

* **Python** — Application logic
* **Tkinter** — Graphical user interface
* **Requests** — Sending HTTP requests to the weather API
* **OpenWeather API** — Providing current weather data
* **python-dotenv** — Loading the API key from environment variables

## How It Works

The application follows a simple process:

1. The user enters a city name in the search field.
2. Python retrieves the entered city using Tkinter.
3. The application sends a request to the OpenWeather API using the Requests library.
4. The API returns the weather information in JSON format.
5. Python extracts the required information from the response.
6. The weather details are displayed in the application window.

### Basic Flow

```text
User enters city
       ↓
Tkinter GUI
       ↓
Python
       ↓
Requests library
       ↓
OpenWeather API
       ↓
JSON response
       ↓
Weather information extracted
       ↓
GUI displays results
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/senthalirv/Weather-Dashboard
```

Move into the project directory:

```bash
cd Weather-Dashboard
```

### 2. Install the Required Libraries

Make sure Python is installed on your system.

Install the project dependencies using:

```bash
py -m pip install -r requirements.txt
```

The required packages are:

```text
requests
python-dotenv
```

### 3. Create an OpenWeather API Key

Create an account on OpenWeather and obtain an API key.

Create a file named:

```text
.env
```

in the root directory of the project.

Add your API key in the following format:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Do not share your API key publicly.

### 4. Verify `.gitignore`

Make sure the `.gitignore` file contains:

```text
.env
__pycache__/
```

This prevents the API key and Python cache files from being uploaded to GitHub.

## How to Run

Run the application using:

```bash
py weather_gui.py
```

A window will open where you can enter a city name and retrieve its current weather information.


## Project Structure

```text
Weather-Dashboard/
│
├── weather_gui.py
├── weather.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── screenshots/
    ├── weather-dashboard.png
    └── weather-result.png
```

> The `.env` file should remain local and must not be uploaded to GitHub.

## Future Improvements

Possible improvements for future versions include:

* Add a multi-day weather forecast
* Display weather icons based on current conditions
* Add additional weather information such as pressure and visibility
* Improve the graphical interface
* Add temperature unit selection between Celsius and Fahrenheit
* Add support for searching using country codes
* Add automatic weather updates
* Improve error handling for network and API errors

## License

This project is created for learning and educational purposes.
