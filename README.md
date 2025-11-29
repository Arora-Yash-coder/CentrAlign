# CentrAlignAI

AI-powered dynamic form generator with context-aware memory retrieval.

## Overview

This project generates dynamic, shareable forms using LLMs.  
It uses contextual memory retrieval so only relevant past forms influence new form creation.

## Tech Stack

### Backend

- FastAPI (Python)
- MongoDB Atlas
- Cloudinary (media)
- SentenceTransformers (embeddings)
- Google Gemini / OpenRouter / Groq (LLM)

### Frontend

- Next.js 15
- TailwindCSS

---

## Features

### 1. Authentication

- Email/password login
- JWT-based authentication

### 2. AI Form Generator

- Prompt → JSON form schema
- Uses top-K relevant past forms for context
- Summaries + embeddings stored for retrieval

### 3. Dynamic Form Rendering

- Public share link: `/forms/:id`
- Supports image uploads

### 4. Submissions Dashboard

- View submissions grouped by form
- Includes uploaded image URLs

### 5. Context-Aware Memory Retrieval

- Every form summary is embedded
- For each new prompt:
  - Embed prompt
  - Vector search top-K relevant forms
  - Inject into LLM as memory
- Scales to thousands of forms

---

## Setup Instructions

### 1. Clone & Install Backend

```bash
cd backend
pip install -r requirements.txt
```
