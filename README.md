# SecPass - Password Strength Analyzer

SecPass is a command-line tool that evaluates the strength of a given password and provides suggestions for improving it.

## Features
- Analyzes password strength
- Provides alternative, stronger password suggestions
- Simple and fast execution

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/shashank0-0/SecPass.git
   ```
2. Navigate to the project directory:
   ```sh
   cd SecPass
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script using Python:
```sh
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

## License
This project is licensed under the MIT License.
