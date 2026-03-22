provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "example" {
  bucket = "example-bucket"
  acl    = "public-read" # MISCONFIGURATION: Publicly readable

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_security_group" "example" {
  name        = "allow_all"
  description = "Allow all inbound traffic"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # MISCONFIGURATION: Allow all traffic
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  # No encryption for root volume (MISCONFIGURATION)
}
