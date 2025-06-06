# 🌤️ Weather API Integration with Python  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A command-line Python application that fetches and displays real-time weather information for any specified city using the OpenWeatherMap API.  
This project demonstrates clean API integration, JSON data parsing, and graceful error handling in Python.

---

## 🚀 Features

- 🔗 **API Integration** – Makes GET requests to OpenWeatherMap using the `requests` library  
- 📊 **Weather Metrics** – Displays:
  - Temperature (°C/°F)
  - Feels Like
  - Humidity
  - Weather Description
  - Sunrise & Sunset (Local Time)
  - Wind Speed  
- 🛡️ **Error Handling** – Gracefully handles invalid city names or failed responses  
- 🧑‍💻 **User Interaction** – Accepts city name input from the user dynamically

---

## 🛠️ Prerequisites

- Python ≥ 3.6  
- `requests` library  

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Avnish1447/weather-api-integration.git
   cd weather-api-integration
   ```

2. **Install Dependencies**
   ```bash
   pip install requests
   ```

3. **Get an API Key**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Create a file named `api_key` (no extension) in the project directory and paste your API key into it

---

## 📈 Usage

Run the script from your terminal:

```bash
python weather_app.py
```

You'll be prompted to enter the name of a city. The app fetches and displays current weather info.

---

## 🧪 Example Output

```plaintext
Enter the name of the city: Mumbai
City: Mumbai
Temperature: 32.99°C / 91.38°F
Feels Like: 38.79°C / 101.82°F
Humidity: 58%
Weather: Smoke
Sunrise (local time): 05:12:34
Sunset (local time): 20:45:21
Wind Speed: 4.12 m/s
```

---

## 📁 Project Structure

```plaintext
weather-api-integration/
├── weather_app.py       # Main application logic
├── api_key              # Your personal OpenWeatherMap API key (not shared)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo  
2. Create a new branch  
   ```bash
   git checkout -b feature-name
   ```
3. Make changes and commit  
   ```bash
   git commit -m "Add: Feature Description"
   ```
4. Push your branch and open a Pull Request

---

## 🪪 License  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

📧 [avnishagrawal1447@gmail.com](mailto:avnishagrawal1447@gmail.com)  
Feel free to reach out for collaboration, questions, or feedback!
