# Real-Time Face Recognition and Attendance Monitoring System

In Collaboration with [@Indra-Fzl02](https://github.com/Indra-Fzl02), [@arkhsat](https://github.com/arkhsat), [@bennynnebenny](https://github.com/bennynnebenny)

## Project Overview
This project aims to develop an advanced real-time face recognition and attendance monitoring system for Binus University. By leveraging OpenCV, Firebase, and the `face_recognition` library, the system captures video frames, detects and recognizes individuals, and records attendance data seamlessly. The solution ensures accuracy, efficiency, and automation in managing attendance tracking for academic purposes.

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
The system employs computer vision techniques to automate the attendance tracking process. It accurately detects and recognizes faculty members, logs their entry and exit times, and updates their attendance records in real-time. By integrating Firebase, the system ensures secure and scalable data storage, facilitating streamlined access and retrieval.

## Workflow
1. **Data Collection and Preparation:**
   - The system begins by capturing datasets of lecturers' facial features to ensure accurate recognition.

2. **Encoding and Camera Calibration:**
   - Face encodings are generated from collected datasets.
   - Camera parameters are calibrated to ensure precise recognition and minimize errors.

3. **Live Monitoring and Recognition:**
   - The system continuously records and monitors activities within the classroom.
   - It detects and identifies known lecturers using pre-encoded face data.

4. **Attendance Logging:**
   - Entry and exit timestamps, along with captured images, are logged securely in the Firebase database.

5. **Automated Data Retrieval & Reporting:**
   - Attendance data is retrieved in real-time and forwarded to a designated Telegram chat (Lecturer Room Manager) via a bot for instant reporting.

6. **Schedule Calibration:**
   - The system integrates a scheduling module to align attendance tracking with class schedules.
   - Ensures accurate reporting by matching attendance records with predefined lecture schedules.

## Installation
### Clone the Repository
```bash
git clone https://github.com/muhammadhardwinv/developing-attendance-monitoring-binus.git
cd developing-attendance-monitoring-binus/
```

### Install Dependencies
```bash
pip install opencv-python cvzone firebase-admin face_recognition numpy
```

### Configure Firebase
1. Download `serviceAccKey.json` from Firebase.
2. Place it in the project's root directory.
3. Configure `databaseURL` and `storageBucket` in the code.

### Add Face Data
- Use `AddDataToData.py` to encode and store facial recognition data.
- Ensure all data is formatted correctly for optimal recognition.

## Usage
To run the attendance system, execute:
```bash
python test_main.py
```
The system will initiate real-time face recognition, log attendance data, and update Firebase accordingly.

## File Structure
```
📦 developing-attendance-monitoring-binus/
 ┣ 📜 test_main.py        # Core face recognition script
 ┣ 📜 schedule.py         # Schedule management module
 ┣ 📜 AddDataToData.py    # Script to encode and store face data
 ┣ 📜 EncodeFile.p        # Stored face encodings
 ┣ 📜 serviceAccKey.json  # Firebase authentication credentials
 ┣ 📜 README.md           # Project documentation
📦 telegrambot/
 ┗ 📜 telegrambot         # Telegram bot configuration
```

## Project Details
The system integrates Firebase services for authentication and attendance tracking:
- **Realtime Database:** Stores attendance logs efficiently.
- **Cloud Storage:** Securely saves entry and exit images.
- **Admin SDK:** Manages authentication, database interactions, and automated processes.

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new feature branch.
3. Make necessary modifications and improvements.
4. Submit a pull request for review.

## License
This project is open-source and distributed under the MIT License.

