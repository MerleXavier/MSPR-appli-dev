#!/bin/bash

# Définissez le chemin du répertoire Semabox ou Semalynx
git_path="/root/test-update/"


# Vérifiez si le répertoire git existe
if [ -d "$git_path" ]; then
  cd "$git_path"

  # Vérifiez s'il y a des mises à jour disponibles
  git remote update
  git status | grep "up to date"
  if [ $? -ne 0 ]; then
    # Mettre à jour le contenu du répertoire
    git $auth pull
  fi
fi
