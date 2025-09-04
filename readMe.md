💻 OBS WebSocket Manager
🚀 Tired of juggling OBS and your Elgato Stream Deck?
The OBS WebSocket Manager is the perfect solution for streamers and content creators with a dual-PC setup. It simplifies the connection and control of OBS from your Elgato device. With this tool, you can manage OBS WebSocket 5.0 commands directly from your Elgato, streamlining your workflow and making your streams smoother than ever.

🚧 Project Status: Early Development
Please note that this project is currently in its very early stages. Many features are a subject to change, and the current functionality is limited. We're actively working on improving the tool and adding more capabilities.

Your feedback and contributions are highly valued as we build this together!

✨ Features
Seamless Integration: Control OBS WebSocket from your Elgato Stream Deck.

Intuitive UI: A clean and straightforward interface makes setup a breeze.

Code Generation: Generate a custom Python script based on your selections.

Dual-PC Friendly: Designed to work perfectly in a dual-PC streaming environment.

🛠️ How It Works
The OBS WebSocket Manager acts as the bridge between your Elgato Stream Deck and OBS. It leverages the OBS WebSocket 5.0 protocol to send commands over your local network.

Select Your Actions: Use the manager's interface to choose the specific OBS actions you want to control (e.g., scene changes, source visibility, etc.).

Generate Your Script: The manager generates a custom Python script tailored to your selections.

Run the Script: Run the generated script on the same network as your OBS machine. This script listens for commands from your Elgato device and sends the corresponding WebSocket commands to OBS.

Control Your Stream: Now you can trigger these actions directly from your Elgato, giving you instant control over your stream.

📥 Installation
Download the OBS WebSocket Manager: [Link to download page/repository]

Ensure OBS WebSocket 5.0 is installed: You'll need the OBS WebSocket 5.0 plugin for OBS. You can download it from the official GitHub page. [Link to OBS WebSocket 5.0]

Set up OBS: Configure your OBS WebSocket settings (e.g., enable WebSocket server and set a password).

Run the Manager: Launch the OBS WebSocket Manager and follow the on-screen instructions to set up your commands and generate your Python script.

🕹️ Integrating with the Stream Deck
Once you have generated your Python script, you need to tell your Elgato Stream Deck to run it. Here’s how:

Open the Stream Deck App: Launch the Stream Deck software on your computer.

Add a New Action: From the actions panel on the right, drag a "System" > "Open" action onto a key on your Stream Deck.

Configure the Action:

In the "App / File" field, navigate to and select the Python script you generated with the OBS WebSocket Manager.

(Optional) You can give your key a custom title and icon to make it easy to identify.

Repeat for Each Action: Repeat this process for every button you want to create on your Stream Deck. Each button will link to a specific command defined in your generated Python script.

🤝 Contributing
We welcome contributions! Whether it's a bug report, a feature request, or a pull request, your help is appreciated. Please see our CONTRIBUTING.md for more details.

📜 License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Need help? 🤔
If you have any questions or run into issues, feel free to open an issue on GitHub. We're here to help you get the most out of your streaming setup!

Happy streaming! 🎮




NOTE: Will rewrite later :> I used GEMENI to create a cool readme