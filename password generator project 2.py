import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QMessageBox
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Password Generator")
        self.setGeometry(100, 100, 400, 250)
        
        self.password_label = QLabel("Generated Password:")
        self.password_label.setFont(QFont("Arial", 12))
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setFont(QFont("Courier New", 12))
        
        self.length_label = QLabel("Password Length:")
        self.length_input = QLineEdit()
        self.length_input.setValidator(QRegExpValidator(QRegExp("[1-9][0-9]{0,2}")))
        self.length_input.setText("12")
        self.length_input.setFixedWidth(50)
        
        self.lowercase_check = QCheckBox("Include lowercase letters")
        self.uppercase_check = QCheckBox("Include uppercase letters")
        self.digits_check = QCheckBox("Include digits")
        self.symbols_check = QCheckBox("Include symbols")
        
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        
        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_password)
        
        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_display)
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)
        layout.addWidget(self.lowercase_check)
        layout.addWidget(self.uppercase_check)
        layout.addWidget(self.digits_check)
        layout.addWidget(self.symbols_check)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.copy_button)
        
        self.setLayout(layout)
    
    def generate_password(self):
        length = int(self.length_input.text())
        include_lowercase = self.lowercase_check.isChecked()
        include_uppercase = self.uppercase_check.isChecked()
        include_digits = self.digits_check.isChecked()
        include_symbols = self.symbols_check.isChecked()
        
        characters = ""
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        
        if not characters:
            QMessageBox.warning(self, "Warning", "Please select at least one character set.")
            return
        
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_display.setText(password)
    
    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_display.text())
        QMessageBox.information(self, "Information", "Password copied to clipboard.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())
