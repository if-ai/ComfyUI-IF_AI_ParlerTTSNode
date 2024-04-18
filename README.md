# IF_ParlerTTSNode: Comfy Node for Parler TTS

This node provides access to the high-quality Parler TTS with promptable descriptions within ComfyUI. It is part of the IF_AI_tools collection.

## Installation

**Prerequisites:**

* **Python environment:** You need a Python environment with pip. You can use virtual environments like venv or conda environments.
* **ComfyUI:** Ensure you have ComfyUI installed and set up.

**Installation Steps:**

1. **Activate your Python environment.**
2. **Install Parler TTS:**
    * **Linux/macOS:**
    ```bash
    pip install git+https://github.com/huggingface/parler-tts.git 
    ```
    * **Windows (Portable Embedded Python):**
    ```bash
    H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install git+https://github.com/huggingface/parler-tts.git
    ```
3. **Install ffmpy (if necessary):**
    * If you encounter issues with ffmpy, follow these instructions:
        1. Download ffmpy from https://pypi.org/project/ffmpy/#files
        2. Extract the downloaded code.
        3. In the `setup.py` file, comment out line 4 (`#from ffmpy import __version__`). 
        4. Change the version string on line 8 to the actual version (e.g., `version="0.3.0"`).
        5. Open a terminal in the extracted ffmpy directory.
        6. Run the following command, replacing `<your python path>` with the path to your Python executable:
            ```bash
            <your python path> setup.py
            ```
4. **Install importlib_resources (Windows Portable Embedded Python only):**
    ```bash
    H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install importlib_resources
    ```

## Usage

1. Once installed, the Parler TTS node should be available within ComfyUI. 
2. You can use it to generate speech audio from text prompts, including descriptive details for controlling the speech style and characteristics. 

## Additional Notes

* Refer to the Parler TTS documentation and examples for more information on using the model effectively.
[* T](https://github.com/huggingface/parler-tts)
