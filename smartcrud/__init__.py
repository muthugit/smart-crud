from .base import SmartCrud


def init(repo_dir):
    sc = SmartCrud(repo_dir)
    return sc