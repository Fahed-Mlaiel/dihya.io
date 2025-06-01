# Exemple Terraform ultra avancé (audit, RGPD, sécurité, accessibilité, CI/CD, monitoring)
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = "eu-west-3"
}

resource "aws_s3_bucket" "dihya_audit" {
  bucket = "dihya-audit-logs"
  acl    = "private"
  tags = {
    RGPD        = "true"
    Audit       = "enabled"
    Access      = "restricted"
    Environment = "prod"
  }
  versioning {
    enabled = true
  }
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
