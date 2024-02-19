# GCP-GKE-Pokemon-App

In this project, I employed Terraform and kubectl to orchestrate the provisioning of a Python-based Flask web application that retrieves and displays Pokémon information using the PokeAPI onto a Kubernetes cluster running on Google Kubernetes Engine (GKE). By integrating a GitHub repository with Google Cloud Source Repositories and establishing a Cloud Build Trigger, I achieved continuous deployment, which automates the validation and deployment of my codebase. The deployment uses dual Cloud Build pipelines; one automates Terraform infrastructure deployment, and the other manages Docker image updates as well as the deployment of the specified Docker image onto the cluster using Kustomize.

To enhance the application's security, I integrated Snyk into the CI/CD pipeline, which actively scans the GitHub repositories for vulnerabilities and provides real-time monitoring and remediation recommendations. Snyk not only examines the application code but also inspects the dependencies, ensuring comprehensive security coverage throughout the development lifecycle.

Additionally, I assigned a custom domain name to the cluster using Google Domains, further enhancing the accessibility and professional appearance of the deployed application. This enhancement improved the application's credibility and overall user experience, making it an appealing and reliable resource for Pokémon enthusiasts.

Link to Website: http://pokemonpokedex.reggietestgcpdomain.com/ (Not currently deployed)

## Architecture Breakdown

The Kubernetes Cluster is broken down into the architecture below:

![kubernetespython](https://github.com/rjones18/Images/blob/main/KubernetesApp%20(4).png)
