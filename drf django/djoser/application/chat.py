import subprocess

def run_model(prompt):
    process = subprocess.Popen(
        ["docker", "model", "run", "ai/gemma3:270M-F16"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    out, err = process.communicate(prompt)
    return out.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() == "q":
            print("Exiting chat...")
            break

        response = run_model(user_input)
        print("Model:", response)
