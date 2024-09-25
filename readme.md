
# Bitcoin Tools

This project provides a simple web application for working with Bitcoin data. It includes two tools:

* **Target Calculator:** This tool allows you to calculate the target value from a given compact target.
* **Block Verifier:** This tool takes a block header as input and verifies its hash.

The application is built using HTML, CSS, and JavaScript. It utilizes Tailwind CSS for styling.

## Getting Started

1. Clone the repository.
2. Open `index.html` in your web browser.
3. Or you can also checkout at [https://dongyukang.github.io/bitcoin-validator](https://dongyukang.github.io/bitcoin-validator)

## Usage

### Target Calculator

1. Enter a compact target value in hexadecimal format (e.g., `0x17038a6d`).
2. Click the "Calculate" button.
3. The results will be displayed, including the target value in decimal and hexadecimal formats, as well as the difficulty.

### Block Verifier

1. Enter a block header in hexadecimal format (80 bytes).
2. Click the "Verify" button.
3. The application will split the input into its components and display the SHA256 hash of the block header.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
