import time

# Simulated analysis function
def analyze_eye_image(image_path: str):
    print("\n[System] Analyzing eye image...")
    time.sleep(2)  # simulate processing delay
    return {"status": "success", "message": f"Analysis complete for {image_path}"}

# Splash Screen
def splash_screen():
    print("\n=== OculaGuard ===")
    print("Neural Body Analysis")
    time.sleep(3)  # wait 3 seconds
    return "auth"

# Auth Screen
def auth_screen():
    print("\n=== Login ===")
    phone = input("Enter phone number: ")
    user = {"phoneNumber": phone}
    print(f"Welcome back, {user['phoneNumber']}!")
    return "dashboard", user

# Dashboard
def dashboard_screen(user):
    print("\n=== Dashboard ===")
    print(f"Hello, {user['phoneNumber']}")
    print("1. Start Neural Health Analysis")
    print("2. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        return "scanner"
    else:
        return "exit"

# Scanner
def scanner_screen():
    print("\n=== Scanner ===")
    image_path = input("Enter path to eye image file: ")
    return "loading", image_path

# Loading Screen
def loading_screen(image_path):
    print("\n=== Loading Analysis ===")
    print("Mapping iris structures to internal organ health...")
    result = analyze_eye_image(image_path)
    return "results", result

# Results Screen
def results_screen(result):
    print("\n=== Results ===")
    print(result["message"])
    print("1. Back to Dashboard")
    print("2. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        return "dashboard"
    else:
        return "exit"

# Main App Flow
def main():
    view = "splash"
    user = None
    image_path = None
    result = None

    while view != "exit":
        if view == "splash":
            view = splash_screen()
        elif view == "auth":
            view, user = auth_screen()
        elif view == "dashboard":
            view = dashboard_screen(user)
        elif view == "scanner":
            view, image_path = scanner_screen()
        elif view == "loading":
            view, result = loading_screen(image_path)
        elif view == "results":
            view = results_screen(result)

    print("\nGoodbye!")

if __name__ == "__main__":
    main()

