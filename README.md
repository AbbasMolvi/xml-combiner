# xml-combiner

This Python script allows you to combine multiple XML files into a single XML file. It supports flexible input and output options via command-line arguments and includes a debug mode for detailed process tracking.

## Features

- **Combine Multiple XML Files**: Merge multiple XML files into one, with all contents nested under a new root element.
- **Command-Line Flexibility**: Specify input XML files and the output file directly from the command line.
- **Debug Mode**: Provides detailed output to help trace the script's execution, useful for troubleshooting.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. **Clone the Repository**:

    Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/yourusername/xml-combiner.git
    ```

2. **Navigate to the Script Directory**:

    Change to the directory containing the script:

    ```bash
    cd xml-combiner
    ```

## Usage

### Basic Command-Line Usage

To combine XML files, use the following command:

```bash
python xml-combiner.py -o output.xml -i file1.xml,file2.xml,file3.xml
```

- `-o output.xml`: Specifies the output file where the combined XML will be saved.
- `-i file1.xml,file2.xml,file3.xml`: A comma-separated list of input XML files to be combined.

### Interactive Mode

If you prefer to enter file paths interactively:

```bash
python combine_xml.py -o output.xml
```

You will be prompted to enter the paths of the XML files one by one. Type `done` when you have finished entering all file paths.

### Debug Mode

Enable debug mode to see detailed logs of the script's execution:

```bash
python xml-combiner.py -o output.xml -i file1.xml,file2.xml -d
```

- `-d`: Enables debug mode, providing additional output to help trace the script's operations.

## Example

To combine `file1.xml` and `file2.xml` into a single file named `combined.xml`, you can run:

```bash
python xml-combiner.py -o C:\path\to\combined.xml -i C:\path\to\file1.xml,C:\path\to\file2.xml
```

If you want to see detailed processing information, add the `-d` flag:

```bash
python xml-combiner.py -o C:\path\to\combined.xml -i C:\path\to\file1.xml,C:\path\to\file2.xml -d
```

## Troubleshooting

- **File Not Found**: Ensure all input file paths are correct and accessible.
- **Parsing Errors**: If an XML file is malformed, the script will report a parsing error. Use debug mode for more details.

## License

This project is licensed under the MIT License.
