# 🏎️ Holley EFI Python Tuning Tools

Free, lightweight Python tools designed to speed up tuning and data analysis for Holley EFI systems (Terminator X, HP, Dominator, and Sniper).

---

## 📦 Requirements & Installation

Before running the scripts, make sure you have Python installed, then open **Command Prompt** by pressing the Windows key + R.  Next, type cmd and press enter. At the flashing prompt, enter:

```cmd
pip install pandas matplotlib seaborn
```

---


```markdown

---

Below is a step-by-step guide on how to run the script in Python.

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

1. Copy the script from the GitHub page (**Ctrl + C**).
2. Click inside your blank Notepad window and paste it (**Ctrl + V**).
3. Save your file:
* Press **Ctrl + S** on your keyboard to save.
* ⚠️ **CRITICAL TIP:** If you use **File → Save As**, always change **Save as type** at the bottom to **`All Files (*.*)`**! If left as `Text Documents (*.txt)`, Windows will name your file `analyzer.py.txt` and Python will not be able to find it.



---

### Step 3: Customize Your Settings (At the Bottom of Notepad)

Scroll down to the **very bottom** of your Notepad window until you see `# CHANGE THESE 3 LINES FOR YOUR DATA LOGS:`.

Change the text inside the quotes for these three settings:

1. **`log_folder` (Where your files are stored):**
* Open the folder containing your data logs in File Explorer.
* Click the top address bar, press **Ctrl + C** to copy, and paste it inside the quotes after the `r`.
* ⚠️ **IMPORTANT:**
* Make sure there is **only ONE quote** on each side: `log_folder = r"C:\Your\Path"`
* **Do NOT put a backslash at the very end of your folder path!** (Use `r"C:\Data Logs"`, NOT `r"C:\Data Logs\"`).




2. **`datalog_prefix` (The main file name):**
* Type the beginning part of your log file name up to the last underscore (e.g., `"09_12_26_1_"`).
* *Note: Do not type part numbers or `.csv`! The script automatically searches for every split part (`_1.csv`, `_2.csv`, `_3.csv`) for you in the background.*


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



```

```
