# 🚀 User Profile Classification Platform

A production-grade cloud-native DevOps project using:

- Python Flask
- Docker
- DockerHub
- Kubernetes
- Helm
- ArgoCD
- Terraform
- AWS EKS
- GitHub Actions
- Prometheus/Grafana
- AI Monitoring
- Slack Alerts

---

# 🔥 PROJECT ARCHITECTURE

User → Flask App → Docker → Kubernetes → AWS EKS → ArgoCD GitOps

---

# 🔥 PREREQUISITES

Install:

- Docker
- kubectl
- Helm
- Terraform
- AWS CLI
- Python 3
- Git

---

# 🔥 CLONE PROJECT

```bash
git clone https://github.com/yourrepo/user-profile-platform.git

cd user-profile-platform
```

---

# 🔥 STEP 1 — BUILD DOCKER IMAGE

```bash
cd app

docker build -t yourdockerhubusername/user-profile-platform:v1 .
```

---

# 🔥 STEP 2 — LOGIN TO DOCKERHUB

```bash
docker login
```

---

# 🔥 STEP 3 — PUSH IMAGE

```bash
docker push yourdockerhubusername/user-profile-platform:v1
```

---

# 🔥 STEP 4 — CONFIGURE AWS

```bash
aws configure
```

Enter:

- AWS Access Key
- AWS Secret Key
- Region: us-west-2

---

# 🔥 STEP 5 — DEPLOY TERRAFORM EKS

```bash
cd terraform

terraform init

terraform apply -auto-approve
```

---

# 🔥 STEP 6 — CONNECT TO EKS

```bash
aws eks update-kubeconfig \
--region us-west-2 \
--name user-profile-eks
```

---

# 🔥 STEP 7 — DEPLOY KUBERNETES APP

```bash
kubectl apply -f kubernetes/
```

---

# 🔥 STEP 8 — DEPLOY HELM

```bash
helm install user-profile ./helm/user-profile
```

---

# 🔥 STEP 9 — INSTALL ARGOCD

```bash
kubectl create namespace argocd

kubectl apply -n argocd \
-f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

---

# 🔥 STEP 10 — DEPLOY ARGOCD APPLICATION

```bash
kubectl apply -f argocd/application.yaml
```

---

# 🔥 STEP 11 — VERIFY DEPLOYMENT

```bash
kubectl get pods

kubectl get svc

kubectl get ingress
```

---

# 🔥 STEP 12 — ACCESS APPLICATION

Get LoadBalancer URL:

```bash
kubectl get svc
```

Open browser:

```text
http://EXTERNAL-IP
```

---

# 🔥 STEP 13 — RUN AI MONITORING

```bash
python scripts/ai_monitor.py
```

---

# 🔥 STEP 14 — SEND SLACK ALERT

```bash
python scripts/slack_alert.py
```

---

# 🔥 STEP 15 — DESTROY EVERYTHING

```bash
chmod +x destroy.sh

./destroy.sh
```

---

# 🔥 FEATURES

- Cloud-native Flask application
- Docker containerization
- Kubernetes orchestration
- AWS EKS cluster
- GitOps with ArgoCD
- Helm package management
- AI monitoring automation
- Slack alerting
- Infrastructure as Code
- CI/CD automation
- Observability integration
- Self-healing deployments

---

# 🔥 FUTURE IMPROVEMENTS

- Canary deployments
- Blue/Green deployments
- Prometheus alerts
- Grafana dashboards
- FinOps cost monitoring
- AI anomaly detection
- OpenTelemetry tracing
- Karpenter autoscaling

---

# 🔥 AUTHOR

Joseph Mbatchou