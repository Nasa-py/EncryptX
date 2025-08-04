# 🔐 EncryptX

A modern, user-friendly GUI application for encrypting and decrypting files using the Fernet encryption algorithm. Built with PyQt5 and featuring a clean, Android-inspired Material Design interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **🎨 Modern GUI**: Clean, Material Design-inspired interface
- **🔒 Secure Encryption**: Uses Fernet symmetric encryption (AES 128)
- **📁 File Management**: Easy file browsing and selection
- **👀 File Preview**: Preview file contents before encryption
- **⚡ Threaded Operations**: Non-blocking UI with progress feedback
- **🔑 Key Management**: Automatic key generation and secure storage
- **📱 Responsive Design**: Android-style tabbed interface
- **🛡️ Error Handling**: Comprehensive validation and error messages

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd file-encryption-tool
   ```

2. **Install required dependencies**
   ```bash
   pip install PyQt5 cryptography
   ```

3. **Run the application**
   ```bash
   python encryption_app.py
   ```

## 📖 How to Use

### 🔒 Encrypting Files

1. Launch the application
2. Go to the **"🔒 Encrypt"** tab
3. Click **"Browse"** to select a text file (.txt)
4. Preview the file content in the text area
5. Click **"🔒 Encrypt File"**
6. The app will generate:
   - `filename_encrypted.enc` - The encrypted file
   - `filename_key.key` - The encryption key (keep this safe!)

### 🔓 Decrypting Files

1. Go to the **"🔓 Decrypt"** tab
2. Select the encrypted file (`.enc`) using the first browse button
3. Select the corresponding key file (`.key`) using the second browse button
4. Click **"🔓 Decrypt File"**
5. The decrypted content will be saved as `filename_decrypted.txt`

## 🔧 Technical Details

### Encryption Algorithm
- **Algorithm**: Fernet (AES 128 in CBC mode with HMAC using SHA256)
- **Key Size**: 256-bit (32 bytes)
- **Security**: Cryptographically secure random key generation

### File Structure
```
your-file.txt           # Original file
your-file_encrypted.enc # Encrypted file (binary)
your-file_key.key       # Encryption key (binary)
your-file_decrypted.txt # Decrypted file
```

### Dependencies
- **PyQt5**: GUI framework for the user interface
- **cryptography**: Provides the Fernet encryption implementation
- **sys, os**: Built-in Python modules for system operations

## 🎨 UI Components

- **Tabbed Interface**: Separate encryption and decryption workflows
- **File Browsers**: Native file selection dialogs
- **Progress Bar**: Visual feedback during operations
- **Preview Panel**: Text preview for files being encrypted
- **Status Messages**: Success and error notifications

## ⚠️ Security Notes

1. **Keep Your Keys Safe**: The `.key` files are essential for decryption. Store them securely!
2. **Key Distribution**: If sharing encrypted files, you must also securely share the key file
3. **File Cleanup**: Consider securely deleting original files after encryption if needed
4. **Backup Keys**: Always backup your key files - lost keys mean permanently lost data

## 🔍 Troubleshooting

### Common Issues

**"Cannot preview file" error**
- Ensure the file is a text file with UTF-8 encoding
- Binary files cannot be previewed but can still be encrypted

**"Cannot read key file" error**
- Verify you selected the correct `.key` file
- Ensure the key file wasn't corrupted or modified

**"Operation failed" during decryption**
- Check that the encrypted file and key file match
- Ensure both files haven't been corrupted

**Application won't start**
- Verify Python 3.7+ is installed: `python --version`
- Check dependencies: `pip list | grep -E "(PyQt5|cryptography)"`

### Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Please select a valid file" | No file selected | Use Browse button to select a file |
| "File not found" | File path is invalid | Ensure file exists and path is correct |
| "Permission denied" | No write access | Check folder permissions |
| "Invalid key" | Wrong key file used | Use the correct key file for this encrypted file |

## 🛠️ Development

### Code Structure
```
encryption_app.py
├── EncryptionWorker      # Background thread for encryption/decryption
├── ModernEncryptionApp   # Main application window
├── UI Components         # Tabs, buttons, file browsers
└── Styling              # Material Design CSS styles
```

### Customization
- **Colors**: Modify the CSS styles in `apply_modern_style()`
- **Layout**: Adjust spacing and margins in the layout methods
- **Features**: Add new tabs or functionality by extending the main class

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test them
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

## 🔮 Future Enhancements

- [ ] Support for multiple file formats (PDF, DOCX, images)
- [ ] Batch encryption/decryption
- [ ] Password-based encryption option
- [ ] Cloud storage integration
- [ ] Mobile app version
- [ ] Command-line interface option
- [ ] Encryption strength selection
- [ ] File shredding after encryption

---

**⚡ Made with Python and PyQt5 | 🔐 Secure • 🎨 Modern • 🚀 Fast**