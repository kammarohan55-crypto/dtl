# How to Run the AI Module Summarization Feature

## Quick Start

### 1. Install Backend Dependencies

```bash
cd c:\Users\Rohan\Desktop\dtl\backend
pip install -r requirements.txt
```

### 2. Start the Backend Server

```bash
python app.py
```

You should see:
```
============================
Module Summarization API Starting...
============================
✓ Curriculum loaded from: ...mathematics_curriculum.json
...
Starting server on http://localhost:5000
============================
```

**Keep this terminal running!**

### 3. Open the Frontend

Open `frontend/module.html` in your web browser:

**Option A - Double-click:**
- Navigate to `c:\Users\Rohan\Desktop\dtl\frontend`
- Double-click `module.html`

**Option B - Command line:**
```bash
start c:\Users\Rohan\Desktop\dtl\frontend\module.html
```

## Using the Feature

1. **Select Level**: Choose Beginner, Intermediate, or Advanced
2. **Select Module**: Pick a specific module from the dropdown
3. **Load Module**: Click "Load Module" to view content
4. **Summarize**: Click the "🤖 Summarize This Module with AI" button
5. **View Summary**: AI-generated summary appears below

## Troubleshooting

### Backend not starting?
- Ensure Python 3.7+ is installed
- Check if port 5000 is available
- Try: `python -m pip install --upgrade pip` then reinstall requirements

### "Unable to connect to AI service" error?
- Verify backend server is running (check terminal)
- Ensure URL is `http://localhost:5000`
- Check browser console for  CORS errors

### Module not loading?
- Verify `mathematics_curriculum.json` is in the `dtl` directory
- Check browser console (F12) for JavaScript errors

## Testing Different Modules

Try these examples:

**Beginner:**
- Linear Equations → Good for checking basic formatting
- Probability Basics → Tests conditional logic display

**Intermediate:**
- Matrices → Tests mathematical notation
- Differentiation → Tests formula rendering

**Advanced:**
- Linear Algebra → Tests complex content summarization
- Math for Machine Learning → Tests technical terminology

## API Endpoints

The backend provides these endpoints:

- `POST /api/summarize` - Generate module summary
- `GET /api/modules` - List all available modules  
- `GET /api/health` - Health check

### Test API Directly (Optional)

```bash
# List all modules
curl http://localhost:5000/api/modules

# Generate summary
curl -X POST http://localhost:5000/api/summarize \
  -H "Content-Type: application/json" \
  -d "{\"module_id\": \"linear_equations\", \"level\": \"beginner\"}"
```

## Project Structure

```
dtl/
├── backend/
│   ├── app.py              # Flask API server
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── module.html         # Main page
│   ├── css/
│   │   ├── module.css      # Page styling
│   │   └── summary.css     # Summary display styling
│   └── js/
│       ├── module.js       # Module loading logic
│       └── summarize.js    # AI summarization logic
└── mathematics_curriculum.json  # All 24 modules

```

## Next Steps

- Deploy to a web server for production use
- Add user authentication
- Cache generated summaries for better performance
- Integrate with actual AI APIs (OpenAI, Anthropic, etc.)
- Add export to PDF functionality

## Success Indicators

✅ Backend runs without errors  
✅ Frontend loads cleanly in browser  
✅ Module selection works smoothly  
✅ "Summarize Module" button appears  
✅ Summary generates and displays  
✅ All sections formatted correctly  
✅ Responsive design works on mobile

---

**Need help?** Check the browser console (F12) and backend terminal for error messages.
