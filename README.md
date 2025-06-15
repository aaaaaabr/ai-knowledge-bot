# AI Knowledge Bot 🤖📚

Welcome to the **AI Knowledge Bot** repository! This project is my custom-built offline AI bot designed to facilitate conversations with PDFs and web pages. By leveraging local embeddings and local LLMs like LLaMA 3, I have created a solution that doesn't depend on external APIs. This bot allows you to interact with your documents seamlessly.

[![Download Releases](https://img.shields.io/badge/Download%20Releases-Click%20Here-brightgreen)](https://github.com/aaaaaabr/ai-knowledge-bot/releases)

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Chat with PDFs**: Easily interact with your PDF documents.
- **Web Page Interaction**: Chat with content from web pages.
- **Local Processing**: Operates entirely offline, ensuring privacy and security.
- **Document Summarization**: Get concise summaries of lengthy documents.
- **Customizable**: Tailor the bot to fit your specific needs.
- **User-Friendly Interface**: Built with Streamlit for easy access.

## Technologies Used

This project incorporates several powerful technologies:

- **LangChain**: For building applications with language models.
- **FAISS**: For efficient similarity search and clustering of dense vectors.
- **HuggingFace**: To utilize pre-trained models for embeddings.
- **Ollama**: To run local LLMs without the need for external APIs.
- **LLaMA 3**: A state-of-the-art local language model.

## Installation

To get started with the AI Knowledge Bot, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aaaaaabr/ai-knowledge-bot.git
   cd ai-knowledge-bot
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Required Models**:
   You can find the necessary models in the [Releases](https://github.com/aaaaaabr/ai-knowledge-bot/releases) section. Download the models and place them in the `models/` directory.

4. **Run the Application**:
   Start the bot with:
   ```bash
   streamlit run app.py
   ```

## Usage

Once you have installed the AI Knowledge Bot, you can begin using it:

1. **Open Your Browser**: Navigate to `http://localhost:8501` to access the bot.
2. **Upload a PDF or Input a Web Page URL**: Use the interface to upload your documents or input URLs.
3. **Start Chatting**: Ask questions or request summaries about the content.

### Example Commands

- "Summarize this document."
- "What are the key points in this PDF?"
- "Explain the content of this web page."

## Contributing

I welcome contributions to enhance the AI Knowledge Bot. If you want to contribute, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right of the page.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Fork**:
   ```bash
   git push origin feature/YourFeature
   ```
6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License. Feel free to use it for personal or commercial purposes.

## Contact

If you have any questions or suggestions, feel free to reach out:

- **Email**: your-email@example.com
- **GitHub**: [your-github-profile](https://github.com/your-github-profile)

For updates and releases, check the [Releases](https://github.com/aaaaaabr/ai-knowledge-bot/releases) section regularly.

## Acknowledgments

- Thanks to the developers of LangChain, FAISS, HuggingFace, and Ollama for their amazing tools.
- Special thanks to the open-source community for their continuous support and contributions.

---

Thank you for checking out the AI Knowledge Bot! I hope you find it useful for your document interaction needs.