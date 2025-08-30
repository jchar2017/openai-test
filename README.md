\# OpenAI API Test with Python



This project demonstrates how to securely use the OpenAI API from Python by storing your API key in a `.env` file and loading it with `python-dotenv`.  



It covers:

\- Project setup with environment variables  

\- Reading an API key securely (without hardcoding)  

\- Sending a simple request to the OpenAI API  

\- Handling quota/billing issues gracefully  

\- A fallback \*\*“fake mode”\*\* for showcasing functionality without incurring API costs  



---



\## 🚀 How It Works

1\. Create a `.env` file in the project folder:

&nbsp;  ```

&nbsp;  OPENAI\_API\_KEY=sk-your\_api\_key\_here

&nbsp;  ```

&nbsp;  ⚠️ Never share your real key — `.env` should be kept private.



2\. Install the required packages:

&nbsp;  ```bash

&nbsp;  pip install openai python-dotenv

&nbsp;  ```



3\. Run the script:

&nbsp;  ```bash

&nbsp;  python test\_env.py

&nbsp;  ```



4\. Expected output:

&nbsp;  ```

&nbsp;  Your API key starts with: sk-proj

&nbsp;  Hi there! 👋 This is a test response.

&nbsp;  ```

\## 📂 Project Structure

```

openai\_test/

│── test\_env.py       # Main script

│── .env              # API key (not shared in repo)

│── requirements.txt  # Dependencies

│── README.md         # Documentation

```



\## 💡 Features

\- \*\*Secure key loading\*\*: Keeps API keys out of source code.  

\- \*\*Real or Fake mode\*\*: Can run with real OpenAI responses (if billing enabled) or fake simulated responses (for demos).  

\- \*\*Extensible\*\*: Can be expanded into a mini chatbot or other OpenAI-powered tools.

&nbsp; 

\## 🔧 Example Code

```python

import os

from dotenv import load\_dotenv, find\_dotenv

import openai



\# Load API key

\_ = load\_dotenv(find\_dotenv())

openai.api\_key = os.getenv("OPENAI\_API\_KEY")



\# Send test request

response = openai.chat.completions.create(

&nbsp;   model="gpt-4o-mini",

&nbsp;   messages=\[{"role": "user", "content": "Hello OpenAI, can you say hi back?"}]

)



print(response.choices\[0].message.content)

```

\## ⚠️ Notes

\- A ChatGPT Plus subscription does \*\*not\*\* include API credits.  

\- To use the API, enable billing here: \[OpenAI Billing](https://platform.openai.com/account/billing/overview).  

\- For demos without billing, switch to \*\*fake mode\*\* in the script.  



\## 📌 Next Steps

\- Turn this into a \*\*mini chatbot\*\* in the terminal.  

\- Add error handling (e.g., quota exceeded, missing key).  

\- Experiment with different OpenAI models.  



---



👨‍💻 Created as a learning project to demonstrate Python + API integration skills.

