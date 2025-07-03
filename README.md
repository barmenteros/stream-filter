# Stream Filter

> **stream-filter**: A lightweight Python tool to extract lines containing a given substring from very large text files without high memory overhead.

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

```bash
python stream_filter.py <path/to/log.txt> "AUDUSD,M15"
```

* **Input**: Path to a `.txt` file (ANSI/UTF-8/UTF-16 LE).
* **Filter**: Case-sensitive substring.
* **Output**: `input_filtered.txt` in the same directory, containing matching lines.

## Contributing

Contributions are welcome! Please open issues or pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
