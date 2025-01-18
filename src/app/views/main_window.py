# --- Файл: src/app/views/main_window.py ---
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class MainWindow(QWidget):
    """
    Главное окно приложения, которое содержит поле для ввода API-ключа
    и кнопки для его сохранения и создания агентов.
    """
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.setWindowTitle("Multi-Agent System")
        self.setGeometry(100, 100, 400, 200)

        # Главный вертикальный слой
        layout = QVBoxLayout()

        # Метка (инструкция)
        self.label = QLabel("Enter GPTunnel API Key:")
        layout.addWidget(self.label)

        # Поле ввода для API-ключа
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("GPTunnel API key")
        layout.addWidget(self.api_key_input)

        # Кнопка сохранения API-ключа
        self.save_button = QPushButton("Save API Key")
        self.save_button.clicked.connect(self.save_api_key)
        layout.addWidget(self.save_button)

        # Кнопка создания агента
        self.create_agent_button = QPushButton("Добавить агента")
        self.create_agent_button.clicked.connect(self.create_agent)
        layout.addWidget(self.create_agent_button)

        # Установка слоя в окно
        self.setLayout(layout)

    def save_api_key(self):
        """
        Сохранение API-ключа. Проверяет, что ключ не пустой.
        """
        api_key = self.api_key_input.text()
        if api_key:
            QMessageBox.information(self, "Success", "API Key saved successfully!")
        else:
            QMessageBox.warning(self, "Error", "API Key cannot be empty!")

    def create_agent(self):
        """
        Заглушка для функционала создания агента.
        """
        QMessageBox.information(self, "Info", "Agent creation feature is under development.")


