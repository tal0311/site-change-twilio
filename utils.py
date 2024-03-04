

def get_env(filename='.env', env_var='API_KEY'):
    with open(filename, 'r') as file:
        lines = file.readlines()
        while lines:
           line = lines.pop(0)
           if line.startswith(env_var):
                return line.split('=')[1].strip()

