# Smart Traffic RL System - Python Edition

A complete Python-based traffic simulation system comparing Q-Learning (Reinforcement Learning) vs Fixed-Signal traffic control strategies.

## 🏗️ Architecture

### Backend (FastAPI)
- **Framework**: FastAPI with async support
- **Database**: SQLAlchemy ORM with SQLite (configurable)
- **Core Engine**: Pure Python traffic simulator with Q-Learning agent
- **API Routes**:
  - `/api/traffic/simulations` - CRUD operations for simulations
  - `/api/traffic/simulations/{id}/run` - Execute simulation
  - `/api/traffic/simulations/{id}/states` - Retrieve simulation states
  - `/api/auth/` - Authentication endpoints

### Frontend (Flask + Jinja2)
- **Framework**: Flask for routing and templating
- **UI**: Tailwind CSS for styling
- **Charts**: Chart.js for data visualization
- **Real-time**: AJAX for seamless updates

### Core Simulation Engine
- **Q-Learning Implementation**: Full epsilon-greedy strategy with decay
- **State Space**: 256 discrete states (4^4 queue levels)
- **Action Space**: 4 traffic light phases
- **Reward Shaping**: Multi-component reward function balancing throughput and queue reduction

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone/Download the project**
```bash
cd smart_traffic_rl_system
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment** (optional)
```bash
cp .env.example .env
# Edit .env with your settings
```

## 🚀 Running the Application

### Terminal 1: Backend API
```bash
cd backend
python main.py
# Runs on http://localhost:8000
# API docs: http://localhost:8000/docs
```

### Terminal 2: Frontend
```bash
cd frontend
python app.py
# Runs on http://localhost:5000
# Visit http://localhost:5000
```

### Or Run Both at Once
```bash
python run.py
```

## 💡 How It Works

### Q-Learning Algorithm
The system uses Q-Learning to train an agent that controls traffic light phases:

1. **State Representation**: Queue lengths at each intersection approach (N, S, E, W)
2. **Action**: Which traffic light phase to activate (0-3)
3. **Reward**: Multi-component function that rewards:
   - Reducing queue lengths
   - Balancing traffic across directions
   - Improving throughput

4. **Learning**: Temporal Difference (TD) learning updates Q-values:
   ```
   Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
   ```

5. **Exploration**: Epsilon-greedy strategy with decay prevents premature convergence

### Fixed-Signal Control
Baseline comparison using pre-programmed timing cycles:
- Each phase lasts ~5 steps
- Rotates through all 4 phases regardless of traffic conditions

## 📊 Key Metrics

- **Average Wait Time**: Mean vehicle waiting time per episode
- **Throughput**: Number of vehicles processed per time unit
- **Total Reward**: Cumulative reward for RL agent
- **Q-Values**: Final learned Q-table values

## 🔧 Configuration

### Traffic Simulator Parameters (in `app/services/traffic_simulator.py`)
```python
BASE_SERVICE_RATE = 3        # Vehicles processed per step
BONUS_SERVICE_RATE = 1       # Extra when green light
ARRIVAL_RATE = 2             # Average vehicles per step
MAX_QUEUE_LENGTH = 30        # Maximum queue size
STEPS_PER_EPISODE = 20       # Steps per episode
```

### Q-Learning Parameters (in `QLearningAgent`)
```python
LEARNING_RATE = 0.1          # α: How much to update Q-values
DISCOUNT_FACTOR = 0.95       # γ: Future reward importance
EPSILON = 0.1                # Exploration rate
EPSILON_DECAY = 0.995        # Exploration decay
```

## 📈 Database Schema

### TrafficSimulation Table
- `id`: Primary key
- `name`: Simulation name
- `algorithm`: "RL" or "Fixed"
- `episodes`: Number of episodes run
- `avg_wait_time`: Average wait time result
- `avg_throughput`: Average throughput result
- `total_reward`: Total reward (RL only)
- `q_values`: Serialized Q-table (RL only)
- `created_by`: User ID
- `created_at`, `updated_at`: Timestamps

### TrafficState Table
- State records for each episode/step
- Linked to TrafficSimulation via foreign key
- Includes queue lengths, actions, and rewards

## 🎯 Features

✅ **Pure Python Implementation**
- No TypeScript, JavaScript backend, or Convex dependencies
- All core logic in Python

✅ **Production-Ready**
- Error handling and validation
- Input sanitization
- Async support in FastAPI
- Database transactions

✅ **Extensible**
- Easy to add more control algorithms
- Configurable reward functions
- Pluggable database backends

✅ **Educational**
- Clear, commented code
- Demonstrates Q-Learning concepts
- Traffic simulation basics

## 🚦 Example Workflow

1. **Create Simulation**: Start either RL or Fixed-Signal simulation
2. **Run Episodes**: Execute 50-100 episodes to train/control traffic
3. **View Results**: Compare metrics between algorithms
4. **Analyze**: Check visualized trends and Q-table values

## 📚 Project Structure

```
smart_traffic_rl_system/
├── backend/
│   ├── app/
│   │   ├── models/          # SQLAlchemy models
│   │   ├── routes/          # FastAPI routers
│   │   ├── services/        # Business logic (simulator)
│   │   ├── database.py      # DB configuration
│   │   └── __init__.py      # FastAPI app
│   └── main.py              # Entry point
├── frontend/
│   ├── app.py               # Flask app
│   ├── templates/           # Jinja2 templates
│   └── static/              # CSS and JS
├── requirements.txt
├── run.py                   # Run both apps
├── test_simulator.py        # Unit tests
└── README.md
```

## 🧪 Testing

Run unit tests:
```bash
python -m pytest test_simulator.py -v
```

Or with unittest:
```bash
python -m unittest test_simulator.py
```

## 🐛 Troubleshooting

**Port already in use**
```bash
# Change port in backend/main.py or frontend/app.py
export PORT=8001
```

**Database issues**
```bash
# Reset database
rm smart_traffic.db
```

**CORS errors**
- Backend already has CORS enabled for all origins
- Ensure backend is running before frontend

**Module not found errors**
```bash
# Ensure you're in the right directory and venv is activated
cd smart_traffic_rl_system
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

