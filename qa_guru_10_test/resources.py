from pathlib import Path
import tests

def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'picture/{file_name}'))
