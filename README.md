# Qwerty-Editor

## Overview

A minimal text editor wrapped around the Curses library. The editor can only run on the following platforms: Mac and Linux-based systems.

Commands:
- Esc to exit the program without saving
- F1 to Save and exit

## Installation

### Prerequisites

- Python 3.14+
- uv

Install uv:

```bash
pip install uv
```

### Clone The Repository

```bash
git clone https://github.com/royalvarez/qwerty-editor.git
cd qwerty-editor
```

### Install Dependencies

```bash
uv sync
```

## Usage

Open the text editor in the terminal:
```bash
uv run main.py
```

## License

This project is licensed under the [MIT License](./LICENSE).