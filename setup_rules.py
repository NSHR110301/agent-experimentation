import json
import os

RULES_PATH = "data/rules.json"


def create_rules():
    rules = {}

    print("📬 Setup your email labels")
    print("Type 'done' when finished\n")

    while True:
        label = input("Enter label name: ").strip()

        if label.lower() == "done":
            break

        examples = []
        print(f"Enter 2-3 example phrases for '{label}'")

        for i in range(3):
            example = input(f"Example {i+1}: ").strip()
            if example:
                examples.append(example)

        rules[label] = examples
        print()

    # save
    os.makedirs("data", exist_ok=True)
    with open(RULES_PATH, "w") as f:
        json.dump(rules, f, indent=2)

    print("✅ Rules saved to data/rules.json")


if __name__ == "__main__":
    create_rules()
