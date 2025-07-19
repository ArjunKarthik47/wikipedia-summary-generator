# wikipedia-summary-generator
# 🧠 Wikipedia Summary Tool

A user-friendly Python desktop application that fetches, displays, speaks, and saves Wikipedia summaries using a simple GUI.

---

## ✨ Features

- 🔍 Search Wikipedia topics
- 📄 View a 10-sentence summary
- 💾 Save the summary as a `.txt` file
- 🔊 Listen to the summary using Text-to-Speech (TTS)
- 🖥️ Clean and responsive Tkinter GUI

---

## 🛠 Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `wikipedia`
  - `pyttsx3`
  - `tkinter` (comes with Python by default)

Install dependencies using:
bash
pip install wikipedia pyttsx3

## 🚀 Installation
### 1. Clone the Repository

git clone https://github.com/your-username/wikipedia-summary-tool.git
cd wikipedia-summary-tool
2. Install Required Libraries
pip install wikipedia pyttsx3
3. Run the Application
python app.py

## 🧭 Usage Guide
Enter a Topic
Type a topic (e.g., Python programming) into the input field.

### Fetch Summary
Click the "Fetch Summary" button to retrieve a 10-sentence Wikipedia summary.

### Save Summary
Click "Save as Topic File" to save the summary locally.

### Speak Summary
Click "Speak Summary" to hear the summary read aloud.

## 💡 Example Topics
Try searching for:
Alan Turing
Artificial Intelligence
World War II
Mount Everest
Elon Musk

## ⚠️ Error Handling
Empty Input: Prompts the user to enter a topic.

Disambiguation Error: Suggests alternative topics if Wikipedia finds multiple pages.

Page Not Found: Displays an error if no Wikipedia page exists for the given input.

## 📁 Project Structure
wikipedia-summary-tool/
│
├── app.py                # Main application script
├── README.md             # Documentation
└── *.txt                 # Saved summaries (created after fetching)

## 🧱 Tech Stack
Python
Tkinter (GUI)
Wikipedia API (wikipedia package)
pyttsx3 (offline TTS)

## 📜 License
This project is licensed under the MIT License.

## Acknowledgements
Wikipedia Python Library
pyttsx3 Text-to-Speech
Python's tkinter module for GUI


## 📬Contact
For questions, feedback, or suggestions:
📧 thakurarjunkarthiksingh@gmail.com
🐙 GitHub: @ArjunKarthik47

---
