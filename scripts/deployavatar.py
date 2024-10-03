import logging
from collections import OrderedDict

import requests
import yaml

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Path to the YAML file
yaml_file_path = "main/_data/autils/modules.yml"


# Custom loader and dumper to handle OrderedDict
def ordered_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )
    return yaml.load(stream, OrderedLoader)


def ordered_dump(data, stream=None, Dumper=yaml.SafeDumper, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_dict(data.items())

    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


# Load the YAML file
with open(yaml_file_path, "r") as file:
    modules = ordered_load(file, yaml.SafeLoader)
    logging.debug(f"Loaded modules: {modules}")

# Update the maintainer image
for module in modules:
    # Iterate through each maintainer in the module
    for maintainer in module.get("maintainers", []):
        github_username = maintainer.get("github_usr_name", "")
        github_username = github_username.strip(": ")
        logging.debug(f"Processing maintainer with GitHub username: {github_username}")
        if github_username:
            response = requests.get(f"https://api.github.com/users/{github_username}")
            logging.debug(
                f"GitHub API response for {github_username}: {response.status_code}"
            )
            if response.status_code == 200:
                user_data = response.json()
                # Update maintainer_image inside the maintainer dictionary
                maintainer["maintainer_image"] = user_data.get("avatar_url", "")
                logging.debug(
                    f"Updated maintainer image for {github_username}: {maintainer['maintainer_image']}"
                )
            else:
                logging.error(
                    f"Failed to fetch data for {github_username}: {response.status_code}"
                )
        else:
            logging.warning(f"No GitHub username found for maintainer: {maintainer}")

# Save the updated YAML file
with open(yaml_file_path, "w") as file:
    ordered_dump(modules, file, default_flow_style=False)
    logging.debug("Saved updated modules to YAML file")
