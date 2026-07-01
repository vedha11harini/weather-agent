conversation = []

def add(role, message):
    conversation.append(
        {
            "role": role,
            "message": message
        }
    )

def get():
    return conversation