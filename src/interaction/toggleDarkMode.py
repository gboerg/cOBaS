import customtkinter as ctk

# You might want to define the initial mode
# ctk.set_appearance_mode("Dark")

def toggleDarkMode():
    # Get the current appearance mode
    current_mode = ctk.get_appearance_mode()

    # Check the current mode and switch to the other
    if current_mode == "Light":
        ctk.set_appearance_mode("Dark")
        print("Switched to Dark Mode")
    elif current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        print("Switched to Light Mode")
    else:
        # Handle "System" mode if necessary
        ctk.set_appearance_mode("Dark")
        print("Switched from System to Dark Mode")