import re
import unicodedata
import tkinter as tk
from tkinter import ttk

# === Build regex for invisible/control Unicode characters ===
INVISIBLE_CHARS = [
    '\u0000',  # NULL
    '\u0001','\u0002','\u0003','\u0004','\u0005','\u0006','\u0007',
    '\u0008','\u0009','\u000A','\u000B','\u000C','\u000D','\u000E','\u000F',
    '\u0010','\u0011','\u0012','\u0013','\u0014','\u0015','\u0016','\u0017',
    '\u0018','\u0019','\u001A','\u001B','\u001C','\u001D','\u001E','\u001F',
    '\u007F',           # DEL
    '\u00A0',           # NBSP
    '\u1680','\u180E',  # Ogham, Mongolian sep
    '\u2000','\u2001','\u2002','\u2003','\u2004','\u2005','\u2006','\u2007',
    '\u2008','\u2009','\u200A',  # various spaces
    '\u200B','\u200C','\u200D','\u200E','\u200F',  # zero-width & marks
    '\u2028','\u2029',           # separators
    '\u202A','\u202B','\u202C','\u202D','\u202E',  # bidi formatting
    '\u2060','\u2061','\u2062','\u2063','\u2064',  # misc invisibles
    '\u2066','\u2067','\u2068','\u2069',           # isolates
    '\uFEFF',           # BOM
    '\uFFF9','\uFFFA','\uFFFB'  # annotation chars
]
_pattern = re.compile("|".join(re.escape(c) for c in INVISIBLE_CHARS))

# Mapping curly quotes and dashes to ASCII equivalents
REPLACEMENTS = {
    '\u2018': "'",  # left single quotation mark
    '\u2019': "'",  # right single quotation mark
    '\u201C': '"',  # left double quotation mark
    '\u201D': '"',  # right double quotation mark
    '\u2013': '-',  # en dash
    '\u2014': '-',  # em dash
}

def clean_text(text):
    """
    Normalize, remove invisible/control characters, and map common
    typographic punctuation to ASCII.
    """
    # Unicode normalization (compatibility) to decompose characters
    text = unicodedata.normalize('NFKC', text)
    # Remove invisible/control characters
    text = _pattern.sub('', text)
    # Replace curly quotes & dashes
    for src, dst in REPLACEMENTS.items():
        text = text.replace(src, dst)
    return text

# === GUI Application ===
class CleanerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Invisible Character Cleaner")
        self.geometry("800x500")

        # Configure grid weights: labels row=0, text row=1, button row=2
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        # Labels
        ttk.Label(self, text="Raw Text").grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))
        ttk.Label(self, text="Cleaned Text").grid(row=0, column=1, sticky="w", padx=10, pady=(10, 0))

        # Raw input text widget
        self.input_txt = tk.Text(self, wrap="word")
        self.input_txt.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=(5, 5))

        # Cleaned output text widget (read-only)
        self.output_txt = tk.Text(self, wrap="word", bg="#f0f0f0", state="disabled")
        self.output_txt.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=(5, 5))

        # Copy to Clipboard button
        self.copy_btn = ttk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_btn.grid(row=2, column=1, sticky="e", padx=10, pady=(0, 10))

        # Bind to <<Modified>> event for live updates
        self.input_txt.bind("<<Modified>>", self.on_modified)
        self.input_txt.edit_modified(False)

    def on_modified(self, event=None):
        if self.input_txt.edit_modified():
            raw = self.input_txt.get("1.0", "end")
            cleaned = clean_text(raw)
            # Update cleaned text pane
            self.output_txt.configure(state="normal")
            self.output_txt.delete("1.0", "end")
            self.output_txt.insert("1.0", cleaned)
            self.output_txt.configure(state="disabled")
            self.input_txt.edit_modified(False)

    def copy_to_clipboard(self):
        """Copy cleaned text to the system clipboard."""
        cleaned = self.output_txt.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(cleaned)

if __name__ == "__main__":
    app = CleanerApp()
    app.mainloop()
