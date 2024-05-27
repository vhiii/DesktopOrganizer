# DesktopOrganizer
Desktop Organizer is a Python-based application that helps you organize files on your desktop by moving them into categorized folders. This application can sort files by type (e.g., documents, images, videos) and place them into corresponding folders to keep your desktop neat and organized.

## Features

-Automatically organize desktop files into folders by file type.
-Customizable folder names and types. 
-Simple and easy-to-use interface. 

### Usage
To use the Desktop Organizer, simply run the executable or the Python script. The program will automatically scan your desktop for files and move them into categorized folders.

### Running the Executable
If you have downlaoded the executable ('desktoporganizerGUI.exe'), simply double-click it to run the program. The executable is self-contained and does not require Python to be installed on your system.

## Installation

### Prerequisites
-Python 3.11.4 or higher
-Pyinstaller 6.7.0 (for creating the executable)

### Steps
1. Clone the repository:

    ```sh
    git clone https://github.com/vhiii/desktoporganizer.git
    cd desktoporganizer
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
    python desktoporganizerGUI.py
    ```

### Command Line
If using the pyhton script directly, you can customize its behavior with command-line arguments:
   
    python desktoporganizerGUI.py --source "C:\Path\To\Desktop" --dest "C:\Path\To\OrganizedFolder"

