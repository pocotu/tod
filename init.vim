"### Configuracion de Vim ###"

" Activa el numerado de lineas
set number

" Establecer 4 espacios para la sangría
set tabstop=4

" Activa el resaltado de sintaxis
syntax enable

" Activa el mouse para seleccionar texto e ir a la linea
set mouse=a

" Activa el resaltado de la línea actual
set cursorline

" Activa mostrar comandos en la barra de estado
set showcmd

" Activa donde termina los parentesis y llaves
set showmatch

" Cambiar el color del color de la sintaxis
" colorscheme desert
"colorscheme darkblue
"colorscheme elflord "good
"colorscheme evening
"colorscheme morning "good
"colorscheme murphy
"colorscheme pablo "good
"colorscheme zellner

call plug#begin('~/.vim/plugged')

" Mejora la sintaxis de Python
Plug 'vim-python/python-syntax'

Plug 'sainnhe/gruvbox-material'

" Mostrar las sangrias con lineas verticales
"Plug 'Yggdroot/indentLine'

" Mejora la barra de estado
Plug 'vim-airline/vim-airline'

Plug 'preservim/nerdtree'

" Mejora la sintaxis de Javascript
Plug 'pangloss/vim-javascript'

call plug#end()

" GRUVBOX CONFIGURATION
set background=dark
left g:gruvbox_material_background = 'medium'
colorscheme gruvbox-material

" INDENTLINE CONFIGURATION
let g:airline#extensions#tabline#enabled = 1

" NERDTREE CONFIGURATION
" Cierra el explorador de archivos al abrir un archivo
let NERDTreeQuitOnOpen=1
" atajo para abrir el explorador de archivos con ctrl + a
nnoremap <C-a> :NERDTreeToggle<CR>
" atajo para cerrar el explorador de archivos con ctrl + q
nnoremap <C-q> :NERDTreeClose<CR>
