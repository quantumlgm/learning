# Design a class named `DataConverter` that utilizes both `@classmethod` and `@staticmethod`
# to process text data and provide alternative constructors.

# Requirements:
# 1. Class Attributes:
#    - `supported_versions` (list): A list of allowed data format versions, e.g., ["v1", "v2", "v3"].

# 2. Instance Initialization (`__init__`):
#    - Accepts two mandatory parameters: `raw_data` (str) and `version` (str).

# 3. Alternative Constructor (`@classmethod`):
#    - Name: `from_list(cls, data_list: list) -> DataConverter`
#    - It must take a list of strings, join them into a single comma-separated string, and return a NEW instance of the class.
#    - The default version for this new instance must be dynamically fetched from the first element of the class's `supported_versions`.

# 4. Utility Method (`@staticmethod`):
#    - Name: `clean_string(text: str) -> str`
#    - An isolated helper function that strips leading/trailing whitespaces and removes specific 
#      special characters (e.g., "#", "$", "@") from the input string, returning the cleaned text.