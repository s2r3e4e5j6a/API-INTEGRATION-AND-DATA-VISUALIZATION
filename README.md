# API-INTEGRATION-AND-DATA-VISUALIZATION
API INTEGRATION  AND DATA  VISUALIZATION is my 1st task for my internship provided by the company Codetech 

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: SREEJA GURRALA

*INTERN ID*:CT04DM1389

*DOMAIN*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


## Project Description: API Integration and Weather Data Visualization

This project demonstrates the powerful combination of fetching real-time data from a public API and presenting it through compelling visualizations. Specifically, it focuses on retrieving current weather conditions and a multi-day forecast for a specified city using the OpenWeatherMap API, and then rendering this information using Matplotlib to create a series of informative plots that function as a basic "weather dashboard."

**Key Components and Their Explanation:**

### 1. API Integration

At its core, the project leverages **API (Application Programming Interface) integration**. An API acts as a messenger that allows different software applications to communicate with each other. In this case, our Python script is the "client" and OpenWeatherMap's servers are the "provider."

* **Public API (OpenWeatherMap):** We utilize the OpenWeatherMap API, a widely used service that provides current and historical weather data, as well as forecasts, for locations worldwide. It's "public" because it's available for developers to use, often with certain usage limits for free tiers.
* **API Key:** To access the OpenWeatherMap API, an `API_KEY` is required. This unique key authenticates our requests, identifies our application to the API provider, and helps in managing usage limits.
* **HTTP Requests:** The `requests` library in Python is used to make HTTP (Hypertext Transfer Protocol) requests to the OpenWeatherMap API endpoints.
    * `GET` requests are used to retrieve data from the API.
    * **Endpoints:** Specific URLs (like `http://api.openweathermap.org/data/2.5/weather` for current weather and `https://api.openweathermap.org/data/2.5/onecall` for the comprehensive forecast) are called "endpoints." Each endpoint serves a different type of data.
* **JSON Response Handling:** The OpenWeatherMap API typically returns data in **JSON (JavaScript Object Notation)** format. This is a lightweight and human-readable data interchange format. The `response.json()` method in the `requests` library automatically parses the JSON string into a Python dictionary, making it easy to access and work with the data (e.g., `data['main']['temp']` to get the temperature).
* **Error Handling:** The `try-except` blocks are crucial for robust API integration. They catch potential `requests.exceptions.RequestException` errors (e.g., network issues, invalid API key, city not found) and provide informative messages, preventing the script from crashing.

### 2. Data Fetching and Processing

This phase involves retrieving the raw data and then transforming it into a usable format for visualization.

* **Current Weather Data:** The `fetch_current_weather` function makes a call to get the present weather conditions (temperature, humidity, wind speed, description) for a specified city. It also extracts the latitude and longitude, which are essential for the more advanced "One Call API."
* **Daily Forecast Data (One Call API):** The `fetch_forecast_data` function uses the OpenWeatherMap One Call API. This API is powerful as it provides a comprehensive set of weather data (current, minutely, hourly, daily, and alerts) for a given geographical coordinate (latitude and longitude). We specifically extract the `daily` forecast data for the next 7 days.
* **Data Extraction and Structuring:** From the raw JSON response, specific weather parameters (e.g., `temp_max`, `temp_min`, `humidity`, `wind_speed`, `weather description`) are extracted. For the daily forecast, these are organized into lists that are then converted into a `pandas.DataFrame`. Pandas DataFrames are highly efficient and convenient for tabular data manipulation, making them ideal for preparing data for plotting.
* **Timestamp Conversion:** The API returns timestamps in Unix (Epoch) time. The `datetime.fromtimestamp()` function is used to convert these numerical timestamps into human-readable date and time formats.

### 3. Data Visualization

This is where the processed data is transformed into graphical representations, making complex information easier to understand at a glance.

* **Matplotlib:** This is the primary plotting library used. Matplotlib is a foundational library in Python for creating static, interactive, and animated visualizations.
* **"Visualization Dashboard" (Conceptual):** While not a dynamic web application dashboard, the project creates a series of sequential plots that collectively serve as a visual "dashboard." Each plot focuses on a different aspect of the weather data, providing a comprehensive overview.
* **Types of Plots Used:**
    * **Bar Charts:** Used for comparing discrete categories, such as "Temperature" vs. "Feels Like Temperature" in the current weather summary, and daily humidity levels.
    * **Line Plots:** Ideal for showing trends over time, such as the maximum and minimum temperatures over the 7-day forecast, and the daily wind speeds.
* **Plot Customization:**
    * `plt.figure(figsize=...)`: Controls the size of each plot for better readability.
    * `plt.xlabel()`, `plt.ylabel()`, `plt.title()`: Provide descriptive labels for axes and a clear title for each plot.
    * `plt.legend()`: Differentiates multiple lines or bars in a single plot (e.g., Max vs. Min Temp).
    * `plt.grid(True)`: Adds a grid to the background for easier reading of values.
    * `plt.xticks(rotation=...)`: Rotates x-axis labels (dates) to prevent overlap.
    * `plt.tight_layout()`: Automatically adjusts plot parameters for a tight layout, preventing labels from overlapping.
    * `ax.text()`: Used in the current weather visualization to add specific text details directly onto the plot.
* **Sequential Presentation:** Each `plt.show()` call displays a new plot. The user closes the current plot window to reveal the next one, guiding them through the weather insights.

### 4. Deliverables

* **`weather_dashboard.py` (Script):** This is the executable Python file containing all the logic for API communication, data processing, and visualization. It's designed to be run from the command line.
* **Visualization Dashboard (Series of Plots):** When the script is executed, it generates multiple graphical windows (Matplotlib figures), each presenting a different aspect of the weather data (current conditions, temperature forecast, humidity forecast, wind speed forecast). These plots collectively form the visual "dashboard" for weather insights.

**In summary, this project provides a practical demonstration of how to:**

* Interact with external web services using APIs.
* Handle and parse structured data (JSON).
* Transform raw data into meaningful insights.
* Create clear and informative data visualizations using a popular Python library.

It serves as a foundational example for anyone looking to build applications that consume external data and present it visually.

*OUTPUT PICTURE*: 

![Image](https://github.com/user-attachments/assets/4d5e62d7-44a3-4d26-89e0-bef4cdbc5141)
