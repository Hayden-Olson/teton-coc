# CSE 270 – Software Testing

## Switching to the Correct Branch for Each Week

Welcome to **CSE 270 – Software Testing** 👋

This repository contains **multiple versions of the software**, organized by **branch**, to support weekly testing activities.
**Each week, you must switch to the correct branch** in order to see and test the appropriate version of the software.

If you stay on the wrong branch, you will be testing the wrong code.

---

## 📌 Branch Structure

Each week’s version of the software is stored in a **remote branch** with the following names:

* `1.2`
* `1.3`
* `1.4`
* `1.5`
* `1.6`

Your instructor will tell you **which branch to use for each week**.
Always make sure you are on the correct branch before starting your testing work.

---

## 🔁 How to Switch Branches in VS Code

Follow these steps **every time you start a new week**.

---

### Step 1: Open the Repository in VS Code

* Open VS Code
* Open the folder containing this repository

---

### Step 2: Open the Source Control Panel

* Click the **Source Control** icon on the left sidebar
  *(it looks like a branching graph)*
  **OR**
* Press:

  * **Windows/Linux:** `Ctrl + Shift + G`
  * **macOS:** `Cmd + Shift + G`

---

### Step 3: Fetch the Latest Branches (Recommended)

Before switching branches, make sure VS Code knows about all remote branches:

* Click the **⋯ (three dots)** in the Source Control panel
* Select **Fetch**

This ensures branches like `1.2`, `1.3`, etc. are available.

---

### Step 4: Switch to the Correct Branch

There are two easy ways to switch branches.

---

#### ✅ Option A: Using the Status Bar (Easiest)

1. Look at the **bottom-left corner** of VS Code
   You will see the current branch name (e.g., `main`)
2. Click the branch name
3. A list of branches will appear
4. Select the correct branch for the week (e.g., `1.4`)

VS Code will automatically switch you to that branch.

---

#### ✅ Option B: Using the Command Palette

1. Open the Command Palette:

   * **Windows/Linux:** `Ctrl + Shift + P`
   * **macOS:** `Cmd + Shift + P`
2. Type:

   ```
   Git: Checkout to...
   ```
3. Press **Enter**
4. Select the correct branch (e.g., `1.5`)

---

### Step 5: Verify You Are on the Correct Branch

* Check the **bottom-left corner** of VS Code
* Confirm it shows the correct branch name (e.g., `1.6`)

If it does, you’re ready to begin testing 👍

---

## ⚠️ Important Notes

* **Do not merge branches**
* **Do not create new branches unless instructed**
* Each branch represents a **different version of the software**
* Tests written for one branch may **not work correctly** on another branch

---

## ✅ Weekly Workflow Summary

For each week:

1. Open the repository in VS Code
2. Fetch the latest branches
3. Switch to the branch assigned for that week
4. Verify the branch name
5. Begin testing

---

If you run into issues switching branches, ask for help **before** starting your assignment.

Happy testing! 🧪
