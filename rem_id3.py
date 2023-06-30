from mutagen import File
import os
def remove_id3_tag(mp3_file_path):
    try:
        audio = File(mp3_file_path, easy=True)
        audio.delete()
        audio.save()
        print("ID3 tag removed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


for file in os.listdir():
    if file.endswith(".mp3"):
        remove_id3_tag(file)
        print('Removed ID3 tag from ' + file)