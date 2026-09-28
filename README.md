# 🏎️ Holley EFI Python Tuning Tools

Free, lightweight Python tools designed to speed up tuning and data analysis for Holley EFI systems (Terminator X, HP, Dominator, and Sniper).

---

## 📦 Requirements & Installation

Before running the scripts, make sure you have Python installed, then open your terminal and run:

```bash
pip install pandas matplotlib seaborn
```

---

## 📊 Fuel Map Analyzer (fuelmapanalyzer1.py)

Compare any starting Base Map against a Dyno or Closed-Loop Learned tune directly from your Windows clipboard without saving any files. Generates side-by-side color-coded heatmaps showing absolute change (lb/hr) and percentage change (%).

### How to Use:
1. Run fuelmapanalyzer1.py in VS Code.
2. In Holley EFI, highlight your Base Map and copy it (Right-Click -> Copy).
3. In the tool window, click "1. Copy Base in Holley -> Click Here".
4. In Holley EFI, highlight your Tuned Map and copy it (Right-Click -> Copy).
5. In the tool window, click "2. Copy Tuned in Holley -> Click Here".
6. Click "3. Compare Fuel Maps" to open your visual difference heatmaps!

### How to Read the Heatmap:
- Red Cells (+): Fuel was added (Base map was running LEAN in this cell).
- Blue Cells (-): Fuel was removed (Base map was running RICH in this cell).
- Compatible with: Standard (16x16) and Large (31x31) Holley fuel grids.
