import sys
import json

def add_to_tree(tree, path):
    for part in path:
        if part not in tree:
            tree[part] = {}
        tree = tree[part]

def print_tree(tree, indent=0):
    for key, value in tree.items():
        print(' ' * indent + key)
        if isinstance(value, dict):
            print_tree(value, indent + 4)

def main(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    imap_paths = data["open"]["all"]

    tree = {}
    for imap_path in imap_paths:
        # Strip the 'imap://' and split by '/'
        parts = imap_path.replace('imap://', '').split('/')
        add_to_tree(tree, parts[1:])

    print_tree(tree)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_file>")
    else:
        file_path = sys.argv[1]
        main(file_path)
