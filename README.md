# Xbox ISO Extractor GUI for macOS

This is a simple graphical interface for extracting Xbox 360 `.iso` game files on macOS using the `extract-xiso` binary.

## Features

- Drag & drop style UI
- Extract ISO files to any location
- One-click usage with embedded `extract-xiso`

## Requirements

- macOS
- Python 3.x
- `tkinter` module (pre-installed on macOS usually)

## Usage

1. Run the `main.py` file.
2. Select the `.iso` file.
3. Select the destination folder (e.g. your USB drive).
4. Click "Extract".

The tool will internally run the embedded `extract-xiso` binary.

## License

### GUI (main.py)
Licensed under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**  
You are free to use, modify, and share for non-commercial purposes with attribution.  
See `LICENSE.txt` for details.

### extract-xiso
This project includes the `extract-xiso` binary by in@fishtank.com, used under a BSD-style license.  
See `LICENSE_extract-xiso.txt` for full details.
