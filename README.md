# VTTCleaner - a VTT to CSV Converter

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Pandas](https://img.shields.io/badge/pandas-1.0%2B-orange)

A Python tool that converts WebVTT (.vtt) caption files with speaker annotations into clean, structured CSV format for easy analysis and processing.

## Features

- 🎤 Extracts speaker names, timestamps, and dialogue from WebVTT files
- 🧹 Cleans formatting artifacts (trailing IDs, tags, etc.)
- 📊 Outputs structured CSV with columns: Timestamp, Speaker, Text
- ⏱ Preserves original timestamp-speaker relationships
- 🚀 Simple command-line interface
- 💾 Creates output in the same directory as input file

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/CTI-Buddy/VTTCleaner.git
   cd vtt-to-csv
   ```

2. Install dependencies:
   ```bash
   pip install pandas
   ```

## Usage

### Basic Command
```bash
python VTTCleaner.py
```

When prompted, enter the full path to your .vtt file:
```
Please enter the full path to your .vtt file: /path/to/your/file.vtt
```

### Example
Input file `meeting.vtt`:
```
WEBVTT

00:00:00.000 --> 00:00:02.340
<v John Doe>Let's begin the meeting
00:00:02.340 --> 00:00:05.670
<v Jane Smith>I agree with the proposal
```

Output file `meeting_formatted.csv`:
```
Timestamp,Speaker,Text
"00:00:00.000 --> 00:00:02.340","John Doe","Let's begin the meeting"
"00:00:02.340 --> 00:00:05.670","Jane Smith","I agree with the proposal"
```

## Input Format Requirements

The script processes WebVTT files with speaker annotations in the format:
```
<v Speaker Name>Spoken text here
```

## Output Format

The generated CSV contains three columns:
| Column | Description |
|--------|-------------|
| Timestamp | Original time range (e.g., "00:00:00.000 --> 00:00:02.340") |
| Speaker | Identified speaker name |
| Text | Cleaned dialogue text |

## Advanced Options

For batch processing, you can modify the script to:
1. Process all .vtt files in a directory
2. Accept command-line arguments instead of prompts
3. Customize output format

(Contributions welcome for these enhancements!)

## Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues or feature requests, please [open an issue](https://github.com/CTI-Buddy/VTTCleaner/issues).



Would you like me to make any adjustments to this README? For example:
- Add a screenshot of the tool in action?
- Include more detailed development instructions?
- Add a FAQ section?
