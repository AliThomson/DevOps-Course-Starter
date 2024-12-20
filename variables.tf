variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "oauth_client_id" {
  type = string
}

variable "oauth_client_secret" {
  type = string
  sensitive = true
}

variable "secret_key" {
  type    = string
  sensitive = true
}
