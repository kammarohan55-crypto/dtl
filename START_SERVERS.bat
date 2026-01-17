@echo off
echo ========================================
echo   AI Module Summarization System
echo ========================================
echo.
echo Starting servers...
echo.

REM Start backend in new window
echo [1/2] Starting Backend API on port 5000...
start "Backend API" cmd /k "cd /d %~dp0backend && python app.py"
timeout /t 3 /nobreak >nul

REM Start frontend in new window
echo [2/2] Starting Frontend Server on port 8000...
start "Frontend Server" cmd /k "cd /d %~dp0 && python serve_frontend.py"
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo   SERVERS STARTED!
echo ========================================
echo.
echo Backend API:  http://localhost:5000
echo Frontend:     http://localhost:8000/module.html
echo.
echo Opening browser in 3 seconds...
timeout /t 3 /nobreak >nul

REM Open browser
start http://localhost:8000/roadmap.html

echo.
echo ========================================
echo   To stop: Close the server windows
echo ========================================
echo.
pause
