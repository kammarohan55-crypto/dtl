# 🚀 Multi-Subject Educational Platform - Quick Start

## What's New
✅ **3 Subjects Available**: Mathematics, AI/ML, Programming C  
✅ **72 Total Modules**: 24 modules per subject  
✅ **Unified Interface**: Same workflow for all subjects

---

## How to Run

### 1. Start Both Servers

**Double-click**: `START_SERVERS.bat`

This automatically:
- Starts backend API on port 5000
- Starts frontend server on port 8000  
- Opens browser to http://localhost:8000/module.html

**Keep the 2 black windows running!**

---

## How to Use

### The 4-Step Workflow:

1. **Select Subject**  
   Choose: Mathematics, AI & Machine Learning, or Programming in C

2. **Select Level**  
   Choose: Beginner, Intermediate, or Advanced  

3. **Select Module**  
   Pick any module from the dropdown  

4. **Load & Summarize**  
   - Click "Load Module" to view content  
   - Click "🤖 Summarize This Module with AI"  
   - AI summary appears below!

---

## Try These Examples

### Mathematics → Beginner → Linear Equations
### AI/ML → Intermediate → Neural Networks  
### Programming C → Beginner → Pointers Basics

Each subject has unique modules with tailored content!

---

## What Each Subject Contains

**Mathematics (24 modules)**  
- Beginner: Number systems, equations, geometry, statistics
- Intermediate: Calculus, matrices, differential equations
- Advanced: Linear algebra, optimization, numerical methods

**AI & Machine Learning (24 modules)**  
- Beginner: Python, NumPy, Pandas, linear/logistic regression
- Intermediate: Neural networks, CNNs, RNNs, NLP  
- Advanced: Transformers, GANs, reinforcement learning, MLOps

**Programming in C (24 modules)**  
- Beginner: Variables, functions, arrays, pointers, structures
- Intermediate: Dynamic memory, file I/O, linked lists, recursion
- Advanced: Trees/graphs, hash tables, bit manipulation, system programming

---

## Troubleshooting

**"Failed to load module"?**  
- Ensure both servers are running (2 black windows)
- Check curriculum files exist in frontend folder

**Backend not starting?**  
```powershell
cd c:\Users\Rohan\Desktop\dtl\backend
pip install Flask flask-cors
```

**Frontend not loading?**  
Manually open: http://localhost:8000/module.html

---

## Files Location

**Curricula**:
- `mathematics_curriculum.json` (copied to frontend/)
- `aiml_curriculum.json` (copied to frontend/)
- `programming_c_curriculum.json` (copied to frontend/)

**Servers**:
- Backend: `backend/` app.py`
- Frontend: `serve_frontend.py`
- Launcher: `START_SERVERS.bat`

---

## Success Checklist

- [ ] Both servers running (2 windows open)
- [ ] Browser shows purple gradient page
- [ ] Subject dropdown has 3 options
- [ ] Selecting subject enables level dropdown
- [ ] Selecting level populates module dropdown
- [ ] Module loads with content
- [ ] Summary button works for all subjects

---

That's it! Explore all 72 modules across 3 subjects! 🎓
