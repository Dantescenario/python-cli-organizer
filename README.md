# 📂 File Organizer CLI Tool

A practical command-line interface (CLI) tool built with **Python** that automatically sorts and organizes files in a specified directory into categorized subfolders based on their file extension.

## ✨ Features

* **Automatic Sorting:** Categorizes files into folders like `IMAGES`, `DOCUMENTS`, `VIDEOS`, `CODE`, and `ARCHIVES`.
* **Safe Execution:** Only moves files; ignores existing directories and the script itself.
* **Flexible:** Uses the `argparse` module to accept any directory path as input.
* **Default Handling:** Places unlisted file types into an `OTHERS` folder.

## 🛠️ Technology Stack

* **Language:** Python 3
* **Modules:** `os`, `shutil`, `argparse` (all standard library modules)

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3** installed on your system.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Dantescenario/file-organizer-cli.git](https://github.com/Dantescenario/file-organizer-cli.git)
    cd file-organizer-cli
    ```
2.  **Verify the Script**
    Ensure the main file `organizer.py` is present.

## How to Use

The script requires you to pass the target directory path as a command-line argument.

### Basic Command Structure

```bash
python organizer.py [PATH_TO_YOUR_DIRECTORY]