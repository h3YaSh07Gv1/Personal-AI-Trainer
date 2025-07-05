# 💪 AI Personal Trainer for Bicep Curls

This project is an **AI-powered Personal Trainer** that uses **Pose Estimation** to automatically count **bicep curls** in real-time using OpenCV and MediaPipe. It's ideal for monitoring workout form and repetition counts without manual input. This tool is especially helpful for fitness enthusiasts, developers learning pose estimation, and physiotherapy applications.

---

## 📌 Features

* 🎥 Real-time video processing with webcam or pre-recorded video
* 🔍 Pose estimation using MediaPipe
* 📀 Angle detection to measure arm curl position
* 🔢 Bicep curl counter based on angle thresholds
* 📊 Visual progress bar and FPS indicator

---

## 🗂️ Project Structure

```
PersonalAITrainer/
│
├── TrainingVideos/
│   └── BicepCurls1.mp4       # Sample training video
│
├── result/
│   ├── PoseEstimationResult.mp4  # Output showing pose detection
│   └── AITrainingResult.mp4       # Output of bicep curl counter
│
├── PoseEstimationMod.py      # Pose detection logic using MediaPipe
├── Personal_AI_Trainer.py    # Main script to run the AI trainer
├── requirements.txt          # Required Python packages
├── README.md                 # Documentation
```

---

## 🛠️ Requirements

Before running the code, install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, install them individually:

```bash
pip install opencv-python mediapipe numpy
```

Python 3.7 or above is recommended.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/h3YaSh07Gv1/Personal-AI-Trainer.git
cd Personal_AI_Trainer
```

### 2. Add Your Own Video (Optional)

Place your video file inside the `TrainingVideos` folder. Update the video path in `Personal_AI_Trainer.py` if necessary:

```python
cap = cv2.VideoCapture("TrainingVideos/YourVideoName.mp4")
```

Supported formats: `.mp4`, `.avi`, `.mov`

### 3. Run the Pose Detection Test (Optional)

To test pose detection separately:

```bash
python PoseEstimationMod.py
```

### 4. Run the AI Personal Trainer

```bash
python Personal_AI_Trainer.py
```

---

## 🧠 How It Works

This section explains the core logic of the system:

1. The `PoseEstimationMod.py` module uses **MediaPipe's Pose** model to extract 33 body landmarks from each video frame.
2. It calculates the **angle between the shoulder, elbow, and wrist** using landmark points `11, 13, 15` (for the left arm).
3. The angle is mapped to a percentage using `np.interp()` to represent how far the curl has progressed.
4. The repetition count increases when a full extension and curl are completed in sequence (down → up → down).

---

## 🎓 Acknowledgements

* [MediaPipe](https://google.github.io/mediapipe/) by Google for fast pose detection
* [OpenCV](https://opencv.org/) for video and image processing
* [NumPy](https://numpy.org/) for numerical operations
