#!/bin/bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

sudo pacman -S --needed alacritty \
	base-devel \
	rofi \
	zsh-autosuggestions \
	zsh-syntax-highlighting \
	zoxide \
	neovim \
	starship \
	exa \
	bat \
	ripgrep \
	fzf \
	qtile \
	picom \
	ueberzug \
	ttf-hack-nerd \
	ttf-nerd-fonts-symbols \
	mpv \
	upower \
	rofi-emoji \
	xdg-user-dirs
	
yay -S xwinwrap \
	i3lock-color
