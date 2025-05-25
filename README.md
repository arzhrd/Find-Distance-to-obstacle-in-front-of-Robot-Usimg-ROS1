# Find-Distance-to-obstacle-in-front-of-Robot-Usimg-ROS1

````markdown
# TurtleBot3 Experiment 2 - Distance to Obstacle Using Laser Scanner

This experiment uses the `/scan` topic from TurtleBot3's LiDAR sensor to find the distance to an obstacle directly in front of the robot.

---

## 📁 Workspace Setup

1. Create and build a catkin workspace:

```bash
mkdir -p ~/experiments_ws/src
cd ~/experiments_ws
catkin_make
````

2. Clone this repository inside the `src` folder:

```bash
cd ~/experiments_ws/src
git clone https://github.com/yourusername/experiment2.git
cd ..
catkin_make
```

---

## 🚀 Running the Simulation

### Step 1: Set TurtleBot3 Model

```bash
export TURTLEBOT3_MODEL=waffle
```

### Step 2: Launch Gazebo World

```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

### Step 3: Run the Node

```bash
rosrun experiment2 exp2.py
```

You should see the distance to the obstacle in front printed in the terminal:

```
[INFO] [timestamp]: Range ahead: 1.2 meters
```

---

## 📊 How it Works

* The `/scan` topic publishes `sensor_msgs/LaserScan` messages.
* The `ranges` array in the message contains distances in a 360-degree sweep.
* The center index (`len(msg.ranges) // 2`) gives the front-facing range.
* The Python node subscribes to the topic and logs the front range.




