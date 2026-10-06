# 🏎️️ Holley EFI Python Tuning Tools

Free, lightweight Python tools designed to speed up tuning and data analysis for Holley EFI systems (Terminator X, HP, Dominator, and Sniper).

---

## 📦 Requirements & Installation

Before running the scripts, make sure you have Python installed, then open **Command Prompt** by pressing the **Windows key + R**. Next, type `cmd` and press **Enter**. At the flashing prompt, enter:

```cmd
pip install pandas matplotlib seaborn

```

---

Below is a step-by-step guide on how to run the min./peak script in Python.

### Step 1: Open Your Script File

1. Open **Command Prompt** by pressing the **Windows key + R**. Next, type `cmd` and press **Enter**.
2. At the flashing prompt, enter:
```cmd
notepad analyzer.py

```


3. A pop-up box will appear saying *"Cannot find the analyzer.py file. Do you want to create a new file?"* Click **Yes**!
4. Place **Notepad on one half of your screen** and the **black Command Prompt window on the other half**.

---

### Step 2: Paste and Save Your Code

1. Copy the script from the GitHub page.
2. Click inside your blank Notepad window and paste it (**Ctrl + V**).
3. Save your file: Press **Ctrl + S** on your keyboard to save.



---

### Step 3: Customize Your Settings (At the Bottom of Notepad)

Scroll down to the **very bottom** of your Notepad window until you see `# CHANGE THESE 3 LINES FOR YOUR DATA LOGS:`.

Change the text inside the quotes for these three settings:

1. **`log_folder` (Where your files are stored):**
* Open the folder containing your data logs in File Explorer.
* Click the top address bar, press **Ctrl + C** to copy, and paste it inside the quotes after the `r`.




2. **`datalog_prefix` (The main file name):**
* Type the beginning part of your log file name up to the last underscore (e.g., `"09_12_26_1_"`).


3. **`variable` (The sensor item you want to scan):**
* Type the exact sensor column name you want Python to analyze (e.g., `"Oil Pressure"`, `"RPM"`, or `"Wheel Slip"`).



Once updated, press **Ctrl + S** to save!

---

### Step 4: Run Your Code

1. Click on the black **Command Prompt** window.
2. Type:
```cmd
python analyzer.py

```


3. Press **Enter** to run your program!

---

### Step 5: Your Reusable Workspace (Making Changes or Running NEW Scripts)

Think of this Notepad window as your **reusable workbench**. You will use this exact same file every time!

* **To change a variable or folder:** Edit the line at the bottom of Notepad $\rightarrow$ Press **Ctrl + S** $\rightarrow$ Click Command Prompt, press the **Up Arrow** key, and press **Enter**.
* **To run a completely NEW script from GitHub:**
1. Click inside Notepad, press **Ctrl + A** to highlight everything, and press **Backspace** to erase it.
2. Copy the new script from GitHub (**Ctrl + C**).
3. Paste it into Notepad (**Ctrl + V**).
4. Update the 3 settings at the bottom and press **Ctrl + S** to save.
5. Click Command Prompt, press the **Up Arrow** key, and press **Enter** to run!
   

### 🔄 Batch Converter: How to Use

Follow this step-by-step guide to run the automated Holley log batch converter.

---

#### Step 1: Install the Required Library
Open **Command Prompt** (or terminal) and run the following command to install the Windows automation library:

```bash
pip install pywinauto
```
Wait for the installation to say Successfully installed before continuing.

Step 2: Check Your Windows Display Scaling
Because GUI automation relies on screen coordinates to click Holley menus, Windows scaling must be set to 100%:
Right-click anywhere on your Windows desktop and select Display settings.
Scroll down to the Scale & layout section.
Make sure the scale dropdown is set to 100%. (If set higher, e.g., 125% or 150%, clicks may miss the menu buttons).

Step 3: Run the Script
Open your terminal or code editor (such as Visual Studio Code) in the folder where your script is saved.
Make sure your .dl or .dlz files are in your target folder.
Run the script:
```bash
python analyzer.py
```

💡 Smart Resuming & Safety
Safe to Stop Anytime: If you interrupt or stop the script mid-run, you don't have to start over from scratch.
Auto-Skip: When re-run, the script automatically checks for existing .csv files (> 2 MB) in the folder and skips already-completed parts, saving you time.
