#!/usr/bin/env python
"""
Smart Traffic RL System - Python Implementation
Complete Setup and Usage Guide
"""

# QUICK REFERENCE

"""
╔════════════════════════════════════════════════════════════════════════════╗
║                 SMART TRAFFIC RL SYSTEM - PYTHON EDITION                  ║
║                                                                            ║
║  A complete reinforcement learning traffic simulation system with          ║
║  Q-Learning agent vs Fixed-Signal control comparison.                     ║
╚════════════════════════════════════════════════════════════════════════════╝

QUICK START (3 STEPS)
═════════════════════

1. Install dependencies:
   pip install -r requirements.txt

2. Run both backend and frontend:
   python run.py

3. Open browser:
   http://localhost:5000


COMPONENTS
══════════

Backend (FastAPI):
  - URL: http://localhost:8000
  - API Docs: http://localhost:8000/docs
  - Swagger UI: http://localhost:8000/swagger-ui

Frontend (Flask):
  - URL: http://localhost:5000
  - Responsive web interface
  - Real-time simulation control


KEY FEATURES
════════════

✓ Pure Python Implementation
  - No TypeScript, no Convex, no complex frameworks
  - Standard Python 3.8+ with popular libraries

✓ Q-Learning Agent
  - 256-state space (4x4 queue discretization)
  - 4-action space (traffic light phases)
  - Epsilon-greedy exploration strategy
  - Temporal difference learning

✓ Traffic Simulator
  - Realistic vehicle dynamics
  - Configurable arrival rates
  - Service rates based on light phase
  - Multi-component reward function

✓ REST API
  - 10+ endpoints for full CRUD
  - Proper error handling
  - Input validation
  - Type hints with Pydantic

✓ Web Interface
  - Create simulations
  - Run RL or Fixed-Signal algorithms
  - View real-time results
  - Compare performance with charts
  - Responsive design


PROJECT STRUCTURE
═════════════════

smart_traffic_rl_system/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   │   └── simulation.py
│   │   ├── routes/          # API endpoints
│   │   │   ├── traffic.py
│   │   │   └── auth.py
│   │   ├── services/        # Business logic
│   │   │   └── traffic_simulator.py  ← Core RL Engine
│   │   ├── database.py      # SQLAlchemy setup
│   │   └── __init__.py      # FastAPI app
│   └── main.py              # Server entry
│
├── frontend/
│   ├── app.py               # Flask app
│   ├── templates/
│   │   └── index.html       # Main UI
│   └── static/
│       ├── css/
│       └── js/
│
├── requirements.txt
├── run.py
├── quickstart.py
├── test_simulator.py
├── PYTHON_README.md
├── CONVERSION_SUMMARY.md
└── README.md


INSTALLATION DETAILS
════════════════════

Prerequisites:
- Python 3.8 or higher
- pip package manager
- ~200MB disk space

Step 1: Create Virtual Environment
  python -m venv venv
  
Step 2: Activate Virtual Environment
  Windows:  venv\\Scripts\\activate
  Mac/Linux: source venv/bin/activate

Step 3: Install Dependencies
  pip install -r requirements.txt

Step 4 (Optional): Configure
  cp .env.example .env
  # Edit .env if needed


RUNNING THE APPLICATION
═══════════════════════

Option A: Run Everything at Once
  python run.py
  # Automatically starts both backend and frontend

Option B: Run Separately (Better for Development)
  Terminal 1 (Backend):
    cd backend
    python main.py
    # Listens on http://localhost:8000

  Terminal 2 (Frontend):
    cd frontend
    python app.py
    # Listens on http://localhost:5000


TESTING
═══════

Run Unit Tests:
  python -m unittest test_simulator.py -v

Or with pytest (if installed):
  pytest test_simulator.py -v

Tests cover:
✓ TrafficState calculations
✓ Q-Learning agent behavior
✓ State discretization
✓ Epsilon decay
✓ Traffic simulation (RL and Fixed)
✓ Reward calculation


API ENDPOINTS
═════════════

Traffic Management:
  GET  /api/traffic/simulations
       List all user simulations

  POST /api/traffic/simulations
       Create new simulation
       Body: {"name": "string", "algorithm": "RL|Fixed"}

  GET  /api/traffic/simulations/{id}
       Get simulation details

  POST /api/traffic/simulations/{id}/run
       Execute simulation
       Body: {"episodes": number(1-1000)}

  GET  /api/traffic/simulations/{id}/states
       Get state history

Authentication:
  POST /api/auth/login
       Body: {"username": "string", "password": "string"}

  POST /api/auth/logout

  GET  /api/auth/me
       Get current user info

Health:
  GET  /health
       Health check


CONFIGURATION
═════════════

Environment Variables (.env file):
  DATABASE_URL=sqlite:///./smart_traffic.db
  API_BASE_URL=http://localhost:8000/api
  PORT=8000
  FLASK_ENV=development
  SECRET_KEY=dev-secret-key

Traffic Simulator (app/services/traffic_simulator.py):
  BASE_SERVICE_RATE = 3        # Vehicles processed/step when green
  BONUS_SERVICE_RATE = 1       # Extra vehicles when green
  ARRIVAL_RATE = 2             # Average vehicles arriving/step
  MAX_QUEUE_LENGTH = 30        # Maximum queue length
  STEPS_PER_EPISODE = 20       # Steps per training episode

Q-Learning (QLearningAgent):
  LEARNING_RATE = 0.1          # α - Q-value update rate
  DISCOUNT_FACTOR = 0.95       # γ - Future reward weight
  EPSILON = 0.1                # Initial exploration rate
  EPSILON_DECAY = 0.995        # Decay per episode
  EPSILON_MIN = 0.01           # Minimum exploration


HOW IT WORKS
════════════

1. CREATE SIMULATION
   - Choose algorithm: RL or Fixed-Signal
   - Give it a name (e.g., "My First RL Test")
   - Stored in database

2. RUN SIMULATION
   - Specify number of episodes (1-1000)
   - Backend executes simulation
   - Results stored with full state history

3. RL Algorithm Details
   - State: 256 possible states based on queue lengths
   - Action: Choose 1 of 4 traffic light phases
   - Reward: Multi-component function:
     * Queue penalty: -0.1 * total_queue
     * Improvement bonus: queue_reduction * 0.5
     * Balance bonus: +2 if max_queue < 10

4. FIXED-SIGNAL Baseline
   - Pre-programmed phase timing
   - Cycles through phases regardless of traffic
   - Used for comparison baseline

5. COMPARE RESULTS
   - Average wait time
   - Throughput (vehicles processed)
   - RL improvement percentage
   - Visualized in charts


EXAMPLE USAGE
═════════════

from backend.app.services.traffic_simulator import TrafficSimulator

# Create simulator
simulator = TrafficSimulator()

# Run RL algorithm for 100 episodes
results = simulator.simulate("RL", episodes=100)

# Access results
print(f"Avg Wait Time: {results['avgWaitTime']:.2f}")
print(f"Throughput: {results['avgThroughput']:.2f}")
print(f"Total Reward: {results['totalReward']:.0f}")

# Results contain full state history
states = results['states']  # List of state records
for state in states:
    print(f"Episode {state['episode']}, Step {state['step']}: "
          f"Reward {state['reward']}")


DATABASE
════════

SQLAlchemy Models:

TrafficSimulation:
  id (Primary Key)
  name: String
  algorithm: Enum[RL, Fixed]
  episodes: Int
  avg_wait_time: Float
  avg_throughput: Float
  total_reward: Float (Optional)
  q_values: JSON (Optional)
  created_by: String
  created_at: DateTime
  updated_at: DateTime
  relationships: [states]

TrafficState:
  id (Primary Key)
  simulation_id (Foreign Key)
  episode: Int
  step: Int
  north_queue: Int
  south_queue: Int
  east_queue: Int
  west_queue: Int
  current_phase: Int
  reward: Float
  action: Int

Indices for performance:
  - TrafficSimulation.created_by (for user queries)
  - TrafficState.simulation_id (for state queries)


TROUBLESHOOTING
═══════════════

Issue: "ModuleNotFoundError: No module named 'fastapi'"
Solution: Ensure virtual environment is activated
  Windows: venv\\Scripts\\activate
  Mac/Linux: source venv/bin/activate

Issue: "Address already in use" (Port 8000 or 5000)
Solution 1: Close other applications using that port
Solution 2: Change port in code
  Backend: backend/main.py (port=8000)
  Frontend: frontend/app.py (port=5000)

Issue: "sqlite3.OperationalError" with database
Solution: Reset database
  rm smart_traffic.db
  (will be recreated on next run)

Issue: CORS errors
Solution: Backend has CORS enabled for all origins
  - Ensure backend is running before accessing frontend
  - Check both are on correct ports

Issue: ImportError on run.py
Solution: Ensure you're in project root directory
  cd smart_traffic_rl_system
  python run.py


EXTENSION IDEAS
═══════════════

Difficulty: Easy
  ✓ Add more metrics (queue variance, cycle time, etc.)
  ✓ Export results to CSV
  ✓ Add simulation pause/resume
  ✓ Real-time simulation progress bar

Difficulty: Medium
  ✓ Implement Deep Q-Network (DQN)
  ✓ Multi-intersection coordination
  ✓ Different reward functions
  ✓ Policy gradient methods (Actor-Critic)
  ✓ Advanced visualization

Difficulty: Hard
  ✓ Real traffic dataset integration
  ✓ Continuous state space (not discretized)
  ✓ Multi-agent RL
  ✓ Distributed training
  ✓ Real-time traffic control system


DEPLOYMENT
══════════

Local Development:
  python run.py

Docker:
  docker build -t traffic-rl .
  docker run -p 8000:8000 -p 5000:5000 traffic-rl

Cloud (Heroku):
  heroku create your-app-name
  git push heroku main

AWS:
  - EC2 instance with Python 3.8+
  - RDS for database
  - Gunicorn + Nginx for production

Production Checklist:
  ☐ Change SECRET_KEY in .env
  ☐ Set DATABASE_URL to production database
  ☐ Use Gunicorn/uWSGI for backend
  ☐ Set up Nginx reverse proxy
  ☐ Enable HTTPS/SSL
  ☐ Configure CORS for production domains
  ☐ Set up logging and monitoring
  ☐ Regular database backups


RESOURCES
═════════

Documentation:
  - FastAPI: https://fastapi.tiangolo.com/
  - Flask: https://flask.palletsprojects.com/
  - SQLAlchemy: https://www.sqlalchemy.org/
  - Pydantic: https://docs.pydantic.dev/

Learning:
  - Q-Learning: https://en.wikipedia.org/wiki/Q-learning
  - RL Tutorial: https://github.com/simoninithub/Deep-Reinforcement-Learning
  - Traffic Control: https://en.wikipedia.org/wiki/Traffic_signal_control

Community:
  - Python: https://www.python.org/community/
  - FastAPI Discord: https://discord.gg/VQjSZaeJmf
  - Reddit: r/Python, r/MachineLearning


PORTFOLIO PRESENTATION
══════════════════════

This project demonstrates:

1. Full-Stack Development
   - Backend: FastAPI with async/await
   - Frontend: Flask + JavaScript
   - Database: SQLAlchemy ORM

2. Reinforcement Learning
   - Q-Learning algorithm
   - State discretization
   - Reward shaping
   - Exploration-exploitation

3. Software Engineering
   - Clean architecture
   - Separation of concerns
   - Error handling
   - Testing

4. API Design
   - RESTful principles
   - Proper HTTP methods
   - Status codes
   - Pagination-ready

5. Database Design
   - Normalization
   - Relationships
   - Indexing
   - Transaction handling

Perfect talking points for interviews!


LICENSE
═══════

MIT License - Free to use, modify, and distribute


VERSION HISTORY
═══════════════

v2.0.0 (Python) - Current
  - Complete Python rewrite
  - FastAPI + Flask
  - SQLAlchemy ORM
  - Comprehensive tests
  - Full documentation

v1.0.0 (TypeScript) - Original
  - React frontend
  - Convex backend
  - Basic functionality


SUPPORT
═══════

For issues or questions:
  1. Check PYTHON_README.md
  2. Review code comments
  3. Run test_simulator.py
  4. Check GitHub issues (if applicable)


═════════════════════════════════════════════════════════════════════════════

Last Updated: 2024
Ready for Production: Yes
Portfolio-Worthy: Yes ✓

Happy Simulating! 🚀

═════════════════════════════════════════════════════════════════════════════
"""
