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
alias ls="exa"
alias ll="exa -alh"
alias tree="exa --tree"
alias cat="bat -p"

export KEYTIMEOUT=1

eval "$(starship init zsh)"
eval "$(zoxide init --cmd cd zsh)"

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

ZSH_AUTOSUGGEST_STRATEGY=(history completion)
