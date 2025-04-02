SecPass - Password Strength Analyzer

SecPass is a command-line tool for analyzing password strength and providing stronger suggestions. It evaluates passwords based on complexity and entropy, ensuring enhanced security.

Features

Evaluates password strength.

Provides suggestions for stronger passwords.

Simple and easy-to-use CLI interface.


Installation

Ensure you have Python installed, then install dependencies:

pip install -r requirements.txt

Usage

Run SecPass using the following command:

python secpass.py -p <your_password>

Example

python secpass.py -p shashank@123#

Output:

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

Contributing

Feel free to submit issues or pull requests to improve SecPass!

License

This project is licensed under the MIT License.


