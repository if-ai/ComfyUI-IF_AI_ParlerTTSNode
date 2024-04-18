import os
import torch
import tempfile
import datetime
import torchaudio
import textwrap
import re
import numpy as np
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import scipy.io.wavfile as wav
import librosa
from nltk.tokenize import sent_tokenize

class IFParlerTTS:
    @classmethod
    def INPUT_TYPES(cls):
        node = cls()
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": node.sample_prompt}),
                "description": ("STRING", {"multiline": True, "default": node.sample_description}),
                "file_name": ("STRING", {"default": node.file_name}),
                "cpu": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("AUDIO", "STRING")
    RETURN_NAMES = ("audios", "wav_16k_path")
    FUNCTION = "generate_audio"

    CATEGORY = "ImpactFrames💥🎞️"
    OUTPUT_NODE = True

    def __init__(self):
        self.file_name = "IF_ParlerTTS"
        self.sample_prompt = "Hey, how are you doing today?"
        self.sample_description = "A female speaker with a slightly low-pitched voice delivers her words quite expressively, in a very confined sounding environment with clear audio quality. She speaks very fast."

    def split_and_prepare_text(self, text):
        chunks = []
        sentences = sent_tokenize(text)
        chunk = ""
        for sentence in sentences:
            # replace fancy punctuation that was unseen during training
            sentence = re.sub('[()]', ",", sentence).strip()
            sentence = re.sub(",+", ",", sentence)
            sentence = re.sub('"+', "", sentence)
            sentence = re.sub("/", "", sentence)
            # merge until the result is < 20s
            if len(chunk) + len(sentence) < 300:
                chunk += " " + sentence
            else:
                chunks.append(chunk)
                chunk = sentence
        if chunk:
            chunks.append(chunk)
        return chunks

    def generate_audio(self, prompt, description, file_name, cpu):
        device = "cpu" if cpu else "cuda:0" if torch.cuda.is_available() else "cpu"
        model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler_tts_mini_v0.1").to(device)
        tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler_tts_mini_v0.1")

        comfy_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_name = f"{file_name}_{timestamp}"
        output_dir = os.path.join(comfy_dir, "output", output_name)
        os.makedirs(output_dir, exist_ok=True)
        wav_16k_path = os.path.join(output_dir, f"{output_name}.wav")
        tmp_dir = os.path.join(comfy_dir, "temp", output_name)
        os.makedirs(tmp_dir, exist_ok=True)
        wav_temp_path = os.path.join(tmp_dir, "audio.wav")

        chunks = self.split_and_prepare_text(prompt)
        audio_segments = []

        for chunk in chunks:
            input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
            prompt_input_ids = tokenizer(chunk, return_tensors="pt").input_ids.to(device)
            generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
            audio_arr = generation.cpu().numpy().squeeze()
            audio_segments.append(torch.from_numpy(audio_arr))

        # Concatenate the audio segments
        audio = torch.cat(audio_segments, dim=-1)

        # Save the audio using scipy.io.wavfile
        wav.write(wav_temp_path, model.config.sampling_rate, audio.numpy())

        # Load the audio using librosa
        audio, sr = librosa.load(wav_temp_path, sr=model.config.sampling_rate)

        # Resample the audio to 16kHz using librosa
        resampled_audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)

        # Save the resampled audio using scipy.io.wavfile
        wav.write(wav_16k_path, 16000, resampled_audio)

        return (audio, wav_16k_path)

NODE_CLASS_MAPPINGS = {"IF_ParlerTTS": IFParlerTTS}
NODE_DISPLAY_NAME_MAPPINGS = {"IF_ParlerTTS": "IF Parler TTS🎤"}