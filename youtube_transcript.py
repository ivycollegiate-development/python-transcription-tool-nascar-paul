# Import the youtube transcription module
from youtube_transcript_api import YouTubeTranscriptApi

# Defines a function to get the transcript
def get_transcript(video_id):
   # Use the YouTubeTranscriptApi to get the transcript of the video
   # The transcript is returned as a list of dictionaries, where each dictionary
   # represents a piece of the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

# Adding options for alternative languages
# Defines a function to write the transcript to a file
def write_transcript_to_file(video_id, transcript):
    # Open a text file with the same name as the video_id
    # The 'w' argument means that the file will be opened for writing
    with open(f"{video_id}.transcript.txt", "w", encoding="utf-8") as file:
        # Iterate over each entry in the transcript
        for entry in transcript:
            # Write the start time, end time, and duration of the entry to the file, followed by a newline character
            # The 'start', 'start' + 'duration', and 'duration' keys of each entry contain the timing information of the transcript
            file.write(f"{entry['start']} - {entry['start'] + entry['duration']}: {entry['text']}\n")

# Set the ID of the video you want to get the transcript for
video_id = input("Enter the YouTube video ID: ")

# Get the transcript of the video

transcript = get_transcript(video_id)

# Write the transcript to a file

write_transcript_to_file(video_id, transcript)
