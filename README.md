# Stream Filter

> **stream-filter**: Lightweight Python tools to filter very large text files without high memory overhead.

## Tools

### 1. stream_filter.py
Extracts lines **containing** a given substring from large text files.

### 2. stream_delete.py
Removes lines **containing** a given substring from large text files.

## Features

- **Streaming**: Processes files line-by-line for O(1) memory usage.
- **Encoding fallback**: Automatically retries on UTF-16 if default encoding yields no matches.
- **Simple, case-sensitive matching**: Just specify the substring.
- **Zero dependencies**: Pure Python standard library.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/barmenteros/stream-filter.git
   cd stream-filter
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```

## Usage

### stream_filter.py - Extract matching lines

```bash
python stream_filter.py <path/to/log.txt> "AUDUSD,M15"
```

* **Input**: Path to a `.txt` file (ANSI/UTF-8/UTF-16 LE).
* **Filter**: Case-sensitive substring to find.
* **Output**: `input_filtered.txt` in the same directory, containing only matching lines.

### stream_delete.py - Remove matching lines

```bash
python stream_delete.py <path/to/log.txt> "ERROR"
```

* **Input**: Path to a `.txt` file (ANSI/UTF-8/UTF-16 LE).
* **Filter**: Case-sensitive substring to delete.
* **Output**: `input_cleaned.txt` in the same directory, with matching lines removed.

## Contributing

Contributions are welcome! Please open issues or pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
