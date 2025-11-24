# JYOTI – Just Your Own Transaction Identifier  
**Lighting the Path to Financial Independence for the Visually Impaired**

### Problem Statement  
In India, over 70 million people live with some form of visual impairment, and nearly 495 million are blind (as of recent epidemiological data). A major daily challenge for them is identifying Indian currency notes independently. Although newer banknotes have tactile markers, these wear out quickly, and older notes lack reliable identifiers. The RBI’s MANI app and other existing solutions suffer from:

- Poor accuracy on folded, damaged, or partially occluded notes  
- Heavy dependence on high-end smartphone cameras  
- Limited usability for non-technical and rural users  
- Inability to work reliably under varying lighting and real-world conditions  

As a result, visually impaired individuals remain highly dependent on others for basic financial transactions, exposing them to fraud, loss of privacy, and erosion of dignity and independence.

### Scope of the Project  
JYOTI is a lightweight, accurate, real-time Indian currency recognition system specifically designed to restore financial autonomy to visually impaired users. The project focuses on:

- Recognition of the six most commonly used Indian banknotes: ₹10, ₹20, ₹50, ₹100, ₹200, and ₹500  
- Robust performance under real-world challenges (rotation, folding, low light, partial occlusion, worn notes)  
- Extremely low computational requirements – runs smoothly on CPU-only devices (laptops, Raspberry Pi, low-cost Android phones)  
- Instant voice feedback in Hindi (with easy integration of regional-language TTS via AI4Bharat)  
- Open-source implementation that can be deployed on existing assistive devices without requiring new expensive hardware  

### Target Users  
- Visually impaired and blind individuals across India (urban and rural)  
- Low-literacy and Braille-illiterate users (approximately 99% of the visually impaired population)  
- Elderly visually impaired persons  
- Organizations and NGOs working for visual impairment rehabilitation  
- Developers and researchers building assistive technology solutions  

### High-Level Features  
| Feature | Description |
|--------|-------------|
| **Real-Time Detection** | Average inference speed of **51.03 FPS** on Raspberry Pi (CPU only) |
| **Robust Feature Matching** | Uses **ORB (Oriented FAST and Rotated BRIEF)** + optional **BEBLID** descriptors for rotation-, scale-, and illumination-invariant recognition |
| **Handles Real-World Variations** | Works reliably with rotated, flipped, folded, crumpled, partially obscured, and worn notes |
| **Audio Feedback** | Announces denomination instantly in **Hindi** via gTTS/pygame (prevents repeated announcements for the same note) |
| **Lightweight & Portable** | No GPU or heavy deep-learning model required; runs efficiently on low-cost embedded platforms |
| **Cross-Platform Ready** | Easily deployable on Raspberry Pi, laptops, or Android devices |
| **Regional Language Support** | Designed for seamless integration with AI4Bharat Indic TTS engines |
| **Open Source & Extensible** | Full code and methodology available for community contributions and further research |

**JYOTI** is more than a technical project — it is a step toward dignity, privacy, and true financial independence for millions of visually impaired Indians.
