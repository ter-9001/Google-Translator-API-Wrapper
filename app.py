# Necessary Libraries for Selenium and Google Translate interaction
import time
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_translation_from_google_translate(text_to_translate, source_lang="en", dest_lang="ru"):
    """
    Performs a request to Google Translate using Selenium in headless mode
    and returns the translated text.

    Args:
        text_to_translate (str): The text string to be translated.
        source_lang (str): The source language code (e.g., 'en', 'pt'). Default is 'en'.
        dest_lang (str): The destination language code (e.g., 'ru', 'es'). Default is 'ru'.

    Returns:
        str or None: The translated text string or None if translation fails.
    """
    # The URL must be encoded for the text to be translated
    encoded_text = quote(text_to_translate)
    url = f'https://translate.google.com/?sl={source_lang}&tl={dest_lang}&text={encoded_text}&op=translate'

    # Selenium configurations
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-blink-features=AutomationControlled')
    # Set headless mode to 'new' for better compatibility
    options.add_argument('--headless=new') 
    # Use a common User-Agent to mimic a regular browser
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"')

    # Attempt to initialize ChromeDriver
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"ERROR starting ChromeDriver. Ensure it is installed and 'webdriver-manager' can access it. Details: {e}")
        return None

    print(f"   Starting Chrome (Headless) to translate to {dest_lang}...")

    try:
        driver.get(url)

        # Wait for the translation element. The selector might change!
        # We use a generic CSS selector that usually works for the destination translation box.
        try:
            wait = WebDriverWait(driver, 15)
            # Try the selector with the lang attribute (more specific)
            # This selector looks for the span element containing the translated text, identified by its language.
            translated_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"span[lang='{dest_lang}']")))
            translated_text = translated_element.text

            # Safety check (the translation might be in another span or empty)
            if not translated_text:
                raise Exception("Empty translated text with specific selector.")
        except Exception:
            # Fallback to a more robust selector, which is often the div/span that holds the result
            # Google Translate often uses a well-defined structure for the first result
            # The data-result-index='0' attribute usually points to the main result box.
            translated_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-result-index='0']"))).text

        # Simple cleanup of the raw text
        translated_text_raw = translated_text.strip()

        return translated_text_raw

    except Exception as e:
        print(f"   Translation failed for {dest_lang}. Error: {e}")
        return None

    finally:
        # Close the browser
        driver.quit()

# --- Example Usage (For demonstration) ---
# Test 1: Simple text translation (English to Russian)
#result_ru = get_translation_from_google_translate("Hello, world of automation!", source_lang="en", dest_lang="ru")
#print(result_ru)  #printing result
# Test 2: Portuguese to Spanish
#result_es = get_translation_from_google_translate("Esta é uma mensagem de teste.", source_lang="pt", dest_lang="es")
#print(result_es) #printing result
