# Simple AI Agent

This repository contains a customizable AI Agent built using the **Phidata framework**. The agent is designed to integrate with various tools, internal APIs, and databases to enable versatile data retrieval, analysis, and automation. It supports dynamic configuration of data sources and AI models, making it adaptable for a wide range of use cases.

---

## Features

### 1. **Tool Customization**

- Integrate various external and internal tools to meet specific business needs.
- Flexibly configure work tools, APIs, and utilities to enhance operational workflows.

### 2. **Database Connectivity**

- Connect to internal databases for seamless querying and real-time data access.
- Supports structured and unstructured data for comprehensive insights.

### 3. **AI Model Integration**

- Leverage pre-trained and custom AI models for tasks such as:
  - Natural Language Processing (NLP)
  - Data analysis and predictions
  - Intelligent automation
- Compatible with popular AI frameworks (e.g., OpenAI, Groq).

### 4. **Scalable and Modular Architecture**

- Add or replace tools, APIs, and data sources easily.
- Scalable design to handle increased data processing or additional features.

---

## Technologies Used

- **Framework**: Phidata
- **Languages**: Python
- **Tools and Libraries**:
  - Pandas (Data manipulation)
  - Python-dotenv (Environment variable management)
  - Custom AI model integrations
- **Database**: Compatible with relational and NoSQL databases
- **Deployment**: Docker (optional for containerized setup)

---

## Installation

### Prerequisites

- Python 3.8 or above
- Virtual Environment (Recommended)
- Git

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/simple-ai-agent.git
   cd simple-ai-agent
   ```

2. **Set up Virtual Environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # For Linux/Mac
   .\.venv\Scripts\activate    # For Windows
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Add Environment Variables**:

   - Create a `.env` file in the root directory.
   - Add the necessary API keys and configuration values. Example:
     ```env
     API_KEY=your-api-key
     DATABASE_URL=your-database-url
     ```

5. **Run the Agent**:

   ```bash
   python main.py
   ```

---

## Usage

- Customize the tools, APIs, and databases in the `config` directory.
- Modify or add AI models in the `models` folder for specific use cases.
- Use the agent to query data, analyze inputs, or automate tasks.

---

## Example

**Query Example**:

```python
from agent import SimpleAgent

agent = SimpleAgent()
response = agent.query("Get latest stock prices")
print(response)
```

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed explanation of changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

- Built with the **Phidata framework**.
- Inspired by the need for customizable AI solutions.

