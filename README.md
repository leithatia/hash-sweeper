# About hash_sweeper
This Python script is designed to enhance cybersecurity efforts by scanning files for known malicious hashes. It cross-references each file in a specified directory against a list of dangerous hash signatures. Upon completion, the app identifies files containing these hazardous elements and provides a count of the number of matches found. This tool is useful for system administrators, cybersecurity professionals, or anyone needing to perform routine checks for compromised files.

The idea is that each file to be scanned represents a system and contains the hashes captured after a snapshot of the system.

# Usage
This script takes the directory path of the files to search through and the path to the file containing the malicious hashes as arguments. The files should only contain the hashes, each on a new line. To run the script use the following command:
```
python hash_sweeper.py <directory_to_scan> <path_to_hash_file>
```
The output is a list of the files and the number of times a malicious hash has been found in each file. The list is sorted by the number of hits, highest first.
