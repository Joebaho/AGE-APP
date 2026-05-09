#!/bin/bash
echo "🚀 Setting up Monitoring (Prometheus + Grafana)..."

kubectl create namespace monitoring --dry-run=client -o yaml | kubectl apply -f -

# Apply all monitoring files
kubectl apply -f monitoring/

echo "✅ Monitoring deployed!"
echo "Prometheus: kubectl get svc prometheus -n monitoring"
echo "Grafana:    kubectl get svc grafana -n monitoring"