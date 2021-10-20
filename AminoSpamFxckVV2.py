import AminoLab
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_GREEN_SEA + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("Aminospamfxckv2", font="eftitalic"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
message = input("Message >> ")
message_type = input("Message Type >> ")
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndc_Id = clients.ndcId[int(input("Select the community >> ")) - 1]
chats = client.my_chat_threads(ndc_Id=ndc_Id, size=100)
for z, title in enumerate(chats.title, 1):
    print(f"{z}.{title}")
thread_Id = chats.thread_Id[int(input("Select The Chat >> ")) - 1]

while True:
    print("Spamming...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
        _ = [
            executor.submit(
                client.send_message,
                ndc_Id,
                thread_Id,
                message,
                message_type) for _ in range(100000)]
