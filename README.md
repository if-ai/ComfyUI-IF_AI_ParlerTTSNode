# IF_ParlerTTSNode
Comfy node for Parler TTS is a high quality TTS with promptable descriptions Part of IF_AI_tools

activate the venv and pip install git+https://github.com/huggingface/parler-tts.git
or windows portable embedded python
H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install git+https://github.com/huggingface/parler-tts.git

IF ffmpy fails follow @dminGod instructions 

Download the file from : https://pypi.org/project/ffmpy/#files
Extract the code
Change the code in the setup.py to comment out the import of the ffmpy module (line 4, #from ffmpy import __version__
Change the version to the actual version using string (line 8) version="0.3.0",
cd <path where you downloaded the ffmpy code>
Use the python environment / binary where you want to install it and run setup.py:

<your python path> setup.py
This should install the ffmpy

H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install importlib_resources
