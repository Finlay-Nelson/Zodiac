"""
gui_main.py

Graphical entry point for the microscopy assembly platform.
Currently a placeholder window; will be expanded with full GUI.
"""

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from core import experiments

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Microscopy Assembly (Placeholder GUI)")
        layout = QVBoxLayout()
        button = QPushButton("Run Test Experiment")
        button.clicked.connect(lambda: experiments.run_experiment("gui_experiment"))
        layout.addWidget(button)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
