# MSYS 22 Exercise and Project Repository

This repository is for collaboration on our project. Please remember to commit your changes so they are updated for everyone.

---

## How to Download Git

### Using GitHub Desktop
1. Download GitHub Desktop: [GitHub Desktop Download](https://desktop.github.com/download/)
2. Set up the repository in the GitHub Desktop app.
3. Open the repository in VS Code.
   - If you can't open it, install Git on your device.

### Installing Git Manually
- **Mac:** [Download Git for Mac](https://git-scm.com/downloads/mac)
- **Windows:** [Git Installation on Windows](https://www.simplilearn.com/tutorials/git-tutorial/git-installation-on-windows) *(not tested on Windows)*

---

## Important Notes

### `.gitignore` Adjustments
- Remove `*` in `msys22/.gitignore` so necessary files can be tracked by Git.
- Add `__pycache__/` to `msys22/.gitignore` to prevent unnecessary file bloating.
- You may also ignore `venv` and local database files.

### Repository Structure
✅ **Only include the project folder in the repository.**  
❌ **Do NOT include the virtual environment (`venv`) or superfolder.**

### Development Workflow
1. **Use a virtual environment** to test changes.
2. **Ensure changes work locally** before committing.
3. **Push updates to GitHub** so they reflect in the repository.
