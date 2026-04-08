variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
  default     = "980440e4-d46f-4734-b1c1-2cf39d6bb311"
}

variable "resource_group_name" {
  description = "Resource Group Name"
  type        = string
  default     = "retail-analytics-rg"
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "eastus"
}

variable "project_name" {
  description = "Project Name"
  type        = string
  default     = "pavanretail2024"
}