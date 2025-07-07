import sys
import serial
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class LEDControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arduino LED Control")
        self.setGeometry(300, 300, 300, 200)

        # Connect to Arduino serial
        try:
            self.arduino = serial.Serial('COM5', 9600, timeout=1)  # Change COM5 to your port
            time.sleep(2)  # Wait for Arduino to reset
        except:
            self.arduino = None

        # Create GUI elements
        self.status_label = QLabel("LED Status: OFF", self)
        self.btn_on = QPushButton("LED ON", self)
        self.btn_off = QPushButton("LED OFF", self)

        # Connect buttons
        self.btn_on.clicked.connect(self.led_on)
        self.btn_off.clicked.connect(self.led_off)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.btn_on)
        layout.addWidget(self.btn_off)

        self.setLayout(layout)

    def led_on(self):
        if self.arduino:
            self.arduino.write(b'ON\n')
            self.status_label.setText("LED Status: ON")

    def led_off(self):
        if self.arduino:
            self.arduino.write(b'OFF\n')
            self.status_label.setText("LED Status: OFF")

    def closeEvent(self, event):
        if self.arduino:
            self.arduino.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LEDControl()
    window.show()
    sys.exit(app.exec_())
