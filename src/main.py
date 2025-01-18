# --- Файл: src/main.py ---
import sys
from PyQt5.QtWidgets import QApplication
from app.views.main_window import MainWindow

def main():
    """
    Точка входа в приложение. Запускает главное окно.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
