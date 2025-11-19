# Simple Mini Encryption Tool

A versatile, lightweight encryption and decryption utility built with Python. This tool offers both a command-line interface (CLI) and a modern graphical user interface (GUI) for quick and easy text processing.

## Features

*   **Multiple Ciphers**:
    *   **Caesar Cipher**: Classic shift-based encryption.
    *   **XOR Cipher**: Simple bitwise encryption with a key.
    *   **Vigenère Cipher**: Polyalphabetic substitution using a keyword.
    *   **Base64**: Standard encoding and decoding.
*   **Dual Interface**:
    *   **CLI**: Fast, interactive terminal menu.
    *   **GUI**: User-friendly Tkinter interface.
*   **GUI Enhancements**:
    *   **Dark Mode**: Toggle between light and dark themes for comfortable viewing.
    *   **Real-time Character Counter**: Track input length instantly.
    *   **Clipboard Integration**: Copy results with a single click.
    *   **Quick Clear**: Reset all fields easily.

## Requirements

*   Python 3.x
*   Tkinter (usually included with Python installations)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/urbancheese/simple-mini-encryption-tool.git
    ```
2.  Navigate to the directory:
    ```bash
    cd simple-mini-encryption-tool
    ```

## Usage

### Graphical User Interface (GUI)
Run the GUI version for a visual experience:
```bash
python gui.py
```

### Command Line Interface (CLI)
Run the terminal version for quick tasks:
```bash
python test.py
```

## Testing
Run the included unit tests to verify functionality:
```bash
python verify_crypto.py
```

## License
MIT
