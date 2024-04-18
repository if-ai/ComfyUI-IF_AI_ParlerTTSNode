import os
import importlib.util
import glob
import shutil

from .IFParlerTTSNode import IFParlerTTS  

NODE_CLASS_MAPPINGS = {
    "IF_ParlerTTS": IFParlerTTS
}

NODE_DISPLAY_NAME_MAPPINGS = {

    "IF_ParlerTTS": "IF Parler TTS🎤"
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
