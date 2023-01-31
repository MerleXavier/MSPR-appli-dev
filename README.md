# MSPR-appli-dev

## Semabox
Pour faire la supervision du réseau.

## Semalynx
Pour garder un contrôle sur les Semabox.

## Pour info
Le script *auto-update-git.sh* va permettre de mettre à jour votre SemaBox et votre Semalynx.
Pour faire fonctionner ce script vous pouvez soit : ```bash auto-update-git.sh```
ou ajouter le script dans votre plannificateur de tâche linux:
```crontab -e```
```@reboot /bin/bash /root/auto-update-git.sh```
Il vous faudra aussi modifier la variable **git_path** si vous ne l'avez pas placé au même endroit.
