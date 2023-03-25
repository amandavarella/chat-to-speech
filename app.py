import openai
import speech_recognition as sr
import pyttsx3
import pyaudio
import os


# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")


# Initialize the text to speech engine 
engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source) 
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping unknown error")


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        # Wait for user to say "Computer"
        print("Say 'assistant' to start recording your question")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "assistant":
                    # Record audio
                    filename = "input.wav"
                    print("Say your question")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())


                    # Transcribe audio to text 
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")


                        # Generate the response
                        response = generate_response(text)
                        print(f"Chat GPT-3 says: {response}")


                        # Speak the response using text-to-speech
                        speak_text(response)
            except Exception as e:
                print("An error occurred: {}".format(e))


if __name__ == "__main__":
    main()