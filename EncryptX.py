import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, 
                             QFileDialog, QMessageBox, QFrame, QProgressBar, QTabWidget)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor
from cryptography.fernet import Fernet

class EncryptionWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self, file_path, operation, key=None):
        super().__init__()
        self.file_path = file_path
        self.operation = operation
        self.key = key
    
    def run(self):
        try:
            if self.operation == "encrypt":
                self.encrypt_file()
            else:
                self.decrypt_file()
        except Exception as e:
            self.error.emit(str(e))
    
    def encrypt_file(self):
        self.progress.emit(10)
        
        # Read the file
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        self.progress.emit(30)
        
        # Generate key and encrypt
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_content = f.encrypt(content.encode())
        
        self.progress.emit(60)
        
        # Save encrypted file
        base_name = os.path.splitext(self.file_path)[0]
        encrypted_file = f"{base_name}_encrypted.enc"
        key_file = f"{base_name}_key.key"
        
        with open(encrypted_file, 'wb') as file:
            file.write(encrypted_content)
        
        with open(key_file, 'wb') as file:
            file.write(key)
        
        self.progress.emit(100)
        self.finished.emit(f"File encrypted successfully!\nEncrypted file: {encrypted_file}\nKey file: {key_file}")
    
    def decrypt_file(self):
        self.progress.emit(10)
        
        # Read encrypted file
        with open(self.file_path, 'rb') as file:
            encrypted_content = file.read()
        
        self.progress.emit(30)
        
        # Read key
        if not self.key:
            raise Exception("No key provided for decryption")
        
        f = Fernet(self.key)
        decrypted_content = f.decrypt(encrypted_content)
        
        self.progress.emit(60)
        
        # Save decrypted file
        base_name = os.path.splitext(self.file_path)[0]
        if base_name.endswith('_encrypted'):
            base_name = base_name[:-10]  # Remove '_encrypted'
        
        decrypted_file = f"{base_name}_decrypted.txt"
        
        with open(decrypted_file, 'w', encoding='utf-8') as file:
            file.write(decrypted_content.decode())
        
        self.progress.emit(100)
        self.finished.emit(f"File decrypted successfully!\nDecrypted file: {decrypted_file}")

class ModernEncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EncryptX")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(800, 600)
        self.setup_ui()
        self.apply_modern_style()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Header
        header_label = QLabel("🔐 File Encryption Tool")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #2196F3;
                margin-bottom: 20px;
            }
        """)
        main_layout.addWidget(header_label)
        
        # Tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #F5F5F5;
                padding: 12px 24px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background-color: #2196F3;
                color: white;
            }
        """)
        
        # Encryption tab
        encrypt_tab = self.create_encrypt_tab()
        self.tab_widget.addTab(encrypt_tab, "🔒 Encrypt")
        
        # Decryption tab
        decrypt_tab = self.create_decrypt_tab()
        self.tab_widget.addTab(decrypt_tab, "🔓 Decrypt")
        
        main_layout.addWidget(self.tab_widget)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 6px;
            }
        """)
        main_layout.addWidget(self.progress_bar)
        
    def create_encrypt_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)
        
        # File selection
        file_section = self.create_file_selection_section("Select file to encrypt:")
        self.encrypt_file_path = file_section[1]
        layout.addWidget(file_section[0])
        
        # File preview
        preview_label = QLabel("File Preview:")
        preview_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #424242;")
        layout.addWidget(preview_label)
        
        self.encrypt_preview = QTextEdit()
        self.encrypt_preview.setMaximumHeight(150)
        self.encrypt_preview.setReadOnly(True)
        self.encrypt_preview.setStyleSheet("""
            QTextEdit {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 10px;
                background-color: #FAFAFA;
                font-family: monospace;
            }
        """)
        layout.addWidget(self.encrypt_preview)
        
        # Encrypt button
        self.encrypt_btn = QPushButton("🔒 Encrypt File")
        self.encrypt_btn.clicked.connect(self.encrypt_file)
        self.encrypt_btn.setStyleSheet(self.get_primary_button_style())
        layout.addWidget(self.encrypt_btn)
        
        return widget
    
    def create_decrypt_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)
        
        # Encrypted file selection
        file_section = self.create_file_selection_section("Select encrypted file (.enc):")
        self.decrypt_file_path = file_section[1]
        layout.addWidget(file_section[0])
        
        # Key file selection
        key_section = self.create_file_selection_section("Select key file (.key):")
        self.key_file_path = key_section[1]
        layout.addWidget(key_section[0])
        
        # Decrypt button
        self.decrypt_btn = QPushButton("🔓 Decrypt File")
        self.decrypt_btn.clicked.connect(self.decrypt_file)
        self.decrypt_btn.setStyleSheet(self.get_secondary_button_style())
        layout.addWidget(self.decrypt_btn)
        
        return widget
    
    def create_file_selection_section(self, label_text):
        section = QFrame()
        section.setFrameStyle(QFrame.Box)
        section.setStyleSheet("""
            QFrame {
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                padding: 10px;
                background-color: #FAFAFA;
            }
        """)
        
        layout = QVBoxLayout(section)
        
        label = QLabel(label_text)
        label.setStyleSheet("font-weight: bold; font-size: 14px; color: #424242;")
        layout.addWidget(label)
        
        file_layout = QHBoxLayout()
        
        file_path = QLineEdit()
        file_path.setPlaceholderText("No file selected...")
        file_path.setReadOnly(True)
        file_path.setStyleSheet("""
            QLineEdit {
                border: 2px solid #E0E0E0;
                border-radius: 6px;
                padding: 8px;
                background-color: white;
            }
        """)
        
        browse_btn = QPushButton("Browse")
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:pressed {
                background-color: #EF6C00;
            }
        """)
        
        browse_btn.clicked.connect(lambda: self.browse_file(file_path, label_text))
        
        file_layout.addWidget(file_path)
        file_layout.addWidget(browse_btn)
        layout.addLayout(file_layout)
        
        return section, file_path
    
    def browse_file(self, line_edit, label_text):
        if "key" in label_text.lower():
            file_path, _ = QFileDialog.getOpenFileName(
                self, "Select Key File", "", "Key Files (*.key);;All Files (*)"
            )
        elif "encrypted" in label_text.lower():
            file_path, _ = QFileDialog.getOpenFileName(
                self, "Select Encrypted File", "", "Encrypted Files (*.enc);;All Files (*)"
            )
        else:
            file_path, _ = QFileDialog.getOpenFileName(
                self, "Select File to Encrypt", "", "Text Files (*.txt);;All Files (*)"
            )
        
        if file_path:
            line_edit.setText(file_path)
            if line_edit == self.encrypt_file_path:
                self.preview_file(file_path)
    
    def preview_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read(500)  # Preview first 500 characters
                if len(content) == 500:
                    content += "\n... (file continues)"
                self.encrypt_preview.setText(content)
        except Exception as e:
            self.encrypt_preview.setText(f"Cannot preview file: {str(e)}")
    
    def encrypt_file(self):
        file_path = self.encrypt_file_path.text()
        
        if not file_path or not os.path.exists(file_path):
            QMessageBox.warning(self, "Warning", "Please select a valid file to encrypt!")
            return
        
        self.start_operation("encrypt", file_path)
    
    def decrypt_file(self):
        file_path = self.decrypt_file_path.text()
        key_path = self.key_file_path.text()
        
        if not file_path or not os.path.exists(file_path):
            QMessageBox.warning(self, "Warning", "Please select a valid encrypted file!")
            return
        
        if not key_path or not os.path.exists(key_path):
            QMessageBox.warning(self, "Warning", "Please select a valid key file!")
            return
        
        try:
            with open(key_path, 'rb') as f:
                key = f.read()
            self.start_operation("decrypt", file_path, key)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot read key file: {str(e)}")
    
    def start_operation(self, operation, file_path, key=None):
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # Disable buttons
        self.encrypt_btn.setEnabled(False)
        self.decrypt_btn.setEnabled(False)
        
        # Start worker thread
        self.worker = EncryptionWorker(file_path, operation, key)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self.on_operation_finished)
        self.worker.error.connect(self.on_operation_error)
        self.worker.start()
    
    def on_operation_finished(self, message):
        self.progress_bar.setVisible(False)
        self.encrypt_btn.setEnabled(True)
        self.decrypt_btn.setEnabled(True)
        
        QMessageBox.information(self, "Success", message)
    
    def on_operation_error(self, error_message):
        self.progress_bar.setVisible(False)
        self.encrypt_btn.setEnabled(True)
        self.decrypt_btn.setEnabled(True)
        
        QMessageBox.critical(self, "Error", f"Operation failed: {error_message}")
    
    def get_primary_button_style(self):
        return """
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #1565C0;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
            }
        """
    
    def get_secondary_button_style(self):
        return """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
            QPushButton:pressed {
                background-color: #2E7D32;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
            }
        """
    
    def apply_modern_style(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
            QWidget {
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)

def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = ModernEncryptionApp()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()