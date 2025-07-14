import sys
import os
import requests

from PyQt5.QtWidgets import (
    QWidget, QApplication, QPushButton, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QComboBox, QSizePolicy
)
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtGui import QPixmap

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_temperature_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.unit_selector = QComboBox()
        self.unit_selector.addItems(["ºC", "ºF"])
        self.weather_pixmap = None
        self.initUI()

        QTimer.singleShot(0, self.force_initial_resize)

    def force_initial_resize(self):
        self.resizeEvent(None)

    def initUI(self):
        self.setWindowTitle("Welcome App Weather")
        self.setMinimumSize(600, 400)

        self.bg_label = QLabel(self)
        self.bg_label.setObjectName("bg_label")
        self.bg_label.setGeometry(self.rect())
        self.bg_label.lower()

        image_path = os.path.join(BASE_DIR, "PixelWeatherPro", "backgrounds", "sunny.png")
        if os.path.exists(image_path):
            self.original_bg = QPixmap(image_path)

        content_layout = QVBoxLayout()
        content_layout.setSpacing(20)
        content_layout.setAlignment(Qt.AlignCenter)

        city_input_group_layout = QVBoxLayout()
        city_input_group_layout.setSpacing(5)
        city_input_group_layout.setAlignment(Qt.AlignCenter)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setWordWrap(True)
        self.city_label.setMaximumWidth(450)
        self.city_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.city_input.setFixedWidth(300)

        city_input_group_layout.addWidget(self.city_label)
        city_input_group_layout.addWidget(self.city_input)
        content_layout.addLayout(city_input_group_layout)

        unit_button_row = QHBoxLayout()
        unit_button_row.setSpacing(10)
        unit_button_row.setAlignment(Qt.AlignCenter)
        self.unit_selector.setFixedSize(120, 50)
        self.get_temperature_button.setFixedSize(120, 50)
        unit_button_row.addWidget(self.unit_selector)
        unit_button_row.addWidget(self.get_temperature_button)

        content_layout.addLayout(unit_button_row)
        content_layout.addWidget(self.temperature_label, alignment=Qt.AlignCenter)
        content_layout.addWidget(self.emoji_label, alignment=Qt.AlignCenter)
        content_layout.addSpacing(80)
        content_layout.addWidget(self.description_label, alignment=Qt.AlignCenter)

        central_container = QHBoxLayout()
        central_container.addStretch()
        central_container.addLayout(content_layout)
        central_container.addStretch()

        main_layout = QVBoxLayout(self)
        main_layout.addStretch()
        main_layout.addLayout(central_container)
        main_layout.addStretch()
        self.setLayout(main_layout)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_temperature_button.setObjectName("get_temperature_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.unit_selector.setObjectName("unit_selector")

        self.setStyleSheet("""
            QLabel, QPushButton, QLineEdit, QComboBox {
                background-color: rgba(255, 255, 255, 0);
                color: black;
            }

            QLabel#city_label {
                font-family: 'Press Start 2P';
                font-size: 32px;
                font-style: italic;
                padding: 10px;
            }

            QLineEdit#city_input {
                font-size: 28px;
                font-family: Calibri;
                color: black;
                border: 2px solid #444;
                border-radius: 10px;
                padding: 10px;
                min-width: 250px;
                background-color: rgba(255, 255, 255, 160);
                qproperty-alignment: AlignCenter;
                text-align: center;
            }

            QComboBox#unit_selector {
                font-size: 20px;
                font-family: Calibri;
                padding: 6px 14px;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 160);
                min-width: 100px;
            }

            QComboBox::drop-down {
                width: 25px;
            }

            QPushButton#get_temperature_button {
                font-size: 20px;
                font-weight: bold;
                font-family: Calibri;
                padding: 6px 14px;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 160);
                min-width: 140px;
            }

            QLabel#temperature_label {
                font-family: 'Press Start 2P';
                font-size: 75px;
            }

            QLabel#description_label {
                font-family: 'Press Start 2P';
                font-size: 50px;
            }

            QLabel#emoji_label {
                margin-top: 10px;
                margin-bottom: 30px;
            }
        """)

        self.description_label.setMinimumHeight(50)
        self.description_label.setText("")
        self.get_temperature_button.clicked.connect(self.get_weather)

    def set_scaled_background(self):
        if hasattr(self, "original_bg") and not self.original_bg.isNull():
            scaled = self.original_bg.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.bg_label.setPixmap(scaled)
            self.bg_label.setAlignment(Qt.AlignCenter)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.bg_label.setGeometry(self.rect())
        self.set_scaled_background()

        if self.weather_pixmap:
            self.set_scaled_weather_pixmap(self.weather_pixmap)

    def set_scaled_weather_pixmap(self, pixmap):
        if not pixmap.isNull():
            side = int(min(self.width(), self.height()) * 0.3)
            side = max(side, 80)
            scaled = pixmap.scaled(
                side,
                side,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.emoji_label.setPixmap(scaled)
            self.emoji_label.setFixedSize(side, side)
            self.emoji_label.setAlignment(Qt.AlignCenter)
            self.emoji_label.setVisible(True)
        else:
            self.emoji_label.clear()
            self.emoji_label.setVisible(False)

    def get_weather(self):
        city = self.city_input.text().strip().capitalize()
        self.city_input.setText(city)
        api_key = "aac2c4f772682d49155bcca800d10a07"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            message = ""
            match status_code:
                case 400: message = "Bad request (400):\nPlease check your input."
                case 401: message = "Unauthorized (401):\nInvalid API key."
                case 403: message = "Forbidden (403):\nYou don't have permission to access this resource."
                case 404: message = "Not found (404):\nCity not found."
                case 429: message = "Too many requests (429):\nAPI rate limit exceeded."
                case 500: message = "Internal server error (500):\nTry again later."
                case 502: message = "Bad gateway (502):\nTemporary server issue."
                case 503: message = "Service unavailable (503):\nThe server is currently down."
                case 504: message = "Gateway timeout (504):\nThe request took too long."
                case _: message = f"Unexpected HTTP error ({status_code})."
            self.display_error(message)
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nPlease check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error:\nThe request took too long to respond.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nThe request URL is likely incorrect or unstable.")
        except requests.exceptions.RequestException as e:
            self.display_error(f"Request failed:\n{str(e)}")
        except Exception as e:
            self.display_error(f"An unexpected error occurred:\n{str(e)}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.setText("No data available")
        self.description_label.setStyleSheet("color: red; font-size: 50px;")

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-family: 'Press Start 2P'; font-size: 75px;")
        self.description_label.setStyleSheet("color: black; font-size: 50px;")

        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67

        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        unit = self.unit_selector.currentText()
        if unit == "ºF":
            self.temperature_label.setText(f"{temperature_f:.0f}ºF")
        else:
            self.temperature_label.setText(f"{temperature_c:.0f}ºC")

        self.description_label.setText(weather_description.capitalize())

        sound_file = self.get_weather_sound_path(weather_id)
        if os.path.exists(sound_file):
            self.play_sound(sound_file)

        image_path = self.get_weather_image_path(weather_id)
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.weather_pixmap = pixmap
            self.set_scaled_weather_pixmap(pixmap)
        else:
            self.emoji_label.setText("❓")

    def get_weather_sound_path(self, weather_id):
        base_path = os.path.join(BASE_DIR,"PixelWeatherPro","sounds")
        if 200 <= weather_id <= 232:
            return os.path.join(base_path, "stormy.wav")
        elif 300 <= weather_id <= 321:
            return os.path.join(base_path, "rainy.wav")
        elif 500 <= weather_id <= 531:
            return os.path.join(base_path, "rainy.wav")
        elif 600 <= weather_id <= 622:
            return os.path.join(base_path, "snowy.wav")
        elif 700 <= weather_id <= 781:
            return os.path.join(base_path, "cloudy.wav")
        elif weather_id == 800:
            return os.path.join(base_path, "sunny.wav")
        elif 801 <= weather_id <= 804:
            return os.path.join(base_path, "cloudy.wav")
        else:
            return ""

    def play_sound(self, sound_path):
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile(sound_path))
        self.sound_effect.setVolume(0.8)
        self.sound_effect.play()

    def get_weather_image_path(self, weather_id):
        base_path = os.path.join(BASE_DIR, "PixelWeatherPro", "images")
        if 200 <= weather_id <= 232:
            return os.path.join(base_path, "storm.png")
        elif 300 <= weather_id <= 321:
            return os.path.join(base_path, "rain.png")
        elif 500 <= weather_id <= 531:
            return os.path.join(base_path, "rain.png")
        elif 600 <= weather_id <= 622:
            return os.path.join(base_path, "snow.png")
        elif 700 <= weather_id <= 781:
            return os.path.join(base_path, "fog.png")
        elif weather_id == 800:
            return os.path.join(base_path, "sun.png")
        elif 801 <= weather_id <= 804:
            return os.path.join(base_path, "cloud.png")
        else:
            return os.path.join(base_path, "unknown.png")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.showMaximized()
    sys.exit(app.exec_())