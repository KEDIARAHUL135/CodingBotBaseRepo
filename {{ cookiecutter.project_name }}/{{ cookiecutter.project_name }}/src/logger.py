import os
import yaml
import logging
import logging.config


def setup_logger(config_file="{{ cookiecutter.project_name }}/configs/logging.yaml") -> None:
    """
    Sets up the logger using the provided YAML configuration file.

    :param config_file: Path to the YAML configuration file.
    """
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)
    else:
        # Fallback configuration
        logging.basicConfig(level=logging.INFO)
    

def get_logger(name):
    """
    Initializes and returns the logger for the file.

    :param name: Name of the file for which the logger should be initialized.
    :return: Configured logger instance.
    """
    setup_logger()
    logger = logging.getLogger(name)
    return logger

# Example usage:
if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Logger is configured and ready!")
