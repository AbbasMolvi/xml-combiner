# xml-combiner

This Python script combines all XML files from a specified directory into a single XML file, offering command-line flexibility and a debug mode for in-depth process tracking. With the ability to handle multiple files automatically, this tool is ideal for users who need to merge large sets of XML files efficiently.

**Features:**
- **Directory-Based XML Combination:** Automatically merge all XML files located within a specified directory, organizing the content under a single root element in the output file.
- **Command-Line Simplicity:** Easily specify the input directory and output file path through command-line arguments, streamlining the file processing workflow.
- **Debug Mode:** Activate detailed logging to monitor the script's operations step by step, useful for identifying issues during execution.

**Prerequisites:** Ensure Python 3.x is installed on your system before running the script.

**Installation:** Clone the repository to your local machine and navigate to the script's directory:
`git clone https://github.com/yourusername/xml-combiner.git` 
`cd xml-combiner`

**Usage:** To combine all XML files from a directory into a single output file, use:
`python xml-combiner.py -o output.xml -i path_to_xml_folder`
- `-o output.xml`: Define the path and name of the output XML file.
- `-i path_to_xml_folder`: Specify the directory containing the XML files you want to combine.

For enhanced tracking of the process, enable debug mode:
`python xml-combiner.py -o output.xml -i path_to_xml_folder -d`

**Example:** Combine all XML files in `C:\path\to\folder` into a file named `combined.xml`:
`python xml-combiner.py -o C:\path\to\combined.xml -i C:\path\to\folder`

To see detailed execution logs, add the `-d` flag:
`python xml-combiner.py -o C:\path\to\combined.xml -i C:\path\to\folder -d`

**Troubleshooting:**
- **File Not Found:** Ensure the input directory exists and contains XML files.
- **Parsing Errors:** Malformed XML files will trigger parsing errors. Use debug mode to pinpoint the issue.

**License:** This project is licensed under the MIT License.
