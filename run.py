#!/usr/bin/env python
"""Run both backend and frontend applications"""

import subprocess
import os
import sys
from pathlib import Path

def main():
    """Start both applications"""
    project_root = Path(__file__).parent
    
    print("=" * 60)
    print("Smart Traffic RL System - Starting Applications")
    print("=" * 60)
    
    # Start backend
    backend_proc = subprocess.Popen(
        [sys.executable, "main.py"],
        cwd=project_root / "backend",
        env={**os.environ, "PYTHONUNBUFFERED": "1"}
    )
    
    # Small delay
    import time
    time.sleep(2)
    
    # Start frontend
    frontend_proc = subprocess.Popen(
        [sys.executable, "app.py"],
        cwd=project_root / "frontend",
        env={**os.environ, "PYTHONUNBUFFERED": "1"}
    )
    
    print("\n" + "=" * 60)
    print("✓ Backend API running on http://localhost:8000")
    print("✓ API Docs: http://localhost:8000/docs")
    print("✓ Frontend running on http://localhost:5000")
    print("=" * 60)
    print("\nPress Ctrl+C to stop all applications\n")
    
    try:
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        print("\n\nShutting down applications...")
        backend_proc.terminate()
        frontend_proc.terminate()
        backend_proc.wait()
        frontend_proc.wait()
        print("Applications stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
