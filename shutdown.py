import os, threading
from pydactyl import PterodactylClient

def shutdown(Client, server_id):
    print('shutdown ' + server_id)
    Client.servers.send_power_action(server_id, 'stop')
    

Client = PterodactylClient(os.environ['PTERODACTYL_API_URL'], os.environ['PTERODACTYL_CLIENT_KEY']).client
App = PterodactylClient(os.environ['PTERODACTYL_API_URL'], os.environ['PTERODACTYL_APP_KEY'])

# Get server identifiers
server_allocs = App.servers.list_servers()
servers = []
for page in server_allocs:
    for item in page.data:
        servers.append(item['attributes']['identifier'])

# Get server states
threads = []
for server_id in servers:
    server = Client.servers.get_server_utilization(server_id)
    state = server['current_state']
    if state != 'offline': # i.e. 'starting' or 'running'
        #Client.servers.settings.send_power_action(server_id)
        t = threading.Thread(target=shutdown, args=(Client, server_id))
        t.start()
        threads.append(t)

for t in threads:
    t.join()