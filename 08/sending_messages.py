msgs1 = ['Hello, Python!', 'Hello, C++!', 'Hello, Emacs!']
msgs2 = []

def send_messages(old_messages, new_messages):
    while old_messages:
        message = old_messages.pop()
        print(message)
        new_messages.append(message)

send_messages(msgs1, msgs2)
print(msgs1)
print(msgs2)
