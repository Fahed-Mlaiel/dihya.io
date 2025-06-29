provider "aws" {
  region = "eu-west-1"
}

# Networking resources
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.0.0"

  name = "analytics-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform = "true"
    Environment = "production"
  }
}

# Security groups
resource "aws_security_group" "analytics_sg" {
  name        = "analytics_sg"
  description = "Security group for analytics application"
  vpc_id      = module.vpc.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "analytics_sg"
  }
}

# EC2 instances for backend
module "ec2_instances" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "3.0.0"

  name           = "analytics-backend"
  instance_count = 2

  ami                    = "ami-0c55b159cbfafe1f0" # Example AMI ID
  instance_type          = "t3.medium"
  key_name               = "analytics-keypair"
  vpc_security_group_ids = [aws_security_group.analytics_sg.id]
  subnet_id              = module.vpc.private_subnets[0]

  tags = {
    Terraform   = "true"
    Environment = "production"
  }
}

# S3 bucket for frontend hosting
resource "aws_s3_bucket" "frontend_bucket" {
  bucket = "analytics-frontend-${random_id.bucket_suffix.hex}"
  acl    = "private"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }

  tags = {
    Name        = "analytics-frontend"
    Environment = "production"
  }
}

# IAM role for EC2 instances
resource "aws_iam_role" "ec2_role" {
  name = "analytics_ec2_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

# Attach necessary policies to the role
resource "aws_iam_role_policy_attachment" "policy_attachment" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM"
}

# Output for connecting to the backend instances
output "backend_instance_ips" {
  value = module.ec2_instances.private_ip
}

# Random ID for unique resource naming
resource "random_id" "bucket_suffix" {
  byte_length = 8
}