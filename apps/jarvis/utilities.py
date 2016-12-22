import re
import string


def clean_string(text):
    """Cleans string."""
    text = re.sub(r' +', ' ', text)  # remove extra spaces
    return text
