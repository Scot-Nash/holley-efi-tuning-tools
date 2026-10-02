# 🏎️ Holley EFI Python Tuning Tools

Free, lightweight Python tools designed to speed up tuning and data analysis for Holley EFI systems (Terminator X, HP, Dominator, and Sniper).

---

## 📦 Requirements & Installation

Before running the scripts, make sure you have Python installed, then open **Command Prompt** by pressing the Windows key + R.  Next, type cmd and press enter. At the flashing prompt, enter:

```cmd
pip install pandas matplotlib seaborn
```

---

Below, is a step-by-step guide on how to run the script in Python

---

### Step 1: Open Your Script File

1. Open **Command Prompt** by pressing the Windows key + R.  Next, type cmd and press enter.


2. At the flashing prompt, enter:

```cmd
notepad analyzer.py 
```
 
 ---

4. A pop-up box will appear saying *"Cannot find the analyzer.py file. Do you want to create a new file?"* Click **Yes**!


5. Place **Notepad on one half of your screen** and the **black Command Prompt window on the other half**.



---

### Step 2: Paste Your Code

1. Copy the script from the GitHub page.


2. Click inside your blank Notepad window and paste it (**Ctrl + V**).



---

### Step 3: Customize Your Settings (At the Bottom of Notepad)

Scroll down to the **very bottom** of your Notepad window until you see the section marked `# CHANGE THESE 3 LINES FOR YOUR DATA LOGS:`.

Change the text inside the quotes for these three settings:

1. **`log_folder` (Where your files are stored):**
* Open the folder containing your data logs in File Explorer.
* Click on the top address bar to highlight the path, then press **Ctrl + C** to copy.
* Paste it between the quotes after the `r`: `log_folder = r"C:\Your\Folder\Path\Here"`


2. **`datalog_prefix` (The starting name of your log files):**
* Type the beginning part of your file name before the wildcard number (e.g., `"09_12_26_1_"`).


3. **`variable` (The sensor item you want to scan):**
* Type the exact column name you want Python to analyze (e.g., `"Oil Pressure"`, `"RPM"`, or `"Wheel Slip"`).



Once all three lines are updated, press **Ctrl + S** on your keyboard to save!

---

### Step 4: Run Your Code

1. Click on the black **Command Prompt** window.


2. At the flashing prompt, enter:
```bash
python analyzer.py
```

---

3. Press **Enter** to run your program!



---

### Step 5: Your Reusable Workspace (Making Changes or Running NEW Scripts)

Think of this Notepad window as your **reusable workbench**. You will use this exact same file every time!

* **To change a variable or folder:** Edit the line at the bottom of Notepad $\rightarrow$ Press **Ctrl + S** $\rightarrow$ Click Command Prompt, press the **Up Arrow** key, and press **Enter**.
* **To run a completely NEW script from GitHub:**
1. Click inside Notepad and press **Ctrl + A** to highlight everything, then hit **Backspace** to erase it.
2. Copy the new script from GitHub (**Ctrl + C**).
3. Paste it into Notepad (**Ctrl + V**).
4. Update the 3 settings at the bottom and press **Ctrl + S** to save.
5. Click Command Prompt, press the **Up Arrow** key, and press **Enter** to run!
