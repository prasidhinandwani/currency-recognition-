# JYOTI: Lighting the Path to Financial Independence for the Visually Impaired

### Overview
JYOTI (Just Your Own Transaction Identifier) is a lightweight, real-time currency recognition system designed to empower visually impaired individuals in India to independently identify Indian banknotes. It addresses the challenges of financial autonomy by using robust feature extraction to detect notes under various real-world conditions, such as rotations, varying lighting, folds, or partial occlusions. The system provides instant voice feedback in Hindi and is optimized for low-cost embedded platforms like Raspberry Pi, with an average inference speed of 51.03 FPS for seamless user experience. It can be integrated with regional TTS engines like AI4Bharat for broader accessibility.

### Features
- **Real-Time Currency Detection**: Identifies Indian notes (₹10, ₹20, ₹50, ₹100, ₹200, ₹500) from webcam feeds or images with high speed and accuracy.
- **Robust to Variations**: Handles rotations (45°, 90°, 180°), flips, contrast changes, grainy textures, folded or partially obscured notes.
- **Voice Feedback in Hindi**: Uses text-to-speech to announce denominations audibly, preventing redundant playback for usability.
- **Lightweight and Portable**: ORB-based pipeline for efficient computation, suitable for embedded devices without GPU requirements.
- **Dataset Augmentation**: Built on a Kaggle dataset augmented for real-world scenarios to ensure reliability.
- **Optional Enhancements**: Supports BEBLID descriptors for improved matching and FLANN for fast nearest-neighbor searches.

### Technologies/Tools Used
- **Python 3.7+**: Core programming language.
- **OpenCV**: For image processing, ORB feature detection, BEBLID descriptors, and FLANN matching.
- **gTTS (Google Text-to-Speech)**: For generating voice output in Hindi.
- **Pygame**: For playing audio feedback in real-time.
- **NumPy**: For numerical computations and data handling.
- **Raspberry Pi**: Prototyped for embedded deployment (optional for testing on laptops/PCs).
- **AI4Bharat TTS** (optional integration): For regional language support.

### Steps to Install & Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prasidhinandwani/currency-recognition-.git
   cd currency-recognition-
   ```

2. **Create a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install opencv-python numpy gtts pygame
   ```

4. **Download Dataset** (if not included):
   - The system uses a subset of the Indian Currency Dataset from Kaggle. Download and place it in a `dataset/` folder if required by the code.

5. **Run the Project**:
   - Execute the main script for real-time detection via webcam:
     ```bash
     python main.py
     ```
   - The system will open the camera feed, detect notes, and provide voice feedback in Hindi.
   - Press `q` or a specified key to quit (check code for details).
   - For testing with a static image (if supported): `python main.py --image path/to/note.jpg`.

Note: For Raspberry Pi deployment, ensure OpenCV is compiled with necessary modules. The pipeline is lightweight and runs efficiently on CPU.

### Instructions for Testing
1. **Real-Time Webcam Testing**:
   - Run `python main.py` and hold an Indian note (₹10, ₹20, ₹50, ₹100, ₹200, or ₹500) in front of the camera.
   - Ensure good lighting and minimal clutter; the system is robust but performs best with clear views.
   - Listen for Hindi voice output announcing the denomination (e.g., "Detected Currency: 100").
   - Test variations: Rotate the note, fold it partially, or use dim lighting to verify robustness.

2. **Console Output Verification**:
   - Monitor the terminal for logs like "Detected Currency: 100" and matching keypoints count.
   - High keypoints (e.g., ~1000) indicate strong matches; expect 100% accuracy on clear notes.

3. **Edge Case Testing**:
   - Use damaged, grainy, or obscured notes to check resilience (ORB/BEBLID excel here).
   - Simulate real-world use: Test in different environments, orientations, and with multiple notes.

4. **Performance Metrics**:
   - The system averages 51.03 FPS; use timing tools in code to measure on your hardware.
   - Compare against non-ideal notes: BEBLID often achieves ~34% matches where others fail.
