from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def process(self) -> None:  # TODO: args
        pass


class StateMachine:
    def __init__(self, state: State) -> None:
        self._state = state

    # TODO: change_state()

    def process(self) -> None:  # TODO: args
        self._state.process()  # TODO: args


# States
class StandbyState(State):
    def __init__(self) -> None:
        print("### Standby ###")

    def process(self) -> None:  # TODO: args
        match command:
            case _:
                print("### Standby ###")
        # TODO: cases


# TODO: states

if __name__ == "__main__":
    # Initialize state machine with the standby state
    state_machine = StateMachine(StandbyState())

    # Input loop
    while (command := input("Enter command: ")) != "q":
        state_machine.process(command)
