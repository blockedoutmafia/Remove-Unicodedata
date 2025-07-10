# Invisible Character Cleaner

A simple Python GUI tool to help you identify and remove hidden/invisible Unicode characters from text. Built with Tkinter, this utility provides a live side-by-side view of your raw input and the cleaned output, plus a one-click "Copy to Clipboard" feature.

---

## Table of Contents

* [Features](#features)
* [Invisible Characters Covered](#invisible-characters-covered)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Development & Contributing](#development--contributing)
* [License](#license)

---

## Features

* **Real-time cleaning**: See invisible/control characters removed as you type or paste.
* **Broad Unicode support**: Strips out nulls, control codes, various spaces (no-break, zero-width, em/en/quads), directional formatting marks, BOMs, and more.
* **Punctuation normalization**: Converts curly quotes and dashes to their ASCII equivalents.
* **Live GUI**: Side-by-side `Raw Text` and `Cleaned Text` panes that resize with the window.
* **Copy to Clipboard**: One-click button to copy cleaned text for pasting elsewhere.

---

## Invisible Characters Covered

This tool removes (but is not limited to):

* **Control codes**: U+0000–U+001F, U+007F (DEL)
* **No-break spaces**: U+00A0, U+202F, etc.
* **Ogham & Mongolian separators**: U+1680, U+180E
* **En/Em/Various Spacing**: U+2000–U+200A, U+3000 (CJK space)
* **Zero-width & Directional marks**: U+200B–U+200F, U+2028–U+202E, U+2060–U+2069
* **Byte Order Mark (BOM)**: U+FEFF
* **Annotation & Isolate controls**: U+FFF9–U+FFFB, U+2066–U+2069
* **Curly quotes & dashes**: U+2018, U+2019, U+201C, U+201D, U+2013, U+2014

> *For a complete list, see the `INVISIBLE_CHARS` array in the source code.*

---

## Requirements

* Python 3.6+ (Tkinter is included in the standard library)

---

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/invisible-char-cleaner.git
   cd invisible-char-cleaner
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\\Scripts\\activate  # Windows
   ```

3. **Install dependencies**

   No external packages required—Tkinter is part of the Python standard library.

---

## Usage

Run the main application script:

```bash
python invisible_char_cleaner.py
```

* **Raw Text** pane (left): Type or paste your text containing hidden/invisible characters.
* **Cleaned Text** pane (right): Updates live to show the cleaned output.
* **Copy to Clipboard** button: Copies the entire cleaned output for easy pasting.

---

## Configuration

* **Modifying the character set**: Open `invisible_char_cleaner.py` and edit the `INVISIBLE_CHARS` list to add or remove code points.
* **Punctuation mapping**: Adjust the `REPLACEMENTS` dictionary for any additional typographic characters you wish to normalize.
* **Window size & title**: Change `self.geometry()` and `self.title()` in the `__main__` block.

---

## Development & Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for:

* Additional control characters or normalization rules.
* Alternative GUI frameworks (PyQt, Kivy).
* File drag-and-drop support.
* Dark/light theme toggles.
* Localization/translation.

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

*Built with ❤️ by Invisible Character Cleaner*
