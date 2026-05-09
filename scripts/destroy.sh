#!/bin/bash
set -e

echo "🛑 Starting Full Destruction of AGE-APP..."

# Delete Application
echo "Deleting Helm release..."
helm uninstall user-profile --namespace default || true

echo "Deleting Kubernetes resources..."
kubectl delete -f kubernetes/ --ignore-not-found=true || true

echo "Deleting ArgoCD Application (if exists)..."
kubectl delete -f argocd/application.yaml --ignore-not-found=true || true

# Destroy Terraform Infrastructure
echo "Destroying Terraform infrastructure..."
cd terraform
terraform init
terraform destroy -auto-approve

echo "✅ All resources destroyed successfully!"
echo "Note: Some resources like EBS volumes or Load Balancers may need manual cleanup in AWS Console."