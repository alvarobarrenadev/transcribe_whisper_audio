# Audio to Text Transcriber

This project allows you to download audio from a YouTube or TikTok video, transcribe it into text using OpenAI's Whisper model, and save the transcription to a text file. It is ideal for converting video content into text, whether for analysis, summaries, or information storage.

## Features

- Support for YouTube and TikTok videos.
- Accurate transcription using advanced Whisper models.
- Automatic text file generation with the transcribed content.
- Automatic deletion of the audio file after transcription to save space.

## Requirements

- **Python 3.10**
- **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)** or **[Anaconda](https://www.anaconda.com/download)**
- **FFmpeg** (installable via `winget`, `brew` or `apt`)


## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/alvarobarrenadev/transcribe_whisper_audio.git
    cd audio_to_text
    ```

2. Create a virtual environment using Miniconda or Conda and activate it:
    ```sh
    conda create -n transcriber python=3.10
    conda activate transcriber
    ```

3. Install the required dependencies:
    ```sh
    pip install openai-whisper yt_dlp
    ```

4. (Optional) Install FFmpeg to process audio:
    ```sh
    sudo apt update
    sudo apt install ffmpeg
    ```

5. (Optional) Update the `yt_dlp` package to the latest version:
    ```sh
   pip install -U yt-dlp
   ```

## Install FFmpeg
#### Windows (using `winget`)

1. **Install `winget`**:  
   `winget` is a command-line package manager for Windows. If you don't have it installed, follow these steps:
   - Download and install `winget` from [here](https://github.com/microsoft/winget-cli).
   - Go to the **Releases** section and download the `.msixbundle` file.
   - Once downloaded, install the `.msixbundle` file by double-clicking it.

2. **Install `ffmpeg` using `winget`**:  
   After installing `winget`, open a command prompt and run the following command to install `ffmpeg`:

   ```bash
   winget install "FFmpeg (Essentials Build)"
   ```

3. **Install Python dependencies**:  
   In the project directory, run the following command to install the required Python libraries:

   ```bash
   pip install ffmpeg-python
   ```

#### macOS

1. **Install `ffmpeg` using Homebrew**:  
   If you are using macOS, you can easily install `ffmpeg` with Homebrew:

   ```bash
   brew install ffmpeg
   ```

2. **Install Python dependencies**:  
   In the project directory, install `ffmpeg-python`:

   ```bash
   pip install ffmpeg-python
   ```

#### Linux (Ubuntu/Debian)

1. **Install `ffmpeg` using `apt`**:  
   On Debian-based distributions (e.g., Ubuntu), you can install `ffmpeg` using `apt`:

   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

2. **Install Python dependencies**:  
   In the project directory, install `ffmpeg-python`:

   ```bash
   pip install ffmpeg-python
   ```

## Usage

1. Run the script:
    ```sh
    python3 app.py
    ```

2. Enter the URL of the YouTube or TikTok video.

3. The transcribed text file will be saved automatically with the video's title.

### Example of Use

#### Input:
Video URL: https://www.youtube.com/watch?v=###

#### Output:
File `Name of Youtube video.txt` containing the transcription.

## Whisper Models

- **tiny**: Fastest but less accurate.
- **base**: Balanced between speed and accuracy.
- **small**: Improved accuracy compared to previous models.
- **medium**: High accuracy but requires more resources.
- **large/large-v2**: Maximum accuracy, ideal for systems with GPUs.

## Common Issues

- **Error: yt_dlp.utils.DownloadError**: Ensure the provided URL is valid.
- **Error loading Whisper**: Make sure PyTorch is installed if not already:
  ```sh
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
  ```

## Contributing

Contributions are welcome. Fork the repository, make your changes, and submit a pull request.

## Notes

- Make sure you have enough disk space to process the audio files.
- The script works locally and does not send data to external servers, ensuring the privacy of your files.

## Limitations

- **Audio Quality**: If the audio is noisy or has interruptions, transcription accuracy may decrease.
- **Languages**: While Whisper supports multiple languages, this script assumes the primary audio language is Spanish. Other languages might require additional configuration.
- **System Resources**: Using larger models like `large-v2` requires a system with sufficient RAM and GPU capabilities. If your system lacks these resources, it is recommended to use the `base` model, which is faster and less resource-intensive but offers lower accuracy.