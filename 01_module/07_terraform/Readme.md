#### Terraform

HashiCorp Terraform is an code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle.

### Why Terraform?

* Simplicity in keeping track of infrastructure 
* Easy collaboration with team members
* Reproducibility of infrastructure
* Ensure resources are removed

### What terraform is not-

* Does not manage and update code on infrastructure
* Does not give you the ability to change immutable resources
* Not used to manage resources not defined in the terraform files


> ## Terraform Basics Video

### **Steps and Commands Used**

---

#### **1. Setting Up a Service Account**
A **service account** is a special account that allows applications or systems to access GCP resources.

1. **Create a Service Account:**
   - Navigate to **IAM & Admin > Service Accounts** in the GCP console.
   - Click **Create Service Account**.
   - Assign the necessary roles:
     - **Cloud Storage Admin**: Full access to Google Cloud Storage.
     - **BigQuery Admin**: Full access to BigQuery.
     - **Compute Admin**: Full access to compute resources.

2. **Manage Keys for the Service Account:**
   - Create a new key for the service account.
   - Save the JSON key file locally.

---

#### **2. Securely Handling Credentials**
- Avoid sharing the JSON key file publicly (e.g., never upload it to GitHub).
- Store sensitive files securely in directories such as `keys/`.

**Command to export credentials:**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/key.json"
```
This environment variable allows Terraform to authenticate using the service account.

---

#### **3. Installing Terraform and Configuring the Provider**
1. **Install Terraform** and set up a directory:
   ```bash
   mkdir terraform_demo
   cd terraform_demo
   ```

2. **Initialize a Terraform Configuration File** (`main.tf`):
   ```hcl
   terraform {
     required_providers {
       google = {
         source = "hashicorp/google"
         version = "6.14.1"
       }
     }
   }

   provider "google" {
    credentials = "./keys/your-key.json"
     project = "your-gcp-project-id"
     region  = "us-central1"
   }
   ```
   - Replace `your-gcp-project-id` with the actual project ID.

3. **Run `terraform init`**:
   ```bash
   terraform init
   ```
   - Initializes Terraform and downloads the required provider plugin.

---

#### **4. Creating a Resource (GCS Bucket)**
**Add a resource definition to `main.tf`:**
```hcl
resource "google_storage_bucket" "demo_bucket" {
  name          = "terraform-demo-bucket-unique-name"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 3
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
```

**Commands to apply changes:**
1. **Plan the changes:**
   ```bash
   terraform plan
   ```
   - Simulates changes without applying them.

2. **Apply the changes:**
   ```bash
   terraform apply
   ```
   - Creates the specified bucket. Confirm with `yes`.

---

#### **5. Verifying and Destroying Resources**
1. **Verify the bucket in the GCP console**:
   - Go to **Storage > Buckets** and confirm the bucket creation.

2. **Destroy the resources:**
   ```bash
   terraform destroy
   ```
   - Removes all resources defined in the state file.

---

### **Best Practices Highlighted**
1. **Handle Credentials Securely:**
   - Use environment variables or secure directories for sensitive files.
   - Never hardcode credentials in Terraform files.

2. **Use `.gitignore` for Sensitive Files:**
   - Prevent key files (e.g., JSON credentials) from being accidentally uploaded to version control.
   ```bash
   *.json
   terraform.tfstate
   ```
   - Example `.gitignore` for Terraform:
     - `.terraform/`
     - `*.tfstate*`
     - `*.json`

3. **Validate and Format Terraform Code:**
   - Use `terraform fmt` to format configuration files neatly.
   - Use `terraform plan` to preview changes before applying.

4. **Avoid Hardcoding Values:**
   - Use variables to make the configuration reusable.

---

### **Commands Cheat Sheet**
| **Command**                  | **Purpose**                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `terraform init`             | Initializes Terraform in the directory and downloads provider plugins.     |
| `terraform plan`             | Simulates changes and shows a detailed plan without applying changes.      |
| `terraform apply`            | Applies the changes and provisions the resources.                         |
| `terraform destroy`          | Destroys all resources defined in the state file.                         |
| `terraform fmt`              | Formats the Terraform configuration files for readability.                |
| `export GOOGLE_APPLICATION_CREDENTIALS="/path"` | Sets the environment variable for credentials.                   |

---

### **Key Takeaways**
- **Terraform's Workflow**: Define → Plan → Apply → Destroy.
- **Security**: Always treat service account keys and Terraform state files as sensitive information.
- **Documentation**: Terraform’s documentation is highly detailed and can help resolve most issues.

This video provides a solid foundation for using Terraform with GCP and sets the stage for more advanced use cases like handling variables and modules in larger projects.