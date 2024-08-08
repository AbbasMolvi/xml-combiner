import xml.etree.ElementTree as ET
import argparse
import os

def combine_xml_files(file_list, output_file, debug=False):
    # Create a new root element for the combined XML
    combined_root = ET.Element("CombinedRoot")

    for file in file_list:
        try:
            if debug:
                print(f"Debug: Parsing file: {file}")
            tree = ET.parse(file)
            root = tree.getroot()

            # Append the root element of each file to the combined root
            combined_root.append(root)
        except ET.ParseError as e:
            print(f"Error parsing {file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with file {file}: {e}")

    # Create a new tree with the combined root and write to output file
    combined_tree = ET.ElementTree(combined_root)
    try:
        combined_tree.write(output_file, encoding="utf-8", xml_declaration=True)
        print(f"Successfully combined XML files into {output_file}")
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Combine multiple XML files into a single XML file.")
    parser.add_argument('-o', '--output', required=True, help='Output file for the combined XML.')
    parser.add_argument('-i', '--input', help='Comma-separated list of XML files to combine.')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode.')

    args = parser.parse_args()

    # Parse the input files argument
    if args.input:
        xml_files = [file.strip() for file in args.input.split(',')]
    else:
        # Interactive input if --input is not provided
        xml_files = []
        print("Enter the XML file paths, one per line. Type 'done' when finished:")
        while True:
            file = input("File path: ").strip()
            if file.lower() == 'done':
                break
            if file:
                xml_files.append(file)
    
    # Check if output directory exists
    output_dir = os.path.dirname(args.output)
    if not os.path.exists(output_dir) and output_dir:
        os.makedirs(output_dir)

    # Combine XML files
    combine_xml_files(xml_files, args.output, debug=args.debug)

if __name__ == "__main__":
    main()
