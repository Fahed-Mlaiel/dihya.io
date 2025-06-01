# Exemple de configuration Terraform – Dihya Coding
#
# Ce fichier montre comment déployer une base PostgreSQL managée sur un cloud public
# en respectant les bonnes pratiques de sécurité, d’automatisation et de traçabilité.
#
# Bonnes pratiques :
# - Ne jamais stocker de credentials en clair (utiliser des variables d’environnement ou un vault)
# - Versionner chaque modification d’infrastructure
# - Documenter chaque ressource
# - Appliquer le principe du moindre privilège

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    postgresql = {
      source  = "cyrilgdn/postgresql"
      version = ">=1.13.0"
    }
  }
}

provider "postgresql" {
  host            = var.db_host
  port            = 5432
  username        = var.db_admin_user
  password        = var.db_admin_password
  sslmode         = "require"
}

variable "db_host" {
  description = "Adresse du serveur PostgreSQL"
  type        = string
}

variable "db_admin_user" {
  description = "Utilisateur admin PostgreSQL"
  type        = string
}

variable "db_admin_password" {
  description = "Mot de passe admin PostgreSQL"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "Nom de la base de données Dihya"
  type        = string
  default     = "dihya_db"
}

resource "postgresql_database" "dihya" {
  name              = var.db_name
  owner             = var.db_admin_user
  encoding          = "UTF8"
  lc_collate        = "fr_FR.UTF-8"
  lc_ctype          = "fr_FR.UTF-8"
  template          = "template0"
  connection_limit  = -1
}

resource "postgresql_role" "dihya_app" {
  name     = "dihya_app"
  login    = true
  password = random_password.app_password.result
}

resource "random_password" "app_password" {
  length  = 20
  special = true
}

output "dihya_app_password" {
  value       = random_password.app_password.result
  sensitive   = true
  description = "Mot de passe généré pour l’utilisateur dihya_app"
}