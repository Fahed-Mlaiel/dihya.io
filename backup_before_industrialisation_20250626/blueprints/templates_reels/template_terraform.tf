terraform {
  required_version = ">= 1.0.0"
}

provider "aws" {
  region = "eu-west-3"
}

resource "aws_s3_bucket" "dihya_storage" {
  bucket = "dihya-platform-bucket"
  acl    = "private"
}
