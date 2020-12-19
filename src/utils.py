from urllib.parse import unquote
import streamlit as st


class Utils:
    def __init__(self, latin_encoder="latin-1"):
        self.latin_encoder = latin_encoder
        
    def _cleanup_latin_encoding(self, word):
        try:
            return unquote(word, errors='strict')
        except UnicodeDecodeError:
            return unquote(word, encoding=self.latin_encoder)

