from abc import ABC, abstractmethod


# High-Level ##########################################
class State(ABC):
    @abstractmethod
    def process(self, state_machine: "StateMachine", command: str) -> None:
        pass


class StateMachine:
    def __init__(self, state: State) -> None:
        self._state = state

    def change_state(self, state: State) -> None:
        self._state = state

    def process(self, command: str) -> None:
        self._state.process(self, command)


# Low-Level ###########################################
# States
class StandbyState(State):
    def __init__(self) -> None:
        print("### Standby ###")

    def process(self, state_machine: StateMachine, command: str) -> None:
        match command:
            case "set":
                print("Activating ACC...")
                state_machine.change_state(ActiveState())
            case "off":
                print("Switching ACC off...")
                state_machine.change_state(OffState())
            case _:
                print("### Standby ###")


class ActiveState(State):
    def __init__(self) -> None:
        print("### Active ###")

    def process(self, state_machine: StateMachine, command: str) -> None:
        match command:
            case "brake":
                print("Driver brakes. Switching to standby...")
                state_machine.change_state(StandbyState())
            case "off":
                print("Brake first, the ACC is still controlling the vehicle.")
            case _:
                print("### Active ###")


class OffState(State):
    def __init__(self) -> None:
        print("### Off ###")

    def process(self, state_machine: StateMachine, command: str) -> None:
        match command:
            case "on":
                print("Switching ACC on...")
                state_machine.change_state(StandbyState())
            case _:
                print("### Off ###")


if __name__ == "__main__":
    state_machine = StateMachine(StandbyState())

    while (command := input("Enter command: ")) != "q":
        state_machine.process(command)
