import base64


def encode_music_file(file_path):
    with open(file_path, "rb") as file:
        encoded_music = base64.b64encode(file.read()).decode('utf-8')
    return encoded_music
