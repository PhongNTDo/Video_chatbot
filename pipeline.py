import warnings
warnings.filterwarnings('ignore')

from get_youtube_video import get_youtube_content
from text_completion import LLM
from asr import get_transcript
from handle_images import extract_embedding, extract_frames


class Video_Chatbot():
    def __init__(self):
        self.llm = None

        self.video_file = ""
        self.script_file = ""
        self.images_folder = ""

    def init_phase(self, video_path):
        if video_path.startswith("http"): # link youtube
            video_file, script_file = get_youtube_content(video_path)
            self.video_file = video_file
            self.script_file = script_file
        else: # video local
            video_file, script_file = get_transcript(video_path)
            self.video_file = video_file
            self.script_file = script_file

        self.images_folder = extract_frames(self.video_file)
        self.llm = LLM(script_file)

    def query(self, question):
        answer = self.llm.get_answer(question)['content']
        return answer

def pipeline():
    chatbot = Video_Chatbot()
    video_link = input("Please enter the video link or path: ")
    chatbot.init_phase(video_link)
    print("Init complete! Please enter 'OK' to stop chatting!")
    while True:
        question = input("Enter the question: ")
        if question.lower().strip() == "ok":
            print("Thank you!")
            break
            
        answer = chatbot.query(question)
        print("System: ", answer)

pipeline()