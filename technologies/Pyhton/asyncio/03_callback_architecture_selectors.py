# DISCLAIMER: The first few lessons of this course are strictly theoretical, focusing
# on the underlying architecture. To ensure the repository remains complete and structured,
# this file serves as a reference cheat-sheet. Deep-dive socket development is deferred to a later
# stage, as the current milestone is mastering asynchronous programming concepts rather than network plumbing.

"""
Lesson 3: Callback-Based Asynchrony using High-Level 'selectors' Module.

This program elevates the manual Event Loop concept by introducing a high-level, cross-platform
abstraction layer ('selectors') and decoupling application logic via Callback functions.

Key Features:
- Platform Agnosticism: Leverages 'selectors.DefaultSelector()' to abstract away OS-specific engines
  (automatically deploying highly optimized epoll on Linux, kqueue on macOS, or WinSock on Windows).
- Decoupled Callback Architecture: Attaches a callable function reference (the callback) directly
  to the socket object entry in the selector data registry via the 'data' parameter.
- Universal Event Loop Pattern: Eliminates hardcoded conditional checks (if/else) inside the core loop.
  The Event Loop becomes a generic runner that extracts the associated callback from 'SelectorKey' and fires it.
- Explicit Lifecycle Management: Showcases the critical rule of calling 'selector.unregister()' before
  closing a socket descriptor to prevent system memory state collision.
"""

import socket
import selectors

selector = selectors.DefaultSelector()


def accept_connection(server_sock):
    client_socket, addr = server_sock.accept()

    selector.register(client_socket, selectors.EVENT_READ, data=send_message)


def send_message(client_sock):
    request = client_sock.recv(1024)

    if request:
        client_sock.send(b"Echo from callback loop: " + request)
    else:
        selector.unregister(client_sock)
        client_sock.close()


def run_callback_loop():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()

    selector.register(server_socket, selectors.EVENT_READ, data=accept_connection)

    while True:
        events = selector.select()

        for key, mask in events:
            callback = key.data
            sock = key.fileobj

            callback(sock)


if __name__ == "__main__":
    run_callback_loop()
