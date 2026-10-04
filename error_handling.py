def handle_action(action):
    valid_actions = ["cool", "heat", "idle"]

    if action in valid_actions:
        return {"status": "success", "action": action}
    else:
        return {
            "status": "error",
            "error": "Invalid action"
        }


# Test cases
print(handle_action("cool"))
print(handle_action("heat"))
print(handle_action("jump"))