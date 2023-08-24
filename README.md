# Thunderbird IMAP Tree

This repository contains a script that processes Thunderbird's `folderTree.json` files to visualize the structure of your email folders in a hierarchical tree format.

## Description

The Python script in this repository interprets the IMAP paths from Thunderbird's `folderTree.json` and presents them as a structured tree representation, similar to a directory structure in a bash shell. This provides an intuitive view of your email folder hierarchy.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/kevinveenbirkenbach/thunderbird-imap-tree.git
   ```

2. Navigate to the directory:
   ```bash
   cd thunderbird-imap-tree
   ```

3. Run the script with the path to your `folderTree.json`:
   ```bash
   python imap_tree.py path/to/your/folderTree.json
   ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

Created by Kevin Veen-Birkenbach
- Email: [kevin@veen.world](mailto:kevin@veen.world)
- Website: [www.veen.world](https://www.veen.world/)


## License

This code is licensed under the GNU Affero General Public License Version 3. Please see the [LICENSE](LICENSE) file for more details or visit the [GNU website](https://www.gnu.org/licenses/agpl-3.0.html).
