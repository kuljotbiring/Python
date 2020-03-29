# Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.


def show_messages(messages):
    for message in messages:
        print(message)


text_messages = ['hmu', 'wyd', 'tgif', 'hbu', 'ngl']
sent_messages = []
show_messages(text_messages)
print("\n")

# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.


def send_messages(messages, sent):
    while messages:
        message_delivery = messages.pop()
        print(message_delivery)

        sent.append(message_delivery)


text_messages = ['hmu', 'wyd', 'tgif', 'hbu', 'ngl']
send_messages(text_messages, sent_messages)
print("\nThe lists contain: ")
print(text_messages)
print(sent_messages)

# Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.


def archive_messages(messages, sent):
    while messages:
        message_delivery = messages.pop()
        print(message_delivery)

        sent.append(message_delivery)


text_messages = ['hmu', 'wyd', 'tgif', 'hbu', 'ngl']
sent_messages.clear()
archive_messages(text_messages[:], sent_messages)
print("\nThe lists contain: ")
print(text_messages)
print(sent_messages)
