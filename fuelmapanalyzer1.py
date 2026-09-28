import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

base_data = None
tuned_data = None

def parse_holley_clipboard(load_type="MAP (kPa)"):
    """Reads 31x31 or 16x16 raw grid and applies MAP or TPS axis labels."""
    df = pd.read_clipboard(sep=r'\t+', header=None, engine='python')
    df = df.apply(pd.to_numeric, errors='coerce')
    
    # 31x31 Large Table
    if df.shape == (31, 31):
        rpm_31 = [500, 783, 1067, 1350, 1633, 1917, 2200, 2483, 2767, 3050, 3333, 3617, 3900, 4183, 4467, 4750, 5033, 5317, 5600, 5883, 6167, 6450, 6733, 7017, 7300, 7583, 7867, 8150, 8433, 8717, 9000]
        df.columns = [str(r) for r in rpm_31]
        
        if "TPS" in load_type:
            tps_31 = [100, 97, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 57, 53, 50, 47, 43, 40, 37, 33, 30, 27, 23, 20, 17, 13, 10, 7, 3, 0]
            df.index = [f"{t}%" for t in tps_31]
        else: # MAP kPa (e.g. 10 to 250+ kPa)
            df.index = [f"Row {i+1}" for i in range(31)]
            
    # 16x16 Standard Table
    elif df.shape == (16, 16):
        df.columns = [str(r) for r in np.linspace(500, 7000, 16).astype(int)]
        if "TPS" in load_type:
            df.index = [f"{t}%" for t in np.linspace(100, 0, 16).astype(int)]
        else:
            df.index = [f"Row {i+1}" for i in range(16)]
            
    return df

def capture_base():
    global base_data
    try:
        base_data = parse_holley_clipboard(combo_type.get())
        lbl_base.config(text=f"✓ Base Map Loaded ({base_data.shape[0]}x{base_data.shape[1]})", fg="green")
        btn_tuned.config(state="normal")
    except Exception as e:
        messagebox.showerror("Error", f"Could not read Base Map.\n\nDetails: {e}")

def capture_tuned():
    global tuned_data
    try:
        tuned_data = parse_holley_clipboard(combo_type.get())
        lbl_tuned.config(text=f"✓ Tuned Map Loaded ({tuned_data.shape[0]}x{tuned_data.shape[1]})", fg="green")
        btn_compare.config(state="normal", bg="#2e7d32", fg="white")
    except Exception as e:
        messagebox.showerror("Error", f"Could not read Tuned Map.\n\nDetails: {e}")

def show_comparison():
    global base_data, tuned_data
    if base_data is None or tuned_data is None:
        messagebox.showwarning("Warning", "Please capture both maps first!")
        return

    if base_data.shape != tuned_data.shape:
        messagebox.showerror("Dimension Mismatch", f"Base Map is {base_data.shape} but Tuned Map is {tuned_data.shape}.")
        return

    base_vals = base_data.values.astype(float)
    tuned_vals = tuned_data.values.astype(float)

    diff_abs_vals = tuned_vals - base_vals
    safe_base = np.where(base_vals == 0, np.nan, base_vals)
    diff_pct_vals = ((tuned_vals - base_vals) / safe_base) * 100

    diff_abs = pd.DataFrame(diff_abs_vals, index=base_data.index, columns=base_data.columns)
    diff_pct = pd.DataFrame(diff_pct_vals, index=base_data.index, columns=base_data.columns)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    cmap = sns.diverging_palette(240, 10, as_cmap=True)
    cell_font = 6 if base_data.shape[0] > 16 else 8
    load_label = combo_type.get()

    # Heatmap 1: Absolute Difference
    sns.heatmap(diff_abs, annot=True, fmt=".1f", cmap=cmap, center=0, ax=ax1,
                annot_kws={"size": cell_font}, cbar_kws={'label': 'Delta (Units)'})
    ax1.set_title("Absolute Change\n(Red = Added | Blue = Removed)", fontsize=11, pad=10)
    ax1.set_xlabel("Engine RPM")
    ax1.set_ylabel(f"Engine Load ({load_label})")

    # Heatmap 2: Percentage Difference
    sns.heatmap(diff_pct.fillna(0), annot=True, fmt=".0f", cmap=cmap, center=0, ax=ax2,
                annot_kws={"size": cell_font}, cbar_kws={'label': '% Change'})
    ax2.set_title("Percentage Change (%)\n(Red = Added | Blue = Removed)", fontsize=11, pad=10)
    ax2.set_xlabel("Engine RPM")
    ax2.set_ylabel(f"Engine Load ({load_label})")

    plt.suptitle(f"Holley EFI Table Comparison ({load_label})", fontsize=14, y=0.98)
    plt.tight_layout()
    plt.show()

# --- GUI Setup ---
root = tk.Tk()
root.title("Holley EFI Map Comparison")
root.geometry("450x360")
root.attributes('-topmost', True)

title = tk.Label(root, text="Holley EFI Table Comparison Tool", font=("Arial", 13, "bold"))
title.pack(pady=10)

# Dropdown for Load Type
frame_type = tk.Frame(root)
frame_type.pack(pady=5)
tk.Label(frame_type, text="Table Load Type: ", font=("Arial", 10)).pack(side="left")
combo_type = ttk.Combobox(frame_type, values=["MAP (Speed Density / Boost)", "TPS (Alpha-N)", "Spark Timing", "Target AFR"], state="readonly", width=26)
combo_type.set("MAP (Speed Density / Boost)")
combo_type.pack(side="left")

# Step 1 Button
btn_base = tk.Button(root, text="1. Copy Base Table in Holley ➔ Click Here", font=("Arial", 10), width=38, height=2, command=capture_base)
btn_base.pack(pady=4)
lbl_base = tk.Label(root, text="Base Table: Not Loaded", fg="gray")
lbl_base.pack()

# Step 2 Button
btn_tuned = tk.Button(root, text="2. Copy Tuned Table in Holley ➔ Click Here", font=("Arial", 10), width=38, height=2, command=capture_tuned, state="disabled")
btn_tuned.pack(pady=4)
lbl_tuned = tk.Label(root, text="Tuned Table: Not Loaded", fg="gray")
lbl_tuned.pack()

# Step 3 Compare Button
btn_compare = tk.Button(root, text="3. Compare Tables", font=("Arial", 11, "bold"), width=30, height=2, command=show_comparison, state="disabled")
btn_compare.pack(pady=12)

root.mainloop()
