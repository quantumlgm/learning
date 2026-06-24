# DISCLAIMER: The first few lessons of this course are strictly theoretical, focusing
# on the underlying architecture. To ensure the repository remains complete and structured,
# this file serves as a reference cheat-sheet. Deep-dive socket development is deferred to a later
# stage, as the current milestone is mastering asynchronous programming concepts rather than network plumbing.

"""
Lesson 2: Asynchrony via Manual Event Loop with Low-Level 'select'.

This program demonstrates the transition from a synchronous model to cooperative multi-tasking
on a single execution thread, using the native OS 'select' system call.

Key Features:
- File Descriptors Monitoring: Showcases how 'select.select()' takes a dynamic list of Python socket
  objects, extracts their underlying integer system IDs (.fileno()), and delegates tracking to the OS kernel.
- Non-blocking I/O Orchestration: Forces the execution flow to pause only at one single point,
  waking up instantly as soon as any monitored socket becomes readable.
- Naive Event Loop Routing: Implements a primitive 'while True' dispatcher that manually inspects
  the active sockets list using conditional logic (if/else) to delegate either accepting connections or reading data.
"""

import socket
import select


def run_select_event_loop():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()

    to_monitor_list = [server_socket]

    while True:
        ready_to_read, _, _ = select.select(to_monitor_list, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                client_socket, addr = server_socket.accept()
                to_monitor_list.append(client_socket)
            else:
                data = sock.recv(1024)
                if data:
                    sock.send(b"Echo: " + data)
                else:
                    to_monitor_list.remove(sock)
                    sock.close()


if __name__ == "__main__":
    run_select_event_loop()
