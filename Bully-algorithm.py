num = int(input("Enter the number of processes: "))
processes = [True for _ in range(num + 1)]

crashed = int(input("Enter crashed process ID: "))
processes[crashed] = False

initiator = int(input("Enter the initiator id: "))
print(f"\nProcess {crashed} has crashed")
print(f"\n{initiator} initiates the election")


def send_election_message(from_id):
    print(f"\nElection message sent from {from_id} to higher process.")
    received_okay = False
    for i in range(from_id + 1, num):
        if processes[i]:
            print(f"\nOkay message from {i} to {from_id}")
            received_okay = True
            send_election_message(i)
            break
    if not received_okay:
        declare_coordinator(from_id)


def declare_coordinator(coordinator_id):
    print(f"\nFinal coordinator is {coordinator_id}")
    for i in range(num):
        if i != coordinator_id and processes[i]:
            print(f"Message to {i+1}: Coordinator is {coordinator_id}")


send_election_message(initiator)
