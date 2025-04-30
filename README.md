# VTTCleaner - a VTT to CSV Converter

A simple Python tool to convert WebVTT (.vtt) files with speaker annotations into a structured CSV format.

## Features

- Extracts speaker names, timestamps, and dialogue from WebVTT files
- Cleans up formatting artifacts (like trailing IDs and tags)
- Outputs a well-structured CSV file with columns: Timestamp, Speaker, Text
- Preserves the original file's timestamp and speaker relationships

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install pandas
Usage
Run the script:

bash
python vtt_to_csv.py
When prompted, enter the full path to your .vtt file

Example: C:\Users\YourName\Documents\transcript.vtt or /home/username/transcript.vtt

The script will generate a CSV file in the same directory as your input file

Output format: [original_filename]_formatted.csv

Input File Format
The script expects WebVTT files with speaker annotations in the format:

WEBVTT

00:00:00.000 --> 00:00:02.340
<v Speaker Name>This is what the speaker said
Output Format
The generated CSV will contain three columns:

Timestamp: The time range from the VTT file

Speaker: The identified speaker

Text: The cleaned dialogue text

Limitations
Currently only processes speaker tags in the format <v Speaker Name>

May need adjustment for VTT files with significantly different formatting

License
This project is open-source and available under the MIT License.
