# 🏎️ Holley EFI Python Tuning Tools

Free, lightweight Python tools designed to speed up tuning and data analysis for Holley EFI systems (Terminator X, HP, Dominator, and Sniper).

---

## 📦 Requirements & Installation

Before running the scripts, make sure you have Python installed, then open your terminal and run:

```bash
pip install pandas matplotlib seaborn
```

---

Below, is a step-by-step guide on how to run the script in Python

### Step 1: Open Your Script File

1. Open **Command Prompt** (the black window).
2. Type `notepad analyzer.py` and press **Enter**.
3. A pop-up box will appear saying *"Cannot find the analyzer.py file. Do you want to create a new file?"* Click **Yes**!
4. Place **Notepad on one half of your screen** and the **black Command Prompt window on the other half**.

---

### Step 2: Paste and Save Your Code

1. Copy the script from the GitHub page (**Ctrl + C**).
2. Click inside your blank Notepad window and paste it (**Ctrl + V**).
3. Press **Ctrl + S** on your keyboard to save.

---

### Step 3: Run Your Code

1. Click on the black **Command Prompt** window.
2. Type:
```cmd
python analyzer.py

```


3. Press **Enter** to run your program!

---

### Step 4: Your Reusable Workspace (Making Changes or Running NEW Scripts)

Think of this Notepad window as your **reusable workbench**. You will use this exact same file every time!

* **To edit your code:** Tweak something in Notepad -> Press **Ctrl + S** -> Click Command Prompt, press the **Up Arrow** key, and press **Enter**.
* **To run a NEW script from GitHub:**
1. Click inside Notepad and press **Ctrl + A** to highlight everything, then hit **Backspace** to erase it.
2. Copy the new script from GitHub (**Ctrl + C**).
3. Paste it into your Notepad workbench (**Ctrl + V**).
4. Press **Ctrl + S** to save.
5. Click Command Prompt, press the **Up Arrow** key, and press **Enter** to run the new script!


### How to Read the Heatmap:
- Red Cells (+): Fuel was added (Base map was running LEAN in this cell).
- Blue Cells (-): Fuel was removed (Base map was running RICH in this cell).
- Compatible with: Standard (16x16) and Large (31x31) Holley fuel grids.
