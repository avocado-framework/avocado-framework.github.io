import os

import yaml


def merge_yaml_files(directory, output_file):
    merged_data = []  # Initialize an empty list to hold merged data

    # Iterate over all files in the directory
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                # Load the YAML data while preserving order
                data = yaml.load(file, Loader=yaml.SafeLoader)  # Use SafeLoader

                # Check if the loaded data is a list
                if isinstance(data, list):
                    merged_data.extend(data)  # Merge the list into merged_data
                else:
                    print(
                        f"Warning: The content of {filename} is not a list. Skipping."
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
