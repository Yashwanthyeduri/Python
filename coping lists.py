document_lines = ["Hello, world!", "This is a test document."]
history = [document_lines.copy()]

document_lines.append("A new line was added.")
history.append(document_lines.copy())

document_lines[0] = "Hello, everyone!"
history.append(document_lines.copy())

print("Current document:", document_lines)
print(f"\nHistory has {len(history)} saved states:")
for i, state in enumerate(history):
    print(f"State {i}: {state}")

print(f"\nOriginal state 0 is genuinely unaffected: {history[0]}")