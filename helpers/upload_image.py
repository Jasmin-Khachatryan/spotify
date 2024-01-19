def upload_music_image(instance, filename):
    return f"{instance.title}/{filename}"


def upload_artist_image(instance, filename):
    return f"{instance.first_name}_{instance.last_name}/{filename}"
