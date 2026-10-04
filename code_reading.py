def agent_loop():
    state = 0

    for step in range(1, 3):
        print(f"\nStep {step}")

        # Observe
        observation = state
        print("Observe:", observation)

        # Decide
        if observation < 1:
            action = "Move Forward"
        else:
            action = "Stop"

        print("Decide:", action)

        # Act
        if action == "Move Forward":
            state += 1
            print("Act: Moving forward")
        else:
            print("Act: Stopping")


agent_loop()
