def emoji_converter(message):
    words = message.split("")
    emojis = {
        ":)" : "1",
        ":(" : "2"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ""
    return output

message = input(">")
#result=emoji_converter(message)
print(emoji_converter(message))







