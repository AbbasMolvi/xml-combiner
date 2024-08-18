import xml.etree.ElementTree as ET
import argparse
import os

def combine_xml_files(folder_path, output_file, debug=False):
    combined_root = ET.Element("CombinedRoot")
    file_count = 0

    # Get all XML files in the provided folder
    file_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xml')]

    if not file_list:
        print(f"No XML files found in the directory: {folder_path}")
        return

    for file in file_list:
        try:
            if debug:
                print(f"Debug: Parsing file: {file}")
            tree = ET.parse(file)
            root = tree.getroot()
            root.set("source", os.path.basename(file))
            combined_root.append(root)
            file_count += 1

            if debug:
                print(f"Debug: Added root tag '{root.tag}' from {file}")

        except ET.ParseError as e:
            print(f"Error parsing {file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with file {file}: {e}")

    if file_count > 0:
        combined_tree = ET.ElementTree(combined_root)
        try:
            combined_tree.write(output_file, encoding="utf-8", xml_declaration=True)
            print(f"Successfully combined {file_count} XML files into {output_file}")
        except Exception as e:
            print(f"Error writing to file {output_file}: {e}")
    else:
        print("No valid XML files to combine. Output file was not created.")

def main():
    parser = argparse.ArgumentParser(description="Combine multiple XML files from a directory into a single XML file.")
    parser.add_argument('-o', '--output', required=True, help='Output file for the combined XML.')
    parser.add_argument('-i', '--input', required=True, help='Input directory containing XML files to combine.')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode.')

    args = parser.parse_args()

    # Validate input directory
    if not os.path.isdir(args.input):
        print(f"Error: The provided input path is not a directory or does not exist: {args.input}")
        return

    # Check if output directory exists
    output_dir = os.path.dirname(args.output)
    if not os.path.exists(output_dir) and output_dir:
        os.makedirs(output_dir)

    # Combine XML files
    combine_xml_files(args.input, args.output, debug=args.debug)

if __name__ == "__main__":
    main()
