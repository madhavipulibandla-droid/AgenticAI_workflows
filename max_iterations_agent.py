def run_agent(max_iters=10):
    for i in range(max_iters):
        print(f"Iteration: {i + 1}")

        # Agent work
        print("Agent is working...")

        # Example success condition
        if i == 5:
            print("Agent completed successfully")
            return "success"

    # If max iterations are exceeded
    return "failure"


# Test the agent
result = run_agent(max_iters=10)

print("Agent result:", result)