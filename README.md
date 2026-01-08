# Log File Analyzer

The Log File Analyzer is a Python-based tool that parses server or application log files, extracts key information, and provides insights such as:
1. HTTP error code counts.
2. Error frequencies
3. IP adress summary

## Features
1. Parse log files line by line
2. Count occurrences of each IP address
3. Count occurrences of HTTP status codes
4. Export a text summary to log_summary.txt
5. Works with standard server log formats

## Tech Stack
```
-- Language : Python
-- Tools: VSCode, Git
-- Libraries: Faker
```

## Project Structure
```
log-file-analyzer-python/
│
|-- src/
|   |-- log_create.py
│   |-- analyzer.py         
│   ├── server_log.txt      
│   └── log_summary.txt  
|    
|-- README.md
|-- .gitignore    
```

## Installation
```
Clone the repository -> git clone https://github.com/Parashuram-V-Pawar/urban-mobility-fleet-management.git

Move to project folder 
    -> cd log-file-analyzer-python

Install dependencies 
    -> pip install -r requirements.txt

Run the application 
    -> First generate log file 
        -> python log_create.py
    -> Then, run analyzer
        -> python analyzer.py
```

## Author
```
Parashuram V Pawar
GitHub username: Parashuram-V-Pawar
```