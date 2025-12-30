# Base64 Encoder/Decoder

A versatile CLI tool for Base64 operations. Easily encode strings or files (like images) into Base64, or decode them back.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **String Handling**: Quickly encode/decode text directly in the terminal.
*   **File Support**: Encode binary files (images, PDFs) to Base64 strings.
*   **Binary Recovery**: Decode Base64 strings back into their original file format.

## Usage

```bash
python run_base64.py [command] [options]
```

### Commands

*   `encode`: Convert to Base64.
*   `decode`: Convert from Base64.

### Examples

**1. Encode a String**
```bash
python run_base64.py encode "Hello World"
# Output: SGVsbG8gV29ybGQ=
```

**2. Decode a String**
```bash
python run_base64.py decode "SGVsbG8gV29ybGQ="
# Output: Hello World
```

**3. Encode an Image to Text File**
```bash
python run_base64.py encode ./logo.png --file --output logo.b64
```

**4. Decode Text File back to Image**
```bash
python run_base64.py decode ./logo.b64 --input-file --output logo_restored.png
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
