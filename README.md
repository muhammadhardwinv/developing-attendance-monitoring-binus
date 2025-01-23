# Developing Attendance Monitoring System at Binus University

In Collaboration with [@Indra-Fzl02](https://github.com/Indra-Fzl02), [@arkhsat](https://github.com/arkhsat), [@bennynnebenny](https://github.com/bennynnebenny)

## Real-Time Face Recognition and Attendance System

This project aims to develop a real-time face recognition and attendance tracking system for Binus University. Utilizing OpenCV, Firebase, and the `face_recognition` library, the system captures video frames, detects and recognizes faces, and records attendance data efficiently.

## Table of Contents
- [Project Description](#project-description)
- [Workflow](#workflow)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Project Details](#project-details)
- [Contributing](#contributing)
- [License](#license)

## Project Description
The system utilizes computer vision techniques to automate attendance tracking. It detects and recognizes individuals' faces, logs their entry and exit times, and updates their attendance status. Firebase is used for data storage and retrieval, ensuring seamless and scalable performance.

## Workflow
1. **Taking data from datasets of lecture faces:** The system starts by collecting face datasets of lecturers for accurate recognition.
2. **Encoding files and calibrating the camera scope:** Face encodings are generated and the camera is calibrated to match the target accurately.
3. **Camera begins to record the activity in the classroom:** The system continuously monitors the classroom environment.
4. **Detecting known lecturers and tracking movements:** The system recognizes lecturers based on the dataset and tracks their activity.
5. **Capturing images, timestamps, and writing information:** Entry and exit data, including images and timestamps, are recorded and sent to the database.
6. **Automated data retrieval and Telegram reporting:** Stored data is pulled from the database and sent to a Telegram chat (Lecturer Room Manager) via a bot for real-time reporting.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/muhammadhardwinv/developing-attendance-monitoring-binus/.git
   cd developing-attendance-monitoring-binus/
   ```
2. **Install dependencies:**
   ```bash
   pip install opencv-python cvzone firebase-admin face_recognition numpy
   ```
3. **Set up Firebase credentials:**
   - Download `serviceAccKey.json` from Firebase.
   - Place it in the project root directory.
   - Configure the `databaseURL` and `storageBucket` in the code.
4. **Add face data:**
   - Use `AddDataToData.py` to create and store face encodings.
   - Ensure that face data is properly formatted for recognition.

## Usage
1. **Run the attendance system:**
   ```bash
   python test_main.py
   ```
2. The system will start detecting and recognizing faces, logging attendance data to Firebase.

## File Structure
```
📦developing-attendance-monitoring-binus/
 ┣ 📜test_main.py       # Core face recognition script
 ┣ 📜schedule.py       # Core schedule management
 ┣ 📜test_main.py       # Core face recognition script
 ┣ 📜AddDataToData.py     # Script to encode and store face data
 ┣ 📜EncodeFile.p         # Stored face encodings
 ┣ 📜serviceAccKey.json   # Firebase authentication credentials
 ┗ 📜README.md            # Project documentation
📦telegrambot/
 ┗ 📜telegrambot          # Telegram configurations

```

## Project Details
The system integrates Firebase for authentication and attendance tracking:
- **Realtime Database** stores attendance logs.
- **Storage** saves entry and exit images securely.
- **Admin SDK** manages authentication and database interactions.

## Contributing
Contributions are welcome! Please fork the repository, make changes in a feature branch, and submit a pull request.

---

