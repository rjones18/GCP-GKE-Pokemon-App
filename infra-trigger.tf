resource "google_cloudbuild_trigger" "example" {
  project = "alert-flames-286515"
  name    = "GKE-Pokemon-App-Trigger"
  disabled = false
  service_account = "projects/alert-flames-286515/serviceAccounts/cloudbuildaccount@alert-flames-286515.iam.gserviceaccount.com"

  trigger_template {
    repo_name   = "github_rjones18_gcp-gke-pokemon-app"
    branch_name = "main"
  }
  filename = "cloudbuild_files/cloudbuild.yaml"
}