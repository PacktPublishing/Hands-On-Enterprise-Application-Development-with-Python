from github import Github
import configparser

# Provide the location of where the config file exists
CONFIG_FILE = 'config.ini'

def parse_config():
    """Parse the configuration file and setup the required configuration."""

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if 'github_auth' not in config.sections():
        return False
    username = config['github_auth']['username']
    password = config['github_auth']['password']

    return (username, password)

def get_repos():
    """Retrieve the github repos associated with the user.

    Returns:
        Dict
    """

    response = {}
    config = parse_config()
    if not config:
        response['message'] = "Unable to read configuration"
        return response
    
    username = config[0]
    password = config[1]
    
    # Create the github object to authenticate
    g = Github(username, password)
    repos = []
    for repo in g.get_user().get_repos():
        repos.append(repo.name)
    response['repos'] = repos
    return response
