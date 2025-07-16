# PATHS

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/shadow/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
 
# CUSTOM
alias vim="nvim"
alias ls="eza"
alias l='eza --git-ignore $eza_params'
alias ll="eza -alh"
alias llm='eza --all --header --long --sort=modified $eza_params'
alias la='eza -lbhHigUmuSa'
alias lx='eza -lbhHigUmuSa@'
alias lt='eza --tree $eza_params'
alias tree="eza --tree"
alias cat="bat -p"
alias ff="fzf --style full --preview 'fzf-preview.sh {}' --bind 'focus:transform-header:file --brief {}'"

export KEYTIMEOUT=1

eval "$(starship init zsh)"
eval "$(zoxide init --cmd cd zsh)"

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

ZSH_AUTOSUGGEST_STRATEGY=(history completion)
