# Quick Setup Guide 🦫

Get started with Capy UI Theme development in 3 minutes!

## Prerequisites

- VS Code installed
- (Optional) Node.js and npm for packaging

## Instant Testing

### Method 1: Press F5 (Recommended)

1. Open this folder in VS Code
2. Press `F5`
3. A new VS Code window opens with the theme loaded
4. Press `Ctrl+K Ctrl+T` and select "Capy UI"

### Method 2: Install Locally

Copy this folder to:
- Windows: `%USERPROFILE%\.vscode\extensions\`
- Mac/Linux: `~/.vscode/extensions/`

Then restart VS Code and activate the theme.

## Customizing Colors

Edit `themes/capy-ui-theme.json`:

```json
{
  "colors": {
    "editor.background": "#1c1d21",  // Change this!
    "statusBar.background": "#1e80c7",  // Or this!
    // ... more colors
  }
}
```

After changes:
1. Save the file
2. In the Extension Development Host window: `Ctrl+R` to reload
3. See your changes instantly!

## Color Palette Reference

```
Primary Accent:      #1e80c7  (electric blue)
Background:          #1c1d21  (tricorn black)
Secondary BG:        #36383f  (onyx)
Muted Blue:          #8bb4d8  (comments)
Light Text:          #f7f9f9  (almost white)
Success Green:       #00ba7c
Error Red:           #e74c3c
Bright Teal:         #5FF4AEFF (symbols)
Grey-Blue:           #93abd0, #a8b9ca, #a0b0c0
```

## Icon Note

The extension currently has an SVG icon (`icon.svg`). To use it in the marketplace, convert it to PNG:

```bash
# Using ImageMagick or any SVG converter
convert icon.svg -resize 128x128 icon.png
```

Or use an online converter like CloudConvert.

## Publishing Checklist

Before publishing to the marketplace:

- [ ] Convert `icon.svg` to `icon.png` (128x128)
- [ ] Update publisher name in `package.json`
- [ ] Add screenshots to README
- [ ] Test on multiple file types
- [ ] Verify all colors have good contrast
- [ ] Update version number

## Need Help?

- Check `TESTING.md` for detailed testing instructions
- See `README.md` for full documentation
- Review `themes/capy-ui-theme.json` for all color definitions

Happy theming! 💙
