from Perfil import Profile
from datetime import datetime


class Messages:
    def user_chat(recipentuser, senderuser, message):
        time = datetime.now().strftime("%H:%M - %d/%m/%Y")

        new_message_recipient = {
            "recipient": recipentuser["username"],
            "sender": senderuser["username"],
            "text": message,
            "vew": 1,
            "time": time
        }

        new_message_sender = {
            "recipient": recipentuser["username"],
            "sender": senderuser["username"],
            "text": message,
            "vew": 0,
            "time": time
        }

        recipentuser["message"].append(new_message_recipient)
        senderuser["message"].append(new_message_sender)

    def community_chat(senderuser, community, message):
        time = datetime.now().strftime("%H:%M - %d/%m/%Y")

        new_message = {
            "sender": senderuser["username"],
            "text": message,
            "time": time
        }

        community["message"].append(new_message)
        
        



profile = Profile()
#carregando os dados de usuario
profile.get_data()

user1 = profile.get_user("mat")
user2 = profile.get_user("leonardo2004")
community = profile.get_community("Subaqua")

Messages.user_chat(user1, user2, "olá leonardo!!")
Messages.user_chat(user2, user1, "olá matheus!!")
Messages.community_chat(user1, community, "Olá pessoal")

for messages in user1["message"]:
    print(messages["text"])
    print(messages["time"])
    print()
print()
print(community["message"])
#print(user2["message"][0]["text"])

