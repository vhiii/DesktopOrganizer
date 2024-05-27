# Desktop Organizer

Desktop Organizer is a Python-based application designed to help you keep your desktop tidy by automatically organizing files into categorized folders. This application sorts files by type (e.g., documents, images, videos) and places them into corresponding folders, ensuring a clutter-free workspace.

## Features

- Automatically organize desktop files into folders based on file type.
- Customizable folder names and types.
- Simple and user-friendly interface.

## Installation

### Prerequisites

- Python 3.11.4 or higher (only needed if running the Python script directly)
- PyInstaller 6.7.0 (for creating the executable, if desired)

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/desktop-organizer.git
    cd desktop-organizer
    ```

2. (Optional) Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the script:

    ```sh
    python desktoporganizer.py
    ```

## Usage

To use the Desktop Organizer, you can either run the executable or the Python script. The program will automatically scan your desktop for files and move them into categorized folders.

### Running the Executable

If you have downloaded the executable (`desktoporganizer.exe`), simply double-click it to run the program. The executable is self-contained and does not require Python to be installed on your system.

### Running the Python Script

If you prefer to run the Python script directly, follow these steps (ensure Python is installed):

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/desktop-organizer.git
    cd desktop-organizer
    ```

2. (Optional) Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the script:

    ```sh
    python desktoporganizer.py
    ```

### Command Line Usage

When using the Python script directly, you can customize its behavior with command-line arguments:

```sh
python desktoporganizer.py --source "C:\Path\To\Desktop" --dest "C:\Path\To\OrganizedFolder"
