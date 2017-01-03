import re
import string


def clean_string(text):
    """Cleans string."""
    text = re.sub(r' +', ' ', text)  # remove extra spaces
    text = re.sub(r'[^A-Za-z0-9 \'.\",]', '', text)
    text = text.strip()
    return text
