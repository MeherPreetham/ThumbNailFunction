# Azure Functions Cold Start Performance Analysis

> Empirical study comparing serverless cold start latency vs. self-hosted performance for cloud-based image processing.

## 🎯 Project Goal

Measure and compare **cold start delays** in Azure Functions (serverless) against consistent performance in self-hosted applications to understand when each architecture is appropriate.

## 📊 Key Findings

| Metric | Azure Functions | Self-Hosted | Performance Impact |
|--------|----------------|-------------|-------------------|
| **Cold Start (20min idle)** | 2,485 ms | 98 ms | **25x slower** |
| **Warm Start** | 165 ms | 98 ms | 1.7x slower |
| **Consistency** | High variance | Predictable | Self-hosted wins |

**Bottom Line:** Serverless cold starts make it unsuitable for latency-sensitive user-facing APIs, but excellent for background processing.

## 🛠️ Technical Implementation

**Azure Functions (CSP):**
- HTTP-triggered image thumbnail generator
- Python 3.9 with OpenCV and NumPy
- Consumption Plan (cold start after ~20 min idle)

**Self-Hosted (Open Source):**
- Flask/Gunicorn web server (always-on)
- Same image processing logic
- Deployed on Ubuntu VM

## 📁 Repository Contents

```
├── function_app.py          # Azure Function implementation
├── host.json                # Runtime configuration
├── requirements.txt         # Dependencies (opencv, numpy)
├── local.settings.json      # Local development settings
└── README.md               # This file
```

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
func start

# Test cold start (after 20min idle)
curl -X POST http://localhost:7071/api/create_thumbnail \
  --data-binary "@test.jpg" \
  --output thumbnail.jpg
```

## 💡 When to Use Each

**Use Azure Functions (Serverless) for:**
- ✅ Background processing, event-driven tasks
- ✅ Sporadic traffic (hours/days between requests)
- ✅ Low-traffic applications (<10K req/day)

**Use Self-Hosted for:**
- ✅ User-facing APIs (<500ms SLA)
- ✅ High-traffic applications (>50K req/day)
- ✅ Predictable, consistent performance needs

## 📈 Performance Breakdown

**Cold Start Components (~2,500ms total):**
- Container provisioning: 1,000ms
- Python runtime: 400ms
- OpenCV loading: 650ms
- NumPy loading: 180ms
- Function execution: 200ms

**Optimisation Attempts:**
- Keep-alive pings: Eliminates cold starts but adds cost
- Premium Plan: No cold starts, but 15x more expensive
- Dependency optimisation: Only reduces by ~20%

## 🎓 Learning Outcomes

- Empirical performance measurement and benchmarking
- Serverless architecture trade-offs (cost vs. performance)
- Cloud cost optimisation strategies
- When to choose managed services vs. self-hosted infrastructure

## 👤 Author

**Meher Preetham Kommera**  
Master's in Cloud Computing  
[LinkedIn](https://www.linkedin.com/in/meher-preetham-kommera-23184023a/) • [GitHub](https://github.com/MeherPreetham)

---

**Academic Project:** Cloud Computing Module - Performance Analysis  
**Key Skill:** Understanding serverless cold start behaviour through empirical testing
