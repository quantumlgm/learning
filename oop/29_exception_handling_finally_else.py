# Design a `SecureDataTransmitter` class that demonstrates the exact
# execution order of nested try-except blocks combined with `else`
# and `finally` statements, specifically showing how `finally` runs
# even after an explicit `return`.

# Requirements:
# 1. Class `SecureDataTransmitter`:
#    - Initialize a protected state `_status` as "idle".
#    - Implement `process_and_send(data: dict) -> str`.
#    - Use an outer try-finally structure to guarantee state cleanup
#      and a printed log message inside `finally`.
#    - Inside the outer try, nest a try-except-else block to validate
#      the presence of the key "payload" in the incoming dictionary.
#    - Handle `KeyError` specifically. Return "Status: validation_error"
#      on failure, and "Status: success" inside the `else` block on success.
#    - Ensure the outer `finally` block resets `_status` to "idle" and
#      prints "System: Session closed." to the console.


class SecureDataTransmitter:
    def __init__(self) -> None:
        self._status = "idle"

    def process_and_send(self, data: dict) -> str:
        if not isinstance(data, dict):
            raise TypeError("Data must be a dict")
        try:
            self._status = "processing"
            try:
                key_payload = data["payload"]
                if not isinstance(key_payload, str):
                    raise TypeError("Payload must be a string")
            except KeyError:
                return "Status: validation_error"
            else:
                self._status = "sending"
                return "Status: success"
        finally:
            self._status = "idle"
            print("System: Session closed")


if __name__ == "__main__":
    transmitter = SecureDataTransmitter()
    print(transmitter._status)  # idle
    print(
        transmitter.process_and_send({"name": "Ruslan", "profession": "developer"})
    )  # Status: validation_error
    print(
        transmitter.process_and_send(
            {"name": "Ruslan", "payload": "useful information"}
        )
    )  # Status: success

    try:
        print(transmitter.process_and_send(10))
    except:
        print(
            "In case data will be a int: ValueError: Data must be a dict"
        )  # "TypeError: Data must be a dict"
