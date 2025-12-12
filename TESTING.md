# Testing Instructions

## How to Test the Capy UI Theme

### Option 1: Install as Development Extension

1. Open VS Code in this directory:
   ```bash
   cd c:\Code\VS-Capy-UI
   code .
   ```

2. Press `F5` to launch Extension Development Host
   - This opens a new VS Code window with the theme loaded
   - The theme will be available in the theme picker

3. In the new window, activate the theme:
   - Press `Ctrl+K Ctrl+T` (or `Cmd+K Cmd+T` on Mac)
   - Select "Capy UI" from the list

### Option 2: Install Locally

1. Package the extension (requires vsce):
   ```bash
   npm install -g @vscode/vsce
   vsce package
   ```

2. Install the generated `.vsix` file:
   ```bash
   code --install-extension capy-ui-theme-1.0.0.vsix
   ```

3. Activate the theme:
   - `Ctrl+K Ctrl+T` → Select "Capy UI"

### Option 3: Copy to Extensions Folder

1. Copy this entire folder to your VS Code extensions directory:
   - **Windows**: `%USERPROFILE%\.vscode\extensions\capy-ui-theme`
   - **macOS/Linux**: `~/.vscode/extensions/capy-ui-theme`

2. Restart VS Code

3. Activate the theme:
   - `Ctrl+K Ctrl+T` → Select "Capy UI"

## What to Test

### Visual Elements to Check

- [ ] **Editor Background**: Should be dark charcoal (`#1c1d21`)
- [ ] **Text Selection**: Should have electric blue background (`#1e80c7` with transparency)
- [ ] **Active Tab**: Should have electric blue accent
- [ ] **Status Bar**: Should be electric blue
- [ ] **Sidebar**: Dark with blue highlights for active items
- [ ] **Activity Bar**: Blue accent for active view

### Syntax Highlighting to Check

Open the demo files in `demo/` folder:

- [ ] **Comments**: Muted blue and italic
- [ ] **Strings**: Green (`#00ba7c`)
- [ ] **Keywords**: Electric blue and bold
- [ ] **Functions**: Grey-blue (`#93abd0`)
- [ ] **Classes/Types**: Light grey-blue (`#a8b9ca`)
- [ ] **Numbers/Constants**: Grey-blue (`#93abd0`)
- [ ] **Variables**: Light text
- [ ] **Operators/Symbols**: Bright teal (`#5FF4AEFF`)

### Files to View

1. `demo/sample.ts` - TypeScript/JavaScript/React syntax
2. `demo/sample.py` - Python syntax
3. Any of your own code files

## Troubleshooting

### Theme Not Showing Up

1. Make sure the folder structure is correct:
   ```
   capy-ui-theme/
   ├── package.json
   ├── themes/
   │   └── capy-ui-theme.json
   └── ...
   ```

2. Check the VS Code Output panel for errors:
   - View → Output → Select "Extensions" from dropdown

3. Reload VS Code window:
   - `Ctrl+Shift+P` → "Developer: Reload Window"

### Colors Look Wrong

1. Make sure you don't have color customizations in your settings:
   - Open Settings (`Ctrl+,`)
   - Search for "color customizations"
   - Remove any `workbench.colorCustomizations` for this theme

2. Try disabling other extensions that might interfere with theming

## Publishing to Marketplace (Future)

To publish this theme to the VS Code Marketplace:

1. Create a publisher account at https://marketplace.visualstudio.com/

2. Get a Personal Access Token from Azure DevOps

3. Login with vsce:
   ```bash
   vsce login <publisher-name>
   ```

4. Publish:
   ```bash
   vsce publish
   ```

## Feedback

If you find any issues or have suggestions:
- Adjust colors in `themes/capy-ui-theme.json`
- Update version in `package.json`
- Document changes in `CHANGELOG.md`
