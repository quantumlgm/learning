"""
DISCLAIMER: The file is strictly theoretical, focusing
on the underlying architecture. To ensure the repository remains complete and structured,
this file serves as a reference cheat-sheet. Deep-dive socket development is deferred to a later
stage, as the current milestone is mastering asynchronous programming concepts rather than network plumbing.

Lesson 5: Asynchrony via Generators and Selector-Driven Event Loop.

This program bridges high-level OS event monitoring ('selectors') with Python's native
generator suspension mechanism ('yield') to build an efficient, non-blocking network server.

Key Features:
- Socket-Yielding Generators: Network functions are refactored into generators that yield
  their socket descriptors and intent ('read' or 'write') back to the dispatcher when blocked.
- Inverted Control Flow: Instead of callbacks executing the logic, the Event Loop registers
  the generator object itself into the selector mapping using the 'data' parameter.
- Efficient Execution Resumption: When the selector signals readiness, the event loop extracts
  the paused generator from 'SelectorKey.data' and resumes it via the 'next()' protocol.
- Resource-Friendly Polling: Combines cooperative task yielding with OS-level execution sleep,
  ensuring 0% CPU utilization while waiting for network input/output events.
"""

import socket
import selectors

selector = selectors.DefaultSelector()
tasks = []

to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()

    while True:
        yield (server_socket, "read")
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield (client_socket, "read")
        request = client_socket.recv(1024)

        if not request:
            break

        yield (client_socket, "write")
        client_socket.send(b"Echo: " + request)

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            events = selector.select()
            for key, mask in events:
                task = key.data
                selector.unregister(key.fileobj)

                if key.fileobj in to_read:
                    del to_read[key.fileobj]
                else:
                    del to_write[key.fileobj]

                tasks.append(task)

        try:
            task = tasks.pop(0)
            sock, action = next(task)

            if action == "read":
                to_read[sock] = task
                selector.register(sock, selectors.EVENT_READ, data=task)
            elif action == "write":
                to_write[sock] = task
                selector.register(sock, selectors.EVENT_WRITE, data=task)

        except StopIteration:
            pass


if __name__ == "__main__":
    tasks.append(server())
    event_loop()
