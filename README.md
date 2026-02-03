# 🛠️ Asana Task Title Updater

This GitHub Action automatically updates Asana task titles with the creation date code (e.g. `3F | Task Name`), running every 15 minutes.

## 🔧 Setup

1. **Fork this repo** into your GitHub account.
2. Go to **Settings > Secrets and variables > Actions > New repository secret** and add:
   - `ASANA_PAT` = your Personal Access Token
   - `PROJECT_ID` = the ID of your Asana project

3. Sit back — your task names will be updated every 15 minutes! ⏰

## 📋 Example

If a task is created on February 3rd with the name:

```
Design Wireframes
```

It will be updated to:

```
3F | Design Wireframes
```