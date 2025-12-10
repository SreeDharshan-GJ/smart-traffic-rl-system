#!/usr/bin/env python
"""Quick start guide - Set up and run Smart Traffic RL System"""

import subprocess
import sys
import os
from pathlib import Path

def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def run_command(cmd, cwd=None, shell=True):
    """Run a shell command"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=shell,
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    project_root = Path(__file__).parent
    
    print_header("Smart Traffic RL System - Quick Setup")
    
    # Check Python version
    print("\n✓ Checking Python version...")
    if sys.version_info < (3, 8):
        print(f"  ✗ Python 3.8+ required (found {sys.version_info.major}.{sys.version_info.minor})")
        return False
    print(f"  ✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Create virtual environment
    print("\n✓ Setting up virtual environment...")
    venv_path = project_root / "venv"
    if not venv_path.exists():
        success, _, _ = run_command(f"{sys.executable} -m venv venv", cwd=project_root)
        if not success:
            print("  ✗ Failed to create virtual environment")
            return False
        print(f"  ✓ Virtual environment created at {venv_path}")
    else:
        print(f"  ✓ Virtual environment already exists")
    
    # Determine activation command
    if sys.platform == "win32":
        activate_cmd = str(venv_path / "Scripts" / "activate.bat") + " && "
        pip_cmd = str(venv_path / "Scripts" / "pip")
    else:
        activate_cmd = f"source {venv_path}/bin/activate && "
        pip_cmd = str(venv_path / "bin" / "pip")
    
    # Install dependencies
    print("\n✓ Installing dependencies...")
    success, stdout, stderr = run_command(
        f"{activate_cmd}{pip_cmd} install -r requirements.txt",
        cwd=project_root
    )
    if not success:
        print(f"  ✗ Failed to install dependencies")
        print(f"  Error: {stderr}")
        return False
    print("  ✓ Dependencies installed successfully")
    
    # Create .env file if needed
    print("\n✓ Checking configuration...")
    env_file = project_root / ".env"
    if not env_file.exists():
        example_env = project_root / ".env.example"
        if example_env.exists():
            env_file.write_text(example_env.read_text())
            print("  ✓ Created .env from .env.example")
        else:
            print("  ⚠ No .env file - using defaults")
    else:
        print("  ✓ .env file exists")
    
    print_header("Setup Complete!")
    print("""
✓ Virtual environment created
✓ Dependencies installed
✓ Configuration ready

Next steps:

1. ACTIVATE VIRTUAL ENVIRONMENT:
   Windows:  venv\\Scripts\\activate
   Mac/Linux: source venv/bin/activate

2. RUN THE APPLICATION:
   
   Option A - Run both apps together:
   python run.py

   Option B - Run separately (2 terminals):
   Terminal 1:
     cd backend
     python main.py
   
   Terminal 2:
     cd frontend
     python app.py

3. OPEN IN BROWSER:
   http://localhost:5000

4. API DOCUMENTATION:
   http://localhost:8000/docs

For more information, see PYTHON_README.md
    """)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
