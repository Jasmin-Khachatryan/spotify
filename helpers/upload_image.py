def upload_music_image(instance, filename):
    return f"{instance.name}/{filename}"


def upload_music_cover_image(instance, filename):
    return f"{instance.name}/{filename}"


def upload_artist_image(instance, filename):
    return f"{instance.pseudonym}/{filename}"


def upload_artist_cover_image(instance, filename):
    return f"{instance.pseudonym}/{filename}"


def upload_album_image(instance, filename):
    return f"{instance.name}/{filename}"


def upload_playlist_image(instance, filename):
    return f"{instance.name}/{filename}"
