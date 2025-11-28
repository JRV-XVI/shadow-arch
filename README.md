# shadow-arch

Personal configuration and dotfiles for an Arch-based setup. This repository collects curated configs for terminal, editor, window manager, and common desktop utilities so they can be replicated or adapted easily.

## Contents

- `install.sh`, `setup.sh` - helper scripts to bootstrap this configuration.
- `alacritty/` - Alacritty terminal configuration.
- `librewolf/` - Firefox/LibreWolf user styles and browser components.
- `nvim/` - Neovim configuration and custom plugins.
- `picom/` - compositor configuration.
- `qtile/` - Qtile window manager configuration and startup scripts.
- `ranger/` - Ranger file manager configuration and commands.
- `rofi/` - Rofi launcher styles and config.
- `starship/` - Starship prompt configuration.
- `wallpapers/` - Wallpapers used by the setup.
- `zsh/` - Zsh configuration files.

## Quick install

1. Review `install.sh` and `setup.sh` before running. They are intended to be run on an Arch-based system.
2. Backup any existing configuration you want to keep.
3. Run:

```bash
./install.sh
./setup.sh
```

Adjust paths or install components manually if you prefer selective setup.

## Customization

Edit files under the relevant directories (for example, `nvim/` or `qtile/`) to customize behavior and appearance. The configs are organized by application to make targeted changes simple.

## Notes

This repository is maintained for personal use; adapt anything here for your own setup. Contributions or suggestions are welcome via issues or pull requests.

---
Updated configuration collection for a personal Arch environment.
