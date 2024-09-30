import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="1"

# import torch
# from transformers import pipeline
import tqdm
import subprocess
import whisper
import datetime

def get_transcript(video):
    audio_path = "audio.wav"
    
    command = f"ffmpeg -i {video} -ab 160k -ac 1 -ar 16000 -vn {audio_path}"
    subprocess.call(command, shell=True)
    model = whisper.load_model("medium")

    index = 0
    transcript =  []
    audio = whisper.load_audio(audio_path)
    chunk = 30 # second

    while tqdm.tqdm(index < len(audio)):
        block = audio[index: index + (chunk * 16000)]
        if block.shape[0] < chunk * 16000:
            break
        mel = whisper.log_mel_spectrogram(block).to(model.device)
    
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)
    
        # print(result.text)
    
        start = chunk * index
        end = chunk * (index + 1)
    
        transcript.append(f"{datetime.timedelta(seconds=start)} -> {datetime.timedelta(seconds=end)}: {result.text}")
        
        index += int(chunk * 16000)

    transcript_path = "captions_handled.txt"
    with open(transcript_path, "w") as f:
        f.write("\n".join(transcript))
    print(f"Transcript done! saved at {transcript_path}.")
    return video, transcript_path