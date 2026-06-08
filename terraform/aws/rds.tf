resource "aws_subnet" "private_a" {
  vpc_id = aws_vpc.main.id

  cidr_block = "10.0.11.0/24"

  availability_zone = "eu-west-2a"

  tags = {
    Name = "ads-platform-private-a"
  }
}

resource "aws_subnet" "private_b" {
  vpc_id = aws_vpc.main.id

  cidr_block = "10.0.12.0/24"

  availability_zone = "eu-west-2b"

  tags = {
    Name = "ads-platform-private-b"
  }
}

resource "aws_db_subnet_group" "main" {
  name = "ads-platform-db-subnet-group"

  subnet_ids = [
    aws_subnet.private_a.id,
    aws_subnet.private_b.id
  ]

  tags = {
    Name = "ads-platform-db-subnet-group"
  }
}

resource "aws_security_group" "rds" {
  name        = "ads-platform-rds"
  description = "Allow PostgreSQL traffic"

  vpc_id = aws_vpc.main.id

  ingress {
    from_port = 5432
    to_port   = 5432
    protocol  = "tcp"

    security_groups = [
      aws_security_group.web.id
    ]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ads-platform-rds-sg"
  }
}

resource "aws_db_instance" "postgres" {
  identifier = "ads-platform-postgres"

  engine         = "postgres"
  engine_version = "18"

  instance_class = "db.t3.micro"

  allocated_storage = 20

  db_name  = "ads_platform"
  username = "ads_user"
  password = var.db_password

  publicly_accessible = false

  skip_final_snapshot = true

  vpc_security_group_ids = [
    aws_security_group.rds.id
  ]

  db_subnet_group_name = aws_db_subnet_group.main.name
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}