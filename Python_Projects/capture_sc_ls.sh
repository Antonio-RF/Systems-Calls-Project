#!/bin/bash

BASE="$HOME"
OUT_DIR="$HOME/Documentos/Systems-Calls-Project/Dates/ls"
OUT_DATA="$OUT_DIR/date_ls.txt"
OUT_CMDS="$OUT_DIR/commands.txt"

mkdir -p "$OUT_DIR"
> "$OUT_DATA"
> "$OUT_CMDS"

# -------------------------------
# Diretórios primários
# -------------------------------
PRIMARY_DIRS=(
  Desktop Documentos Imagens Músicas Downloads Public
  Templates Videos snap fake ""
)

# -------------------------------
# Subdiretórios
# -------------------------------
DOCUMENTOS=(
  circuitos Antonio-RF.github.io Strong-Password-Generator
  Computer-Science-Freshmen-at-UFPR Scientific-Calculator
  Sorting-and-Searching-Algorithms The-Boys
  certificados_cursos Competitive-programming Capture-The-Flag
)

IMAGENS=(Images Screenshots)
SNAP=(firefox snapd-desktop-integration spotify)

DOWNLOADS=(
  testes firefox coord.o entrada2.txt forrest-sense-of-self-1.pdf
  Generator2.py index.html outfile.tga dark_room.png
  entrada.txt forrest-sense-of-self.pdf Generator.py
  main.py strace_r.txt
)

# -------------------------------
# Opções do ls
# -------------------------------
LS_OPTIONS=(
  "" "-a" "-l" "-i" "-lh" "-1" "-s" "-t"
  "/" ".." "-la" "-S" "*.txt" "*"
)

# -------------------------------
# Número de execuções
# -------------------------------
RUNS=10000
COUNT=1

# -------------------------------
# Loop principal
# -------------------------------
for ((i=0; i<RUNS; i++)); do

  PRIMARY=${PRIMARY_DIRS[$RANDOM % ${#PRIMARY_DIRS[@]}]}
  PATH_PART=""

  if [[ "$PRIMARY" == "Documentos" ]]; then
    SEC=${DOCUMENTOS[$RANDOM % ${#DOCUMENTOS[@]}]}
    PATH_PART="/$PRIMARY/$SEC"

  elif [[ "$PRIMARY" == "Imagens" ]]; then
    SEC=${IMAGENS[$RANDOM % ${#IMAGENS[@]}]}
    PATH_PART="/$PRIMARY/$SEC"

  elif [[ "$PRIMARY" == "snap" ]]; then
    SEC=${SNAP[$RANDOM % ${#SNAP[@]}]}
    PATH_PART="/$PRIMARY/$SEC"

  elif [[ "$PRIMARY" == "Downloads" ]]; then
    SEC=${DOWNLOADS[$RANDOM % ${#DOWNLOADS[@]}]}
    PATH_PART="/$PRIMARY/$SEC"

  elif [[ "$PRIMARY" == "" ]]; then
    PATH_PART=""

  else
    PATH_PART="/$PRIMARY"
  fi

  OPTION=${LS_OPTIONS[$RANDOM % ${#LS_OPTIONS[@]}]}

  CMD="strace ls $OPTION $BASE$PATH_PART"

  echo "$COUNT. $CMD" >> "$OUT_CMDS"

  # -------------------------------
  # EXECUÇÃO REAL (SHELL PURO)
  # -------------------------------
  TRACE=$(
    strace ls $OPTION "$BASE$PATH_PART" 2>&1 |
    sed -n 's/^\([a-zA-Z_][a-zA-Z0-9_]*\)(.*/\1/p' |
    tr '\n' ';'
  )

  echo "$CMD| $TRACE" >> "$OUT_DATA"

  ((COUNT++))
done
