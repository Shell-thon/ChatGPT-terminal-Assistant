## **Full Changelog: How I Got the Voice-Activated ChatGPT CLI Working**

**Project:** _Build a Voice-Activated ChatGPT CLI Without API_  
**Period:** August 15, 2025 — 02:25 AM to 03:55 AM WAT

---

### **1. Initial Issue** _(~02:25 AM WAT)_

**Problem:**  
`ModuleNotFoundError: No module named 'pyaudio'` when running `vn.py`.

**Cause:**  
`PyAudio` was missing — this is required by `speech_recognition` for microphone access.

**Fix:**

- Installed PyAudio:
    
    ```bash
    pip install PyAudio
    ```
    
- Suggested alternative: install from a precompiled wheel or downgrade to Python 3.12 for better compatibility (PyAudio builds for Python 3.13 can be tricky).
    

---

### **2. No Speech Detected** _(~02:37 AM WAT)_

**Problem:**  
`Unexpected error: listening timed out while waiting for phrase to start`.

**Cause:**

- Wrong `DEVICE_INDEX`.
    
- Microphone not capturing audio in a quiet environment.
    

**Fix:**

- Added **dynamic `DEVICE_INDEX` input** to script.
    
- Increased `adjust_for_ambient_noise()` duration from 1s to 3s for better calibration.
    
- Recommended checking microphone settings in OS before running script.
    

---

### **3. Mic Volume Too Low** _(~02:50 AM WAT)_

**Problem:**

- Iriun Webcam mic gave no usable input.
    
- Realtek mic worked but at **4% volume** — far too quiet.
    

**Cause:**

- Iriun mic driver/hardware limitation.
    
- Realtek mic volume not boosted.
    

**Fix:**

- Switched to Realtek mic (`index 7`).
    
- Boosted mic gain to **+20 dB** in OS sound settings.
    
- Adjusted script for better quiet-room performance.
    

---

### **4. Static Noise & Sample Rate Mismatch** _(~03:10 AM WAT)_

**Problem:**

- `Unexpected error: 'NoneType' object has no attribute 'close'` with index 13.
    
- `"Sorry, I didn’t catch that"` on index 7 with static noise in output WAV.
    

**Cause:**

- Invalid mic index (13).
    
- Iriun mic recorded static due to **48000 Hz sample rate** mismatch with `speech_recognition` default (16000 Hz).
    

**Fix:**

- Avoided invalid mic index.
    
- Set `sample_rate=48000` and `chunk_size=2048`.
    
- Raised `energy_threshold` after calibration.
    
- Added `pause_threshold=1.5` for better segmentation.
    

---

### **5. Library Parameter Mismatch** _(~03:25 AM WAT)_

**Problem:**  
`Recognizer.listen() got an unexpected keyword argument 'pause_threshold'` in `vn_2.py`.

**Cause:**

- `pause_threshold` is **not a valid parameter** in current `speech_recognition` version (<3.10).
    
- The library uses `phrase_time_limit` instead.
    

**Fix:**

- Removed `pause_threshold` argument.
    
- Kept `phrase_time_limit=15`.
    
- Retained `energy_threshold` adjustment for accuracy.
    

---

### **6. Final Success** _(~03:55 AM WAT)_

**Problem:**  
None — script finally worked flawlessly.

**Cause of Success:**

- Correct mic index (`1` for Realtek).
    
- Low `energy_threshold` (50) optimized for a quiet room.
    

**Final Fixes Applied:**

- Dynamically scaled `energy_threshold` by `*0.3` for responsiveness.
    
- Added clear success feedback in console.
    
- Stabilized mic capture with proper gain and calibration.
    

---

## **Summary**

The debugging process moved in stages:

1. Fixing dependencies.
    
2. Correct mic selection & OS configuration.
    
3. Boosting volume for clarity.
    
4. Solving static noise & sample rate mismatch.
    
5. Resolving library argument conflicts.
    
6. Optimizing thresholds for stable final performance.
    

Each step built on the last — resulting in a **stable, working, voice-activated ChatGPT CLI without using any API keys**.

---
