#!/bin/bash

diretorio="/home/ulisses/DDSM-all/CBIS-DDSM-png/full_img_dir"

cd "$diretorio" || exit

for arquivo in *P_*.png; do
    if [ -f "$arquivo" ]; then
        nome_sem_prefixo="${arquivo#*P_}"
        novo_nome="P_${nome_sem_prefixo}"
        mv "$arquivo" "$novo_nome"
        
        echo "Arquivo $arquivo renomeado para $novo_nome"
    fi
done