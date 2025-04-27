n = int(input("Enter the number of sites: "))

request_set = {}
for i in range(1, n + 1):
    lst = []
    for j in range(1, n + 1):
        if i != j:
            lst.append(j)
    request_set[i] = lst

# Input of Sites Wanting to Enter CS
required_client = int(input("Enter the number of sites who wants to enter the CS: "))
required_sites = []

for i in range(required_client):
    t, id = map(int, input("Enter t and id for site: ").split())
    required_sites.append((t, id))

required_sites.sort()

# Request Phase Simulation
print(" -----------Request Phase---------------")
for i, id in required_sites:
    for j in request_set[id]:
        print(f"Request sent from {id} to {j}")

# Reply Phase + Critical Section Entry
pending_task = [id for t, id in required_sites]

for t, id in required_sites:
    for i in request_set[id]:
        if i not in pending_task:
            print(f"Reply from {i} to {id}")
        else:
            for peer_time, peer_id in required_sites:
                if peer_id == id and peer_time > t:
                    print(f"Site {i} sends reply to site {id}")

    print(f"Site {id} enters the critical section")

x = input("Enter anything to exit CS....")
print(f"Site {id} exits the Critical Section\n")
pending_task.remove(id)
