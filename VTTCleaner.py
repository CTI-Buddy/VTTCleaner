import os
import re
import pandas as pd

# Ask user for the path to the .vtt file
vtt_file_path = input("Please enter the full path to your .vtt file: ").strip()

# Check if the file exists
if not os.path.exists(vtt_file_path):
    print(f"Error: The file '{vtt_file_path}' does not exist. Please check the file path and try again.")
    exit()

# Read the file lines
with open(vtt_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize variables
entries = []
current_speaker = None
current_timestamp = None
current_text = []

# Regular expression patterns
timestamp_pattern = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3})")  # Timestamp
speaker_pattern = re.compile(r"<v ([^>]+)>(.*)")  # Speaker tag with text
cleanup_pattern = re.compile(r"</v>|[a-f0-9-]+/\d+-\d+$")  # Remove trailing IDs and tags

# Process lines
for line in lines:
    line = line.strip()
    
    if timestamp_pattern.match(line):  # If it's a timestamp
        current_timestamp = line if not current_speaker else current_timestamp  # Keep only the first timestamp
    elif speaker_pattern.match(line):  # If it's a speaker tag
        match = speaker_pattern.match(line)
        speaker = match.group(1).strip()  # Extract speaker name
        text = match.group(2).strip()  # Extract spoken text
        
        if speaker != current_speaker:  # If the speaker changes, save the previous entry
            if current_speaker and current_text:
                entries.append([current_timestamp, current_speaker, " ".join(current_text)])
            
            # Update current speaker and reset text
            current_speaker = speaker
            current_text = [cleanup_pattern.sub("", text).strip()]  # Clean text
        else:
            current_text.append(cleanup_pattern.sub("", text).strip())  # Append to existing speaker text
    elif line:  # If it's a continuation of the previous response
        current_text.append(cleanup_pattern.sub("", line).strip())

# Save last speaker's entry
if current_speaker and current_text:
    entries.append([current_timestamp, current_speaker, " ".join(current_text)])

# Convert to DataFrame
df = pd.DataFrame(entries, columns=["Timestamp", "Speaker", "Text"])

# Generate output filename
filename_without_ext = os.path.splitext(os.path.basename(vtt_file_path))[0]
csv_output_path = os.path.join(
    os.path.dirname(vtt_file_path),
    f"{filename_without_ext}_formatted.csv"
)

# Save to CSV
df.to_csv(csv_output_path, index=False)

# Output confirmation
print(f"\nFormatted CSV saved to: {csv_output_path}")
