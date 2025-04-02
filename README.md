---

# SecPass - Password Strength Analyzer

SecPass is a cross-platform command-line tool that evaluates password strength and provides suggestions for improvement.

## Features
- Analyzes password strength using `zxcvbn`
- Provides alternative, stronger password suggestions
- Works on **Linux** and **Windows**
- Simple and fast execution

## Installation

### Clone the repository:
```sh
git clone https://github.com/shashank0-0/SecPass.git
cd SecPass
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```sh
python secpass.py -p <your-password>
```

### Example Output:
```
   _____           ____                 
  / ___/___  _____/ __ \____ ___________
  \__ \/ _ \/ ___/ /_/ / __ `/ ___/ ___/
 ___/ /  __/ /__/ ____/ /_/ (__  |__  ) 
/____/\___/\___/_/    \__,_/____/____/  
                                        
          Password Strength Tool

Password strength: Very Strong

Suggestions to improve your password:
- @bc@123##34234r23w33
- @bc@123##34234r23we3
- Abc@123##34234r23we3
```

## Running on Windows
For Windows users, you can run the standalone executable:

1. Download the latest **SecPass.exe** from [Releases](https://github.com/shashank0-0/SecPass/releases).
2. Open **PowerShell** in the same directory as the `.exe` file.
3. Run:
   ```sh
   .\SecPass.exe -p <your-password>
   ```

## License
This project is licensed under the **MIT License**.


---

