# 🌤️ Weather API Integration with Python [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project is a command-line Python application that fetches and displays real-time weather information for any specified city using the OpenWeatherMap API. It demonstrates how to interact with external APIs, parse JSON data, and handle potential errors gracefully.

---

## 🚀 Features

* **API Integration**: Utilizes the `requests` library to make GET requests to the OpenWeatherMap API.
* **Data Parsing**: Extracts and presents temperature (in Celsius and Fahrenheit), humidity, weather descriptions, sunrise and sunset times, and wind speed in a user-friendly format.
* **Error Handling**: Implements mechanisms to manage failed requests and invalid responses gracefully.
* **User Input**: Prompts the user to enter the name of the city for which they want to retrieve weather information.

---

## 🛠️ Prerequisites

* Python 3.6 or higher
* `requests` library

---

## 📦 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Avnish1447/weather-api-integration.git
   cd weather-api-integration
   ```



2. **Install Dependencies**:

   ```bash
   pip install requests
   ```



3. **Obtain an API Key**:

   * Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get a free API key.
   * Create a file named `api_key` in the project directory and paste your API key into it.

---

## 📈 Usage

Run the script using the following command:

```bash
python weather_app.py
```



You'll be prompted to enter the name of the city. The application will then fetch and display the current weather information for that city

---

## 🧪 Example Output

```
Enter the name of the city: Mumbai
City: Mumbai
Temperature: 32.99°C/91.38°F
Feels Like: 38.79°C / 101.82°F
Humidity: 58%
Weather: Smoke
Sunrise (local time): 05:12:34
Sunset (local time):  20:45:21
Wind Speed: 4.12 m/s
```



---

## 📁 File Structure

```plaintext
weather-api-integration/
├── weather_app.py      # Main application script
├── README.md           # Project documentation
└── requirements.txt    # List of dependencies
```



---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---
## License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
---
## 📬 Contact

For any inquiries or feedback, please contact [your.email@example.com](mailto:your.email@example.com).


