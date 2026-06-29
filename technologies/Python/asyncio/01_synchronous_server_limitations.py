"""
DISCLAIMER: The first few lessons of this course are strictly theoretical, focusing
on the underlying architecture. To ensure the repository remains complete and structured,
this file serves as a reference cheat-sheet. Deep-dive socket development is deferred to a later
stage, as the current milestone is mastering asynchronous programming concepts rather than network plumbing.

Lesson 1: Introduction to Synchronous Server Architecture and its Bottlenecks.

This program implements a classic, blocking TCP echo server using the native 'socket' module.
It serves as a baseline to demonstrate the fundamental limitations of synchronous
I/O operations in network applications.

Key Features:
- Blocking Execution: Illustrates how operations like accept() and recv() halt the entire
  program execution thread while waiting for OS network buffers to fill.
- Single-Client Constraint: Demonstrates why a synchronous architecture cannot handle
  a second concurrent client connection if the main thread is trapped inside an active loop with the first.
- Resource Underutilization: Visualizes the architectural gap where the CPU idles 100% of the
  waiting time instead of switching to other executable tasks.
"""

import socket


def run_synchronous_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()
    print("Server is listening on port 5000 (Synchronous mode)...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection accepted from {addr}")

        while True:
            request = client_socket.recv(1024)

            if not request:
                break

            client_socket.send(b"Echo: " + request)

        client_socket.close()
        print(f"Connection with {addr} closed. Returning to listen.")


if __name__ == "__main__":
    run_synchronous_server()
