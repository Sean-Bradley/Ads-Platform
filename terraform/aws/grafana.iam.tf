resource "aws_iam_user" "grafana" {
  name = "Grafana"

  tags = {
    Name = "grafana-monitoring-user"
  }
}

resource "aws_iam_access_key" "grafana" {
  user = aws_iam_user.grafana.name
}

resource "aws_iam_user_policy_attachment" "grafana_cloudwatch" {
  user       = aws_iam_user.grafana.name
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess"
}

output "grafana_access_key_id" {
  value = aws_iam_access_key.grafana.id
}

output "grafana_secret_access_key" {
  value     = aws_iam_access_key.grafana.secret
  sensitive = true
}