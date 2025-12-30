# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import base64
import os

class Base64Tool:
    @staticmethod
    def encode_string(text):
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')

    @staticmethod
    def decode_string(b64_str):
        try:
            return base64.b64decode(b64_str).decode('utf-8')
        except Exception:
            # Handle case where it might not be valid UTF-8, return bytes string representation
            try:
                data = base64.b64decode(b64_str)
                return str(data)
            except Exception as e:
                return f"Error: {e}"

    @staticmethod
    def encode_file(filepath):
        try:
            with open(filepath, "rb") as f:
                return base64.b64encode(f.read()).decode('utf-8')
        except Exception as e:
            return f"Error reading file for encoding: {e}"

    @staticmethod
    def decode_file(b64_str, output_path):
        try:
            data = base64.b64decode(b64_str)
            with open(output_path, "wb") as f:
                f.write(data)
            return True, "Success"
        except Exception as e:
            return False, f"Error writing decoded file: {e}"

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
