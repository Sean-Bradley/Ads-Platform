resource "aws_ecs_cluster" "main" {
  name = "ads-platform-cluster"
}

resource "aws_ecs_task_definition" "app" {
  family                   = "ads-platform-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]

  cpu    = 256
  memory = 512

  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name  = "ads-platform"
      image = "190934385828.dkr.ecr.eu-west-2.amazonaws.com/ads-platform:latest"

      essential = true

      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
        }
      ]

      environment = [
        {
          name  = "APP_ENV"
          value = "production"
        },
        {
          name  = "APP_HOST"
          value = "0.0.0.0"
        },
        {
          name  = "APP_PORT"
          value = "8000"
        },
        {
          name  = "DATABASE_URL"
          value = "postgresql://ads_user:${var.db_password}@${aws_db_instance.postgres.address}:5432/ads_platform"
        }
      ]
    }
  ])
}