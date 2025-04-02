# SecPass - Password Strength Analyzer ðŸ”

SecPass is a **command-line tool** that evaluates the strength of a given password and provides suggestions for improving it.

## ðŸš€ Features
- **Analyzes password strength** using advanced entropy calculations.
- **Provides alternative, stronger password suggestions**.
- **Simple and fast execution**.
- **Cross-platform support** (Linux & Windows).

---

## ðŸ“¥ Installation

### Linux/macOS
```bash
git clone https://github.com/shashank0-0/SecPass.git
cd SecPass
pip install -r requirements.txt
```

### Windows (PowerShell)
```powershell
git clone https://github.com/shashank0-0/SecPass.git
cd SecPass
pip install -r requirements.txt
```

---

## âš¡ Usage

### Running on Linux/macOS
```bash
python secpass.py -p <your-password>
```

### Running on Windows (Command Prompt or PowerShell)
```powershell
python secpass.py -p <your-password>
```

### Example Output
```
   _____           ____                 
  / ___/___  _____/ __ \____ ___________
  \__ \/ _ \/ ___/ /_/ / __ `/ ___/ ___/
 ___/ /  __/ /__/ ____/ /_/ (__  |__  ) 
/____/\___/\___/_/    \__,_/____/____/  

          Password Strength Tool

Password strength: Strong

Suggestions to improve your password:
- $h@sH@nk@123#
- sha$Hank@123#
- Sh@$hank@123#
```

---

## ðŸ—ï¸ Windows Executable

To use SecPass without installing Python, you can download the **pre-built Windows executable** from the [Releases](https://github.com/shashank0-0/SecPass/releases) section.

Alternatively, you can build it yourself:
```powershell
pyinstaller --onefile secpass.py
```

This will create a standalone `SecPass.exe` inside the `dist/` folder.

---

## ðŸ“œ License
This project is licensed under the **MIT License**.
