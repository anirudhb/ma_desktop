" set nocompatible
set ts=4
set et
set ru
set nu
function! OpenInBrowser()
    !google-chrome-stable %
endfunction
command OpenBrowser call OpenInBrowser()
" execute pathogen#infect()
