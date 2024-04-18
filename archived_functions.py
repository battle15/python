def show_messages(texts, sent):

    while texts:
        removed_text = texts.pop()
        sent.append(removed_text)

        #print(text)


text_messages = ['hey', 'whats up?', 'how are you?']
sent_messages = []

show_messages(text_messages[:], sent_messages)

print(text_messages)
print(sent_messages)