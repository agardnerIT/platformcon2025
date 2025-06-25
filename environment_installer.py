import os
from loguru import logger

NAME = os.environ.get("NAME", "")
COLOUR = os.environ.get("COLOUR", "blue")

replaced_lines = []

# Read all the existing lines
with open("/var/www/html/index.html", mode="r") as file:
    lines = file.readlines()

    # If a line contains a placeholder
    # replace it
    for line in lines:
        if "PLACEHOLDER" not in line:
            logger.info("Uninteresting line. Skipping")
            replaced_lines.append(line)
            continue

        if "NAME_PLACEHOLDER" in line:
            # Must replace NAME_PLACEHOLDER
            line = line.replace("NAME_PLACEHOLDER", NAME)
        elif "COLOUR_PLACEHOLDER" in line:
            # Must replace COLOUR_PLACEHOLDER
            line = line.replace("COLOUR_PLACEHOLDER", COLOUR)
        
        replaced_lines.append(line)

with open("/var/www/html/index.html", mode="w") as file:
    file.writelines(replaced_lines)