### Terraform Variables
---

### **Key Steps and Commands**

---

#### **1. Recap of Terraform Basics**
- **Creating a Storage Bucket**:
  ```hcl
  resource "google_storage_bucket" "demo_bucket" {
    name          = "terraform-demo-bucket"
    location      = "US"
    force_destroy = true
  }
  ```
  - Use `terraform apply` to create the bucket.
  - Use `terraform destroy` to remove it.

- **State Files**:
  - `terraform.tfstate`: Tracks the current state of infrastructure.
  - `.backup`: A backup of the state file for recovery in case of failure.

---

#### **2. Adding a BigQuery Dataset**
- **Creating a BigQuery Dataset**:
  ```hcl
  resource "google_bigquery_dataset" "demo_dataset" {
    dataset_id     = "demo_dataset"
    location       = "US"
    delete_contents_on_destroy = true
  }
  ```
  - **Explanation**:
    - `dataset_id`: Unique name for the dataset.
    - `delete_contents_on_destroy`: Deletes tables within the dataset when the resource is destroyed.
  - Commands:
    - Use `terraform apply` to create the dataset.
    - Verify in the GCP console under **BigQuery**.

---

#### **3. Using Variables for Flexibility**
- **Defining Variables**:
  Create a `variables.tf` file for centralized variable management.
  ```hcl
  variable "location" {
    description = "Project location"
    default     = "US"
  }

  variable "gcs_bucket_name" {
    description = "Name of the GCS bucket"
    default     = "terraform-demo-bucket"
  }

  variable "bq_dataset_name" {
    description = "Name of the BigQuery dataset"
    default     = "demo_dataset"
  }
  ```

- **Using Variables in Terraform**:
  Reference variables in the `main.tf` file.
  ```hcl
  resource "google_storage_bucket" "demo_bucket" {
    name     = var.gcs_bucket_name
    location = var.location
  }

  resource "google_bigquery_dataset" "demo_dataset" {
    dataset_id = var.bq_dataset_name
    location   = var.location
  }
  ```

- **Benefits**:
  - Centralizes configurations.
  - Simplifies project updates (e.g., changing location from "US" to "EU").

---

#### **4. Handling Credentials Securely**
- **Avoid Hardcoding Credentials**:
  - Use environment variables:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"
    ```

- **Defining Credentials in Variables**:
  - Add credentials as a variable in `variables.tf`:
    ```hcl
    variable "credentials" {
      description = "Service account credentials"
      default     = "keys/my-credentials.json"
    }
    ```

  - Reference it in the provider block:
    ```hcl
    provider "google" {
      credentials = file(var.credentials)
      project     = var.project_id
      region      = var.location
    }
    ```

- **Security Tips**:
  - Use `.gitignore` to exclude sensitive files like `.tfstate` and JSON credentials:
    ```plaintext
    *.tfstate*
    keys/*.json
    ```

---

#### **5. Workflow Summary**
- **Terraform Commands**:
  - `terraform plan`: Preview changes before applying them.
  - `terraform apply`: Apply changes to create resources.
  - `terraform destroy`: Remove all defined resources.

---

### **Best Practices**
1. **Variables for Modularity**:
   - Store reusable configurations in `variables.tf`.
   - Use descriptive variable names and comments.

2. **Handle State Files Carefully**:
   - Protect `.tfstate` and `.backup` files; they store sensitive metadata.
   - Use remote state storage for team collaboration.

3. **Secure Credentials**:
   - Avoid hardcoding credentials in Terraform files.
   - Always exclude sensitive files from version control.

4. **Use `terraform fmt`**:
   - Format Terraform code for readability:
     ```bash
     terraform fmt
     ```

5. **Leverage Terraform Documentation**:
   - Detailed examples and usage for all providers and resources.

---

### **Commands Cheat Sheet**
| **Command**                 | **Purpose**                                                       |
|-----------------------------|-------------------------------------------------------------------|
| `terraform init`            | Initialize Terraform and download provider plugins.              |
| `terraform plan`            | Show a preview of changes Terraform will apply.                  |
| `terraform apply`           | Apply the planned changes to create or modify resources.         |
| `terraform destroy`         | Destroy all resources defined in the state file.                |
| `terraform fmt`             | Automatically format `.tf` files for consistency.               |
| `export GOOGLE_APPLICATION_CREDENTIALS="/path"` | Set credentials for Terraform to authenticate with GCP. |

---
