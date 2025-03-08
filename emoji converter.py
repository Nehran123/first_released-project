def emoji_converter(message):
    words= message.split(' ')
    emoji={
        ":)": "😊",  # Smiley face
        ":(": "😢",  # Sad face
        ":D": "😄",  # Big smile
        ":P": "😛",  # Tongue out
        ";)": "😉",  # Wink
        "<3": "❤️",  # Heart
        ":O": "😮",  # Surprised
        ":/": "😕",  # Unsure
        ":|": "😐",  # Neutral
        ">:(": "😠",  # Angry
        "^_^": "😁",  # Happy face
        " :$": "🤑",
        " 8)": "😎",
        ":*": "😘",
        ":$": "🤑",
        "8)": "😎"
    }
    output=""
    for word in words:
        output+=emoji.get(word, word)+ " "
    return output

print(emoji_converter(input("Express how u feel= ")))
