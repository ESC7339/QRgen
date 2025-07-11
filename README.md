# QR Code Generator

A simple command-line tool to generate QR codes from arbitrary strings.

## Features

- Validates input data and output path  
- Generates high-quality PNG QR codes  
- Customizable error-correction level, box size, and border via code modifications

## Requirements

- Python 3.6 or higher  
- [qrcode](https://pypi.org/project/qrcode/)  
- [Pillow](https://pypi.org/project/Pillow/) (for image generation)

## Installation

```bash
git clone https://github.com/esc7339/qr-code-generator.git
cd qr-code-generator
pip install qrcode pillow
