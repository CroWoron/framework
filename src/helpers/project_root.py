from pathlib import Path


def get_project_root():
    """получение полного пути к корневой директории"""
    return Path(__file__).parent.parent.parent
