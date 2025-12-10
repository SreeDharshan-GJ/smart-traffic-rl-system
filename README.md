# Smart Traffic RL System

An intelligent traffic control system comparing Reinforcement Learning (Q-Learning) algorithms with traditional fixed-signal traffic control. This project demonstrates how adaptive RL-based traffic light management can reduce average wait times and improve traffic throughput.

## 🎯 Overview

This application simulates a 4-way intersection with traffic coming from North, South, East, and West directions. It compares two control strategies:

1. **RL Algorithm (Q-Learning)**: Adaptive control that learns optimal signal timing based on real-time queue lengths
2. **Fixed-Signal Control**: Traditional predetermined timing cycles

## 🏗️ Architecture

### Technology Stack

- **Frontend**: React 19 + TypeScript + Vite
- **Styling**: Tailwind CSS + PostCSS
- **Backend**: Convex (Serverless Backend-as-a-Service)
- **Authentication**: Convex Auth with Anonymous login
- **Notifications**: Sonner (Toast notifications)

### Project Structure

```
smart_traffic_rl_system/
├── src/                              # React frontend
│   ├── App.tsx                       # Main app component with error boundary
│   ├── TrafficDashboard.tsx          # Control panel and simulation list
│   ├── TrafficVisualization.tsx      # Visual representation of traffic state
│   ├── SimulationResults.tsx         # Comparison and results display
│   ├── SignInForm.tsx                # Authentication UI
│   ├── SignOutButton.tsx             # Logout button
│   ├── ErrorBoundary.tsx             # Error handling component
│   ├── lib/
│   │   ├── types.ts                  # Type definitions and utilities
│   │   └── utils.ts                  # General utilities
│   ├── index.css                     # Global styles
│   └── main.tsx                      # React entry point
│
├── convex/                           # Convex backend
│   ├── schema.ts                     # Database schema definitions
│   ├── traffic.ts                    # Traffic simulation logic & RL algorithm
│   ├── auth.ts                       # Authentication handlers
│   ├── auth.config.ts                # Auth configuration
│   ├── http.ts                       # HTTP route setup
│   ├── router.ts                     # Custom HTTP routes
│   └── _generated/                   # Auto-generated Convex types
│
└── Configuration files (vite, tailwind, TypeScript, ESLint, etc.)
```

## 🤖 Q-Learning Algorithm

### State Space
- **256 discrete states** (4^4): Each direction's queue length quantized to 4 levels
- Queue levels: 0-4, 5-9, 10-14, 15+ vehicles

### Action Space
- **4 actions**: Control which direction gets the green light (North, South, East, West)

### Learning Parameters
- **Learning Rate (α)**: 0.1 - Controls how quickly new information is incorporated
- **Discount Factor (γ)**: 0.95 - Balances immediate vs future rewards
- **Epsilon (ε)**: 0.1 - Exploration rate with decay (0.995 per episode)

### Reward Function
$$R(s, a) = -Q_{total} \times 0.1 + \Delta Q + B_{balance}$$

Where:
- $Q_{total}$ = Total vehicles in all queues (penalty for congestion)
- $\Delta Q$ = Queue reduction from action (reward for progress)
- $B_{balance}$ = Bonus for balanced queue management

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ and npm
- Git

### Installation

```bash
# Clone repository
git clone <repository-url>
cd smart_traffic_rl_system

# Install dependencies
npm install

# Create environment file (if needed for Convex)
# Instructions in Convex dashboard
```

### Running Locally

```bash
# Start both frontend and backend
npm run dev

# This runs:
# - Frontend: Vite dev server (usually http://localhost:5173)
# - Backend: Convex local environment

# In separate terminal, you can run just frontend:
npm run dev:frontend

# Or just backend:
npm run dev:backend
```

### Building for Production

```bash
npm run build
```

### Linting and Type Checking

```bash
npm run lint
```

## 📊 How to Use

1. **Sign In**: Anonymous authentication (no credentials needed)
2. **Create Simulation**: Click "Create RL Simulation" or "Create Fixed-Signal Simulation"
3. **Run Simulation**: Select a simulation and choose episode count (50 or 100)
4. **View Results**: 
   - See real-time traffic visualization
   - Compare metrics (wait time, throughput)
   - Observe learning progress in RL vs fixed control

## 📈 Key Metrics

- **Average Wait Time**: Mean queue length across all episodes
- **Throughput**: Average vehicles processed per time step
- **Total Reward**: Cumulative reward (RL only)
- **Improvement**: Percentage reduction in wait time vs fixed control

## 🔧 Configuration

### Traffic Parameters (in `convex/traffic.ts`)

```typescript
const LEARNING_RATE = 0.1;      // How fast the agent learns
const DISCOUNT_FACTOR = 0.95;   // Future reward importance
const EPSILON = 0.1;             // Exploration probability

const BASE_SERVICE_RATE = 3;    // Vehicles processed per step
const ARRIVAL_RATE = 2;          // New vehicles per step
```

### Simulation Parameters (in `src/TrafficDashboard.tsx`)

- Episodes: 50 or 100 (configurable)
- Steps per episode: 20

## 🧪 Testing

```bash
# Run type checking
tsc -p . -noEmit

# Run ESLint
npx eslint src convex
```

## 📚 Database Schema

### trafficSimulations
- `name`: string - Simulation identifier
- `algorithm`: "RL" | "Fixed" - Control type
- `episodes`: number - Training episodes completed
- `avgWaitTime`: number - Average queue length
- `avgThroughput`: number - Vehicles processed
- `totalReward`: number (optional) - Cumulative RL reward
- `qValues`: number[] (optional) - Q-table flatten
- `createdBy`: id - User reference

### trafficStates
- `simulationId`: id - Reference to parent simulation
- `episode`: number - Episode number
- `step`: number - Step within episode
- `northQueue`, `southQueue`, `eastQueue`, `westQueue`: number
- `currentPhase`: number - Active signal (0-3)
- `reward`: number - Reward for this step
- `action`: number - Action taken (0-3)

## 🚀 Deployment

The app is connected to Convex deployment: `beaming-hyena-88`

See [Convex Docs](https://docs.convex.dev/production/) for deployment instructions.

## 🔐 Security

- Anonymous authentication (no credentials stored)
- User data isolated per session
- Convex provides built-in security with authentication tokens

## 🤝 Contributing

1. Create a feature branch
2. Make improvements following the existing code style
3. Test changes locally
4. Submit pull request

## 📝 Future Improvements

- [ ] Multi-intersection coordination
- [ ] Real traffic data integration
- [ ] Different RL algorithms (DQN, Policy Gradient)
- [ ] More sophisticated reward shaping
- [ ] Performance metrics export
- [ ] Real-time visualization updates
- [ ] Traffic pattern analysis tools

## 📖 Resources

- [Convex Documentation](https://docs.convex.dev/)
- [Convex Auth](https://auth.convex.dev/)
- [Q-Learning Basics](https://en.wikipedia.org/wiki/Q-learning)
- [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)

## 📄 License

This project is provided as-is for educational purposes.




