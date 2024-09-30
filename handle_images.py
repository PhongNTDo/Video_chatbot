import cv2
import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="1"

import torch
from PIL import Image
from imgbeddings import imgbeddings
ibed = imgbeddings()


# Function to extract frames from a video until reaching the desired frame count
def extract_frames(video_file):
    video_file = "video.mp4"
    cap = cv2.VideoCapture(video_file)
    
    frame_rate = 2  # Desired frame rate (1 frame every 0.5 seconds)
    frame_count = 0
    
    # Get the video file's name without extension
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    
    # Create an output folder with a name corresponding to the video
    output_directory = f"{video_name}_frames"
    os.makedirs(output_directory, exist_ok=True)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_count += 1
        
        # Only extract frames at the desired frame rate
        if frame_count % int(cap.get(5) / frame_rate) == 0:
            output_file = f"{output_directory}/frame_{frame_count}.jpg"
            cv2.imwrite(output_file, frame)
            # print(f"Frame {frame_count} has been extracted and saved as {output_file}")
    
    cap.release()
    cv2.destroyAllWindows()
    return output_directory


def extract_embedding(image_path):
    image = Image.open(image_path)
    embedding = ibed.to_embeddings(image)
    return embedding


if __name__ == "__main__":
    video_file = r"video.mp4"  # Replace with your video's name
    
    # extract_frames(video_file)

    image_path = "video_frames/frame_10010.jpg"
    # image = Image.open(image_path).load().data
    embedding = extract_embedding(image_path)
    print(embedding)