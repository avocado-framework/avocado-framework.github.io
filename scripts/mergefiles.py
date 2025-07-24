import glob
import os

import yaml


def merge_yaml_files(directory, output_file):
    merged_data = []  # Initialize an empty list to hold merged data

    # Find all YAML files recursively in subdirectories

    yaml_files = glob.glob(os.path.join(directory, "**", "*.yml"), recursive=True)
    yaml_files.extend(
        glob.glob(os.path.join(directory, "**", "*.yaml"), recursive=True)
    )

    # Process each YAML file found
    for file_path in sorted(yaml_files):
        filename = os.path.basename(file_path)
        with open(file_path, "r") as file:
            # Load the YAML data while preserving order
            data = yaml.load(file, Loader=yaml.SafeLoader)  # Use SafeLoader

            # Check if the loaded data is a dictionary
            if isinstance(data, dict):
                merged_data.append(data)  # Append the dictionary to merged_data
            else:
                print(
                    f"Warning: The content of {filename} is not a dictionary. Skipping."
                )

    # Write the merged data to the output YAML file
    with open(output_file, "w") as outfile:
        yaml.dump(
            merged_data, outfile, default_flow_style=False, sort_keys=False
        )  # Use sort_keys=False to maintain order


if __name__ == "__main__":
    input_directory = "main/_data/autils"
    output_file = "main/_data/autils/modules.yml"
    merge_yaml_files(input_directory, output_file)
    print(f"Merged YAML files from {input_directory} into {output_file}")
