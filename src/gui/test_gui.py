# src/gui/test_gui.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class TestGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test GUI")
        layout = QVBoxLayout()
        label = QLabel("Hello! The GUI works!")
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TestGUI()
    gui.show()
    sys.exit(app.exec())