## 📝 Future Enhancements

- [ ] Deep Q-Network (DQN) implementation
- [ ] Multi-intersection coordination
- [ ] Real traffic dataset integration
- [ ] Advanced visualization with flow diagrams
- [ ] Policy gradient methods (Actor-Critic)
- [ ] Docker containerization
- [ ] Deployment guides (AWS, Heroku, etc.)
- [ ] Tensorflow/PyTorch models
- [ ] REST API documentation (Swagger)
- [ ] WebSocket support for real-time updates

## 🔗 API Endpoints

### Traffic Simulations
- `GET /api/traffic/simulations` - List all simulations
- `POST /api/traffic/simulations` - Create simulation
- `GET /api/traffic/simulations/{id}` - Get simulation details
- `POST /api/traffic/simulations/{id}/run` - Execute simulation
- `GET /api/traffic/simulations/{id}/states` - Get state history

### Authentication
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user

## 💻 System Requirements

- **Minimum**: 2GB RAM, Python 3.8
- **Recommended**: 4GB RAM, Python 3.9+
- **Tested**: Windows 10/11, macOS 10.14+, Linux (Ubuntu 20.04+)

## 📄 License

MIT License - Feel free to use this for educational and commercial projects

## 👨‍💻 Portfolio Highlights

This project demonstrates:
- **Reinforcement Learning**: Full Q-Learning implementation with epsilon-greedy exploration
- **Full-Stack Development**: Backend API + Frontend with proper separation of concerns
- **Software Engineering**: Clean architecture, error handling, testing, documentation
- **Database Design**: Proper schema with relationships and indexing
- **Web Development**: FastAPI + Flask + modern frontend technologies
- **DevOps Thinking**: Configuration management, environment handling
- **Code Quality**: Type hints, docstrings, comments, clean code practices

Perfect for showcasing in portfolio or job interviews!
