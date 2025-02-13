Welcome to the AI Code Reviewer project! This tool leverages the power of AI to review code, provide bug reports, and suggest fixed code. It uses the `gemini-2.0-flash-exp` model to deliver accurate and reliable code reviews.

## Features
- **Code Review:** Automatically review your code and identify potential bugs.
- **Bug Reports:** Receive detailed bug reports outlining issues in your code.
- **Fixed Code:** Get suggestions for fixing the identified bugs.
- **User Queries:** Enter specific queries to receive targeted feedback and changes in your code.

## Getting Started

### Prerequisites
- [Python](https://www.python.org/downloads/)
- [Streamlit](https://docs.streamlit.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai) (API Key required)

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/aicode-reviewer.git
    ```
2. **Navigate to the Project Directory:**
    ```bash
    cd aicode-reviewer
    ```
3. **Install the Required Libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **API Key Setup:**
    - Create a text file named `keys.txt` in the project directory.
    - Add your Google Generative AI API key to the `keys.txt` file.

### Running the Application

1. **Start the Streamlit App:**
    ```bash
    streamlit run app.py
    ```
2. **Use the Interface:**
    - Enter your code in the provided text area.
    - Optionally, enter a specific query for more tailored feedback.
    - Click the 'Review Code' button to get the bug report and fixed code suggestions.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request with your changes. Make sure to follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Inspired by the [Streamlit](https://www.streamlit.io/) framework.
- Powered by [Google Generative AI](https://cloud.google.com/generative-ai).

---

Happy coding! If you have any questions or run into any issues, feel free to open an issue in the repository.
