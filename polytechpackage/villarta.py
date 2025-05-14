import emoji

def display_emoji_message():
    message = emoji.emojize(
        "You've reached the final stop! :rocket: :snake: :sunglasses:",
        language='alias'
    )
    print(message)
