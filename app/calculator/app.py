from __future__ import annotations
from app.calculation import CalculationFactory, CalculationHistory


def parse_number(text: str) -> float:
    try:
        return float(text.strip())
    except ValueError as e:
        raise ValueError(f"Invalid number: {text}") from e


def format_help() -> str:
    ops = ", ".join(CalculationFactory.supported_operations())
    return (
        "Commands:\n"
        "  help     -> show this help\n"
        "  history  -> show calculation history\n"
        "  exit     -> quit\n\n"
        "Operations (type one):\n"
        f"  {ops}\n"
        "You can also use symbols: +  -  *  /\n"
    )


def repl() -> None:
    history = CalculationHistory()
    print("Professional CLI Calculator")
    print("Type 'help' for commands.\n")

    while True:
        cmd = input("calc> ").strip().lower()

        if cmd in ("exit", "quit"):
            print("Bye!")
            return

        if cmd == "help":
            print(format_help())
            continue

        if cmd == "history":
            if history.is_empty():
                print("No history yet.\n")
            else:
                for i, item in enumerate(history.all(), start=1):
                    print(f"{i}. {item}")
                print()
            continue

        a_raw = input("Enter first number: ")
        b_raw = input("Enter second number: ")

        try:
            a = parse_number(a_raw)
            b = parse_number(b_raw)
            calc = CalculationFactory.create(cmd, a, b)
            history.add(calc)
            print(f"Result: {calc.result}\n")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":  # pragma: no cover
    repl()