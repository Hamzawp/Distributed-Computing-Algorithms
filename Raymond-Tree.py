tokens = {1: True, 2: False, 3: False, 4: False, 5: False}
parents = {1: None, 2: 1, 3: 1, 4: 3, 5: 3}
queues = {i: [] for i in range(1, 6)}


def display_queue():
    print("Current Queue: ")
    for k, v in queues.items():
        print(f" - Node {k} : {v}")


def request_cs(node_id):
    if tokens[node_id]:
        print(f"Node {node_id} already has the token and can enter the CS.")
        display_queue()
        return

    parent = parents[node_id]
    if node_id not in queues[parent]:
        queues[parent].append(node_id)
        print(f"Node {node_id} requests token via Parent {parent}")
        display_queue()

    request_cs(parent)


def pass_token(current_holder):
    while queues[current_holder]:
        next_node = queues[current_holder].pop(0)
        tokens[current_holder] = False
        print(f"Tokens passed from Node {current_holder} -> Node {next_node} ")
        display_queue()
        current_holder = next_node

    print(f"Node {current_holder} has the token and can enter the CS")
    display_queue()


print("Node 4 wants to enter the Critical Section: ")
request_cs(4)

print("Passing token along the request path: ")
pass_token(1)
