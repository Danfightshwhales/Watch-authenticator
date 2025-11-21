# Watch Authenticator AI

An AI-powered system that analyzes watch photos to determine if a watch is:
- **Authentic**
- **Replica / Fake**
- **Frankenstein** (real parts mixed with aftermarket parts)

This project uses:
- A computer vision model trained on real vs. fake watch reference images  
- A part-level detection system to look for mismatched bezels, dials, crowns, cases, and backplates  
- A FastAPI backend to run the model  
- Optional Vercel/Railway deployment for hosting the service online  
- An image-based inference pipeline for real user uploads

---

## 🚀 Features

### 🔍 Photo-Based Watch Authentication
Upload watch images and receive:
- Authenticity score (0–100%)
- Part-by-part evaluation
- Explanation of why it looks real or fake
- Model certainty / confidence metrics

### 🧩 Part-Level Detection
The system examines:
- Dial layout  
- Crown shape  
- Hands length and alignment  
- Bezel font  
- Caseback engravings  
- Logo accuracy  
- Bracelet links  
- Serial & reference markings  

### 🧠 Training Pipeline
The model trains on:
- Authentic watch images sourced from eBay Authenticity Guarantee  
- Verified real references  
- Known replica examples  
- Aftermarket part catalogs  

Includes data augmentation such as:
- Blur  
- Lighting changes  
- Perspective distortion  
- Zoom  
- Low resolution  
- Glare handling  

### 🌐 API-Ready
A FastAPI server exposes endpoints like:
- `/predict` — submit watch images  
- `/part-analysis` — detailed breakdown  
- `/health` — system check  

### ☁️ Deployment Options
Out of the box, supports:
- **Railway deployment**  
- **Vercel server deployment**  
- Local Docker container  

---

## 🏗 Project Structure
