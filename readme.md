
## 🌍 Google Translate Selenium Wrapper

  

This repository contains a simple Python wrapper (`app.py`) that utilizes **Selenium** and **Chrome (Headless)** to perform translations via the Google Translate web interface.

  

This method is useful when direct API access is unavailable or when simulating browser behavior is necessary.

  

---

  

## 🛠️ Prerequisites

  

To run this application, you will need Python and the necessary dependencies installed.

  

### 1. Google Chrome/Chromium Browser

  

Since Selenium requires a real browser to operate, you must have **Google Chrome** or **Chromium** installed on the machine where the script will be executed.

  

### 2. Python Dependencies

  

The script uses `selenium` and `webdriver-manager`. It is highly recommended to use a virtual environment:

  

```bash

# Create and activate the virtual environment

python3  -m  venv  venv

source  venv/bin/activate

  

# Install required libraries

pip  install  selenium  webdriver-manager

  

```

  

>  **Note:** The `webdriver-manager` library will automatically manage and download the correct `ChromeDriver` upon the first execution.

  

---

  

## 🚀 How to Import and Use

  

The main functionality is provided by the `get_translation_from_google_translate` function in the `app.py` file.

  

### 1. Importing the Function

  

You can simply import the function directly into your project:

  

```python

from app import get_translation_from_google_translate

  

```

  

**NOTE**: Assuming that the `app.py` file is in the same folder as your project and that you have not changed its name.

#### 1.1 EASY WAY
 `    You can also just copy and paste the function code along with its libraries; it will work the same way :)`

  

### 2. Basic Usage

  

The function accepts three arguments, the last two being optional:

  

```python

get_translation_from_google_translate(text_to_translate, source_lang="en", dest_lang="ru")

  

```

  

| Parameter | Type | Default | Description |

| --- | --- | --- | --- |

| `text_to_translate` | `str` | N/A | The input text to be translated. |

| `source_lang` | `str` | `"en"` | The two-letter code for the source language. |

| `dest_lang` | `str` | `"ru"` | The two-letter code for the destination language. |

  

### 3. Common Language Codes (Examples)

  

| Language | Code |

| --- | --- |

| **Portuguese** | `pt` |

| **English** | `en` |

| **Spanish** | `es` |

| **Russian** | `ru` |

| **French** | `fr` |

| **German** | `de` |

| **Japanese** | `ja` |

  

### 4. Execution Examples

  

```python

from app import get_translation_from_google_translate

  

# Example 1: English (en) to Russian (ru)

result_ru = get_translation_from_google_translate(

"Hello, this is a test from my Python script.",

source_lang="en",

dest_lang="ru"

)

print(f"Translation to Russian: {result_ru}")

# Output: Translation to Russian: Здравствуйте, это тест из моего скрипта Python.

  

# Example 2: Portuguese (pt) to Spanish (es)

result_es = get_translation_from_google_translate(

"Onde está o erro na infraestrutura?",

source_lang="pt",

dest_lang="es"

)

print(f"Translation to Spanish: {result_es}")

# Output: Translation to Spanish: ¿Dónde está el error en la infraestructura?

  

```

  

---