import json
import os
import re

# Define the path to the directory containing the JSON files
json_dir = "./jsons"

# Define the path to the Python script that will work with the output text file
script_path = "./generator.py"

# Create a new directory to store the output files
output_dir = "./input_files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all the JSON files in the directory
json_files = [f for f in os.listdir(json_dir) if f.endswith(".json")]

# Loop through each JSON file
for i, json_file in enumerate(json_files):

     # Open the JSON file and create a new output file for it
    with open(os.path.join(json_dir, json_file), "r") as jf:
        for line in jf:
            if line.startswith('			"category":'):
                output_path = os.path.join(output_dir, f"input_file{i+1}.txt")
                with open(output_path, "w") as f:
                    f.write("#Mandatory value:\nEventType->"+line.split('"')[3])
            if line.startswith('				"Image":'):
                output_path = os.path.join(output_dir, f"input_file{i+1}.txt")
                with open(output_path, "a") as f:
                    f.write("\nImage->"+line.split('"')[3])
            if line.startswith('				"CommandLine":'):
                output_path = os.path.join(output_dir, f"input_file{i+1}.txt")
                with open(output_path, "a") as f:
                    f.write("\n\n#Fill only one:\nCommandLine->"+line.split('"')[3]+"\nTargetFileName->")
                break
            if line.startswith('				"TargetFilename":'):
                output_path = os.path.join(output_dir, f"input_file{i+1}.txt")
                with open(output_path, "a") as f:
                    f.write("\n\n#Fill only one:\nCommandLine->\n"+"TargetFileName->"+line.split('"')[3])
                break

# Loop through each file in the directory
for filename in os.listdir(output_dir):
    filepath = os.path.join(output_dir, filename)
    
    # Check if the file is a text file
    if os.path.isfile(filepath) and filename.endswith(".txt"):
        # Read the contents of the file
        with open(filepath, "r") as f:
            file_contents = f.read()
        
        # Replace all occurrences of \\ with /
        new_contents = re.sub(r"\\\\", "/", file_contents)
        
        # Write the updated contents back to the file
        with open(filepath, "w") as f:
            f.write(new_contents)
 
